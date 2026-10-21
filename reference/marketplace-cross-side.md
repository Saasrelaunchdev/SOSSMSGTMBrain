# Marketplace cross-side check

Load for: any asset that makes a promise to one side that the other side has to keep, and any question about the twelve decisions. Distills `sources/raw/gtm/marketplace/cross-side-check.md` (2026-10-01; revised by the membership revision, 2026-10-11, the tiers revision, 2026-10-20, and the pricing revision, 2026-10-21).

The rule: neither side's copy may promise something the other side's terms do not deliver. Every promise to a member is kept by a contractor first. The plans never reach the contractor side: a contractor's terms never depend on the member's plan, no plan is faster, and the late-arrival credit and Premier's covered trip charge are SOS SMS's costs, never the contractor's.

## The eight shared rows

| # | Member-side promise | Contractor-side term that keeps it | Status | What closes it |
|---|---|---|---|---|
| 1 | An arrival time inside 90 minutes from the request text; on Plus and Premier, 6 or 12 months of membership credited on a late arrival or a no-show | A late contractor keeps the trip charge less the fee; a no-show is paid nothing; both are recorded, and two in 90 days pause requests (R67). The credit is SOS SMS's cost | Closed | Decision 3 (revised 2026-10-20 and 2026-10-21), plus conflict B |
| 2 | NEXT after a miss | The first contractor is treated as a no-show: the trip charge back to the member in full, the contractor paid nothing; a new acceptance is a new request with its own $99 and its own 90 minutes, so SOS SMS pays no second trip charge | Closed | R17, decided 2026-10-11, revised 2026-10-20 |
| 3 | One text reaches every matched contractor in plumbing, HVAC, or electrical | "Lose the race, lose nothing", shared openly; no priority for anyone | Consistent | Decision 4 |
| 4 | Only the accepting contractor gets the address | Problem and photos before accepting | Consistent | Decision 4 |
| 5 | Trip charge credited to the job | The crediting obligation in the agreement | Consistent | The contractor agreement |
| 6 | Known arrival time | Commitment on acceptance, in the terms on one page | Consistent | The terms on one page |
| 7 | License and insurance checked | Onboarding step for each trade taken, rechecked every 6 months and at each policy's expiry | Closed | Decision 7 (revised 2026-10-20), same words both sides |
| 8 | Zero cost to join | $0 to join and per request; $25 per completed paid job from the first job, the same for every contractor in every trade; members fund the network through Basic, Plus, or Premier | Consistent | Decision 2, revised 2026-10-11, 2026-10-20, and 2026-10-21 |

## The eight conflicts, A to H

| # | Conflict | Resolution (decided 2026-10-03, revised 2026-10-11 and 2026-10-20) |
|---|---|---|
| A | Who sets the trip charge | One per trade and zone, set by SOS SMS. Contractor copy says "your price for the work", never "your trip charge" |
| B | Accepting with an arrival time outside the window | Dispatch only allows acceptance with an arrival time inside the remaining window. If no one can, nobody accepts: the member is told within 15 minutes and never charged, and no contractor is paid (decision 3) |
| C | Address before acceptance | Approximate distance or cross-street area before acceptance, full address after |
| D | Requests without a card | Joining puts a card on file, with an optional backup card; no dispatch without an authorized trip charge; if both decline, the member is told at once and dispatch starts the moment a card authorizes; a text from a non-member gets the free help by text and nothing is charged (R16, R57). No pay-on-arrival path |
| E | A contractor's own customers | No priority for anyone (R13, retired 2026-10-11): every request goes to all matched contractors at once. A contractor may refer their own customers through the affiliate program on the same terms as any partner (R61); the repair stays theirs whenever they take the job |
| F | Gas and life-safety texts | Texts that mention gas, smoke, fire, sparks, a burning smell, a shock, or injury get the safety reply first; not broadcast until the member confirms it is safe and 911 or the utility has been called (decision 8) |
| G | Memberships ahead of density | Memberships open only in zones where each of the three trades meets the density number in every hour band (R15, R55); before then, the launch list. Sign-ups pause automatically when acceptance in any trade falls: paid social stops and affiliate links show the launch list (R34) |
| H | Payment hold timing | Stripe Connect: the card saved at joining; authorize on the card on file when the request text arrives (the backup card if the first declines), capture at acceptance, hold, release on arrival, payout within 2 business days less the $25 contractor fee; on a no-show the trip charge goes back to the member in full (decision 6, S30) |

## Result
All eight rows are closed or consistent, and all eight conflicts are resolved: the twelve decisions (`ops/decisions.md`) closed them without rewrites, and the membership revision (2026-10-11), the tiers revision (2026-10-20), and the pricing revision (2026-10-21) kept every row closed or consistent.

## How to use it
Before writing a member promise, find its row and confirm the contractor term is in place. Before writing a contractor term, check whether it changes a member promise. If a change to one side's terms would break the other side's promise, log it in `ops/signal-log.md` and follow the amendment order before any copy changes.
