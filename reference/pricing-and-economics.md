# Pricing and unit economics

Load for: any question about who pays what, the take rate, the late-arrival rule, fee ceilings, or paid search payback. Distills Run 1 and Run 2 Phase 9 and `speed-to-scale-plan.md` section 5. Every SOS SMS price is {TBD}. Grade C figures are internal direction only and never appear in customer or contractor copy.

## The structure, recommended, not decided (decision 2)

| Money flow | Who pays | Who receives | Amount |
|---|---|---|---|
| Trip charge | Customer, before dispatch | Contractor, released on arrival; credited to the repair | {TBD}, one per trade and zone, set by SOS SMS (decision 5) |
| SOS SMS fee | Customer, on top of the trip charge | SOS SMS | {TBD} |
| Contractor fee, founding period | Contractor | SOS SMS | $0 (recommended) |
| Contractor fee, after | Contractor, per completed paid job, never per request | SOS SMS | {TBD}, below about $125 |
| 90-minute refund | The contractor (own missed commitment) or SOS SMS (misses it causes) | Customer | Equal to the trip charge (recommended) |
| Processing | Deducted | Payment provider | {TBD} |

Rejected metrics: per request received for contractors (it is the per-lead model), per seat (contradicts "no subscription"), an after-hours premium for customers (the surprise fee customers resent, S50, S51). Flag only: paid priority, household membership.

## The late-arrival rule (decision 3)

| Option | Rule | Effect on "paid to show up" |
|---|---|---|
| A, contractor forfeits | Any miss refunds from the contractor's trip charge | Narrows; fewer night acceptances |
| B, SOS SMS absorbs | SOS SMS refunds and still pays the contractor | Holds; costs refund rate × trip charge |
| C, fault-based (recommended) | The contractor's own missed commitment funds the refund; SOS SMS pays for no acceptance or dispatch failure | "The trip charge is yours when you arrive by the time you committed to" |

Guarantee cost to SOS SMS = share of requests with a miss SOS SMS causes × trip charge. At 5 percent, the fee must cover 5 percent of T before processing and operations (arithmetic, not a forecast).

## The contractor fee ceiling
Cost per booked job = cost per lead ÷ close rate. At a 20 percent close: Angi $125 to $300 (S03, C), Thumbtack $125 to $225 (S06, C), Google LSA $285 to $345 (S08, C). The lowest, about $125, is the ceiling for any future per-job fee. Recompute with founding contractors' real close rates before any fee is set.

## Paid search payback, illustrative
Paid cost per paid job = cost per click ÷ click-to-text rate ÷ text-to-paid rate.

| Basis | Per first text | Per paid job at 50 percent text-to-paid | Source |
|---|---|---|---|
| Plumbing benchmark, $10.49 a click, 7.63 percent | about $137 | about $275 | S15, B |
| Emergency dataset, $66.82 a click, 31 percent | about $216 | about $431 | S69, C |
| Microsoft, 30 to 60 percent cheaper clicks | about $55 to $96 | about $110 to $192 | S74, C |

Against trip charges of $75 to $100 when charged (S28, C) and after-hours call fees of $150 to $250 (S50, C), **a customer fee alone will not pay back paid search on the first job.**

## The four levers
1. **Owned share.** Blended cost = (1 - owned share) × paid cost. At 30 percent owned about $192; 50 percent about $137; 70 percent about $82.
2. **Jobs per customer.** At 1.5 jobs, $275 becomes about $183.
3. **Cheaper clicks.** Microsoft Ads and long-tail problem keywords, tested in every proving zone.
4. **Both sides pay** after the founding period: take per job = customer fee + contractor fee.

Paid search is the liquidity engine of a new zone; owned channels are the profit engine of a mature one. The ceiling per zone is {TBD} (decision 12). Runway to cover several proving zones is {TBD}.

## Honest positions available now
Against a home warranty, a covered failure is usually cheaper through the warranty, and SOS SMS says so. Against search and call, the comparison is the after-hours call fee against a trip charge credited to the repair.
