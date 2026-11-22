# Venues (DRAFT - not frozen)

The venues are close proxies for the pilot's questions, not identical questions. Their rule texts are not republished here: each is recorded by address, capture time and fingerprint (sha256), so anyone can check the text they retrieve against the one the pilot saw.

## Identifiers

| Question | Kalshi event | Kalshi contracts (suffix) | Polymarket event slug |
|---|---|---|---|
| FOMC-2026-12 | `KXFEDDECISION-26DEC` | `-C26` cut50, `-C25` cut25, `-H0` hold, `-H25` hike25, `-H26` hike50 | `fed-decision-in-december-20260729232808632` |
| FOMC-2027-01 | `KXFEDDECISION-27JAN` | same five suffixes | `fed-decision-in-january-20260729233815502` |

Polymarket contracts are matched by their titles: "50+ bps decrease" cut50, "25 bps decrease" cut25, "No change" hold, "25 bps increase" hike25, "50+ bps increase" hike50. Token identifiers are read from the live event response at each capture, never typed in by hand.

## Addresses read at each capture

| Venue | Address | Used for |
|---|---|---|
| Kalshi | `https://api.elections.kalshi.com/trade-api/v2/markets?event_ticker=<event>&limit=20` | Best bid and best ask per contract (`yes_bid_dollars`, `yes_ask_dollars`), sizes, last price, update time |
| Kalshi | `https://api.elections.kalshi.com/trade-api/v2/markets/<contract>/orderbook` | Depth |
| Polymarket | `https://gamma-api.polymarket.com/events?slug=<slug>` | Best bid and best ask per contract (`bestBid`, `bestAsk`), last trade, token identifiers |
| Polymarket | `https://clob.polymarket.com/book?token_id=<token>` | Depth, book timestamp |

## Adapter rules (confirmed by the probe of 22 Nov 2026)

- **Kalshi order book holds bids only**, for the YES side and the NO side. A YES ask is 1 minus the best NO bid. On 22 Nov this matched the `yes_ask_dollars` field exactly, so the markets address is used for top of book and the order book for depth.
- **Kalshi book arrays run from worst to best**: the best bid is the last entry.
- **Polymarket book arrays also run from worst to best**: best bid is the highest bid, best ask the lowest ask.
- **Identifier check.** A capture is valid only if the response names the expected event, the five expected contracts and their labels. An empty response is a failed capture.
- **Reading method.** Scripts inside the page could not fetch from Kalshi on 22 Nov; the response was read from the page after navigating to the address. Fingerprints are therefore of the text as displayed.

## Rule-text fingerprints (captured 22 Nov 2026, about 09:00 UTC)

| Text | Length | sha256 |
|---|---|---|
| Kalshi December, shared secondary rules (identical on all five contracts) | 320 | `42ed5fc9491c83df65f41a636c6b12407d28644ef39f36edb2171ed8dad07882` |
| Kalshi December, primary rules, `-H25` | 98 | `e90ad146167a0a1a675d2bcd86b8b73531838b16e86eec8fe9a6ec7b98e8e561` |
| Kalshi December, primary rules, `-H0` | 97 | `222b185773b0362a4cab3acdfefedc59094c5a14edbf7ee09eddd4d011a5a30a` |
| Kalshi December, primary rules, `-H26` | 100 | `db2b74209855c9d116a82830ba872605a729530cfc78c3dcea04051e6d72659c` |
| Kalshi December, primary rules, `-C25` | 97 | `a357ca23c6075be9ff8d019e7e9d4c43950ab0c5f0fa00083a3d21db263d1cc6` |
| Kalshi December, primary rules, `-C26` | 99 | `18849560fab63d8c6448897bc5c51bad7fce315768a999646c458499b1eb741d` |
| Polymarket December, event description | 1319 | `fdb210318474078daa855d747ed941b2113f64d186318fe4a0e4776c7737e4e6` |

January rule-text fingerprints are captured at the rehearsal.

## Known differences from the pilot's question (in our words)

- Kalshi's contracts are mutually exclusive and treat a cancelled meeting as "maintains rate".
- Polymarket measures the change in the upper bound against the level before the meeting, rounds an odd-sized move up to the next 25, and has its own rule for a missing statement.
- The pilot voids its question if no statement is issued on the scheduled day.
- Any difference in how a venue finally resolves is reported with the results.
