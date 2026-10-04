# Pricing and unit economics

Load for: any question about who pays what, the take rate, the late-arrival rule, fee ceilings, or paid search payback. Distills Run 1 and Run 2 Phase 9 and `speed-to-scale-plan.md` section 5. Every SOS SMS price is decided (decisions 2 and 5, 2026-10-03) and may go into copy on the side it belongs to. Grade C figures are internal direction only and never appear in customer or contractor copy.

## The structure, decided (decisions 2 and 5)

| Money flow | Who pays | Who receives | Amount |
|---|---|---|---|
| Trip charge | Customer, captured at acceptance | Contractor, released on arrival; credited to the repair | $99, one per trade and zone, day or night, set by SOS SMS (decision 5) |
| SOS SMS fee | Customer, a separate line, only when a contractor accepts | SOS SMS | $49 per dispatched request |
| Contractor fee, founding period | Contractor | SOS SMS | $0 a job (the founding zone's first 6 months open) |
| Contractor fee, after | Contractor, per completed paid job, never per request; deducted from the payout | SOS SMS | $25; founding contractors $0 for 12 months after the founding period |
| 90-minute refund | The contractor (own missed commitment) or SOS SMS (misses it causes) | Customer | The $99 trip charge (decision 3) |
| Processing | Deducted | Stripe Connect (decision 6) | Planning value 2.9 percent plus $0.30 a charge (R31) |

Rejected metrics: per request received for contractors (it is the per-lead model), per seat (contradicts "no subscription"), an after-hours premium for customers (the surprise fee customers resent, S50, S51). Not at launch: paid priority, household membership (R19).

## The price points and how they were set (pricing model, 2026-10-03)

From `Fit137/SOSSMSGTMBuild`, `google-folder/SOS_SMS_Pricing_Model.xlsx` (live formulas; handoff in `gtm/pricing/pricing-handoff.md`), built on the direction logged 2026-10-03: contractors join free, SOS SMS earns on transactions. Decisions 2 and 5 set these amounts the same day. The basis column is internal: it cites grade C figures.

| Item | Decided | How it was set |
|---|---|---|
| Contractor, to join and per request | $0 | The direction: the lowest barrier of entry |
| Contractor fee, per completed paid job, after the founding period | $25 | Value ceiling: 20 percent of the cheapest per-lead cost per booked job (about $125, S03, S06, C); floor about $10; deducted from the trip charge payout |
| Founding contractors | $0 a job through the founding period and 12 months after | Founding terms, in the founding agreement from day one |
| Trip charge, one per trade and zone | $99 | Inside the S28 band ($75 to $100, C); paid to the contractor, credited to the repair |
| SOS SMS fee, per request | $49 | Floor about $42 (refund reserve, processing, messaging, support); value ceiling $50 (25 percent of the S50 after-hours call fee midpoint, C) |
| Help by text (first reply) | $0 | Value before payment |

Model outputs, per completed job (illustrative): SOS SMS nets about $31 in the founding period and about $56 after it. At the S15 benchmark and the 50 percent text-to-paid planning value (R30), a paid job costs about $275 from search; at a 50 percent owned share and the contractor fee on, about 2.5 jobs pay it back. The model's planning values are listed in the handoff, each with its basis, and measured figures replace them once the founding zone runs.

## The late-arrival rule (decision 3)

| Option | Rule | Effect on "paid to show up" |
|---|---|---|
| A, contractor forfeits | Any miss refunds from the contractor's trip charge | Narrows; fewer night acceptances |
| B, SOS SMS absorbs | SOS SMS refunds and still pays the contractor | Holds; costs refund rate × trip charge |
| C, fault-based (decided) | The contractor's own missed commitment funds the refund; SOS SMS pays for no acceptance or dispatch failure | "The trip charge is yours when you arrive by the time you committed to" |

Guarantee cost to SOS SMS = share of requests with a miss SOS SMS causes × trip charge. At the 5 percent planning value (R29), that is $4.95 a request, inside the $49 fee's $42 cost floor (arithmetic, not a forecast).

## The contractor fee ceiling
Cost per booked job = cost per lead ÷ close rate. At a 20 percent close: Angi $125 to $300 (S03, C), Thumbtack $125 to $225 (S06, C), Google LSA $285 to $345 (S08, C). The lowest, about $125, is the value ceiling; the decided $25 contractor fee is a fifth of it. The founding contractors' real close rates, counted from their first jobs, check it before the founding period ends.

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

Paid search is the liquidity engine of a new zone; owned channels are the profit engine of a mature one. The ceiling per zone is $275 per paid job while proving, $192 by the end of month 6, and $137 by the end of month 12 (decision 12). Runway: at least 18 months at Stage A spending, enough for the founding zone and two more zones proving at once (R35).

## Honest positions available now
Against a home warranty, a covered failure is usually cheaper through the warranty, and SOS SMS says so. Against search and call, the comparison is the after-hours call fee against a trip charge credited to the repair.
