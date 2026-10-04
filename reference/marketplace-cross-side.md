# Marketplace cross-side check

Load for: any asset that makes a promise to one side that the other side has to keep, and any question about the twelve decisions. Distills `sources/raw/gtm/marketplace/cross-side-check.md` (2026-10-01).

The rule: neither side's copy may promise something the other side's terms do not deliver. Every customer promise is kept by a contractor first.

## The eight shared rows

| # | Customer-side promise | Contractor-side term that keeps it | Status | What closes it |
|---|---|---|---|---|
| 1 | 90-minute guarantee, refund on a miss | Fault-based late-arrival rule (option C) | Closed | Decision 3, plus conflict B |
| 2 | Relaunch guarantee | SOS SMS pays the second trip charge from its fee | Held out of copy until dispatch supports it | R17 |
| 3 | One text reaches the matched contractors | "Lose the race, lose nothing", shared openly | Consistent | Decision 4 |
| 4 | Only the accepting contractor gets the address | Problem and photos before accepting | Consistent | Decision 4 |
| 5 | Trip charge credited to the job | The crediting obligation in the agreement | Consistent | The founding contractor agreement |
| 6 | Known arrival time | Commitment on acceptance, in the terms on one page | Consistent | The terms on one page |
| 7 | License and insurance checked | Onboarding step, rechecked every 6 months and at each policy's expiry | Closed | Decision 7, same words both sides |
| 8 | Zero cost to join | $0 to contractors, fee per completed job later | Consistent | Decision 2 |

## The eight conflicts, A to H

| # | Conflict | Resolution (decided 2026-10-03) |
|---|---|---|
| A | Who sets the trip charge | One per trade and zone, set by SOS SMS. Contractor copy says "your price for the work", never "your trip charge" |
| B | Accepting with an arrival time outside the window | Dispatch only allows acceptance with an arrival time inside the remaining window. If no one can, the miss is caused by SOS SMS and SOS SMS pays |
| C | Address before acceptance | Approximate distance or cross-street area before acceptance, full address after |
| D | Customers without a card | Dispatch needs a card or a phone wallet through the payment link; without one, free help by text and nothing charged. No pay-on-arrival path at launch (R16) |
| E | A contractor's own customers | 5 minutes of first refusal; SOS SMS is offered as a contractor's after-hours line only once dispatch supports it (R13) |
| F | Gas and life-safety texts | Safety reply first; not broadcast until the customer confirms it is safe and 911 or the utility has been called |
| G | Paid search ahead of density | Geofence to zones at the density number, schedule to covered hours, pause automatically when acceptance falls |
| H | Payment hold timing | Stripe Connect: authorize at the confirming text, capture at acceptance, hold, release on arrival, payout within 2 business days; refunds per the late-arrival rule (decision 6, S30) |

## Result
All eight rows are closed or consistent, and all eight conflicts are resolved: the twelve decisions (`ops/decisions.md`) closed them without rewrites.

## How to use it
Before writing a customer promise, find its row and confirm the contractor term is in place. Before writing a contractor term, check whether it changes a customer promise. If a change to one side's terms would break the other side's promise, log it in `ops/signal-log.md` and follow the amendment order before any copy changes.
