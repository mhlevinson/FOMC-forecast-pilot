# FOMC forecast pilot

**Status: DRAFT. The protocol is not frozen. No scored forecast has been made.**

A supervised pilot by the Computational Deliberation Lab. At fixed checkpoints before two Federal Reserve decisions (8-9 December 2026 and 26-27 January 2027), three sources give probabilities for the same five outcomes:

- **Deliberate** - the lab's deliberation system, as deployed
- **Fable** - a single model call, and the plain average of ten calls
- **Benchmark** - a two-venue synthetic reference built from Kalshi and Polymarket midpoints

At each checkpoint a fingerprint of the model forecasts is committed here before the market is measured. The forecasts are disclosed afterwards. Everything is scored the same way once the Fed decides.

## What this repository is

The public record. Files are added, never rewritten.

| Folder | Contents | When it is written |
|---|---|---|
| `protocol/` | Design, run sheet, question files, prompts, source list, venue rule texts, parser and scoring tools, schedule | Before the freeze |
| `rehearsal/` | The unscored dress rehearsal and the list of changes made after it | Before the freeze |
| `commitments/` | One fingerprint file per checkpoint, with its independent archive receipt | At each checkpoint, before the market is measured |
| `ledger/` | Per checkpoint: evidence pack and manifest, forecasts, Deliberate's final call, raw venue files, benchmark, compliance record | At each checkpoint, after the commitment |
| `results/` | Scores, chart, rebuild report, corrections | After each decision |

## What the pilot can and cannot show

It can show an honest, witnessed record of what each system said and when, and a diagnosis of where the pipeline works and breaks.

It cannot show that any system forecasts better than another, or why. One or two decisions cannot separate skill from luck, and the pilot does not isolate Deliberate's method from model mix, compute, starting claim or answer format. The full list of permitted and forbidden claims is in `protocol/design.md`, section C.

## Disclosure

The Computational Deliberation Lab builds Deliberate and runs, scores and publishes this pilot itself. No outside reader reviewed the protocol before the freeze. Nothing here is investment advice.
