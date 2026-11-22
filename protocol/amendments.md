# Draft changes since design.md was pushed on 22 Nov 2026 (not frozen)

These are folded into the frozen design text at the freeze. No forecast, scored or unscored, existed when they were made.

| # | Section | Change | Why |
|---|---|---|---|
| 1 | 3 | The parser ignores a FORECAST line that only repeats the format template with unfilled placeholders, and ignores quotation marks around a line. The prompts give the format inside a sentence, with letters in place of numbers. | Deliberate restates its question at the start of every call. With the old wording that restatement would have counted as a second, conflicting forecast line and voided every run. |
| 2 | 9 | Twin claim rule completed: if the starting claim is itself a move of any size, the twin claim is "no change". | The old wording covered only a 25 bp starting claim. |
| 3 | 1, 13 | Venue rule texts are recorded by address, capture time and fingerprint, not republished. Raw venue responses are kept privately with their fingerprints; the public ledger carries the extracted quote tables. | The rule texts belong to the venues. A fingerprint lets anyone check the text without the pilot copying it. |
| 4 | 1 | January identifiers added (see `venues.md`). | Found by the probe. |
| 5 | 6 | Adapter rules confirmed (see `venues.md`). | Probe. |
| 6 | 4, 5 | How documents are saved to disk unaltered is open. Re-typing by a model is ruled out. | In the probe a small model failed to copy 2,000 characters of an official page exactly, twice. |
