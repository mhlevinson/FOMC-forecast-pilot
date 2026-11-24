# Run sheet - one checkpoint (protocol v4, frozen 24 Nov 2026; see `FREEZE.md`)

This sheet governs alone for a checkpoint. If it and `design.md` disagree, the runner records the disagreement in `deviations.md`, follows this sheet, and the principal adjudicates afterwards. Anything not written here is not done. A checkpoint runs unattended (amendment 13): the runner never waits for a person, and every decision it would have asked about is either fixed here or logged and left for the principal.

## Roles

| Role | Who | Sees |
|---|---|---|
| Principal | The lab's principal. Sets up the machine once (see "Standing setup"), reads the record afterwards, adjudicates deviations | Everything |
| Runner | A scheduled session started at T0. Conducts, records, commits, publishes. Forecasts nothing | Pack and forecasts. **Never opens the `private/market_*` folders before T3** |
| Document collector | The runner itself, driving the principal's Chrome through Claude in Chrome | Official pages only |
| Quote collector | One helper call on Sonnet, at T0 and again at T2, driving the same Chrome | Venue pages only. Reports file names, byte counts and fingerprints, never prices |
| Model arms | Ten Fable calls; Deliberate (scored run only) plus its elicitation step | The pack file and the question. Nothing else |

## Standing setup (done once by the principal, checked by the runner at every checkpoint)

- "Generate memory from chats" is paused for the whole pilot.
- One Chrome profile has the Claude extension enabled, with "Ask where to save each file before downloading" off, downloads to `~/Downloads`, and automatic downloads allowed for `[*.]federalreserve.gov`, `[*.]bls.gov`, `[*.]bea.gov`, `[*.]kalshi.com`, `[*.]polymarket.com`.
- On checkpoint days the Mac is awake from 08:45 to 15:00 Israel time, with Chrome and the Claude desktop app open.

## Folders

On the principal's machine, under the experiment folder: `repo/` (a clone of this repository, kept for reading) and `checkpoints/<ID>/` with `capture/`, `pack/`, `answers/`, `deliberate/`, `private/market_T0/`, `private/market_T2/`, `transcripts/`, `state.json`, `deviations.md`.
In the session workspace: `cp/<ID>/pack.md` (the only input file) and `cp/<ID>/answers/`.

## Before T0 (from 08:45)

1. Fetch this repository; record its commit in `state.json` and check the sha256 of every file listed in `protocol/FREEZE.md` against the value recorded there. A missing file or a mismatch is a failed checkpoint, logged; nothing runs.
2. Run the three test files in `protocol/`. All must pass, or the checkpoint fails, logged.
3. **Preflight.** Check the standing setup: (a) channel check: one fresh call of the type used by the Fable arm, run on model Sonnet, with the channel-check prompt in `prompts.md` (four yes/no questions, amendment 26); it must end CHANNEL CLEAN, meaning no venue name, no price or probability tied to the decision, and nothing about this experiment (names and descriptions of the principal's installed tools and skills do not count, amendment 25). No call is ever asked to list or reproduce what it was shown; (b) the agent type `fomc-pilot:pilot-forecaster` is available and has only Read and Write; (c) one test save in Chrome reaches `~/Downloads` within 30 seconds. A failed (a) or (b) means the model arms do not run and the checkpoint fails, logged. A failed (c) is retried once after 2 minutes; a second failure fails the checkpoint, logged.
4. Write `state.json`: checkpoint ID, questions, starting claim per `questions.md`, the scored run's name, planned T0 and deadline. Open `deviations.md`.

## T0 - evidence cutoff (09:00 Israel time)

5. Record T0 in UTC.
6. **Quote collector, capture T0.** For each address in `venues.md`, for each open question: navigate in Chrome, then run the save snippet with the name `fomcpilot-<ID>-T0-<venue>-<event>-<part>.json` (part: `markets`, `event`, or `book-<outcome>`). Its report lists only file names, byte counts and fingerprints.
7. **Verify on arrival.** Within 60 seconds of each collector's report, the runner lists `~/Downloads` from the machine's shell. Every reported file must be present with its reported size. The runner then computes each file's sha256 on disk and logs it; that is the file's fingerprint. Where the in-page fingerprint came back unredacted, the two must match. A missing or mismatched file is re-saved once at once, with its new capture time logged; a second failure is logged and that venue is invalid for that capture.
8. **Document collection.** For each index page in `sources.md`: navigate, save the page with the snippet as `fomcpilot-<ID>-idx-<n>.txt`, list the documents the rule selects, then save each as `fomcpilot-<ID>-doc-<class>-<nn>.txt`. A PDF is fetched from its own address and saved as `.pdf`. One line per saved file goes to `collector_log.jsonl` (kind index, document or pdf; file, address, class, title, publication time as stated or "not stated", retrieval time, in-page fingerprint, bytes, order with 1 = newest in its class). Verified on arrival as in step 7.
9. Move every verified `fomcpilot-<ID>-*` file from `~/Downloads` into `checkpoints/<ID>/` (documents to `capture/`, quote files to `private/market_T0/`). Touch no other file in Downloads. If the move fails because deletion is not permitted in `~/Downloads`, request delete permission once, for `~/Downloads` only; if it is not granted, copy the files, leave the originals, and log it (amendment 27).
10. A script copies the document lines of `collector_log.jsonl` unchanged into `capture_log.jsonl` and index lines into `index_log.jsonl`. PDFs are converted with `pdftotext -layout`; the text file is logged with its own fingerprint and the PDF's.
11. Run `pack_tools.build_pack` on `capture/`, with the cutoff set to T0. Outputs: `pack.md`, `manifest.json`, `pack.sha256`, `pack_diff.md`. Record pack-ready time. Copy `pack.md` to `cp/<ID>/pack.md` and check its fingerprint there.

**Save snippet** (the only way anything is saved; the page text is never re-typed by a model):

```js
const sha = async s => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))).map(b => b.toString(16).padStart(2, '0')).join('');
const text = document.body.innerText;
const a = document.createElement('a');
a.href = URL.createObjectURL(new Blob([text], {type: 'text/plain;charset=utf-8'}));
a.download = NAME;
a.addEventListener('click', e => e.stopImmediatePropagation());
document.body.appendChild(a); a.click(); a.remove();
({name: NAME, bytes: new TextEncoder().encode(text).length, sha256: await sha(text), url: location.href, title: document.title, at: new Date().toISOString()})
```

## T1 - forecasts

12. Dispatch the ten Fable calls together (fresh context each, model Fable, effort high, agent type `fomc-pilot:pilot-forecaster`, which can only read and write files) with the prompt in `prompts.md`. Each writes `cp/<ID>/answers/F01.md` ... `F10.md` and replies only DONE. Keep each call's tool record. Record requested model, recorded model, start and end time.
13. Run Deliberate (scored run) with the settings and starting claim in `prompts.md`, corpus `cp/<ID>/pack.md`. Before any dispatch, build every read-set file the run's dispatches name, from a written checklist, and check each exists. Each dispatch carries the call-record schema. Save the text of Deliberate's final call as `answers/D_scored_final.md`.
14. **Elicitation step** (amendment 15). One call, prompt in `prompts.md`, reads `D_scored_final.md` and writes `answers/D_scored.md`. Record its finish time.
15. One retry of a failed call with the identical message; then it is recorded as failed. An accepted answer file is never regenerated or overwritten. A call record the harness blocks is logged as missing; the runner never writes it for the operator. A call that writes its answer file but replies with more than DONE has not failed: the answer file governs, and the extra reply is logged without any numbers (amendment 28).
16. Run `forecast_tools.parse_forecast` on every answer file except `D_scored_final.md`. Write `forecasts.json`.

## T2 - commitment (by 15:00 Israel time)

17. At the deadline, any arm without an answer file has failed this checkpoint. Late output is kept, labelled late, never scored.
18. Run `pack_tools.commit_bundle` over `pack.sha256`, the answer files present (including `D_scored_final.md`) and `forecasts.json`. Push `commitment.json` to `commitments/<ID>.json` through the GitHub connector. Record the commit address and server time.
19. Witness: open `https://web.archive.org/save/<commit address>` in Chrome and record the archive address. If it fails, retry once after 2 minutes, then log and continue.
20. **Only now: quote collector, capture T2**, as in steps 6-7 with `T2` in the names. Move the files to `private/market_T2/`.

## T3 - disclosure

21. Run `venue_tools` on the T0 and T2 quote files. Write `quotes_T0.json`, `quotes_T2.json`.
22. Fill the compliance record (`design.md`, section 14), including the tool-record scan of every model call.
23. Publish to `ledger/<ID>/` through the GitHub connector: `pack.sha256`, `manifest.json`, `pack_diff.md`, the answer files, `forecasts.json`, `commitment_private.json`, the two quote tables, the compliance record, `deviations.md`, and `pack.md` split into numbered parts of at most 60 KB (`pack.part01.md`, ...) whose concatenation must reproduce `pack.sha256`. After the push, compare each file's git blob hash on GitHub with the local file; a mismatch is re-pushed once, then logged.
24. Save every call's transcript to `transcripts/` and copy the Deliberate run folder to `deliberate/`.
25. Send the principal a short notice: checkpoint done or failed, arms valid, commitment address. No prices.

## Never

- Never score anything before the question resolves.
- Never open, summarise or mention venue quotes before T3. Never pass a venue file, a venue name's price or a prior checkpoint's ledger to a model call.
- Never edit an answer, a pack or a prompt. Never repair a forecast line.
- Never save a page by copying its text through a model.
- Never resume a checkpoint on a later day.
- Never wait for a person. Never change this sheet during a checkpoint; a needed change is a deviation now and an amendment afterwards.
