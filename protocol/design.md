# Experiment design - v3 (22 Nov 2026) - supervised prospective pilot

**Status: DRAFT, not frozen.** The working copy lives in the lab's notebook until the freeze. At the freeze this file is replaced by the frozen text and its fingerprint is recorded.

**Rigor budget: audience = hostile reviewer. Scope = pilot.** v3 applies the lab's decisions of 22 Nov 2026 and a written design review of v2 (dispositions in section 17).

> **Bottom line.** This is a supervised pilot on two live questions: the December and January Fed decisions. At each checkpoint Deliberate and Fable forecast from the same pack of official documents. A fingerprint of their forecasts is committed in public before the market is measured, and the forecasts are disclosed after. Everything is scored the same way once the Fed decides.
>
> **What it can deliver.** An honest, witnessed record of what each system said and when; a diagnosis of where the pipeline works and breaks; and, if the Fed surprises, a pre-declared reading of whether Deliberate saw it coming (section 8).
>
> **What it cannot deliver.** Proof that any system forecasts better than another, or why. That needs a larger study, designed after this pilot shows where useful information is produced.

## A. Why run it at near-consensus (decision of 22 Nov)

The market puts the quarter-point hike near 90%. The design review warned that December may therefore teach little about the product. Decision: run it anyway. If the Fed does something the market treats as unlikely and Deliberate had lowered the consensus probability or named the outcome, that is a result worth the cost. The price of that bet is stated here in advance: roughly nine times in ten there is no surprise, and any distance Deliberate keeps from the consensus then costs it a little on the score (worked example in section 8).

## B. Standard of evidence - binding on every checkpoint, both questions

| # | Rule | Objection it answers |
|---|---|---|
| S1 | **Freeze before the first scored forecast.** Protocol, prompts, parser, scoring script and schedule are frozen, fingerprinted (sha256, a checksum that changes if one character changes) and registered publicly with an outside witness before any scored forecast is made. A scheduled checkpoint that falls before the freeze is forfeited. A later change creates a new version and a new cohort; earlier forecasts stay under the rules they were made under. | "You tuned the rules after seeing forecasts." |
| S2 | **Commit, then measure, then disclose.** At each checkpoint a fingerprint of the forecast bundle is committed publicly and witnessed. Only then is the market measured for the comparison. Only then are the forecasts disclosed. Every scheduled checkpoint appears in the ledger, including failures. | "Forecasts were edited afterwards", "only good runs were shown", and "publishing the forecast moved the market you measured." |
| S3 | **One question, defined by us; venues are close proxies.** The question and its resolution rule are written here. Both venues' full rules are archived and the known differences listed. | "The arms answered different questions." |
| S4 | **Same pack, built by rule, documents left whole.** All model arms get the identical pack from a small fixed source list. No model selects, trims or rewrites anything. The claim is narrow: the experiment supplies no market prices. Official documents are included as published, whatever they say about market expectations. | "The pack was curated" and "the isolation claim is stronger than the method." |
| S5 | **Market quotes never enter a model's inputs.** A separate collector captures quotes and hands back only file names and fingerprints. The runner does not open those files before disclosure. This is separation by construction of inputs plus an audit of every call's tool record, and is described as that. | "The models, or the runner, saw the price." |
| S6 | **Isolation is audited and disclosed.** The channel cannot strip tools from a call. Each model call's tool record is kept raw and scanned for web access and for market quotes in any tool result. Flagged calls are scored and reported both with and without. | "How do you know a call did not look things up?" |
| S7 | **Comparators are named for what they are.** The test is of the deployed Deliberate configuration against realistic alternatives. The ten-call Fable average is a cheap ensemble, not a compute-matched control. Latency and resource use are reported beside every score. | "The gain is just more compute or a different model." |
| S8 | **Fixed failure policy, stated denominators.** Section 8 says exactly how a failed, late or missing forecast is scored and what each average is taken over. | "Failures were quietly excluded." |
| S9 | **One primary comparison; no choosing among runs.** One comparison is primary. Everything else is exploratory. When Deliberate runs more than once on a pack, which run is scored is fixed before any of them starts. | "You reported the flattering measure, or the better run." |
| S10 | **Claims are capped by the register** (section C), in every post, essay and conversation. | "One lucky call presented as skill." |
| S11 | **Pin and record.** Per call: requested model, model recorded by the harness, plugin version, effort, prompt fingerprints, start and end times, tokens where reported ("unreported" where not). | "Which model produced this, and at what cost?" |
| S12 | **Raw records; a stranger can rebuild the score; publish either way.** Raw pages, raw venue responses and call transcripts are kept untruncated. A fresh session with no history rebuilds every score from the bundle before results are written. Results and corrections are published whichever way they fall, with the conflict of interest stated. | "We have to take your word for it." |
| S13 | **Diagnostics are labelled unscored before they run** and never enter a score. | "A test run was promoted to a result after the fact." |

**Three gates only.** No scored forecast before the freeze is public and witnessed. No forecast counts after its availability deadline. No pack, no checkpoint. Everything else is logged, audited afterwards and adjudicated by the lab's principal.

## C. Claims register

| Situation | May be said | May not be said |
|---|---|---|
| Any pilot result | "At these committed checkpoints, each system gave these probabilities; here is how each scored." | Better or worse forecaster. "Beat the market." Any statement of skill. |
| A surprise that Deliberate caught in part or called (definitions in section 8) | "Before the decision, in a record committed in advance, Deliberate gave X% to the outcome the market benchmark gave Y%." Stated together with: the anchor check, both Fable figures, and Deliberate's false alarms. | "Deliberate predicts what markets miss." Any wording that drops "one event." If the anchor check fails: any wording that hides that the result depended on the starting claim. |
| No surprise | Agreement or disagreement with the benchmark, checkpoint by checkpoint, and what the diagnostics showed. | "Deliberate matched the market" as evidence of quality. |
| Deliberate against Fable | The score difference for this configuration, with latency and resource use. | "The method adds value" or "structured deliberation beats a plain model." The pilot does not isolate method from model mix, compute, starting claim or probability format. |
| The benchmark | "A two-venue synthetic benchmark from midpoints." | "The market probability." Any suggestion of a tradable edge. |
| The channel | Model identity as the harness records it; isolation as audited. | "Wire-verified." "No call could reach the web." |

## D. Decisions taken (22 Nov 2026)

| # | Decision |
|---|---|
| 1 | No back-dated replay until a Deliberate version can search a dated copy of the web. A resolved meeting may be used only to test software. |
| 2 | January is a second live question. One January checkpoint runs before 9 Dec so later ones show the effect of the December decision. |
| 3 | Deliberate starts from a fixed rule claim (section 2). |
| 4 | Budget: 20 Deliberate runs, 10 Fable calls per checkpoint. |
| 5 | Public registry: this repository plus a one-time protocol registration at a recognised registry such as OSF. |
| 6 | Documents and venue quotes are captured with a browser on the lab's machine. |
| 7 | Public: forecasts and Deliberate's final call. Full run folders are fingerprinted at commitment and shown to a reviewer on request. |
| 8 | No outside human reader before the freeze. Every write-up says so. |

## 1. The question and the venues

> By how many basis points will the FOMC change the upper bound of the federal funds target range in the statement released after its 8-9 December 2026 meeting, compared with the upper bound in effect immediately before the meeting? Outcomes: cut of 50 bp or more; cut of 25 bp; no change; hike of 25 bp; hike of 50 bp or more.

- **Resolution.** Read from the FOMC statement on the scheduled decision day: new upper bound minus the upper bound before the meeting. A move that is not a multiple of 25 is rounded up to the next 25.
- **No statement on the scheduled day:** the question is void and reported unscored. The protocol does not guess what the venues will do in that case.
- **January question:** same text for the 26-27 January 2027 meeting. Its contract identifiers are added before the freeze.

| Our outcome | Kalshi contract | Polymarket contract |
|---|---|---|
| Cut 50+ | Cut >25bps (KXFEDDECISION-26DEC-C26) | 50+ bps decrease |
| Cut 25 | Cut 25bps (-C25) | 25 bps decrease |
| Hold | Fed maintains rate (-H0) | No change |
| Hike 25 | Hike 25bps (-H25) | 25 bps increase |
| Hike 50+ | Hike >25bps (-H26) | 50+ bps increase |

- **Proxies, not identical questions.** Each venue's full rule text is saved into this folder before the freeze. Known differences so far: the venues treat a cancelled meeting or missing statement differently from each other and from this protocol. Any difference in how a venue finally resolves is reported.
- Links: [Kalshi KXFEDDECISION-26DEC](https://kalshi.com/markets/kxfeddecision/fed-meeting/kxfeddecision-26dec), [Polymarket "Fed Decision in December?"](https://polymarket.com/event/fed-decision-in-december-20260729232808632).

## 2. The arms

| Arm | What it is | Role |
|---|---|---|
| **D - Deliberate as deployed** | Deliberate 0.5.0: lock mode auto (no pause for a human), probes closed (no web), descriptive question, one attack cycle, default model settings (a mix of Fable and Opus), fixed starting claim, forecast line | The system under test |
| **F1 - Fable one-off** | The first of ten Fable 5.2 calls, effort high, neutral forecasting prompt, forecast line | "Just ask the model" |
| **F10 - Fable ten-call average** | Plain average of the ten calls | A cheap ensemble. Not a compute-matched control |
| **B - Benchmark** | Two-venue synthetic benchmark (section 6) | The market reference |

**The starting claim is part of the system under test.** Deliberate needs a claim to attack and defend; Fable gets a neutral question. That difference is part of what "Deliberate as deployed" means here and is named in every write-up.

**Rule for the claim, fixed for every checkpoint:** *the FOMC will make the same change as at its most recent concluded scheduled meeting.* The October meeting left the range unchanged, so for every checkpoint before 9 Dec the claim is "no change", for both questions. After 9 Dec the January claim becomes whatever the December meeting did.

> At its 8-9 December 2026 meeting the FOMC will leave the target range unchanged, as it did at its previous meeting. Whatever the verdict on this claim, the final answer must end with one line in exactly this form, in percentages to one decimal place that sum to 100, none 0 or 100:
>
> `FORECAST | cut50=__ ; cut25=__ ; hold=__ ; hike25=__ ; hike50=__`

**Which Deliberate run is scored (S9).** One run per checkpoint with the rule claim, named as the scored run before dispatch. Any other run on the same pack is a diagnostic (section 9).

## 3. Reading the forecast: a line and a parser, no model

- Every model arm must end its final answer with the FORECAST line above.
- A small script (`forecast_tools.py`) reads that line. No model reads, copies or interprets a forecast.
- **Valid:** exactly one distinct FORECAST line in the final answer; all five outcomes present; each value above 0 and below 100; sum between 99.5 and 100.5 (then rescaled to 100).
- **Invalid, scored under the failure policy:** no line; two different lines; a missing outcome; a value out of range; a sum outside the band.
- The line governs. Nothing else in the answer is read, even if a table elsewhere disagrees.
- **Tested before the freeze on made-up answers** (`test_forecast_tools.py`): two conflicting lines, missing outcome, decimals instead of percentages, bad rounding, malformed text, a final line that contradicts an earlier table.
- **If the rehearsal shows Deliberate does not reliably produce the line:** one added step that states the line from Deliberate's final call becomes a named, frozen part of the system, and the arm is called "Deliberate plus elicitation step" everywhere.

## 4. The evidence pack

**Small enough to be provably complete.**

| Source (one index page each) | What is taken |
|---|---|
| Federal Reserve Board - FOMC calendar page | Latest statement, implementation note, minutes, projections and press-conference transcript that are posted at the cutoff |
| Federal Reserve Board - speeches and testimony pages | Every Board member speech and testimony since the last FOMC meeting |
| Federal Reserve Board - Beige Book page | Latest Beige Book |
| BLS | Latest Employment Situation and CPI news releases |
| BEA | Latest Personal Income and Outlays and GDP news releases |

- **Inclusion rule:** a document is in if it is listed on its index page when that page is captured at the cutoff. The saved index page is the proof. This avoids arguing about publication dates.
- **Whole documents.** No trimming, no quotas, no word filter. If the rehearsal shows a size ceiling is needed, the only permitted drop is oldest speeches first, set once and frozen.
- **Left out on purpose, and named as a limit:** regional bank presidents' speeches, interviews, other data releases, all news and analysis, all market prices.
- **Per-document manifest:** source and address; publication time as stated by the source, with uncertainty noted; retrieval time; fingerprint of the saved page; extraction version; included, omitted or dropped; position in the pack; count of passages that mention market pricing (disclosed, not removed).
- **Pack-difference report** against the previous checkpoint: added, revised, dropped. So a change in forecast can be set beside a change in evidence.
- **Extraction check in the rehearsal:** headline figures from each data release's tables must appear in the extracted text.
- One pack serves both questions on the same day.

## 5. One checkpoint: four times, three roles

| Time | What happens | Who |
|---|---|---|
| **T0 - evidence cutoff** | Index pages and documents captured; pack built and fingerprinted. Benchmark captured. | Runner builds the pack. Collector captures quotes. |
| **T1 - forecast ready** (per arm) | Ten Fable calls and the scored Deliberate run finish. Each arm's finish time is logged. | Model calls. They receive the pack and the question, nothing else. |
| **T2 - commitment** | Fingerprint of the bundle (pack, forecasts, Deliberate final call, a random salt) is pushed to this repository and witnessed. Then the benchmark is captured again. | Runner commits. Collector captures quotes. |
| **T3 - disclosure** | Forecasts, pack, raw quote files and the compliance record are pushed in clear. | Runner. |

- **Two comparisons, named separately.** *Deployment* (primary): forecasts against the benchmark at T2, when the forecasts actually existed. *Information cutoff* (secondary): forecasts against the benchmark at T0.
- **Availability deadline.** T0 is 09:00 Israel time. T2 must happen by 15:00 Israel time the same day. An arm not finished by then has failed that checkpoint; its late output is kept, labelled late and never scored. A run never resumes into the next day as the earlier day's forecast. The six-hour window is confirmed in the rehearsal and then frozen.
- **Why mornings.** US data releases land at 15:30 Israel time, after the deadline, so no scheduled release falls between cutoff and commitment.
- **The collector** is a separate call. It saves raw venue responses to a folder no model call is given and returns only file names and fingerprints. The runner does not open that folder before T3.
- **Witness.** This repository's server-side push time, plus a capture of the commitment page by an independent web archive. Git timestamps alone are not treated as proof. The repository blocks rewriting of history.
- **Supervision.** The lab's principal starts every checkpoint and is reachable until T3. No unattended runs in the pilot.

## 6. The benchmark

- **Per contract:** midpoint between best bid and best ask.
- **Per venue:** the five midpoints divided by their sum.
- **Benchmark:** plain average of the two venue vectors. It is a synthetic reference, not a price anyone could trade at.

**Checks and failure handling, fixed in advance**

| Case | Handling |
|---|---|
| Identifier check | Each response must name the expected contract and question text. An empty or mismatched response is a failed capture, even if the request "succeeded" |
| Kalshi asks | Derived from the opposite side of the book where the venue reports bids only; the rule is written into the adapter and tested in the rehearsal |
| One-sided or empty book on a contract | Last trade if within 24 hours, flagged; otherwise that venue's vector is invalid for this capture |
| Bid-ask gap over 10 points | Used, flagged wide |
| Five midpoints sum outside 95-105 | Used after scaling, flagged incoherent |
| Contracts captured more than 5 minutes apart | Recapture once; then flagged |
| One venue invalid | Benchmark is the other venue alone, flagged |
| Both venues invalid | No benchmark; the checkpoint has no paired comparison (section 8) |

Saved for every capture: raw responses, order-book quantities, identifiers, capture times, the sum before scaling.

**Worked example (quotes read 20 Nov 2026).**

| Outcome | Kalshi midpoint | Polymarket midpoint | Kalshi, scaled | Polymarket, scaled | Benchmark |
|---|---|---|---|---|---|
| Cut 50+ | 0.5 | 0.15 | 0.5 | 0.1 | 0.3 |
| Cut 25 | 0.5 | 0.25 | 0.5 | 0.2 | 0.4 |
| Hold | 4.5 | 3.8 | 4.4 | 3.8 | 4.1 |
| Hike 25 | 90.5 | 92.5 | 89.2 | 91.9 | 90.5 |
| Hike 50+ | 5.5 | 3.95 | 5.4 | 3.9 | 4.7 |
| Sum | 101.5 | 100.65 | 100 | 100 | 100 |

## 7. Schedule

Every checkpoint: cutoff 09:00, deadline 15:00, Israel time. Operating dates were chosen for completeness of documents, not for speed of reaction. The pilot does not test who reacts faster to news.

| ID | Date | Question | What is new in the pack |
|---|---|---|---|
| R | Before the freeze | December (unscored) | Dress rehearsal, section 11 |
| K1 | Thu 26 Nov 2026 | December | October PCE, Q3 GDP revision, Beige Book |
| K2 | Mon 30 Nov 2026 | December | Blackout has begun; last speeches are in |
| K3 / J1 | Sun 6 Dec 2026 | December and January | November jobs report |
| K4 | Tue 8 Dec 2026 | December | Final December checkpoint |
| J2 | Thu 10 Dec 2026 | January | December decision and projections. Committed before that day's CPI release |
| - | Thu 10 Dec 2026 | December | Resolve, rebuild scores, publish |
| J3 | Thu 24 Dec 2026 | January | November CPI and PCE |
| J4 | Sun 10 Jan 2027 | January | December jobs report |
| J5 | Thu 14 Jan 2027 | January | December CPI |
| J6 | Tue 26 Jan 2027 | January | Final January checkpoint |

- K1 is forfeited under S1 if the freeze is not public and witnessed by 09:00 on 26 Nov.
- J2's update reflects the December decision without that morning's CPI. J3 onward mix several releases; no single update is attributed to a single release.
- If the December debrief changes the protocol, later January checkpoints run as a new cohort (S1).

## 8. Scoring

**Score:** Brier score over the five outcomes (the sum of squared gaps between the stated probabilities and what happened; 0 is perfect, 2 is worst), averaged over a question's checkpoints.

**Primary comparison (the only one):** Deliberate against the benchmark, deployment timing, end-to-end view. Reported as numbers. No verdict.

**Two views, with their denominators**

| View | Counts | Failure handling |
|---|---|---|
| **End-to-end** (headline) | Every scheduled checkpoint after the freeze | A model arm with no valid forecast line by the deadline scores as 20% on each outcome. A failed Fable call is filled the same way before the ten are averaged. A checkpoint that never ran counts as a failure for every model arm |
| **Conditional on delivery** (secondary) | Only forecasts actually delivered on time | None needed |

- **Benchmark missing:** that checkpoint drops out of paired comparisons in both views and is listed. The benchmark is never filled in. For a checkpoint that never ran, the benchmark is rebuilt from the venues' price history at the deadline time and flagged as rebuilt.

**The surprise reading, fixed before any forecast (applies to each question's final checkpoint, deployment timing)**

| Term | Definition |
|---|---|
| Surprise | The outcome that happened had less than 20% in the benchmark |
| Caught in part | Deliberate's probability on that outcome was at least 10 points above the benchmark's and at least double it |
| Called | That outcome was Deliberate's top outcome |
| False alarm | An outcome that did not happen on which Deliberate stood 10 points or more above the benchmark. Reported for every checkpoint, surprise or not |
| Anchor check | The twin run's probability on the same outcome (section 9). If the surprise is the outcome named in the starting claim and the twin run does not itself meet "caught in part", the result is reported as dependent on the starting claim |

**Worked example.** Benchmark on 20 Nov: hold 4.1, hike 25 at 90.5, hike 50+ at 4.7. Suppose Deliberate's final line says hold 15, hike 25 at 78, hike 50+ at 6.

- If the Fed hikes 25 (no surprise): benchmark 0.013, Deliberate 0.075. Deliberate pays a small price for its doubt.
- If the Fed holds (a surprise): benchmark 1.74, Deliberate 1.33. "Caught in part" is met: 15 is more than 10 points above 4.1 and more than double it. Whether it may be reported plainly then depends on the anchor check, because "hold" is also the starting claim.

**Exploratory, always labelled so**

- Information-cutoff comparison; Deliberate against F1 and F10; each venue alone.
- Log score (punishes confident misses harder; values under 0.5% treated as 0.5%) and ranked probability score (credits near misses, since the outcomes are ordered).
- **Did the benchmark later move toward the forecast?** Measured on one outcome fixed at the question's first scored checkpoint (the benchmark's top outcome then), from each checkpoint's T2 to the next checkpoint's T0. Moves under 1 point count as unchanged and are reported. Descriptive only: shared reaction to later news, drift away from extremes and overlapping intervals can all produce apparent hits.
- The spread of the ten Fable calls, reported as run-to-run variability under one prompt. It is not a significance test.
- Latency (T1 minus pack ready) and resource use per arm.

**Verdict cap.** The pilot ends as Ambiguous, with the direction and the surprise reading described, or Inconclusive if fewer than three checkpoints were scored on a question. Confirms and Refutes are not available to a pilot.

## 9. Diagnostics (unscored, labelled before they run)

| Diagnostic | What it is | When | Why |
|---|---|---|---|
| **Twin run** | Deliberate on the same pack with the opposite starting claim, set by rule: a 25 bp move in the direction of the FOMC's most recent change (today: "hike 25"). If the rule claim is itself a 25 bp move, the twin is "no change" | K1-K4, J1, J2, J6 | Shows how much the answer follows the claim it was handed. Required for the anchor check |
| **Repeat run** | Deliberate twice on the same pack with the same claim | Rehearsal | Shows run-to-run variability |
| **Parser tests** | Made-up answers through the parser | Before the freeze | Section 3 |

Budget: 3 rehearsal runs, 8 for December (4 scored, 4 twins), 9 for January (6 scored, 3 twins). 20 in total.

## 10. What the runner must do

- Stable IDs for question, checkpoint, arm and call.
- One retry of a failed call with the identical message; then recorded as failed.
- A completion record written once per call, after its output is saved. Accepted outputs are never regenerated or overwritten.
- Full transcripts kept, saved only after a call has ended.
- Statuses: on time, late, failed, not run.
- Resume picks up unfinished calls only, and only before the deadline.
- A deviations file in the runner's own words.
- Models requested and recorded per call; the working folder of a model call holds only the pack.

## 11. Dress rehearsal (before the freeze, supervised, unscored)

One complete run of a checkpoint on the live December question, labelled rehearsal before it starts and published as such. Forecasting wording in the prompts is fixed before the rehearsal; only mechanics may change after it (format, parser, pack size ceiling, timings), and the list of changes is published with the freeze.

It must answer:

1. Does every model arm demonstrably receive the same intended pack?
2. Does Deliberate reliably end on one valid FORECAST line? (Two repeat runs and one twin run.)
3. Does the runner keep every accepted output and resume safely?
4. Are quotes captured at T0 and T2 without reaching any model call or the runner?
5. Can a fresh session rebuild the scores from the saved bundle alone?

Plus the channel check: list what the harness puts in front of a model call (date, tool list, skill list, any stored memory) and scan it for market quotes and for anything about this experiment; confirm the recorded model changes when a different one is requested; confirm the web-archive capture works.

## 12. Limits declared in advance

- **A weak result has many possible causes.** Deliberation adds nothing to forecasting; the forecast-line interface is poor; the starting claim anchors the answer; the pack leaves out what decided the outcome; the domain is already forecast efficiently; or the tool improves reasoning without improving the numbers. The pilot cannot tell these apart. The diagnostics narrow two of them.
- **A strong result is one event.**
- **Not a test of method.** Model mix, compute, starting claim and answer format all differ between Deliberate and Fable.
- **The market knows more.** Model arms see a small set of official documents. This runs against the model arms.
- **Official documents may describe market expectations.** They are not removed.
- **The benchmark is synthetic** and says nothing about tradable edge.
- **Isolation is audited, not guaranteed.** Model identity is as the harness records it.
- **Everything, including the runner, is Claude.**
- **No outside human reader before the freeze** (decision 8).

## 13. Records and publication

```
This repository (history rewriting blocked)
  protocol/     this file, run sheet, question files, prompts, source list,
                venue rule texts, parser and scoring tools, schedule
  commitments/  one fingerprint file per checkpoint, pushed at T2, with the archive receipt
  ledger/       per checkpoint, pushed at T3: pack + manifest + difference report, forecasts,
                Deliberate final call, raw venue files, benchmark, compliance record
  rehearsal/    rehearsal bundle and the list of changes made after it
  results/      scores, chart, rebuild report, corrections

Kept privately by the lab
  everything above, plus full Deliberate run folders and raw call transcripts
```

- **Rebuild before results (S12).** A fresh session gets only the bundle and checks: freeze unchanged; each commitment witnessed before its T2 capture and before the outcome; disclosed forecasts match their commitment; pack built to rule; tool-record scan; scores rebuilt from the forecast lines; every scheduled checkpoint accounted for. PASS, FAIL or CANNOT VERIFY per item, published as written.
- **Corrections** are dated entries with before and after figures.
- **Line for every write-up:** "The Computational Deliberation Lab builds Deliberate and ran, scored and published this pilot itself. The protocol was frozen and every forecast committed in public before the outcome. No outside reader reviewed the protocol before the freeze."

## 14. Compliance record (filled and published at every checkpoint)

| Field | Value |
|---|---|
| Question, checkpoint, protocol fingerprint in force | |
| Pack fingerprint; documents included, omitted, dropped; market-pricing passages (count) | |
| T0, each arm's T1, T2, T3; status of each arm (on time, late, failed) | |
| Per model call: requested model, recorded model, effort, tokens or "unreported" | |
| Tool-record scan per arm: web access (count), market quotes in tool results (count) | |
| Commitment fingerprint; push time; archive receipt | |
| Benchmark at T0 and T2: flags raised (wide, incoherent, one venue, last trade used) | |
| Forecast lines valid? Any scored under the failure policy? | |
| Diagnostics run on this pack | |
| Deviations, in the runner's own words | |

## 15. Checked versus assumed (22 Nov 2026)

| Item | Status |
|---|---|
| Kalshi and Polymarket top-of-book quotes for the five December contracts are readable | Checked 20 Nov |
| Deliberate 0.5.0 supports lock mode auto with probes closed | Checked in the plugin files |
| Parser and scoring tools pass their tests, including the worked examples above | Checked 22 Nov |
| How each venue's order book reports bids and asks; Polymarket's rule on a missing statement | Taken from the design review's reading of the venues' documentation; confirmed in the rehearsal |
| A browser on the lab's machine can save raw venue responses and page text unaltered | Assumed - rehearsal |
| An independent web archive can capture the commitment page | Assumed - rehearsal |
| Deliberate ends on one valid FORECAST line | Assumed - rehearsal |
| Pack size Deliberate can take; six-hour window is enough | Assumed - rehearsal |
| January contract identifiers | Not yet checked |
| Exact models, or only model families, can be pinned on this channel | Not yet checked |

## 16. Build checklist

- [x] Public repository created
- [x] Parser and scoring tools written and tested on made-up answers and forecasts
- [ ] History rewriting blocked on this repository
- [ ] Source list, question files, venue rule texts, prompts written
- [ ] Collector and benchmark adapter written, with the checks in section 6
- [ ] Run sheet written (two pages)
- [ ] Dress rehearsal run; five questions answered; channel check done
- [ ] Changes after rehearsal listed
- [ ] Freeze: fingerprint, public push, archive capture, registry receipt
- [ ] Rebuild prompt written before the first scored checkpoint
- [ ] K1 onward, each started by the lab's principal

## 17. Amendment log and review dispositions

| Date | Change | Why | Favours | Forecast or outcome data existing |
|---|---|---|---|---|
| 20 Nov 2026 | v1 to v2: standard of evidence and claims register added; public ledger; pack built by rule; failures scored | Rigor budget set to hostile reviewer | No arm | None |
| 22 Nov 2026 | v2 to v3: reframed as a supervised pilot; replay removed; commit-measure-disclose with a separate quote collector; two named comparisons; forecast line and parser replace the card reader; starting claim defined mechanically and named as part of the system; twin-run diagnostic; reduced source list with manifest and difference report, word filter removed; benchmark failure handling; one primary comparison; denominators defined; freeze moved to before the first scored forecast; pooled 30-question test removed; surprise reading pre-declared; schedule moved to mornings with a deadline; unattended runs removed | The lab's decisions and the design review of v2 | No arm; narrows what may be claimed | None |

**Design review of v2 (received 22 Nov 2026) - dispositions**

| Review point | Disposition |
|---|---|
| No common forecast time; publishing before measuring | Accepted. Four times defined; commit, measure, disclose; deployment comparison primary (section 5) |
| No compute-matched baseline; F10 is not a compute control; spread is not a significance threshold | Accepted. Test is of the deployed system; wording changed (S7, sections 2 and 8) |
| Starting claim is inconsistent and confounds the treatment | Accepted. Rule defined; named as part of the system; twin run added (sections 2 and 9) |
| Probability extractor can become a forecaster | Accepted. Fixed line and deterministic parser (section 3) |
| Evidence pack underspecified; quotas, publication time, extraction | Accepted. Source list cut down; listed-at-cutoff rule; manifest; difference report (section 4) |
| Market-word filter is weak | Accepted, and taken further: the filter is removed and the claim narrowed (S4) |
| Venue-specific collection and missing cases; benchmark label | Accepted (section 6) |
| Contract equivalence | Accepted. Venues are proxies; rules archived; missing statement voids the question (section 1) |
| 30 questions and 8 events; three primary comparisons | Accepted. Pooled test removed from this protocol; one primary comparison |
| "Every forecast counts" not operational | Accepted. Two views with denominators (section 8) |
| Amendment window closes too late | Accepted (S1) |
| "Market moved toward us" is descriptive | Accepted (section 8) |
| Drop the replay | Accepted (decision 1) |
| Operational risk; no unattended runs; Git is not a witness | Accepted (sections 5, 10, 13) |
| Calendar: CPI after the decision; next-day checkpoints; January attribution | Accepted (section 7) |
| Run a dress rehearsal before adding protocol | Accepted (section 11) |
| A near-consensus Fed decision may be a poor test of Deliberate | Noted and overruled by the lab (section A). The bet and its price are stated in advance; the pilot is framed as diagnosis plus a pre-declared surprise reading |
