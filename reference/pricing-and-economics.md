# Pricing and unit economics

Load for: any question about who pays what, the membership, the take rate, the late-arrival rule, fee ceilings, member economics, or acquisition cost. Distills Run 1 and Run 2 Phase 9, the pricing model, and `speed-to-scale-plan.md` section 5 (the membership revision, 2026-10-11). The trip charge and the contractor amounts are decided (decisions 2 and 5) and may go into copy on the side they belong to; the membership prices are planning values and go into copy only as `{{monthly price}}` and `{{annual price}}`. Grade C figures are internal direction only and never appear in member or contractor copy.

## The structure (decisions 2 and 5; decision 2 revised 2026-10-11)

| Money flow | Who pays | Who receives | Amount |
|---|---|---|---|
| Membership | Member, monthly or annually, billed to the card on file | SOS SMS | Planning values $10 a month or $100 a year (R51, R52), set as the launch price in Stage 0 |
| Trip charge, on use | Member, on the card on file when a contractor accepts | Contractor, released on arrival; credited to the repair | $99, one per trade and zone, day or night, set by SOS SMS (decision 5) |
| Fee per request | Nobody | n/a | $0: the SOS SMS fee is retired (R02) |
| Contractor fee, founding period | Contractor | SOS SMS | $0 a job (the founding zone's first 6 months open to members) |
| Contractor fee, after | Contractor, per completed paid job, never per request; deducted from the payout | SOS SMS | $25; founding contractors $0 for 12 months after the founding period |
| 90-minute refund | The contractor (own missed commitment) or SOS SMS from membership revenue (misses it causes) | Member | The $99 trip charge (decision 3) |
| Processing | Deducted | Stripe Connect (decision 6) | Planning value 2.9 percent plus $0.30 a charge (R31) |

Rejected metrics: per request received for contractors (it is the per-lead model), per seat (contradicts "no subscription" for contractors), a fee per request for members (charged at the worst moment), an after-hours premium (the surprise fee homeowners resent, S50, S51). Not at launch: paid priority, repair coverage or discounts (R21, R53), a free trial, a member referral reward (R62).

## The price points and how they were set (pricing model)

From `Fit137/SOSSMSGTMBuild`, `google-folder/SOS_SMS_Pricing_Model.xlsx` (live formulas; handoff in `gtm/pricing/pricing-handoff.md`, tables in `gtm/pricing/pricing-model.md`). The basis column is internal: it cites grade C figures.

| Item | Value | How it was set |
|---|---|---|
| Contractor, to join and per request | $0, decided | The direction: the lowest barrier of entry |
| Contractor fee, per completed paid job, after the founding period | $25, decided | Value ceiling: 20 percent of the cheapest per-lead cost per booked job (about $125, S03, S06, C); floor about $10; deducted from the trip charge payout |
| Founding contractors | $0 a job through the founding period and 12 months after, decided | Founding terms, in the founding agreement from day one |
| Trip charge, one per trade and zone | $99, decided | Inside the S28 band ($75 to $100, C); paid to the contractor, credited to the repair |
| Membership, a month | $10, planning value (R51) | At the closest analog's price, a plumber's club at $10 a month (S75): the value ceiling. Inside the band of emergency memberships and plumbing plans, $4.83 to $22.99 a month (S75 to S78, S80). Floor about $3.75 at a 65 percent margin |
| Membership, a year | $100, planning value (R52) | Two months free, the most common annual discount (S90) |
| Help by text, for anyone who texts | $0 | The safety line, the stop-the-water steps, and how to join (R57) |

## Member economics, illustrative (pricing model)

| A member | Monthly plan at $10, a month | Annual plan at $100, a year |
|---|---|---|
| Card processing on the membership | $0.59 | $3.20 |
| Messages, support, and platform | $0.55 | $6.60 |
| Requests, both sides, including the refund reserve, at 0.25 a year (R58) | $0.35 | $4.23 |
| Contribution, founding period | about $8.51 | about $85.97 |
| Contribution after the founding period, with the $25 contractor fee | about $9.03 | about $92.22 |

A request costs about $16.92 on both sides: the refund reserve ($4.95 at the 5 percent planning value, R29), processing on the trip charge ($3.17), messages ($0.30), member support and platform ($5.00), and the contractor-side payout, checks, and support ($3.50). The membership carries it; there is no fee per request.

## The acquisition ceiling and the channels

**Acquisition ceiling per new paid member = the first 6 months of contribution on the monthly plan: about $43** at $8.51 a month and 6.5 percent monthly churn (R59, R63), reviewed weekly by channel and zone (decision 12). Lifetime contribution on the monthly plan is about $131.

| Channel | Cost per new paid member | Against the ceiling | Basis |
|---|---|---|---|
| Affiliates | $20, the commission (R61), paid after the first paid month | Under, by about $23; paid back in the third month | Market $4 to $56 an enrollment (S85, C) |
| Email, SOS SMS's own list | Counted from the first opening email (Stage 2) | Measured | S92, C (open and click only) |
| Paid search, plumbing benchmark | about $137: $10.49 a click, 7.63 percent converting, assumed equal for sign-ups | Over, about 3 times | S15, B |
| Paid search, Microsoft | about $55 to $96 | Over | S74, C |

**Affiliates and email lead; paid sign-ups support, only where measured cost comes in under the ceiling.** The levers: partner-led acquisition, retention (every point of churn removed raises what a member is worth), annual plans and more trades behind the same membership, and the contractor fee after the founding period (about $0.52 a member a month). About 430 members per zone keep 9 founding contractors at about one request a month (R64). Runway: at least 18 months at Stage A spending, because each zone recruits contractors and grows its launch list before any membership revenue (R35).

## The late-arrival rule (decision 3)

| Option | Rule | Effect on "paid to show up" |
|---|---|---|
| A, contractor forfeits | Any miss refunds from the contractor's trip charge | Narrows; fewer night acceptances |
| B, SOS SMS absorbs | SOS SMS refunds and still pays the contractor | Holds; costs refund rate × trip charge |
| C, fault-based (decided) | The contractor's own missed commitment funds the refund; SOS SMS pays for no acceptance or dispatch failure | "The trip charge is yours when you arrive by the time you committed to" |

Guarantee cost to SOS SMS = share of requests with a miss SOS SMS causes × trip charge. At the 5 percent planning value (R29), that is $4.95 a request, about $0.10 a member a month at 0.25 requests a year (arithmetic, not a forecast).

## The contractor fee ceiling
Cost per booked job = cost per lead ÷ close rate. At a 20 percent close: Angi $125 to $300 (S03, C), Thumbtack $125 to $225 (S06, C), Google LSA $285 to $345 (S08, C). The lowest, about $125, is the value ceiling; the decided $25 contractor fee is a fifth of it. The founding contractors' real close rates, counted from their first jobs, check it before the founding period ends.

## Honest positions available now
Against a home warranty or a utility-partner plan, a covered failure is usually cheaper through the plan, and SOS SMS says so: they pay for repairs, SOS SMS gets someone there. Against a plumber's club, the planning price matches the club's $10 a month; the club gives one company's priority and repair discounts, SOS SMS gives many contractors at once and a window from the text. Against doing nothing, the comparison is the after-hours call fee at the moment of need (S50, C, internal) against a membership paid in advance and a trip charge credited to the repair.
