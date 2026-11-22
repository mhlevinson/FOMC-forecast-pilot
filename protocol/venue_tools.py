"""Venue adapter for the FOMC forecast pilot. DRAFT - not frozen.

Turns saved Kalshi and Polymarket responses into quotes, midpoints and a two-venue benchmark.
No model is involved. All prices are in points (0-100).
"""
import json

from forecast_tools import OUTCOMES, venue_vector, benchmark

KALSHI_SUFFIX = {"C26": "cut50", "C25": "cut25", "H0": "hold", "H25": "hike25", "H26": "hike50"}
POLY_TITLE = {"50+ bps decrease": "cut50", "25 bps decrease": "cut25", "No change": "hold",
              "25 bps increase": "hike25", "50+ bps increase": "hike50"}
WIDE = 10  # a spread above this many points is flagged


class CaptureError(Exception):
    """A saved response is unusable: it does not parse or does not hold what was expected."""


def _load(text):
    """Parse JSON text or raise CaptureError."""
    try:
        return json.loads(text)
    except (TypeError, ValueError) as e:
        raise CaptureError("unparseable JSON: %s" % e)


def _points(x):
    """Dollar price (string or number) as points; None if absent or empty."""
    if x is None or x == "":
        return None
    return round(float(x) * 100, 6)


def _size(x):
    """Size as a float; None if absent or empty."""
    if x is None or x == "":
        return None
    return float(x)


def _check_five(quotes_by_outcome, count):
    """Raise CaptureError unless there are exactly five contracts, one per outcome."""
    if count != len(OUTCOMES) or set(quotes_by_outcome) != set(OUTCOMES):
        raise CaptureError("the five outcomes are not each present exactly once")


def kalshi_quotes(text, event_ticker):
    """Read a saved Kalshi markets response into quotes per outcome; CaptureError if it is not the expected event."""
    data = _load(text)
    markets = data.get("markets") if isinstance(data, dict) else None
    if not markets:
        raise CaptureError("no markets")
    quotes, count = {}, 0
    for m in markets:
        if m.get("event_ticker") != event_ticker:
            raise CaptureError("unexpected event_ticker %r" % m.get("event_ticker"))
        outcome = KALSHI_SUFFIX.get(str(m.get("ticker", "")).rsplit("-", 1)[-1])
        if outcome is None:
            raise CaptureError("unknown ticker %r" % m.get("ticker"))
        count += 1
        quotes[outcome] = {"bid": _points(m.get("yes_bid_dollars")), "ask": _points(m.get("yes_ask_dollars")),
                           "last": _points(m.get("last_price_dollars")),
                           "bid_size": _size(m.get("yes_bid_size_fp")), "ask_size": _size(m.get("yes_ask_size_fp")),
                           "id": m["ticker"]}
    _check_five(quotes, count)
    return quotes


def polymarket_quotes(text, slug):
    """Read a saved Polymarket event response into quotes per outcome; CaptureError if it is not the expected event."""
    data = _load(text)
    if not isinstance(data, list) or len(data) != 1:
        raise CaptureError("expected a list with exactly one event")
    event = data[0]
    if event.get("slug") != slug:
        raise CaptureError("unexpected slug %r" % event.get("slug"))
    quotes, count = {}, 0
    for m in event.get("markets") or []:
        outcome = POLY_TITLE.get(m.get("groupItemTitle"))
        if outcome is None:
            raise CaptureError("unknown groupItemTitle %r" % m.get("groupItemTitle"))
        count += 1
        try:
            token = json.loads(m["clobTokenIds"])[0]
        except (KeyError, TypeError, ValueError, IndexError):
            token = None
        quotes[outcome] = {"bid": _points(m.get("bestBid")), "ask": _points(m.get("bestAsk")),
                           "last": _points(m.get("lastTradePrice")),
                           "bid_size": None, "ask_size": None, "id": token}
    _check_five(quotes, count)
    return quotes


def midpoints(quotes):
    """Midpoint per outcome with flags; (None, flags) if any contract has no bid, ask or last."""
    mids, flags = {}, []
    for k in OUTCOMES:
        q = quotes[k]
        has_bid = q["bid"] is not None and q["bid"] > 0
        has_ask = q["ask"] is not None and q["ask"] < 100
        if has_bid and has_ask:
            mids[k] = (q["bid"] + q["ask"]) / 2
            if q["ask"] - q["bid"] > WIDE:
                flags.append("wide:" + k)
        elif has_bid or has_ask:
            mids[k] = ((q["bid"] if has_bid else 0) + (q["ask"] if has_ask else 100)) / 2
            flags.append("one_sided:" + k)
        elif q["last"] is not None:
            mids[k] = q["last"]
            flags.append("last_trade_used:" + k)
        else:
            return None, flags + ["invalid:" + k]
    return mids, flags


def venue_capture(quotes):
    """Summarise one venue: valid or not, its vector (sums to 100), the sum before scaling, flags and the quotes."""
    mids, flags = midpoints(quotes)
    if mids is None:
        return {"valid": False, "vector": None, "sum_before": None, "flags": flags, "quotes": quotes}
    vector, total, vflags = venue_vector(mids)
    return {"valid": True, "vector": vector, "sum_before": total, "flags": flags + vflags, "quotes": quotes}


def two_venue_benchmark(kalshi_capture, polymarket_capture):
    """Average of the valid venue vectors; flags one_venue or no_benchmark when fewer than two are valid."""
    used = [(n, c) for n, c in (("kalshi", kalshi_capture), ("polymarket", polymarket_capture)) if c["valid"]]
    flags = []
    if len(used) == 1:
        flags.append("one_venue")
    elif not used:
        flags.append("no_benchmark")
    return {"benchmark": benchmark([c["vector"] for _, c in used]) if used else None,
            "venues_used": [n for n, _ in used], "flags": flags}
