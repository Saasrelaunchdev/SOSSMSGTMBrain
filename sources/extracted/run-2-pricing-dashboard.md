# Source: run-2-pricing_dashboard.xlsx

Original path: `Fit137/SOSSMSGTMBuild`, `gtm/run-2-demand-customers/output/pricing_dashboard.xlsx`
Type: xlsx
Size: 23,597 bytes

## Sheet: README

| Phase 9. Pricing and Packaging Dashboard, customer side |
| A customer buys one emergency call, rarely. The skill's subscription tiers describe nothing they buy, so per ../SKILL-ADAPTATION.md this phase builds the customer side of the take rate. Every SOS SMS price is {TBD} (open decision 3). Run 1 Phase 9 recommended that SOS SMS's revenue come from this... |
| Live calculators are in pricing_dashboard.xlsx. |
| Generated from gtm/run-2-demand-customers/output/phase-9-pricing.md by gtm/tools/render.py. The Markdown file is the source of truth; edit it, then re-render. |
| Source IDs (S01, S02, ...) refer to gtm/research/SOURCES.md, which gives each source's URL and evidence grade (A primary, B secondary, C vendor estimate). |
| {TBD} marks an SOS SMS unknown. SOS SMS is pre-launch: no figure in this workbook is an SOS SMS result. |

## Sheet: Calculators

| Customer-side calculators (live formulas) |
| Legend: yellow cells with blue text are inputs. The example trip charge is an illustrative market reference (S28: $75 to $100 when charged), NOT an SOS SMS price. Every SOS SMS price is {TBD}. |
| 1. Guarantee economics: the minimum SOS SMS fee per request |
| Trip charge per request (T) | 90 | Illustrative only. Not an SOS SMS price |
| Share of requests with an SOS-caused miss | 0.05 | Illustrative; {TBD} until the founding zone runs |
| Refund as a share of the trip charge | 1 | Recommended: the full trip charge (Run 2 Phase 9) |
| Payment processing per request | 0 | {TBD}, depends on the provider |
| Operations cost per request | 0 | {TBD} |
| Expected refund cost per request | 4.5 |
| Minimum SOS SMS fee per request to break even | 4.5 |
| Minimum fee as a share of the trip charge | 0.05 |
| Sensitivity: refund cost per request by SOS-caused miss share |
| SOS-caused miss share | Refund cost per request | As a share of T |
| 0.02 | 1.8 | 0.02 |
| 0.05 | 4.5 | 0.05 |
| 0.1 | 9 | 0.1 |
| 0.2 | 18 | 0.2 |
| 2. What the customer pays before the repair starts (Phase 9, Anchor 2) |
| Option | Low | High | Source |
| After-hours service call fee, search and call | 150 | 250 | S50, C |
| Home warranty service fee (covered failures only) | 75 | 125 | S56, C |
| SOS SMS trip charge ({TBD}) |
| SOS SMS fee per request ({TBD}) |
| SOS SMS cost before the repair starts | {TBD} |
| Extra cost of SOS SMS if the work goes ahead (trip charge credited) | {TBD} |
| Compared with the after-hours call fee, low to high | {TBD} |
| 3. Paid acquisition: cost per paid job and contribution (product-led, paid search first) |
| Example inputs: cost per click and click-to-first-text from S15 (grade B, plumbing search benchmark). First-text-to-paid rate and owned share are illustrative assumptions, {TBD} until measured. |
| Cost per click | 10.49 | S15, B. Emergency keywords averaged $66.82 in one dataset (S69, C) |
| Click to first text rate | 0.0763 | S15, B: plumbing click-to-lead rate |
| First text to paid request rate | 0.5 | Illustrative assumption |
| Owned share of requests (saved number, shares, organic) | 0 | 0 for a new zone; rises as loops work |
| Paid jobs per acquired household over its lifetime | 1 | 1 means no repeat or referral yet |
| SOS SMS customer fee per request ({TBD}) |  | Enter once open decision 2 sets it |
| Contractor fee per completed job ({TBD}, after the founding period) |  | Run 1 Phase 9: below the Anchor 3 ceiling |
| Cost per first text | 137.483617300131 |
| Paid cost per paid job | 274.967234600262 |
| Blended cost per paid job (after owned share) | 274.967234600262 |
| Acquisition cost per job over the household's lifetime | 274.967234600262 |
| Take per job (customer fee plus contractor fee) | {TBD} |
| Contribution per job after acquisition, refunds, and processing | {TBD} |
| Take per job needed to break even | 279.467234600262 |

## Sheet: Value_Metric

| Step 9.1. Value metric selection |
| Denominator | Correlation to Value | Scalability | Ease of Measurement | Score (1 to 10) | Verdict |
| Per request, flat (trip charge plus an SOS SMS fee) | High. One request is one emergency handled | High | High | 8.2 | Primary |
| Per outcome: the fee is what the guarantee refunds on a miss | High. The customer pays for arrival inside the window | High | Medium. Needs arrival logging | 7.1 | Built into the primary: the guarantee makes the request price outcome-backed |
| Per completed repair, as a percentage | Medium. SOS SMS does not control the repair or its price | Medium | Low unless payment for the work flows through SOS SMS | 4.6 | Reject at launch |
| Per household per year (membership) | Low to medium. Emergencies are rare for any one household | Medium | High | 3.9 | Later option only; competes with home warranties (D6) |
| Per capability (priority, after-hours premium) | Medium | Medium | High | 3.2 | Reject. An after-hours premium is the surprise fee customers complain about (S50, S51) |
| Recommendation for the founders (not a decision): |
| Primary value metric: per request. The customer sees two lines before anyone is sent: the trip charge, credited to the repair if they go ahead, and the SOS SMS fee, which pays for dispatch and the guarantee. |
| Secondary usage metric, for tracking: requests per 1,000 owner-occupied homes in the zone per month. |
| Rationale: the customer is paying for speed and certainty. A flat, stated price matches that, avoids the after-hours surprise the research found customers resent, and puts the guarantee's cost where its value is felt. |

## Sheet: Packaging

| Step 9.2. Packaging: the customer price structure |
| Plan | Price | What it covers | Guarantee | Position | Target share of requests |
| Standard request | Trip charge {TBD} plus SOS SMS fee {TBD} | Dispatch to the matched contractors; the trip; the trip charge credited to the repair if the customer goes ahead | 90-minute guarantee, scope per open decision 4 | Default | About all requests at launch |
| Request outside covered hours (if offered at all) | Same | Same | None, stated before the customer agrees | Only if the founders choose to serve hours below the density target | {TBD}, possibly zero |
| Household membership (flag only) | {TBD} a year | Reduced or waived SOS SMS fee | Same | Later option; competes with home warranties | 0 at launch |
| Not offered: requests outside the founding zone. Those customers are told plainly that SOS SMS does not cover their area yet. |

## Sheet: Guarantee_Economics

| Guarantee economics |
| Share of requests with an SOS-caused miss | Refund cost per request, as a share of the trip charge | Minimum fee to cover refunds alone |
| 2 percent | 0.02 × T | 2 percent of T |
| 5 percent | 0.05 × T | 5 percent of T |
| 10 percent | 0.10 × T | 10 percent of T |
| 20 percent | 0.20 × T | 20 percent of T |
| Under option B (SOS SMS absorbs every miss), replace "SOS-caused" with all misses, and the fee must cover the full miss rate. The miss rate is {TBD} until the founding zone runs. The table is arithmetic, not a forecast. |

## Sheet: Paid_Acquisition

| Paid acquisition economics |
| Basis | Cost per click | Click to first text | Cost per first text | Paid cost per paid job at 50 percent | Source and grade |
| Plumbing search benchmark | $10.49 | 7.63 percent | about $137 | about $275 | S15, B |
| Emergency plumbing dataset | $66.82 | 31 percent | about $216 | about $431 | S69, C |
| Microsoft Ads, 30 to 60 percent cheaper clicks on the benchmark basis | $4.20 to $7.34 | 7.63 percent, assumed equal | about $55 to $96 | about $110 to $192 | S74, C |
| Paid acquisition economics |
| Owned share of requests | Blended cost per paid job, benchmark basis |
| 0 percent | about $275 |
| 30 percent | about $192 |
| 50 percent | about $137 |
| 70 percent | about $82 |
| What it means. A customer fee on its own will not pay back a paid-search job on the first request: the trip charge benchmarks are $75 to $100 (S28) and after-hours call fees $150 to $250 (S50). Four levers close the gap, and Phase 9 of Run 1 and the speed-to-scale plan carry them: a rising owned ... |

## Sheet: ROI_Anchors

| Anchor 1. Cost of the problem |
| Problem Scenario | Cost Without Solution | SOS SMS Cost | ROI Multiple |
| Water damage that becomes an insurance claim | Average water damage and freezing claim $13,954 (2018 to 2022) (S57, B) | Trip charge {TBD} plus fee {TBD}, trip charge credited to the repair | Not computed. SOS SMS gets a contractor there; it does not claim to prevent the damage |
| Waiting until morning | EPA: dry water-damaged areas within 24 to 48 hours to prevent mold (S58, A) | Same | Not computed, same reason |
| Anchor 2. Alternative comparison |
| Alternative | Their Cost Before the Repair | What They Promise on Arrival | SOS SMS | Source and grade |
| D1 Search and call, after hours | Service call fees commonly $150 to $250 after hours; labor 1.5 to 3 times standard rates | Nothing, unless the business offers it | Trip charge {TBD}, credited to the repair; fee {TBD} | S50, C |
| D2 Roto-Rooter | No extra charge for nights, weekends, holidays; job price varies | Typically within two hours for true emergencies, no refund promise (C) | Same | S41, A and C |
| D3 Benjamin Franklin | Varies by franchise | $5 a minute late, up to $300, on scheduled appointments | Same; [the trip charge] back if not there within 90 minutes of [scope] | S40, A |
| D4 Angi, D5 Thumbtack | Free to request; booking prices vary | No arrival guarantee found; guarantees cover the work | Same | S44 to S46, A |
| D6 American Home Shield | Service fee typically $75 to $125, for covered failures | Contractor contacted within 4 business hours, or 48 hours on weekends and holidays; no guarantee of timely emergency service | Same | S20, B; S56, C |
| Do it yourself, or wait | $0 tonight | n/a; the damage keeps going | Same | S57, S58 |
| Savings percentage against each alternative is {TBD} until the trip charge and fee exist. Two honest positions SOS SMS can take now: against D6, a covered failure is usually cheaper through the warranty, and SOS SMS should say so; against D1, the comparison is the after-hours service call fee aga... |
| Anchor 3. Breakeven |
| Plan | Price per Request | Cost Components SOS SMS Must Cover | Breakeven Condition | Payback Period |
| Standard request | Trip charge {TBD} plus fee F {TBD} | Refunds (share × T), processing, operations | F ≥ (SOS-caused miss share × T) + processing + operations per request | n/a for a per-request price |
| "One outcome" message, adapted |
| Outcome | Message |
| The window is missed | "If your contractor isn't there within 90 minutes of [your text], [the trip charge] comes back to you, automatically." |
| The work goes ahead | "Your [trip charge] counts toward the bill, so you don't pay twice." |

## Sheet: Decisions

| Pricing decisions the founders need to make, in order |
| # | Decision | Recommended | Blocks |
| 1 | Where SOS SMS revenue comes from (shared with Run 1) | A per-request SOS SMS fee on the customer side; $0 to contractors during the founding period, then a per-completed-job contractor fee, because paid search costs are unlikely to be covered by the customer fee alone | Phases 6 and 8, both runs |
| 2 | The guarantee scope (open decision 4) | Clock starts at the customer's text; refund equal to the trip charge; covered areas and hours named; when no one accepts, the customer is told within {TBD} minutes and pays nothing | Phase 6 drill 3; the guarantee page |
| 3 | Who sets the trip charge | One SOS SMS trip charge per trade and zone, so the customer sees one price before dispatch | First reply; Run 1 terms |
| 4 | Is the SOS SMS fee refunded on a miss too | Yes, if the miss is SOS-caused; it makes the promise simpler to state | Guarantee page |
| 5 | What happens for customers without a card | {TBD}: a pay-on-arrival path with the contractor, without the guarantee, stated plainly | Phase 7 blocker |
| 6 | The paid search ceiling per zone | {TBD}: the highest blended cost per paid job the founders will accept while proving a zone, and the date by which it must fall | Phase 8 Channel 1 budgets; speed-to-scale plan, section 8 |
