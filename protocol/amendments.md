# Draft changes since design.md was pushed on 22 Nov 2026 (not frozen)

These are folded into the frozen design text at the freeze. No forecast, scored or unscored, existed when they were made.

| # | Section | Change | Why |
|---|---|---|---|
| 1 | 3 | The parser ignores a FORECAST line that only repeats the format template with unfilled placeholders, and ignores quotation marks around a line. The prompts give the format inside a sentence, with letters in place of numbers. | Deliberate restates its question at the start of every call. With the old wording that restatement would have counted as a second, conflicting forecast line and voided every run. |
| 2 | 9 | Twin claim rule completed: if the starting claim is itself a move of any size, the twin claim is "no change". | The old wording covered only a 25 bp starting claim. |
| 3 | 1, 13 | Venue rule texts are recorded by address, capture time and fingerprint, not republished. Raw venue responses are kept privately with their fingerprints; the public ledger carries the extracted quote tables. | The rule texts belong to the venues. A fingerprint lets anyone check the text without the pilot copying it. |
| 4 | 1 | January identifiers added (see `venues.md`). | Found by the probe. |
| 5 | 6 | Adapter rules confirmed (see `venues.md`). | Probe. |
| 6 | 4, 5 | Documents and venue responses are saved by a download triggered inside the browser page, with a fingerprint computed in the page and checked against the saved file. No model re-types any page. | In the probe a small model failed to copy 2,000 characters of an official page exactly, twice. A test download matched its in-page fingerprint byte for byte. |
| 7 | 6 | One-sided books: a missing bid counts as 0 and a missing ask as 100, flagged. Only when both are missing is the last trade used, flagged; with no last trade either, the venue is invalid for that capture. | Under the old wording Kalshi would have been invalid at every capture, because its far-from-the-money contracts routinely have no bid. |
| 8 | 2 | Each Fable call writes its answer to a file and replies only that it is done. The forecasting wording is unchanged. | The runner never re-types an answer and never needs to read one before the commitment. |
| 9 | 5, 9 | The twin Deliberate run starts after the scored run and may end after the deadline. It gets its own commitment when it ends. | It is a diagnostic and is never scored; two full runs may not fit one window. |
| 10 | 4 | Speeches and testimony are taken from the Board's yearly listing pages. Pages are saved whole, menus included. | The combined landing page shows only recent items. Saving the whole page removes a judgment about where a document starts. |
