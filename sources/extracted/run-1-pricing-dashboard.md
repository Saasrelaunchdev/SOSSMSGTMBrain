# Source: run-1-pricing_dashboard.xlsx

Original path: `Fit137/SOSSMSGTMBuild`, `gtm/run-1-supply-contractors/output/pricing_dashboard.xlsx`
Type: xlsx
Size: 25,759 bytes

## Sheet: README

| Phase 9. Pricing and Packaging Dashboard, contractor side |
| The skill assumes a subscription: per-seat value metrics and four Decoy, Hero, Anchor plans. Contractors pay nothing to join SOS SMS by design, so per ../SKILL-ADAPTATION.md this phase builds the supply side of the take rate instead. The prices here were decided on 2026-10-03 (decision 2, ../../marketplace/resolution-register.md), from the pricing model in ../../pricing/pricing-model.md, and revised on 2026-10-11, the membership revision: the member side became a membership, and every contractor pays the same contractor fee from the first completed paid job, with no founding period. Revised 2026-10-20, the tiers revision: contractors in three trades (plumbing, HVAC, electrical), the same $99 trip charge and $25 fee in each, and a late arrival keeps its trip charge (decision 3). Market figures carry source IDs and grades; grade C figures are internal direction only. |
| What this phase delivers: the decided structure, the options weighed with their consequences, and calculators that run on a contractor's own numbers. The live calculators are in pricing_dashboard.xlsx. |
| Generated from gtm/run-1-supply-contractors/output/phase-9-pricing.md by gtm/tools/render.py. The Markdown file is the source of truth; edit it, then re-render. |
| Source IDs (S01, S02, ...) refer to gtm/research/SOURCES.md, which gives each source's URL and evidence grade (A primary, B secondary, C vendor estimate). |
| SOS SMS values are decided, planning values with their basis, or counted at a named stage (gtm/marketplace/resolution-register.md). SOS SMS is pre-launch: no figure in this workbook is an SOS SMS result. |

## Sheet: Calculators

| Contractor-side calculators (live formulas) |
| Legend: yellow cells with blue text are inputs; everything else is calculated. Example inputs are illustrative values inside grade C market ranges (S03, S06, S98), not data about any contractor or SOS SMS. |
| 1. Lead Cost Check (the contractor's own numbers) |
| Leads paid for last month | 20 | Illustrative |
| Average cost per lead | 40 | Illustrative; inside the S03 and S06 plumbing ranges |
| Share of leads that became booked jobs | 0.15 | Illustrative; inside S03's reported 10 to 20 percent |
| Trips last month without getting paid | 2 | Illustrative |
| Trip charge the contractor would have charged | 90 | Illustrative; S28 reports $75 to $100 for plumbing when charged |
| Monthly answering service cost | 0 | Enter 0 if none; S21 reports $250 to $720 |
| Monthly lead spend | 800 |
| Booked jobs from leads | 3 |
| Lead spend per booked job | 266.666666666667 |
| Monthly spend on leads that never became jobs | 680 |
| Yearly spend on leads that never became jobs | 8160 |
| Yearly value of unpaid trips | 2160 |
| Yearly answering service cost | 0 |
| Yearly total of the three leaks | 10320 |
| 2. Cost per booked job by alternative, in three trades (Phase 9, Anchor 2) |  |  |  | Close rates (inputs) |
| Alternative | Cost per lead, low | Cost per lead, high | Source | 0.1 | 0.2 | 0.333333333333333 |
| C1 Angi Leads (plumbing) | 25 | 60 | S03, C | $250 to $600 | $125 to $300 | $75 to $180 |
| C2 Thumbtack (plumbing) | 25 | 45 | S06, C | $250 to $450 | $125 to $225 | $75 to $135 |
| C3 Google LSA (plumbing) | 57 | 69 | S08, C | $570 to $690 | $285 to $345 | $171 to $207 |
| Search ads (plumbing) | 129 | 129 | S15, B | $1,290 to $1,290 | $645 to $645 | $387 to $387 |
| C4 Service Direct (plumbing, exclusive) | 60 | 255 | S10, A | $600 to $2,550 | $300 to $1,275 | $180 to $765 |
| Angi Leads (HVAC service call) | 15 | 40 | S98, C | $150 to $400 | $75 to $200 | $45 to $120 |
| Thumbtack (HVAC basic service) | 25 | 60 | S98, C | $250 to $600 | $125 to $300 | $75 to $180 |
| Google LSA (HVAC) | 51 | 51 | S98, C | $510 to $510 | $255 to $255 | $153 to $153 |
| Google LSA (electrical) | 39 | 39 | S98, C | $390 to $390 | $195 to $195 | $117 to $117 |
| SOS SMS lead cost per booked job | 0 |
| SOS SMS contractor fee per completed paid job, from the first job, in every trade (decision 2) | 25 |
| 3. Fee ceiling (Phase 9, Anchor 3) |
| Lowest cost per booked job among per-lead platforms, any trade, at the middle close rate | 75 |
| Any SOS SMS per-job fee below this stays cheaper than every per-lead option above |
| Headroom at the fee entered in B35 | 50 |

## Sheet: Value_Metric

| Step 9.1. Value metric selection |
| Denominator | Correlation to Value | Scalability | Ease of Measurement | Score (1 to 10) | Verdict |
| Per request received (per lead) | Low. Value arrives only when a job happens; this is exactly the complaint against C1 to C4 | High | High | 1.8 | Reject. Contradicts VP1 and the positioning |
| Per contractor or technician, monthly (per seat) | Low. A quiet month costs the same as a busy one | High | High | 2.6 | Reject. "No subscription" is a stated promise |
| Per accepted job (usage) | Medium. Accepting is a choice, but the member may still decline the quote | High | High | 5.7 | Possible, second choice |
| Per completed paid job, as a share of the trip charge or the job (outcome) | High. The contractor pays only when revenue exists | High | Medium. SOS SMS sees the trip charge but not the job value unless payment for the work flows through it | 7.4 | Best fit, and the basis of the contractor fee |
| Paid priority or extra zones (capability) | Medium | Medium | High | 3.1 | Rejected. Conflicts with "every matched contractor sees the request at once" and with "decline freely" |
| Decided (decision 2): |
| Primary value metric: per completed paid job, from the first job. Contractors pay $0 to join and $0 per request, and $25 per completed paid job, deducted from the trip charge payout, never per request, far below the Anchor 3 ceiling, and written into the contractor agreement so nobody is surprised. The same terms apply to every contractor in every zone: there is no founding period, no founding terms, and no founding list. Supply is the constrained side, so entry stays free and "no lead fees" stays true; the fee is paid only from revenue the job already produced. |
| Why from the first job: every request then pays for itself, about $13.03 net after its costs on both sides, and the fee adds about $0.89 a Basic or Plus member a month at 0.50 requests a member a year across the three trades, 90 percent accepted and 95 percent arriving (R58), which raises what SOS SMS can spend to acquire each member (speed-to-scale plan, section 5). Members fund the network through the membership. |
| Secondary usage metric, for tracking only: accepted jobs per active contractor per month, by hour band. It measures whether the supply side is healthy, not what to charge. |
| Rationale: in a marketplace, the side whose participation is hardest to get is usually subsidized, and the side that captures urgent value pays. Here the member pays for readiness and speed through the membership, and on Plus and Premier for the 90-minute guarantee, whose credit SOS SMS pays; a late contractor keeps the trip charge. Monetizing that side keeps the contractor pitch clean. |

## Sheet: Packaging

| Step 9.2. Packaging: the contractor participation structure |
| Plan | Price to contractor | Requests | Commitments | Position | Target share of contractors |
| Contractor | $0 to join and per request; $25 per completed paid job from the first job, deducted from the trip charge payout | All matched requests in their trades (plumbing, HVAC, electrical) and area | Response window when available (10 minutes); credit the trip charge; current documents; the three-question text after five jobs; permission clause | The one plan, the same for every contractor in every zone; the first cohort makes the launch zone dense enough to open | Every contractor; 9 per trade in the launch zone first, 27 in all, the Phase 5 density number (R08) |
| Priority (rejected) | Not offered | n/a | n/a | Conflicts with the dispatch rule (decision 4: every matched contractor sees the request at once) | 0 |

## Sheet: Take_Rate

| The take rate, both sides |
| Money flow | Who pays | Who receives | Amount | Notes |
| Trip charge | Member, on the card on file when a contractor accepts | Contractor, released on arrival | $99 per request, one per trade and zone, the same in all three trades, day or night, set by SOS SMS (decision 5) | Market reference: plumbing trip charges about $75 to $100 when charged (S28, C); HVAC service calls $70 to $200 (S95, C); electrical $52 to $200 (S96, C); after-hours service call fees commonly $150 to $250 (S50, C) |
| Membership | Member, monthly or yearly, billed to the card on file | SOS SMS | Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350 (R51, R52, R65, R66) | The member side of SOS SMS revenue (Run 2 Phase 9); no fee per request |
| Share of the trip charge | Contractor | SOS SMS | $25 per completed paid job, from the first job (the contractor fee); the contractor receives $74 of the $99 | Nothing is paid to join or to see a request, so "zero cost to join" stays true as written |
| Share of the job | Contractor | SOS SMS | $0. The price for the work stays the contractor's | Payment for the work never flows through SOS SMS |
| Late-arrival credit | SOS SMS | Member, on Plus and Premier | The membership paid in the 6 months (Plus) or 12 months (Premier) before the request, on the next bills | Option D below, decided 2026-10-20; the contractor's trip charge is untouched |
| Payment processing | Deducted from the flows above | Stripe Connect | About 2.9% + $0.30 a card charge (planning value) | Stripe's standard US card price |

## Sheet: Late_Arrival

| The late-arrival rule: the options for decision 3, and the one decided |
| Option | Rule | What happens to "paid to show up" | Contractor behavior to expect | Cost to SOS SMS |
| A. Contractor forfeits | Any arrival after 90 minutes refunds the member from the contractor's trip charge | Narrows to "paid when you arrive inside the 90-minute window" | Fewer night acceptances; contractors decline anything far away | None |
| B. SOS SMS absorbs | SOS SMS refunds the member and still pays the contractor | Holds as written | Highest acceptance; some contractors may accept jobs they cannot reach in time | Refund rate × trip charge, funded from membership revenue |
| C. Fault-based (the 2026-10-03 rule, replaced) | The contractor commits to an arrival time when accepting. If they miss their own committed time, the member's refund comes from their trip charge. If no contractor accepts in time, or the miss is not the contractor's, SOS SMS pays | Narrows to "the trip charge is yours when you arrive by the time you committed to", which every contractor controls | Contractors commit to times they can keep, which protects the member promise too | Refunds only for misses SOS SMS causes (no acceptance, dispatch failure) |
| D. The trip charge stands (decided) | The contractor commits to an arrival time inside the window when accepting. A late arrival keeps the trip charge, because it pays for the work; the late arrival is recorded, and two late arrivals or no-shows in 90 days pause the contractor's requests until a person reviews them (R67). A contractor who accepts and does not come is paid nothing, and the trip charge goes back to the member. SOS SMS credits the member 6 months of membership on Plus and 12 on Premier | Holds as written: "paid to show up" is true whenever the contractor shows up | Contractors commit to times they can keep, because standing depends on it; no fear that a late arrival forfeits the trip | The late-arrival credit on Plus and Premier, about $0.17 a Plus member a month at a 5 percent late share (R29) |
| Option D keeps "paid to show up" true for every contractor who shows up, and keeps the member's guarantee honest through the credit SOS SMS pays on Plus and Premier. Standing, not the trip charge, is what holds a contractor to the time they committed to. The member-side guarantee is worded around the committed arrival time inside the 90-minute window: 90 minutes from the member's request text, and on Plus and Premier the membership paid in the 6 months (Plus) or 12 months (Premier) before the request credited on a late arrival (Run 2 decision 4, merged decision 3). Decided 2026-10-20, the tiers revision; option C, decided 2026-10-03, refunded the member from a late contractor's trip charge. |

## Sheet: ROI_Anchors

| Anchor 1. Cost of the problem |
| Problem Scenario | Cost Without SOS SMS | SOS SMS Cost | Formula |
| Lead spend on requests that never became jobs | Monthly lead spend × (1 minus close rate), × 12 | $0 in lead fees; $25 per completed paid job | (leads × cost per lead) × (1 - close rate) × 12 |
| Unpaid trips | Unpaid trips a month × trip charge the contractor would have charged, × 12 | $0, if the trip charge is collected before rolling | unpaid trips × trip charge × 12 |
| After-hours answering | Monthly answering service cost × 12 | $0 | monthly fee × 12 |
| Worked example, internal only, built from grade C ranges: 20 plumbing leads a month at $40 each (inside S03 and S06 ranges) with a 15 percent close rate (inside S03's reported 10 to 20 percent) is $800 of lead spend, about 3 booked jobs, and $680 a month on requests that never became work, or $8,160 a year. These are illustrative inputs, not a claim about any contractor. |
| Anchor 2. Alternative comparison |
| Alternative | Cost per lead or call | Per booked job at 10 percent close | At 20 percent | At one in three | SOS SMS lead cost | Source and grade |
| C1 Angi Leads (plumbing) | $25 to $60, plus about $300 a year | $250 to $600 | $125 to $300 | $75 to $180 | $0 | S03, C |
| C2 Thumbtack (plumbing) | $25 to $45 | $250 to $450 | $125 to $225 | $75 to $135 | $0 | S06, C |
| C3 Google LSA (plumbing) | about $57 to $69 | $570 to $690 | $285 to $345 | $171 to $207 | $0 | S08, C |
| Search ads (plumbing) | about $129 per tracked lead | $1,290 | $645 | $387 | $0 | S15, B |
| Angi Leads (HVAC service call) | $15 to $40 | $150 to $400 | $75 to $200 | $45 to $120 | $0 | S98, C |
| Thumbtack (HVAC basic service) | $25 to $60 | $250 to $600 | $125 to $300 | $75 to $180 | $0 | S98, C |
| Google LSA (HVAC) | about $51 | $510 | $255 | $153 | $0 | S98, C |
| Google LSA (electrical) | about $39 | $390 | $195 | $117 | $0 | S98, C |
| C4 Service Direct (plumbing, exclusive) | $60 to $255 | $600 to $2,550 | $300 to $1,275 | $180 to $765 | $0 | S10, A |
| C4 Service Direct (water damage, exclusive) | $500 to $2,250 | Exclusive calls book at a higher rate; the vendor claims 85 percent for water damage (C), so the 10 percent to one-in-three columns understate this option |  |  | $0 | S10, A for price |
| Answering service | $250 to $720 a month, fixed | n/a, a cost not a source of jobs |  |  | $0 | S21, C |
| In-house 24/7 dispatcher | about $205,900 a year in wages | n/a |  |  | $0 | S22, A, arithmetic |
| C5 Warranty network | No fee; set rates below private work | Discount set by each warranty company's rate card |  |  | $0 | S20, C |
| C6 Status quo | $0 | $0 |  |  | $0 |
| Savings per booked job are the alternative's cost per booked job minus the $25 contractor fee: about $100 against the cheapest plumbing per-lead options at a 20 percent close rate, and about $50 against the cheapest HVAC service-call leads. |
| Anchor 3. Breakeven: the ceiling on the contractor fee |
| Comparison | Alternative cost per booked job (20 percent close, low to high) | Fee ceiling for SOS SMS to stay cheaper | Payback period |
| Against Thumbtack | $125 to $225 | Under $125 to stay cheaper across the range | Immediate: there is no upfront cost to pay back |
| Against Angi | $125 to $300 | Under $125 | Immediate |
| Against Google LSA | $285 to $345 | Under $285 | Immediate |
| Against Angi, HVAC service call | $75 to $200 | Under $75 | Immediate |
| Against Google LSA, electrical | about $195 | Under $195 | Immediate |
| Against status quo | $0 | Any fee is a cost the status quo does not have; the case rests on the trip charge and the extra jobs, not on savings | n/a |
| The lowest ceiling, about $75 per booked job against the cheapest HVAC service-call leads at a 20 percent close rate, is the number to beat in any trade; the $25 fee is a third of it, and a fifth of the plumbing ceiling of about $125. Grade C inputs, internal only; the contractors' real close rates are counted from their first jobs (R43). |
| "One job pays for" calculator, adapted |
| Contractor's cost per lead | Close rate | Lead spend behind one booked job | Message |
| {{their number}} | {{their number}} | {{cost per lead ÷ close rate}} | "Every booked job from your leads cost you {{result}} before the truck moved. On SOS SMS, seeing a request costs nothing." |
| Worked example, internal only: $40 per lead at 20 percent close is $200 of lead spend behind each booked job. |

## Sheet: Decisions

| Pricing decisions, decided 2026-10-03, revised 2026-10-11 and 2026-10-20 |
| # | Decision | Decided | Where it shows |
| 1 | Where SOS SMS revenue comes from | Members pay a plan, Basic, Plus, or Premier, monthly or annual (revised 2026-10-20, the tiers revision); contractors pay $25 per completed paid job from the first job, below the Anchor 3 ceiling, which adds to the contribution each member brings (../../marketplace/speed-to-scale-plan.md, section 5) | Phases 6 and 8 in both runs |
| 2 | Late-arrival rule | Option D, revised 2026-10-20: the trip charge stands on a late arrival; a no-show is paid nothing; two in 90 days pause requests (R67) | Copy drills 4 and 5; Run 2 guarantee wording |
| 3 | Who sets the trip charge | SOS SMS: one trip charge per trade and zone, $99 in each of plumbing, HVAC, and electrical, so the member sees one price before joining; contractors keep their price for the work | Run 2 Phase 9 |
| 4 | Payout timing | Stripe Connect; paid out within 2 business days of arrival, stated in writing | Copy drill 5 |
| 5 | The contractor fee | $25 per completed paid job from the first job, deducted from the trip charge payout, the same for every contractor in every trade; no founding period or founding terms | Contractor agreement |
