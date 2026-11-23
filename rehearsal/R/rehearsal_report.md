# Dress rehearsal R - results of the rehearsal-only steps (REHEARSAL, unscored)

Written by the runner on 23 Nov 2026 after T3. Sources are the files under `checkpoints/R/` and the reports of the helper calls named below.

## 1. Channel check (design section 11)

Two fresh helper calls were asked, with no tools, to list everything they were shown before their prompt and to search it for venue names, prices and this experiment. One was the agent type used by the Fable arm (general-purpose, model fable). The other was the Deliberate operator type (model opus).

| Finding | Fable-arm type | Deliberate operator |
|---|---|---|
| The principal's memory summary (profile, preferences, a list of about 75 memory files with one-line descriptions) is in the context | yes | yes |
| That list names the experiment: "Deliberate vs prediction markets - Fed decision, 8-9 Dec 2026", alias "Predicting Dec 26 FOMC Decision" | yes | yes |
| It names Kalshi and Polymarket (in an unrelated business-idea entry) | yes | yes |
| Any price, probability or percentage tied to the Fed decision | none | none |
| Tools that can reach the world or the memory store | web search, web fetch, memory read and list | none (no web tools by construction) |
| CLAUDE.md or project instructions | none | none |

Verdict: CHANNEL HIT. No market numbers reached any model call through its context. But every call, the model arms included, was told that the principal runs a "Deliberate vs prediction markets" experiment on this meeting. The Fable arm also had web and memory tools available. Its answers contain no web addresses and no venue names, but the harness kept no tool transcripts, so whether a Fable call used those tools is unverified.

## 2. Fresh-session rebuild from the published bundle

A fresh helper call (model sonnet) cloned the public repository and used only `rehearsal/R/` and `protocol/`.

- Commitments: MATCH. `verify_bundle` reproduces both fingerprints, 71f8c3ef... (13 files) and 153a592e... (3 files). This needed `pack.sha256`, which was not published. The helper rebuilt it from `pack.md` as the pack hex followed by one newline (65 bytes); the version without the newline does not match.
- Forecasts: MATCH. `parse_forecast` on all 12 answer files reproduces `forecasts.json` and `forecasts_twin.json` field by field.
- Benchmarks: MATCH, exact. The venue vectors and benchmarks for T0, T2 and T2r were recomputed from the stored quotes. The step from raw responses to quotes cannot be rerun, because the raw files are private by design.
- Time: about one minute of compute.

`pack.sha256` was published after this check, so the bundle now rebuilds with no assumptions.

## 3. Extraction check

The pack (21 documents, 60,724 words) contains, in extracted text, each headline figure checked:

- the October core CPI line;
- payrolls +165,000;
- Q3 GDP 3.4 percent;
- September PCE 3.6 percent;
- unemployment 4.1 percent;
- the range "3-3/4 to 4 percent";
- the September dot counts at 4.375, 4.125 and 3.875;
- the minutes' "high probabilities assigned to a 25 basis point hike" line;
- the dissents' "preferred to raise the target range".

The next meeting's dates are written with an en dash ("December 8–9"). Two model calls reported passages that looked blank in their copy (some forward-looking lines, and closing lines of a Waller speech). That is not yet traced: it may come from the strip step inside Deliberate rather than from extraction.

## 4. Step timings (UTC, 23 Nov 2026)

| Step | Start | End | Wall time | Note |
|---|---|---|---|---|
| Setup: clone, tests, push check | 05:53 | 05:57 | 4 min | |
| T0 recorded | 07:06:35 | | | |
| Quote collector, T0 | 07:07:42 | 07:09:21 | 2 min | files reached disk only at 09:47 (manual save) |
| Stall: downloads awaiting manual save | 07:10 | 09:47 | 2 h 37 min | not a protocol step |
| Document collector, clean pass | 09:47:37 | 09:51:35 | 4 min | |
| Fed downloads (modal fix, runner saves) | 09:55 | 10:58 | about 1 h | about 4 min once the fix was in |
| Pack build | 10:58:36 | 10:58:50 | under 1 min | |
| Fable arm, 10 calls in parallel | 10:59:58 | 11:02:22 | 2.5 min | |
| Deliberate, scored run | 11:09:20 | 12:38:45 | 1 h 29 min | final answer at 12:21:33 (72 min) |
| Commit and push | 12:42:21 | 12:42:40 | under 1 min | |
| Archive witness | | 13:04:26 | | |
| Quote collector, T2 | 13:05:20 | 13:07:10 | 2 min | 23 of 24 files never reached disk |
| Deliberate, twin run | 13:07 | 14:19:23 | 1 h 12 min | final answer at 14:02:46 (55 min) |
| T2r late re-capture | 15:27:02 | 15:29:54 | 3 min | principal saved each file |
| T3: quote tables, compliance record | 15:31 | 15:35 | 4 min | |
| T3: publish to GitHub | 15:35 | about 16:10 | about 35 min | connector one file at a time; pack uploaded by the principal |

Estimated clean run, with downloads working and the push done by git: T0 to T2 about 2 h 45 min, of which the scored Deliberate run is about 1.5 h; T3 about 15 min. A six-hour window holds one scored run with margin. It does not hold the scored run, a repeat and a twin in sequence unless the runs go in parallel.

## 5. Plan usage (as read by the principal)

| Reading | All models | Fable only |
|---|---|---|
| 1 - before the first model call | 23% | 24% |
| 2 - after the ten Fable calls | 27% | 31% |
| 3 - after the scored Deliberate run | 32% | 34% |
| 4 - after the twin Deliberate run | 37% | 36% |

Per arm:

- Ten Fable calls: +4 points all models, +7 points Fable only; about 2.18 million subagent tokens.
- One Deliberate run: about +5 points all models, +2 to +3 points Fable only (its five Fable calls); about 5.8 to 6.7 million subagent tokens.

The runner's own work is inside the all-models figures and cannot be separated out. Inference: a scored checkpoint with ten Fable calls and three Deliberate runs costs about 19 points of the all-models meter.

## 6. Candidate amendments (for the principal; nothing is changed by this report)

1. **Channel.** Run checkpoints with memory off. Either use an incognito chat or turn off "Generate memory from chats" in Settings for the checkpoint. Then repeat the channel check and require CHANNEL CLEAN before T0.
2. **Fable arm tools.** Dispatch the Fable calls on an agent type with no web and no memory tools, as the Deliberate operator type already is. Keep each call's tool record so that design §14's tool-record scan can actually be done.
3. **Downloads.** Add `a.addEventListener('click', e => e.stopImmediatePropagation());` to the save snippet for every page, not only federalreserve.gov. After each collector pass, the runner checks that every reported file is on disk before the collector ends. A collector that saves N files must see N files arrive.
4. **T2 capture.** Treat a T2 file missing from disk as a failed capture at once, and retry within minutes, not hours. Record the retry time.
5. **Forecast line.** Add a frozen elicitation step after Deliberate's last Closer call. One short call reads `closer-final.md` and outputs only the FORECAST line on a line of its own; the parser reads that file. Test the parser on a real final call before the freeze. Both rehearsal runs failed on this.
6. **Conductor read-sets.** Every relocation script the conductor needs (future-backwards, all-headers, briefs, variant ledger) is built and checked before dispatch, from a written checklist. Give operators the call-record schema in the dispatch, so that they do not open other calls' records to copy it.
7. **Blocked call records.** The permission classifier blocked one operator's record write. Decide in advance what the conductor does then: record the gap, never write it for the operator.
8. **Publishing.** Push with git from the principal's machine, set up once with `gh auth login`. The connector cannot carry the pack and changes `\u` escapes. Publish `pack.sha256` with the bundle and add it to the step 23 list.
9. **Deadline.** Run the twin and the repeat in parallel with the scored run, or drop the twin from scored checkpoints. Sequential runs take about 1.2 h each.
10. **Clean-up.** The `fomcpilot-*` files in Downloads stay there. Decide whether the runner moves them into the checkpoint folder after verification.
