"""Tests for forecast_tools.py on made-up answers and the worked examples in design.md. Run: python3 test_forecast_tools.py"""
from forecast_tools import *

GOOD = "FORECAST | cut50=0.5 ; cut25=0.5 ; hold=15.0 ; hike25=78.0 ; hike50=6.0"

def reason(text):
    return parse_forecast(text)["reason"]

# --- parser ---
assert reason("Reasoning...\n" + GOOD) == "ok"
assert reason("**" + GOOD + "**") == "ok"                                  # markdown decoration ignored
assert reason(GOOD + "\n" + GOOD) == "ok"                                  # identical repeat is one distinct line
assert reason("no forecast here") == "no_line"
assert reason(GOOD + "\nFORECAST | cut50=1 ; cut25=1 ; hold=10 ; hike25=80 ; hike50=8") == "conflicting_lines"
assert reason("FORECAST | cut50=0.5 ; cut25=0.5 ; hold=15 ; hike25=84") == "missing_outcome"
assert reason("FORECAST | cut50=0.005 ; cut25=0.005 ; hold=0.15 ; hike25=0.78 ; hike50=0.06") == "sum_out_of_band"   # decimals, not percentages
assert reason("FORECAST | cut50=0.5 ; cut25=0.5 ; hold=15 ; hike25=78 ; hike50=5") == "sum_out_of_band"            # sums to 99.0
assert reason("FORECAST | cut50=0 ; cut25=1 ; hold=15 ; hike25=78 ; hike50=6") == "out_of_range"
assert reason("FORECAST | cut50=__ ; cut25=__ ; hold=__ ; hike25=__ ; hike50=__") == "no_line"                     # template returned unfilled
assert reason("FORECAST | cut50=A ; cut25=B ; hold=C ; hike25=D ; hike50=E") == "no_line"                          # template returned unfilled
assert reason("FORECAST | cut50=A ; cut25=B ; hold=C ; hike25=D ; hike50=E\nwork...\n" + GOOD) == "ok"           # question restated, then answered
assert reason('"' + GOOD + '"') == "ok"                                    # quotation marks ignored
assert reason("FORECAST | cut50=x1 ; cut25=0.5 ; hold=15 ; hike25=78 ; hike50=6") == "malformed"
assert reason('The format is "FORECAST | cut50=1 ; cut25=1 ; hold=10 ; hike25=80 ; hike50=8" as above.\n' + GOOD) == "ok"  # only a line that starts with FORECAST counts
assert reason("FORECAST | cut50=0.5 ; cut25=0.5 ; hold=15 ; hike25=78 ; hike25=6") == "bad_keys"
assert reason("FORECAST | cut50=0.5 ; cut25=0.5 ; hold=15 ; hike25=78 ; raise50=6") == "bad_keys"
# the line governs even when a table elsewhere disagrees
table_then_line = "| hold | 40% |\n| hike25 | 50% |\n" + GOOD
assert abs(parse_forecast(table_then_line)["forecast"]["hold"] - 15.0) < 1e-9
# a sum inside the band is rescaled to 100
r = parse_forecast("FORECAST | cut50=0.5 ; cut25=0.5 ; hold=15.0 ; hike25=78.3 ; hike50=6.0")
assert r["valid"] and abs(sum(r["forecast"].values()) - 100) < 1e-9 and r["sum_stated"] == 100.3

# --- benchmark: worked example of 20 Nov 2026 ---
k, ksum, kflags = venue_vector({"cut50": 0.5, "cut25": 0.5, "hold": 4.5, "hike25": 90.5, "hike50": 5.5})
p, psum, pflags = venue_vector({"cut50": 0.15, "cut25": 0.25, "hold": 3.8, "hike25": 92.5, "hike50": 3.95})
assert ksum == 101.5 and abs(psum - 100.65) < 1e-9 and not kflags and not pflags
b = benchmark([k, p])
assert [round(b[x], 1) for x in OUTCOMES] == [0.3, 0.4, 4.1, 90.5, 4.7]
assert benchmark([k]) == k and benchmark([]) is None
assert venue_vector({"cut50": 1, "cut25": 1, "hold": 5, "hike25": 80, "hike50": 5})[2] == ["incoherent"]

# --- scores: worked example in section 8 ---
bench = {"cut50": 0.3, "cut25": 0.4, "hold": 4.1, "hike25": 90.5, "hike50": 4.7}
d = parse_forecast(GOOD)["forecast"]
assert round(brier(bench, "hike25"), 3) == 0.013 and round(brier(d, "hike25"), 3) == 0.075
assert round(brier(bench, "hold"), 2) == 1.74 and round(brier(d, "hold"), 2) == 1.33
assert abs(brier(UNIFORM, "hold") - 0.8) < 1e-9
assert rps(d, "hike25") < rps(d, "cut50")                                  # near miss costs less than a far miss
assert log_score({**bench, "cut50": 0.1}, "cut50") == log_score({**bench, "cut50": 0.5}, "cut50")

# --- denominators ---
arm, ref, n = paired([d, None, d], [bench, bench, None], "hike25", "end_to_end")
assert n == 2 and abs(arm - (brier(d, "hike25") + brier(UNIFORM, "hike25")) / 2) < 1e-9
arm, ref, n = paired([d, None, d], [bench, bench, None], "hike25", "conditional")
assert n == 1 and abs(arm - brier(d, "hike25")) < 1e-9
assert paired([None], [None], "hold", "end_to_end") == (None, None, 0)
assert fable_average([d] * 9 + [None], "end_to_end")["hold"] == (9 * 15.0 + 20.0) / 10
assert fable_average([d] * 9 + [None], "conditional")["hold"] == 15.0

# --- surprise reading ---
twin_low = {"cut50": 0.5, "cut25": 0.5, "hold": 5.0, "hike25": 88.0, "hike50": 6.0}
twin_high = {"cut50": 0.5, "cut25": 0.5, "hold": 16.0, "hike25": 77.0, "hike50": 6.0}
s = surprise_reading(bench, d, "hold", twin=twin_low, start_claim="hold")
assert s["surprise"] and s["caught_in_part"] and not s["called"] and s["anchor_check"]["depends_on_starting_claim"]
s = surprise_reading(bench, d, "hold", twin=twin_high, start_claim="hold")
assert not s["anchor_check"]["depends_on_starting_claim"]
s = surprise_reading(bench, d, "hike25")
assert not s["surprise"] and not s["caught_in_part"] and s["false_alarms"] == ["hold"]

print("all tests passed")
