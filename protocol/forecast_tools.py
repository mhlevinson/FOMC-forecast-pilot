"""Forecast tools for the FOMC forecast pilot. DRAFT - not frozen.

Three jobs, none of which involves a model:
  1. read the FORECAST line from a final answer (parse_forecast)
  2. build the two-venue benchmark from midpoints (venue_vector, benchmark)
  3. score forecasts once the outcome is known (brier, log_score, rps, paired, surprise_reading)

All probabilities are percentages (0-100). Rules are those of protocol/design.md, sections 3, 6 and 8.
"""
import math
import re

OUTCOMES = ["cut50", "cut25", "hold", "hike25", "hike50"]  # ordered from lowest rate to highest
UNIFORM = {k: 20.0 for k in OUTCOMES}  # failure policy: 20% on each outcome
_DECORATION = "*`_> \t"  # markdown characters ignored at either end of a line


def _forecast_lines(text):
    lines = []
    for raw in text.splitlines():
        s = raw.strip(_DECORATION)
        if re.match(r"FORECAST\s*\|", s):
            lines.append(re.sub(r"\s+", "", s))
    return lines


def _invalid(reason, line=None, total=None):
    return {"valid": False, "reason": reason, "line": line, "sum_stated": total, "forecast": None}


def parse_forecast(text):
    """Return the forecast stated on the single FORECAST line of a final answer.

    Valid only if: exactly one distinct FORECAST line; the five outcomes, each once;
    every value above 0 and below 100; sum between 99.5 and 100.5 (then rescaled to 100).
    Nothing else in the answer is read. Nothing is repaired or guessed.
    """
    lines = _forecast_lines(text)
    if not lines:
        return _invalid("no_line")
    if len(set(lines)) > 1:
        return _invalid("conflicting_lines")
    line = lines[0]
    values = {}
    for part in line.split("|", 1)[1].lower().split(";"):
        if not part:
            continue
        m = re.fullmatch(r"([a-z0-9]+)=(-?\d+(?:\.\d+)?)%?", part)
        if not m:
            return _invalid("malformed", line)
        key, value = m.group(1), float(m.group(2))
        if key not in OUTCOMES or key in values:
            return _invalid("bad_keys", line)
        values[key] = value
    if set(values) != set(OUTCOMES):
        return _invalid("missing_outcome", line)
    if any(v <= 0 or v >= 100 for v in values.values()):
        return _invalid("out_of_range", line)
    total = round(sum(values.values()), 6)
    if not 99.5 <= total <= 100.5:
        return _invalid("sum_out_of_band", line, total)
    return {"valid": True, "reason": "ok", "line": line, "sum_stated": total,
            "forecast": {k: 100 * values[k] / total for k in OUTCOMES}}


def venue_vector(midpoints):
    """Scale one venue's five midpoints (in points) to sum to 100. Returns (vector, sum_before, flags)."""
    total = sum(midpoints[k] for k in OUTCOMES)
    flags = [] if 95 <= total <= 105 else ["incoherent"]
    return {k: 100 * midpoints[k] / total for k in OUTCOMES}, total, flags


def average(vectors):
    """Plain average of forecast vectors; None if there are none."""
    if not vectors:
        return None
    return {k: sum(v[k] for v in vectors) / len(vectors) for k in OUTCOMES}


def benchmark(valid_venue_vectors):
    """Two-venue synthetic benchmark: average of the valid venue vectors (one venue alone if only one)."""
    return average(valid_venue_vectors)


def fable_average(slots, view):
    """Ten-call average. slots holds a forecast or None per call.
    end_to_end: a failed call is filled with UNIFORM before averaging. conditional: delivered calls only."""
    if view == "end_to_end":
        return average([s or UNIFORM for s in slots])
    return average([s for s in slots if s])


def brier(forecast, outcome):
    """Sum of squared gaps over the five outcomes. 0 is perfect, 2 is worst."""
    return sum((forecast[k] / 100 - (k == outcome)) ** 2 for k in OUTCOMES)


def log_score(forecast, outcome, floor=0.5):
    """Negative log of the probability given to what happened; values under the floor count as the floor."""
    return -math.log(max(forecast[outcome], floor) / 100)


def rps(forecast, outcome):
    """Ranked probability score: like Brier on cumulative probabilities, so near misses cost less."""
    cum_f = cum_o = total = 0.0
    for k in OUTCOMES[:-1]:
        cum_f += forecast[k] / 100
        cum_o += k == outcome
        total += (cum_f - cum_o) ** 2
    return total / (len(OUTCOMES) - 1)


def paired(forecasts, benchmarks, outcome, view, score=brier):
    """Average score of an arm and of the benchmark over a question's scheduled checkpoints.

    forecasts, benchmarks: one entry per scheduled checkpoint; None where missing.
    A checkpoint with no benchmark drops out of the pairing in both views.
    end_to_end: a missing forecast scores as UNIFORM. conditional: it is left out.
    Returns (arm_mean, benchmark_mean, n) or (None, None, 0).
    """
    arm, ref = [], []
    for f, b in zip(forecasts, benchmarks):
        if b is None:
            continue
        if f is None:
            if view != "end_to_end":
                continue
            f = UNIFORM
        arm.append(score(f, outcome))
        ref.append(score(b, outcome))
    if not arm:
        return None, None, 0
    return sum(arm) / len(arm), sum(ref) / len(ref), len(arm)


def _caught(prob, bench_prob):
    return prob >= bench_prob + 10 and prob >= 2 * bench_prob


def surprise_reading(bench, scored, outcome, twin=None, start_claim=None):
    """The pre-declared surprise reading at a question's final checkpoint (design.md, section 8)."""
    b = bench[outcome]
    surprise = b < 20
    reading = {
        "surprise": surprise,
        "caught_in_part": surprise and _caught(scored[outcome], b),
        "called": surprise and max(OUTCOMES, key=lambda k: scored[k]) == outcome,
        "false_alarms": [k for k in OUTCOMES if k != outcome and scored[k] >= bench[k] + 10],
        "anchor_check": None,
    }
    if twin is not None:
        twin_caught = _caught(twin[outcome], b)
        reading["anchor_check"] = {
            "twin_probability": twin[outcome],
            "twin_caught_in_part": twin_caught,
            "depends_on_starting_claim": outcome == start_claim and not twin_caught,
        }
    return reading
