"""Tests for venue_tools.py on made-up saved responses. DRAFT - not frozen. Run: python3 test_venue_tools.py"""
import copy
import json

from venue_tools import *

EV = "KXFEDDECISION-26DEC"
SLUG = "fed-decision-in-december"


def kmarket(suffix, bid, ask, last, bid_size="100.00"):
    return {"ticker": EV + "-" + suffix, "event_ticker": EV, "yes_sub_title": suffix,
            "yes_bid_dollars": bid, "yes_ask_dollars": ask, "last_price_dollars": last,
            "yes_bid_size_fp": bid_size, "yes_ask_size_fp": "50.00", "updated_time": "2026-11-22T10:00:00Z"}


def kalshi_data():
    return {"markets": [kmarket("C26", "0.0000", "0.0100", "0.0100", "0.00"),
                        kmarket("C25", "0.0000", "0.0100", "0.0100", "0.00"),
                        kmarket("H0", "0.0700", "0.0800", "0.0800"),
                        kmarket("H25", "0.8900", "0.9000", "0.9000"),
                        kmarket("H26", "0.0200", "0.0300", "0.0200")], "cursor": ""}


def pmarket(title, bid, ask):
    m = {"question": title, "groupItemTitle": title, "bestBid": bid, "bestAsk": ask,
         "lastTradePrice": ask, "clobTokenIds": json.dumps(["tok-" + title, "no-" + title])}
    return m


def poly_data():
    return [{"slug": SLUG, "title": "Fed decision", "markets": [
        pmarket("50+ bps decrease", 0.004, 0.005), pmarket("25 bps decrease", 0.006, 0.007),
        pmarket("No change", 0.065, 0.067), pmarket("25 bps increase", 0.89, 0.90),
        pmarket("50+ bps increase", 0.021, 0.022)]}]


def kq(d=None):
    return kalshi_quotes(json.dumps(d or kalshi_data()), EV)


def pq(d=None):
    return polymarket_quotes(json.dumps(d or poly_data()), SLUG)


def raises(f, *args):
    try:
        f(*args)
    except CaptureError:
        return True
    return False


# --- parsing ---
k = kq()
assert k["hike25"]["bid"] == 89.0 and k["hike25"]["ask"] == 90.0 and k["hike25"]["id"] == EV + "-H25"
assert k["cut50"]["bid"] == 0.0 and k["cut50"]["bid_size"] == 0.0 and k["hold"]["bid_size"] == 100.0
p = pq()
assert p["hike25"]["bid"] == 89.0 and p["cut50"]["ask"] == 0.5 and p["hold"]["id"] == "tok-No change"
assert p["hold"]["bid_size"] is None

# --- midpoints and venue capture ---
mids, flags = midpoints(k)
assert mids["cut50"] == 0.5 and mids["cut25"] == 0.5 and mids["hike25"] == 89.5
assert "one_sided:cut50" in flags and "one_sided:cut25" in flags
kc, pc = venue_capture(k), venue_capture(p)
assert kc["valid"] and pc["valid"]
assert abs(kc["sum_before"] - 100.5) < 1e-9 and "incoherent" not in kc["flags"]
bm = two_venue_benchmark(kc, pc)
assert bm["venues_used"] == ["kalshi", "polymarket"] and bm["flags"] == []
assert abs(sum(bm["benchmark"].values()) - 100) < 1e-9 and 88 < bm["benchmark"]["hike25"] < 90

# --- capture errors ---
assert raises(kalshi_quotes, json.dumps(kalshi_data()), "OTHER-EVENT")
assert raises(polymarket_quotes, json.dumps(poly_data()), "other-slug")
d = kalshi_data(); del d["markets"][3]
assert raises(kalshi_quotes, json.dumps(d), EV)
d = kalshi_data(); d["markets"].append(copy.deepcopy(d["markets"][3]))
assert raises(kalshi_quotes, json.dumps(d), EV)
d = poly_data(); del d[0]["markets"][0]
assert raises(polymarket_quotes, json.dumps(d), SLUG)
d = poly_data(); d[0]["markets"].append(copy.deepcopy(d[0]["markets"][0]))
assert raises(polymarket_quotes, json.dumps(d), SLUG)
assert raises(kalshi_quotes, "not json {", EV) and raises(polymarket_quotes, "not json {", SLUG)
assert raises(kalshi_quotes, json.dumps({"markets": []}), EV)
assert raises(polymarket_quotes, json.dumps(poly_data() + poly_data()), SLUG)

# --- a contract with no bid, no ask and no last invalidates the venue ---
d = kalshi_data(); d["markets"][2].update(yes_bid_dollars="", yes_ask_dollars=None, last_price_dollars="")
bad = venue_capture(kq(d))
assert not bad["valid"] and bad["vector"] is None and bad["sum_before"] is None and "invalid:hold" in bad["flags"]
bm = two_venue_benchmark(bad, pc)
assert bm["venues_used"] == ["polymarket"] and "one_venue" in bm["flags"]
assert abs(bm["benchmark"]["hike25"] - pc["vector"]["hike25"]) < 1e-9
bm = two_venue_benchmark(bad, bad)
assert bm["benchmark"] is None and bm["venues_used"] == [] and "no_benchmark" in bm["flags"]

# --- last trade used when there is no book ---
d = kalshi_data(); d["markets"][2].update(yes_bid_dollars="0.0000", yes_ask_dollars="1.0000")
m2, f2 = midpoints(kq(d))
assert m2["hold"] == 8.0 and "last_trade_used:hold" in f2

# --- wide book ---
d = kalshi_data(); d["markets"][3].update(yes_bid_dollars="0.7000", yes_ask_dollars="0.9000")
assert "wide:hike25" in venue_capture(kq(d))["flags"]
assert not any(f.startswith("wide") for f in kc["flags"])

# --- incoherent sum ---
d = kalshi_data(); d["markets"][3].update(yes_bid_dollars="0.9500", yes_ask_dollars="0.9700")
assert "incoherent" in venue_capture(kq(d))["flags"]

print("all tests passed")
