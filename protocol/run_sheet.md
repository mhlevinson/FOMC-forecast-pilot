# Run sheet - one checkpoint (DRAFT for the dress rehearsal - not frozen)

This sheet governs alone for a checkpoint. If it and `design.md` disagree, stop and ask the principal. Anything not written here is not done. When unsure, ask the principal; never improvise.

## Roles

| Role | Who | Sees |
|---|---|---|
| Principal | The lab's principal. Starts the checkpoint, approves the downloads and folder access, stays reachable until T3 | Everything |
| Runner | The main session. Conducts, records, commits. Forecasts nothing | Pack and forecasts. **Never opens the `private/market_*` folders before T3** |
| Document collector | One helper call on a cheaper model | Official pages only |
| Quote collector | A separate helper call on a cheaper model, at T0 and again at T2 | Venue pages only. Reports file names and fingerprints, never prices |
| Model arms | Ten Fable calls; Deliberate (scored run, then twin run) | The pack file and the question. Nothing else |

## Folders

On the principal's machine, under the experiment folder: `repo/` (a clone of this repository, pulled at the start) and `checkpoints/<ID>/` with `capture/`, `pack/`, `answers/`, `deliberate/`, `private/market_T0/`, `private/market_T2/`, `transcripts/`, `state.json`, `deviations.md`.
In the session workspace: `cp/<ID>/pack.md` (the only file there) and `cp/<ID>/answers/`.

## Before T0

1. Pull `repo/`. Record the commit in `state.json`. After the freeze: check it against the frozen fingerprint.
2. Run the three test files in `repo/protocol/`. All must pass.
3. Write `state.json`: checkpoint ID, questions, starting claim and twin claim per `questions.md`, which Deliberate run is scored, planned T0 and deadline.
4. Open `deviations.md`. Every departure from this sheet goes there, in the runner's words, when it happens.

## T0 - evidence cutoff (09:00 Israel time)

5. Record T0 in UTC.
6. **Quote collector, capture T0.** For each address in `venues.md`, for each open question: navigate to it, then run the save snippet below with the name `fomcpilot-<ID>-T0-<venue>-<event>.json`. Its report lists only file names, byte counts and fingerprints.
7. **Document collector.** For each index page in `sources.md`: navigate, save the page with the snippet as `fomcpilot-<ID>-idx-<n>.txt`, list the documents the rule selects, then for each document navigate and save it as `fomcpilot-<ID>-doc-<class>-<nn>.txt`. A PDF is fetched from its own site and saved as `.pdf`. For every saved file it writes one line to `capture_log.jsonl`: file, address, class, title, publication time as the page states it (or "not stated"), retrieval time, in-page fingerprint, bytes, order (1 = newest in its class).
8. Runner, in the machine's shell: copy every `fomcpilot-<ID>-*` file from Downloads into `checkpoints/<ID>/` (documents to `capture/`, quote files to `private/market_T0/`). Touch no other file in Downloads. Check each file's fingerprint and size against what its collector reported.
9. PDFs are converted to text with `pdftotext -layout`; the text file is logged with its own fingerprint and the PDF's.
10. Run `pack_tools.build_pack` on `capture/`. Outputs: `pack.md`, `manifest.json`, `pack.sha256`, `pack_diff.md`. Record pack-ready time.
11. Copy `pack.md` into the session workspace as `cp/<ID>/pack.md`. Check its fingerprint again there.

**Save snippet** (the only way anything is saved; the page text is never re-typed by a model):

```js
const sha = async s => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))).map(b => b.toString(16).padStart(2, '0')).join('');
const text = document.body.innerText;
const a = document.createElement('a');
a.href = URL.createObjectURL(new Blob([text], {type: 'text/plain;charset=utf-8'}));
a.download = NAME;
document.body.appendChild(a); a.click(); a.remove();
({name: NAME, bytes: new TextEncoder().encode(text).length, sha256: await sha(text), url: location.href, title: document.title, at: new Date().toISOString()})
```

## T1 - forecasts

12. Dispatch the ten Fable calls (fresh context each, model Fable, effort high) with the prompt in `prompts.md`. Each writes its answer to `cp/<ID>/answers/F01.md` ... `F10.md` and replies only DONE. Record each call's requested model, recorded model, start and end time.
13. Run Deliberate (scored run) with the settings and starting claim in `prompts.md`, corpus `cp/<ID>/pack.md`. Save the text of its final call as `answers/D_scored.md`. Record its finish time.
14. One retry of a failed call with the identical message; then it is recorded as failed. An accepted answer file is never regenerated or overwritten.
15. Run `forecast_tools.parse_forecast` on every answer file. Write `forecasts.json` (per arm: valid or the reason, the line, the forecast).
16. Start the twin Deliberate run (diagnostic) on the same pack once the scored run has finished. It may end after the deadline; it gets its own commitment when it ends.

## T2 - commitment (by 15:00 Israel time)

17. At the deadline, any arm without an answer file has failed this checkpoint. Late output is kept, labelled late, never scored.
18. Run `pack_tools.commit_bundle` over `pack.sha256`, the answer files present and `forecasts.json`. Push `commitment.json` to `commitments/<ID>.json` in this repository. Record the commit address and time.
19. Witness: open `https://web.archive.org/save/<commit address>` in the browser and record the archive address it returns. If the archive fails, record that and continue.
20. **Only now: quote collector, capture T2**, as in step 6 with `T2` in the names. Copy the files to `private/market_T2/` and check fingerprints.

## T3 - disclosure

21. Run `venue_tools` on the T0 and T2 quote files. Write `quotes_T0.json`, `quotes_T2.json` (quotes, venue vectors, flags, benchmark).
22. Fill the compliance record (`design.md`, section 14), including the tool-record scan of every model call: web access, and venue names or prices in any tool result.
23. Push to `ledger/<ID>/`: `pack.md`, `manifest.json`, `pack_diff.md`, the answer files, `forecasts.json`, `commitment_private.json` (the salt), the two quote tables, the compliance record, `deviations.md`. Raw quote files and Deliberate run folders stay private; their fingerprints are in the compliance record.
24. Save every call's transcript to `transcripts/` and copy the Deliberate run folders to `deliberate/`.
25. When the twin run ends: save `answers/D_twin.md`, parse it, commit its fingerprint as `commitments/<ID>-twin.json`, then push it to the ledger.

## Never

- Never score anything before the question resolves.
- Never open, summarise or mention venue quotes before T3. Never pass a venue file, a venue name's price or a prior checkpoint's ledger to a model call.
- Never edit an answer, a pack or a prompt. Never repair a forecast line.
- Never save a page by copying its text through a model.
- Never resume a checkpoint on a later day.
- Never change this sheet during a checkpoint. A needed change is a deviation now and an amendment afterwards.

## Extra steps in the dress rehearsal only

- Channel check (`design.md`, section 11): list what a fresh helper call is shown before its prompt; scan it for venue names, prices and this experiment.
- Run Deliberate twice with the starting claim (repeat test) and once with the twin claim.
- After T3, a fresh session rebuilds the forecasts and benchmark from the pushed bundle alone.
- Record how long each step took. The six-hour window and any pack size ceiling are set from this.
