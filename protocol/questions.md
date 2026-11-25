# Questions (protocol v5, frozen 25 Nov 2026; see `FREEZE.md`)

Outcome keys used everywhere: `cut50` (cut of 50 bp or more), `cut25` (cut of 25 bp), `hold` (no change), `hike25` (hike of 25 bp), `hike50` (hike of 50 bp or more).

## FOMC-2026-12

**Question.** By how many basis points will the FOMC change the upper bound of the federal funds target range in the statement released after its 8-9 December 2026 meeting, compared with the upper bound in effect immediately before the meeting?

**Resolution.** Read from the FOMC statement on 9 December 2026: new upper bound minus the upper bound before the meeting. A move that is not a multiple of 25 is rounded up to the next 25. No statement on that day: the question is void and reported unscored.

**Starting claim for Deliberate (rule: same change as at the most recent concluded scheduled meeting).** The October 2026 meeting left the range unchanged, so the claim is `hold` at every December checkpoint.

**Twin claim (diagnostic).** `hike25` - a 25 bp move in the direction of the FOMC's most recent change (the September 2026 hike).

**Venue proxies.** Kalshi event `KXFEDDECISION-26DEC`. Polymarket event slug `fed-decision-in-december-20260729232808632`.

## FOMC-2027-01

**Question.** By how many basis points will the FOMC change the upper bound of the federal funds target range in the statement released after its 26-27 January 2027 meeting, compared with the upper bound in effect immediately before the meeting?

**Resolution.** As above, read from the FOMC statement on 27 January 2027.

**Starting claim for Deliberate (same rule).**

- Checkpoints before 9 December 2026: `hold` (the October meeting's change).
- Checkpoints after 9 December 2026: whatever the December meeting did.

**Twin claim (diagnostic).** If the starting claim is `hold`: a 25 bp move in the direction of the FOMC's most recent change. If the starting claim is itself a move: `hold`.

**Venue proxies.** Kalshi event `KXFEDDECISION-27JAN`. Polymarket event slug `fed-decision-in-january-20260729233815502`.
