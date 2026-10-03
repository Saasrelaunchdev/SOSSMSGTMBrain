# Source: run-1-pricing_dashboard.xlsx

Original path: `/tmp/claude-0/-home-user-SOSSMSGTMBuild/58c92b90-19cc-5fc7-89d9-27b8a51bab42/scratchpad/xsrc/run-1-pricing_dashboard.xlsx`
Type: xlsx
Size: 24,219 bytes

## Sheet: README

| Phase 9. Pricing and Packaging Dashboard, contractor side |
| The skill assumes a subscription: per-seat value metrics and four Decoy, Hero, Anchor plans. Contractors pay nothing to join SOS SMS by design, so per ../SKILL-ADAPTATION.md this phase builds the supply side of the take rate instead. Every SOS SMS price is {TBD} until the founders settle open dec... |
| What this phase delivers: a recommended structure, the decision options with their consequences, and calculators that produce numbers the moment the inputs exist. The live calculators are in pricing_dashboard.xlsx. |
| Generated from gtm/run-1-supply-contractors/output/phase-9-pricing.md by gtm/tools/render.py. The Markdown file is the source of truth; edit it, then re-render. |
| Source IDs (S01, S02, ...) refer to gtm/research/SOURCES.md, which gives each source's URL and evidence grade (A primary, B secondary, C vendor estimate). |
| {TBD} marks an SOS SMS unknown. SOS SMS is pre-launch: no figure in this workbook is an SOS SMS result. |

## Sheet: Calculators

| Contractor-side calculators (live formulas) |
| Legend: yellow cells with blue text are inputs; everything else is calculated. Example inputs are illustrative values inside grade C market ranges (S03, S06), not data about any contractor or SOS SMS. |
| 1. Lead Cost Check (the contractor's own numbers) |
| Leads paid for last month | 20 | Illustrative |
| Average cost per lead | 40 | Illustrative; inside the S03 and S06 plumbing ranges |
| Share of leads that became booked jobs | 0.15 | Illustrative; inside S03's reported 10 to 20 percent |
| Trips last month without getting paid | 2 | Illustrative |
| Trip charge the contractor would have charged | 90 | Illustrative; S28 reports $75 to $100 when charged |
| Monthly answering service cost | 0 | Enter 0 if none; S21 reports $250 to $720 |
| Monthly lead spend | 800 |
| Booked jobs from leads | 3 |
| Lead spend per booked job | 266.666666666667 |
| Monthly spend on leads that never became jobs | 680 |
| Yearly spend on leads that never became jobs | 8160 |
| Yearly value of unpaid trips | 2160 |
| Yearly answering service cost | 0 |
| Yearly total of the three leaks | 10320 |
| 2. Cost per booked job by alternative (Phase 9, Anchor 2) |  |  |  | Close rates (inputs) |
| Alternative | Cost per lead, low | Cost per lead, high | Source | 0.1 | 0.2 | 0.333333333333333 |
| C1 Angi Leads (plumbing) | 25 | 60 | S03, C | $250 to $600 | $125 to $300 | $75 to $180 |
| C2 Thumbtack (plumbing) | 25 | 45 | S06, C | $250 to $450 | $125 to $225 | $75 to $135 |
| C3 Google LSA (plumbing) | 57 | 69 | S08, C | $570 to $690 | $285 to $345 | $171 to $207 |
| Search ads (plumbing) | 129 | 129 | S15, B | $1,290 to $1,290 | $645 to $645 | $387 to $387 |
| C4 Service Direct (plumbing, exclusive) | 60 | 255 | S10, A | $600 to $2,550 | $300 to $1,275 | $180 to $765 |
| SOS SMS lead cost per booked job | 0 |
| SOS SMS per-completed-job fee, if ever introduced ({TBD}) | 0 |
| 3. Fee ceiling (Phase 9, Anchor 3) |
| Lowest cost per booked job among per-lead platforms at the middle close rate | 125 |
| Any SOS SMS per-job fee below this stays cheaper than every per-lead option above |
| Headroom at the fee entered in B31 | 125 |

## Sheet: Value_Metric

| Step 9.1. Value metric selection |
| Denominator | Correlation to Value | Scalability | Ease of Measurement | Score (1 to 10) | Verdict |
| Per request received (per lead) | Low. Value arrives only when a job happens; this is exactly the complaint against C1 to C4 | High | High | 1.8 | Reject. Contradicts VP1 and the positioning |
| Per contractor or technician, monthly (per seat) | Low. A quiet month costs the same as a busy one | High | High | 2.6 | Reject. "No subscription" is a stated promise |
| Per accepted job (usage) | Medium. Accepting is a choice, but the customer may still decline the quote | High | High | 5.7 | Possible, second choice |
| Per completed paid job, as a share of the trip charge or the job (outcome) | High. The contractor pays only when revenue exists | High | Medium. SOS SMS sees the trip charge but not the job value unless payment for the work flows through it | 7.4 | Best fit if a contractor fee is ever introduced |
| Paid priority or extra zones (capability) | Medium | Medium | High | 3.1 | Flag only. Conflicts with "every matched contractor sees the request at once" and with "decline freely" |
| Recommendation for the founders (not a decision): |
| Primary value metric: none at launch. Contractors pay $0. Supply is the constrained side, the customer promise depends on density, and "no lead fees" is the reason a contractor tries one more platform. |
| A contractor fee after the founding period, planned from the start: per completed paid job, never per request, below the Anchor 3 ceiling, and written into the founding agreement so nobody is surprised. The product-led plan buys customers with paid search, and the speed-to-scale plan (section 5) ... |
| Secondary usage metric, for tracking only: accepted jobs per active contractor per month, by hour band. It measures whether the supply side is healthy, not what to charge. |
| Rationale: in a marketplace, the side whose participation is hardest to get is usually subsidized, and the side that captures urgent value pays. Here the customer is the one paying for speed and the guarantee, and the 90-minute refund liability also sits on the customer side. Monetizing that side... |

## Sheet: Packaging

| Step 9.2. Packaging: the contractor participation structure |
| Plan | Price to contractor | Requests | Commitments | Position | Target share of contractors |
| Founding contractor | $0 | All matched requests in their zone, first in each new zone | Response window when available ({TBD} minutes); credit the trip charge; current documents; five-job feedback; permission clause | Launch cohort that makes the zone dense enough to open | {TBD}, set by the Phase 5 density number per zone |
| Standard contractor | $0. A per-completed-job fee only if open decision 2 introduces one ({TBD}) | All matched requests | Same, without the feedback commitment | Default after the founding period | {TBD} |
| Priority (flag only) | Not designed | n/a | n/a | Conflicts with the dispatch rule; revisit only if the rule changes | 0 |

## Sheet: Take_Rate

| The take rate, both sides |
| Money flow | Who pays | Who receives | Amount | Notes |
| Trip charge | Customer | Contractor, released on arrival | {TBD}. Who sets it, SOS SMS or each contractor, is also {TBD} | Market reference: plumbing trip charges about $75 to $100 when charged (S28, C); after-hours service call fees commonly $150 to $250 (S50, C) |
| SOS SMS service fee | Customer, on top of the trip charge | SOS SMS | {TBD} | Recommended home for SOS SMS revenue (Run 2 Phase 9) |
| Share of the trip charge | Contractor | SOS SMS | {TBD}, recommended $0 | Any value above $0 makes "zero cost to join" untrue as written |
| Share of the job | Contractor | SOS SMS | {TBD}, recommended $0 at launch | Requires payment for the work to flow through SOS SMS |
| 90-minute refund | SOS SMS, or the contractor, per the late-arrival rule | Customer | Equal to the trip charge, or {TBD} | See the late-arrival options below |
| Payment processing | Deducted from the flows above | Payment provider | {TBD} | Depends on the provider chosen |

## Sheet: Late_Arrival

| The late-arrival rule: options for open decision 3 |
| Option | Rule | What happens to "paid to show up" | Contractor behavior to expect | Cost to SOS SMS |
| A. Contractor forfeits | Any arrival after 90 minutes refunds the customer from the contractor's trip charge | Narrows to "paid when you arrive inside the 90-minute window" | Fewer night acceptances; contractors decline anything far away | None |
| B. SOS SMS absorbs | SOS SMS refunds the customer and still pays the contractor | Holds as written | Highest acceptance; some contractors may accept jobs they cannot reach in time | Refund rate × trip charge, funded from the customer fee |
| C. Fault-based (recommended) | The contractor commits to an arrival time when accepting. If they miss their own committed time, the customer's refund comes from their trip charge. If no contractor accepts in time, or the miss is not the contractor's, SOS SMS pays | Narrows to "the trip charge is yours when you arrive by the time you committed to", which every contractor controls | Contractors commit to times they can keep, which protects the customer promise too | Refunds only for misses SOS SMS causes (no acceptance, dispatch failure) |
| Option C ties the refund to the promise the contractor made, which is fair to the contractor and keeps the customer's guarantee honest. It requires the customer-side guarantee to be worded around the committed arrival time inside the 90-minute window (Run 2, open decision 4). Recommendation, not ... |

## Sheet: ROI_Anchors

| Anchor 1. Cost of the problem |
| Problem Scenario | Cost Without SOS SMS | SOS SMS Cost | Formula |
| Lead spend on requests that never became jobs | Monthly lead spend × (1 minus close rate), × 12 | $0 in lead fees; per-job fee {TBD} | (leads × cost per lead) × (1 - close rate) × 12 |
| Unpaid trips | Unpaid trips a month × trip charge the contractor would have charged, × 12 | $0, if the trip charge is collected before rolling | unpaid trips × trip charge × 12 |
| After-hours answering | Monthly answering service cost × 12 | $0 | monthly fee × 12 |
| Worked example, internal only, built from grade C ranges: 20 plumbing leads a month at $40 each (inside S03 and S06 ranges) with a 15 percent close rate (inside S03's reported 10 to 20 percent) is $800 of lead spend, about 3 booked jobs, and $680 a month on requests that never became work, or $8,... |
| Anchor 2. Alternative comparison |
| Alternative | Cost per lead or call | Per booked job at 10 percent close | At 20 percent | At one in three | SOS SMS lead cost | Source and grade |
| C1 Angi Leads (plumbing) | $25 to $60, plus about $300 a year | $250 to $600 | $125 to $300 | $75 to $180 | $0 | S03, C |
| C2 Thumbtack (plumbing) | $25 to $45 | $250 to $450 | $125 to $225 | $75 to $135 | $0 | S06, C |
| C3 Google LSA (plumbing) | about $57 to $69 | $570 to $690 | $285 to $345 | $171 to $207 | $0 | S08, C |
| Search ads (plumbing) | about $129 per tracked lead | $1,290 | $645 | $387 | $0 | S15, B |
| C4 Service Direct (plumbing, exclusive) | $60 to $255 | $600 to $2,550 | $300 to $1,275 | $180 to $765 | $0 | S10, A |
| C4 Service Direct (water damage, exclusive) | $500 to $2,250 | Exclusive calls book at a higher rate; the vendor claims 85 percent for water damage (C), so the 10 percent to one-in-three columns understate this option |  |  | $0 | S10, A for price |
| Answering service | $250 to $720 a month, fixed | n/a, a cost not a source of jobs |  |  | $0 | S21, C |
| In-house 24/7 dispatcher | about $205,900 a year in wages | n/a |  |  | $0 | S22, A, arithmetic |
| C5 Warranty network | No fee; set rates below private work | Discount {TBD} percent of each job |  |  | $0 | S20, C |
| C6 Status quo | $0 | $0 |  |  | $0 |
| Savings percentage against each alternative is 100 percent of lead cost while SOS SMS charges no fee. If a per-completed-job fee f is introduced, savings per booked job become (alternative cost per booked job) minus f. |
| Anchor 3. Breakeven: the ceiling on any future contractor fee |
| Comparison | Alternative cost per booked job (20 percent close, low to high) | Fee ceiling for SOS SMS to stay cheaper | Payback period |
| Against Thumbtack | $125 to $225 | Under $125 to stay cheaper across the range | Immediate: there is no upfront cost to pay back |
| Against Angi | $125 to $300 | Under $125 | Immediate |
| Against Google LSA | $285 to $345 | Under $285 | Immediate |
| Against status quo | $0 | Any fee is a cost the status quo does not have; the case rests on the trip charge and the extra jobs, not on savings | n/a |
| The lowest ceiling, about $125 per booked job against the cheapest per-lead options at a 20 percent close rate, is the number to beat. Grade C inputs: recompute with real close rates from the founding contractors' invoices before any fee is set. |
| "One job pays for" calculator, adapted |
| Contractor's cost per lead | Close rate | Lead spend behind one booked job | Message |
| [their number] | [their number] | [cost per lead ÷ close rate] | "Every booked job from your leads cost you [result] before the truck moved. On SOS SMS, seeing a request costs nothing." |
| Worked example, internal only: $40 per lead at 20 percent close is $200 of lead spend behind each booked job. |

## Sheet: Decisions

| Pricing decisions the founders need to make, in order |
| # | Decision | Recommended | Blocks |
| 1 | Where SOS SMS revenue comes from | Customer service fee; $0 to contractors during the founding period; a per-completed-job contractor fee after it, below the Anchor 3 ceiling, because paid search acquisition costs are unlikely to be covered by a customer fee alone (../../marketplace/speed-to-scale-plan.md, section 5) | Phases 6 and 8 in both runs |
| 2 | Late-arrival rule | Option C, fault-based | Copy drills 4 and 5; Run 2 guarantee wording |
| 3 | Who sets the trip charge | {TBD}. If contractors set it, the customer sees different prices for the same request; if SOS SMS sets it, contractors lose a lever | Run 2 Phase 9 |
| 4 | Payout timing | As fast as the payment provider allows, stated in writing | Copy drill 5 |
| 5 | Any future contractor fee | Per completed paid job only, below the Anchor 3 ceiling, never during the founding period | Founding agreement |
