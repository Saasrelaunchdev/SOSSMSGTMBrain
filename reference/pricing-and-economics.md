# Pricing and unit economics

Load for: any question about who pays what, the three plans and their entitlements, the take rate, the late-arrival rule and its credit, fee ceilings, member economics, or acquisition cost. Distills Run 1 and Run 2 Phase 9, the pricing model, and `speed-to-scale-plan.md` section 5 (the membership revision, 2026-10-11; the tiers revision, 2026-10-20; the pricing revision, 2026-10-21). The plan prices, the trip charge, and the contractor amounts are decided (decisions 2 and 5) and go into copy on the side they belong to. The economics are illustrative planning values: never results, never on a member or contractor page. Grade C figures are internal direction only. The workbook is `Fit137/SOSSMSGTMBuild`, `google-folder/SOS_SMS_Pricing_Model.xlsx`: its first sheet, "Founder Inputs", holds every input (prices, credit months, phones, plan mix, costs, churn, the trade table) and drives every other sheet. As tables: `sources/raw/gtm/pricing/pricing-model.md`; the handoff: `sources/raw/gtm/pricing/pricing-handoff.md`.

## The structure (decisions 2 and 5; decision 2 revised 2026-10-11, 2026-10-20, and 2026-10-21)

| Money flow | Who pays | Who receives | Amount |
|---|---|---|---|
| Membership | Member, monthly or annually, billed to the card on file | SOS SMS | Basic $10 a month or $100 a year; Plus $15 or $150; Premier $35 or $350; two months free on every annual plan, the most common annual discount (R51, R52, R65, R66, S90) |
| Trip charge, on use | Member, on the card on file when a contractor accepts | Contractor, released on arrival, less the contractor fee; credited to the repair | $99 per request, one per trade and zone, the same in plumbing, HVAC, and electrical, day or night (decision 5, R01) |
| Contractor fee | Every contractor in every trade, per completed paid job, from the first job; deducted from the payout | SOS SMS | $25, so the contractor receives $74 of the $99 (R03), whatever the member's plan. Never to join, per request, or for a declined or lost request |
| Late-arrival credit, the 90-minute guarantee | SOS SMS, never the contractor | Member on Plus or Premier, on the next bills or the renewal, never cash | The membership paid in the 6 months (Plus) or 12 months (Premier) before the request (R65, R66) |
| Processing | Deducted | Stripe Connect (decision 6) | Planning value 2.9 percent plus $0.30 a charge (R31) |

SOS SMS's revenue is the membership and the contractor fee; there is no fee per request (R02, retired), and no share of the repair (R04, R09). Rejected: per request received for contractors (the per-lead model), per seat, a fee per request for members, an after-hours premium (S50, S51), paid priority, faster dispatch on a higher plan, repair coverage or discounts (R21, R53), a fee-free period for contractors (R05 to R07, retired), paid search at launch (decision 11). Not at launch: a free trial, a member referral reward (R62).

## The three plans and their entitlements (decided 2026-10-21)

| Entitlement | Basic, $10 or $100 | Plus, $15 or $150 (most popular) | Premier, $35 or $350 |
|---|---|---|---|
| Late-arrival credit | None | Last 6 months of membership: up to $90 monthly, $75 annual | Last 12 months: up to $420 monthly, $350 annual |
| Phones that can text for the home (R69) | The member's phone | Up to 5 | Up to 10, across two homes |
| A trip charge a year paid by SOS SMS; a second home | None | None | One trip charge a membership year (annual from joining, monthly after 6 paid months); a second home in an open zone |

Every plan gets the same dispatch: one text to every matched contractor in the three trades at once, an arrival time inside 90 minutes, never charged if no one accepts, NEXT, a person by text (HELP), the readiness kit and a readiness check once a year (R53). No plan is faster; none pays for the repair, parts, or a guarantee on the work. Basic has no guarantee. The page shows Plus first, in the middle, on the annual plan, flagged "Most popular". Monthly dispatch starts 30 days after joining, annual at once (R54). Help by text is free for anyone: the safety line, the first steps for the problem, and how to join (R57).

## The price points and how they were set (the bottom-up method, internal)

| Item | Value | How it was set (grade C figures and the role names Hero, Decoy, Anchor stay off every page) |
|---|---|---|
| Contractor fee, per completed paid job, from the first job | $25, decided | Cost floor $17.50 (cost to serve $3.50 at an 80 percent margin); value ceiling $25, a third of about $75, the cheapest lead spend per booked job (HVAC service-call leads at a 20 percent close, S98, C) |
| Trip charge | $99, decided | Inside plumbing $75 to $100 (S28, C), HVAC $70 to $200 with $89 the most common (S95, C), electrical $52 to $200 (S96, C) |
| Plus, a month | $15, decided (R65) | The Hero: just under the market median of $16.99 (band $4.83 to $36.95, S75 to S78, S80, S100), above its cost floor of about $9.48 at an 80 percent margin |
| Basic, a month | $10, decided (R51) | The method's Decoy at half of Plus, $7.50, sits under Basic's floor of about $7.69, so Basic sits at the closest analog's price, a plumber's club at $10 (S75) |
| Premier, a month | $35, decided (R66) | The Anchor at 2.33 times Plus, inside the method's 2 to 4 times, under the HVAC clubs' top plans of $30.30 to $36.95 (S100, C). Before 2026-10-21: $25 |

## Member economics by plan, illustrative (pricing model)

| A member, a month, monthly plan | Basic | Plus | Premier |
|---|---|---|---|
| Card processing; messaging by phones on file; support and platform; requests, both sides | $0.59; $0.05; $0.50; $0.46 | $0.73; $0.25; $0.50; $0.46 | $1.32; $0.50; $0.50; $0.70 |
| Contractor fee from the member's requests, at 0.50 a year (R58) | $0.89 | $0.89 | $1.34 |
| Expected late-arrival credit; trip charge paid by SOS SMS | $0; $0 | $0.17; $0 | $1.18; $2.53 |
| Contribution (share of the price) | about $9.29 (93%) | about $13.77 (92%) | about $29.62 (85%) |
| Lifetime at 6.5 percent churn (R59) | about $143 | about $212 | about $456 |
| Annual plan: contribution a year; lifetime at 75 percent renewal (R60) | about $95.31; about $381 | about $139.78; about $559 | about $278.05; about $1,112 |

At the plan mix a member contributes about $14.91 a month. Every completed job nets about $13.03: the $25 fee less $3.17 of processing on the trip charge and $8.80 of messages, support, platform, payout, and checks. One zone of about 410 members (R64) contributes about $6,134 a month on monthly billing. Cost floors at an 80 percent margin: about $7.69 Basic, $9.48 Plus, $32.95 Premier.

## The acquisition ceiling and the channels (decision 12, revised 2026-10-21)

**One ceiling per plan = the first 6 months of that plan's contribution** at 6.5 percent monthly churn (R59, R63): about $47 Basic, $70 Plus, $151 Premier on the monthly plan; about $48, $70, $139 on the annual plan, paid up front; about $76 blended at the plan mix. Every channel scales while its measured cost per new paid member, commissions included, is at or under the ceiling of the plan joined, and stops when it is not; reviewed weekly by channel, plan, and zone.

| Channel | Cost per new paid member | Against the ceilings | Basis |
|---|---|---|---|
| Affiliates | $20, the commission (R61), any plan, paid once the second monthly or first annual payment clears | Under, by about $27 on Basic and $50 on Plus; paid back in month 2 on Plus | Market $4 to $56 an enrollment (S85, C) |
| Email, SOS SMS's own list | Counted from the first opening email (Stage 2) | Measured | S92, C (open and click only) |
| Paid social, sign-ups before the need | Counted in each open zone | Scales only at or under the plan's ceiling; pauses with sign-ups (R34) | Measured |
| Paid search, plumbing benchmark | about $137: $10.49 a click, 7.63 percent converting, assumed equal for sign-ups | Over, about 3 times Basic's ceiling and 1.8 times the blended; not run at launch (decision 11) | S15, B |

Search volume for SOS SMS by name is counted once a zone has been open 6 months (R68, Stage 3); a brand campaign may then run at or under the ceiling. Runway: at least 18 months at Stage A spending, because each zone recruits 27 contractors across three trades (R08) and grows its launch list before any membership revenue (R35).

## The plan mix and the levers (internal)
The plan mix is a planning value, never written on a page (R70): Basic 10, Plus 80, Premier 10 percent, read from the first members by plan; mostly Basic means Plus is overpriced or underbuilt, mostly Premier that Plus is underpriced. The levers: partner-led acquisition (affiliates and email under every ceiling); retention (every point of churn removed raises the ceiling); annual plans (an annual Plus member about $559 against about $212 monthly) and three trades in one membership; the ladder (Plus keeps about $4.49 a month more than Basic for a credit that costs about $0.17 and 5 phones that cost $0.20 more; each extra $1 of price adds about $0.97 of contribution on Basic, $0.96 on Plus, $0.94 on Premier, the workbook's Price Tests sheet); and the contractor fee from the first job, about $0.89 a Basic or Plus member a month.

## When the 90 minutes are missed (decision 3, revised 2026-10-20 and 2026-10-21)

| Case | Member | Contractor | SOS SMS on the request, monthly plan |
|---|---|---|---|
| No contractor accepts | Told within 15 minutes; never charged (R11) | No one is paid | $0: nets to zero |
| Arrives after the 90 minutes | The $99 stands: it pays for the work. Plus and Premier get the credit | Keeps the trip charge less the fee; recorded (R67) | About $13.03 on Basic; at the full credit about -$76.97 on Plus, -$406.97 on Premier |
| Accepts and does not come, or NEXT after the 90 minutes | The $99 back in full; the request goes to the other matched contractors (R17); Plus and Premier get the credit | Paid nothing; recorded (R67) | About -$8.47 on Basic, -$98.47 on Plus, -$428.47 on Premier |

Two late arrivals or no-shows in a rolling 90 days pause a contractor's requests until a person from SOS SMS reviews them (R67). Expected credit cost at the 5 percent late share (R29): about $0.17 a Plus member a month, $1.18 on Premier (arithmetic, not a forecast). The credit never returns more than the membership already paid; Premier monthly, 12 payments in, with the credit used in full, is the one member case that can cost SOS SMS money (about -$14.75), and its expected cost sits inside Premier's contribution. Before 2026-10-20 the $99 came back on a late arrival, funded by fault (option C), now retired.

## The contractor fee ceiling
Cost per booked job = cost per lead ÷ close rate. At a 20 percent close: Angi plumbing $125 to $300 (S03, C), Thumbtack plumbing $125 to $225 (S06, C), Google LSA plumbing $285 to $345 (S08, C), Angi HVAC service calls $75 to $200 (S98, C), Google LSA electrical $195 (S98, C). The lowest, about $75, is the ceiling in any trade; the decided $25 fee is a third of it and a fifth of the plumbing ceiling of about $125. The first cohort's real close rates, counted from their first jobs (R43), check it.

## Honest positions available now
Against a home warranty or a utility-partner plan, a covered failure is usually cheaper through the plan, and SOS SMS says so: they pay for repairs, SOS SMS gets someone there. Against a plumber's club, Basic matches the club's $10 a month (S75) and covers HVAC and electrical too; the club gives one company's priority, a lower trip charge, and repair discounts, SOS SMS gives many contractors at once, an arrival time from the text, and on Plus and Premier a credit when the contractor is late. Against doing nothing, the comparison is the after-hours call fee at the moment of need (S50, C, internal) against a plan paid in advance and a trip charge credited to the repair.
