# Compliance record - checkpoint K1 (FOMC-2026-12)

| Field | Value |
|---|---|
| Question, checkpoint, protocol fingerprint in force | FOMC-2026-12; K1 (26 Nov 2026); protocol v6, combined fingerprint 4b0fe75b8e7f257238cb3bfb2bff91ecbca401a7b0aba3909a63a651febc51ab, repository commit 31ad1a3 (all 14 frozen files OK; all three test files pass) |
| Pack fingerprint; documents included, omitted, dropped; market-pricing passages (count) | bd32507ea6d00a100777babe3a21421ad6d5634734f58a54c2c9827d09f69575; 22 included, 0 capture_failed, 0 dropped; market-term passages in included documents: 16 (pack_tools count). No venue name appears in the pack. |
| T0, each arm's T1, T2, T3; status of each arm | T0 2026-11-26T07:03:09Z (planned 07:00:00Z; deviation D4). Pack ready 07:10:24Z. Fable x10: 07:10:37Z-07:13:11Z, all on time. Deliberate (scored run K1-scored): init 07:14:01Z, final call 08:29:53Z, elicitation 08:30Z, on time. T2 commit server time 08:30:23Z (deadline 13:00Z). T2 quotes 08:33:10Z-08:35:12Z. T3 quote tables computed ~08:37Z. |
| Per model call: requested model, recorded model, effort, tokens | Fable calls below. Elicitation: requested sonnet, recorded claude-sonnet-5-5. Channel check (x2): requested sonnet, recorded claude-sonnet-5-5. Deliberate calls (53 sub-agent transcripts incl. operators): recorded models {'claude-opus-5-5': 48, 'claude-fable-5-2': 5}; per-call requested/recorded models are in each call record under deliberate/K1-scored/calls/. Tokens: per-call subagent totals kept in the session; input/output split unreported. |
| Tool-record scan per arm: web access (count), market quotes in tool results (count) | Fable arm: see table (all 0/0; tools Read and Write only; files read: pack.md only). Elicitation: 0/0. Deliberate operator calls: web/browser tool uses 0; tool results mentioning a venue name 0. (Venue names appear in collector transcripts only; collectors are not model arms.) |
| Commitment fingerprint; push time; archive receipt | bundle 6ceccbb912a77fd1837353211ec7ddc31957c6765755e8a3c037175efad9cc38 (14 files); commitments/K1.json in commit 32cda45adecea0dede09f077bff353760dc37e18, server time 2026-11-26T08:30:23Z; archive https://web.archive.org/web/20261126083154/https://api.github.com/repos/mhlevinson/FOMC-forecast-pilot/commits/32cda45adecea0dede09f077bff353760dc37e18 (snapshot shows the sha and date) |
| Benchmark at T0 and T2: flags raised | T0: {"FOMC-2026-12": {"kalshi": ["one_sided:cut50", "one_sided:cut25"], "polymarket": [], "benchmark": []}, "FOMC-2027-01": {"kalshi": ["one_sided:cut50"], "polymarket": [], "benchmark": []}}  T2: {"FOMC-2026-12": {"kalshi": ["one_sided:cut50", "one_sided:cut25"], "polymarket": [], "benchmark": []}, "FOMC-2027-01": {"kalshi": ["one_sided:cut50"], "polymarket": [], "benchmark": []}} (all four venue captures valid at both times) |
| Forecast lines valid? Any scored under the failure policy? | All 11 valid (F01-F10, D_scored). None under the failure policy. |
| Diagnostics run on this pack | Twin Deliberate run (hike25 claim): see deviations.md for its status. |
| Deviations, in the runner's own words | See deviations.md (D1-D11 and later). |

## Fable arm detail

| Call | Requested | Recorded | Effort | Tokens | Web uses | Market terms in tool results | Parse |
|---|---|---|---|---|---|---|---|
| F01 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F02 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F03 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F04 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F05 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F06 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F07 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F08 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F09 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
| F10 | fable | claude-fable-5-2 | high | see usage in transcript | 0 | 0 | ok |
