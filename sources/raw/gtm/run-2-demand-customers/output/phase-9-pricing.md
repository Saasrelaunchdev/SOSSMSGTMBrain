# Phase 9. Pricing and Packaging Dashboard, member side

A member pays to be ready before anything breaks. Per `../SKILL-ADAPTATION.md`, the skill's subscription logic fits, narrowed to one membership billed monthly or annually. The prices here are planning values set by the membership revision on 2026-10-11 (decision 2, revised; `../../marketplace/resolution-register.md`, R51 to R64) and recomputed in the pricing model (`../../pricing/pricing-model.md`): $10 a month or $100 a year until the launch price is set in Stage 0, shown in copy as `{{monthly price}}` and `{{annual price}}`, plus the $99 trip charge on use (decision 5). Contractors pay nothing in the founding period, then $25 per completed paid job (Run 1 Phase 9).

The live model is `SOS_SMS_Pricing_Model.xlsx` in the Google folder; the calculators in `pricing_dashboard.xlsx` follow this file.

## Step 9.1. Value metric selection

<!-- sheet: Value_Metric -->
| Denominator | Correlation to Value | Scalability | Ease of Measurement | Score (1 to 10) | Verdict |
|---|---|---|---|---|---|
| Per household, monthly or annual (membership) | High. The member pays to be ready before anything breaks, and every month they are | High | High | 8.2 | Primary |
| Per outcome: the guarantee refunds the trip charge on a miss | High. The member pays for arrival inside the window | High | Medium. Needs arrival logging | 7.1 | Built into the primary: the guarantee is part of the membership |
| Per completed repair, as a percentage | Medium. SOS SMS does not control the repair or its price | Medium | Low unless payment for the work flows through SOS SMS | 4.6 | Reject |
| Per request, an SOS SMS fee at the moment of need | Medium. Charged at the worst moment, after a search a member would rather not make | High | High | 4.2 | Replaced by the membership (decision 2, revised 2026-10-11) |
| Per capability (priority, after-hours premium) | Medium | Medium | High | 3.2 | Reject. An after-hours premium is the surprise fee customers complain about (S50, S51) |

**Decided (decision 2), revised 2026-10-11 by the membership revision:**

- **Primary value metric: per household, monthly or annual.** The member pays `{{monthly price}}` a month or `{{annual price}}` a year (planning values $10 and $100, R51, R52), billed to the card on file. No fee per request.
- **The use charge:** the $99 trip charge, on the card on file when a contractor accepts, paid to the contractor and credited to the repair (decision 5).
- **Secondary usage metrics, for tracking:** requests per member per year (planning value 0.25, R58), and members per zone against about 430 (R64).
- **Rationale:** the member pays to be ready, so the emergency is one text with nothing to agree to at the worst moment. A flat monthly or annual price, stated before joining, avoids the after-hours surprise the research found customers resent, and the guarantee's cost sits inside the membership.

## Step 9.2. Packaging: the member price structure

<!-- sheet: Packaging -->
| Plan | Price | What it covers | Guarantee | Position | Target share |
|---|---|---|---|---|---|
| Monthly membership | `{{monthly price}}` a month (planning value $10, R51) | One-text dispatch to the matched contractors; an arrival time on acceptance; a person by text; the readiness kit (R53) | 90 minutes from the member's request text; the $99 trip charge back on a miss | Default | Measured from the first members |
| Annual membership | `{{annual price}}` a year (planning value $100: two months free, R52) | The same | The same | The second shape; renews each year with a reminder before `{{renewal date}}` (R56) | Measured from the first members |
| The trip charge, on use | $99 per request, on the card on file when a contractor accepts | The contractor's trip, credited to the repair if the member goes ahead | Refunded on a miss | Every request | n/a |
| Request outside covered hours | Not dispatched | Stop-the-water steps and the safety line by text, free | None | The membership page names covered hours (R15) | 0 |
| A text from a non-member | Not dispatched | The safety line, the stop-the-water steps, and how to join, free (R57) | None | Dispatch is for members | 0 |

Not offered: memberships outside open zones. Homeowners there are told plainly that SOS SMS does not cover their area yet, and may join the launch list (R55). The membership does not pay for the repair or parts and carries no guarantee on the work (R21, R53).

### Expansion levers

1. More trades behind the same membership: water damage first, then electrical, HVAC, and locksmith, each opened only when Run 1 reaches density for that trade.
2. More zones, opened behind supply (launch sequence, Stage 3).
3. Annual memberships, which churn far less than monthly ones (R60).
4. Member referral through the forwardable contact card; no reward at launch (R62).
5. Affiliates who reach a whole zone at once: utilities, cities, and associations (S93).
6. Property managers, as a separate future run (the demand side is homeowners, brief decision 1).

## Guarantee economics

What the 90-minute guarantee costs SOS SMS depends on Run 1's late-arrival rule. Under the decided fault-based rule (Run 1, option C; decision 3), a contractor who misses their own committed time funds the refund from their trip charge, and SOS SMS pays only for misses it causes: no acceptance in time, or dispatch failure.

Expected refund cost per request = (share of requests where SOS SMS causes a miss) × (refund amount). With the refund equal to the trip charge T, membership revenue must reserve at least that share of T for every request, before processing and operations.

<!-- sheet: Guarantee_Economics -->
| Share of requests with an SOS-caused miss | Refund cost per request, as a share of the trip charge | Reserve per request to cover refunds alone |
|---|---|---|
| 2 percent | 0.02 × T | 2 percent of T |
| 5 percent | 0.05 × T | 5 percent of T |
| 10 percent | 0.10 × T | 10 percent of T |
| 20 percent | 0.20 × T | 20 percent of T |

Under option B (SOS SMS absorbs every miss), replace "SOS-caused" with all misses, and the reserve must cover the full miss rate. The SOS-caused miss share is planned at 5 percent (R29) until the founding zone runs: $4.95 of reserve per request on the $99 trip charge, or about $0.10 a member a month at 0.25 requests a year (R58). The table is arithmetic, not a forecast.

## Acquisition economics per member

Revised 2026-10-11, the membership revision. The question this answers: what one new paid member costs to acquire, by channel, and what the membership pays back to cover it.

**Cost per new paid member = channel cost ÷ new paid members from it**, by channel and zone, with affiliate commissions counted in.

**Ceiling per new paid member = the first 6 months of contribution on the monthly plan: about $43 (R63)**, at $8.51 a month in the founding period and 6.5 percent monthly churn (R59).

Illustrative, using the planning values and market benchmarks, replaced by measured costs once the zone runs:

<!-- sheet: Acquisition -->
| Channel | Cost basis | Cost per new paid member | Against the ceiling of about $43 | Source and grade |
|---|---|---|---|---|
| Affiliates | $20 commission per new paid member, paid after the first paid month (planning value) | $20 | Under, by about $23 | R61; market $4 to $56 an enrollment, S85, C |
| Email, SOS SMS's own list | The sending tool and the scorecard; almost no cost per send | Counted from the first opening email (Stage 2) | Measured | S92, C (open and click benchmarks only) |
| Paid search, plumbing benchmark | $10.49 a click; 7.63 percent of clicks converting, assumed equal for sign-ups | about $137 | Over, about 3 times | S15, B |
| Paid search, Microsoft, 30 to 60 percent cheaper clicks | $4.20 to $7.34 a click, the same conversion | about $55 to $96 | Over | S74, C |

<!-- sheet: Acquisition -->
| Plan, at the planning price | Contribution a month | Churn or renewal | First 6 months of contribution | Lifetime contribution |
|---|---|---|---|---|
| Monthly at $10, founding period | $8.51 | 6.5 percent a month (R59) | about $43, the ceiling (R63) | about $131 |
| Monthly at $10, after the founding period | $9.03, with the $25 contractor fee | 6.5 percent a month | about $46 | about $139 |
| Annual at $100, founding period | about $7.16, paid as about $85.97 a year | 75 percent renewal (R60) | paid up front | about $85.97 a year while renewed |

**What it means.** Affiliates at the planning commission come in under the ceiling, and SOS SMS's own email list costs almost nothing per send. Paid search at plumbing benchmarks does not pay back inside 6 months on one new member, which is why it supports sign-ups in open zones and never leads: each zone fills first through affiliates and the launch list, and paid search keeps running only where its measured cost per new paid member sits under the ceiling. Annual members, referrals, more trades behind the same membership, and the contractor fee after the founding period all raise the contribution the ceiling is drawn from. The live calculator is the Calculators sheet in `pricing_dashboard.xlsx`.

## Step 9.3. ROI anchoring

### Anchor 1. Cost of the problem

Context the member already feels. SOS SMS does not claim to prevent damage, so no ROI multiple is computed against it.

<!-- sheet: ROI_Anchors -->
| Problem Scenario | Cost Without Solution | SOS SMS Cost | ROI Multiple |
|---|---|---|---|
| Water damage that becomes an insurance claim | Average water damage and freezing claim $13,954 (2018 to 2022) (S57, B) | `{{monthly price}}` a month (planning value $10), plus the $99 trip charge on use, credited to the repair | Not computed. SOS SMS gets a contractor there; it does not claim to prevent the damage |
| Waiting until morning | EPA: dry water-damaged areas within 24 to 48 hours to prevent mold (S58, A) | Same | Not computed, same reason |

### Anchor 2. Alternative comparison

What a household pays for the same readiness elsewhere, and what it pays with no plan when something breaks.

<!-- sheet: ROI_Anchors -->
| Alternative | Price in Advance | Cost When Something Breaks | What They Promise on Arrival | SOS SMS | Source and grade |
|---|---|---|---|---|---|
| D1 Search and call, no plan | Nothing | Service call fees commonly $150 to $250 after hours; labor 1.5 to 3 times standard rates | Nothing, unless the business offers it | `{{monthly price}}` a month; the $99 trip charge on use, credited to the repair | S50, C |
| D2 Plumber clubs | $8.25 to $19.99 a month (Benjamin Franklin: $10 a month or $120 a year) | Club trip charge $49 instead of $89; 10 percent off repairs; no after-hours fees (Benjamin Franklin) | Priority scheduling; $5 a minute late, up to $300, on scheduled appointments | Same; the $99 trip charge back if no one is there within 90 minutes of the text | S40, S75, S76, A; S77, C |
| D3 Home warranties | $47 to $82 a month | Service fee $75 to $125 a visit, for covered failures | Contractor contacted within 4 business hours, or 48 hours on weekends and holidays; no guarantee of timely emergency service | Same | S20, S79, B |
| D4 Utility-partner plans | $16.99 to $22.99 a month | Covered repairs up to $2,500 a call, after a 30-day waiting period | None found | Same | S78, A |
| D5 Frontdoor | $25 to $149 a year | Video help; a visit is arranged separately | Not applicable | Same | S81, A, B |
| D6 Marketplaces | Nothing | Free to request; booking prices vary | No arrival guarantee found; guarantees cover the work | Same | S44 to S46, A |

Against D1, a member pays `{{monthly price}}` a month (planning value $10) before anything breaks, and $99 when they use it, credited to the repair; a household with no plan pays nothing in advance and an after-hours call fee of $150 to $250 when it happens (S50, C, internal only). Against D2, the planning price matches the plumber club's $10 a month (S75): the club gives one company's priority, a lower trip charge, and repair discounts; SOS SMS gives many contractors at once and a money-backed window from the text. Against D3 and D4, a covered failure is usually cheaper through the warranty or the plan, and SOS SMS should say so: they pay for repairs, SOS SMS gets someone there.

### Anchor 3. Breakeven

**Member view.** The membership is worth keeping when being one text away from a vetted contractor, with a money-backed window, is worth more to the household than `{{monthly price}}` a month. That is a judgment, not a number: SOS SMS does not claim the membership pays for itself, and the membership page makes the judgment easy by stating the price, the trip charge on use, and what is not included.

**SOS SMS view.** The membership must at least cover card processing (2.9 percent plus $0.30 a charge, R31), messaging, support and platform, and its share of per-request costs on both sides, including the refund reserve: about $1.49 a member a month at the planning values. At a 65 percent target margin the floor is about $3.75 a month, and the $10 planning price clears it, leaving about $8.51 a month of contribution in the founding period (pricing model).

<!-- sheet: ROI_Anchors -->
| Plan | Price | Cost Components SOS SMS Must Cover | Breakeven | Payback Period |
|---|---|---|---|---|
| Monthly membership | `{{monthly price}}` a month (planning value $10) | Processing, messaging, support and platform, per-request costs including the refund reserve | M × (1 − 0.029) ≥ $0.30 + $0.05 + $0.50 + $0.35 a month: about $1.24 against $10 | An affiliate's $20 is paid back in the third month at $8.51 a month |
| Annual membership | `{{annual price}}` a year (planning value $100) | The same, for a year | A × (1 − 0.029) ≥ $0.30 + $0.60 + $6.00 + $4.23 a year: about $11.46 against $100 | Paid back at joining at the $20 commission |

### "One outcome" message, adapted

The skill's "one outcome pays for X years" is not claimed: SOS SMS does not say the membership pays for itself. The adapted message, for the membership and guarantee pages, written to decision 3:

<!-- sheet: ROI_Anchors -->
| Outcome | Message |
|---|---|
| The window is missed | "If your contractor isn't there within 90 minutes of your text, the $99 trip charge comes back to you, automatically." |
| The work goes ahead | "Your $99 trip charge counts toward the bill, so you don't pay twice." |
| Nothing breaks this month | "Most months nothing breaks. Your membership is there for the night something does, and you can cancel any time." |

## Pricing decisions, decided 2026-10-03, revised 2026-10-11

<!-- sheet: Decisions -->
| # | Decision | Decided | Where it shows |
|---|---|---|---|
| 1 | Where SOS SMS revenue comes from (shared with Run 1) | Members pay a monthly or annual membership, billed to the card on file: planning values $10 a month or $100 a year (R51, R52), no fee per request. Contractors pay $0 in the founding period, then $25 per completed paid job (decision 2, revised 2026-10-11) | Phases 6 and 8, both runs |
| 2 | The guarantee scope (decision 3) | 90 minutes from the member's request text; the refund is the $99 trip charge, automatic; covered areas and hours named on the membership page; when no one accepts, the member is told within 15 minutes and pays nothing | Phase 6 drill 3; the guarantee page |
| 3 | Who sets the trip charge | SOS SMS: one $99 trip charge per trade and zone, stated on the membership page before joining | Membership page; Run 1 terms |
| 4 | What the membership includes | One-text dispatch; an arrival time on acceptance; the 90-minute guarantee; a person by text; the readiness kit. Not included: the repair, parts, or a guarantee on the work (R53) | Membership page; Phase 6 drill 6 |
| 5 | Cancelling and renewal | Cancel any time, on the membership page or by texting HELP; a monthly membership ends at the end of the paid month; annual members get a reminder before `{{renewal date}}` (R56) | Member terms; member emails |
| 6 | The acquisition ceiling | About $43 per new paid member, by channel: the first 6 months of contribution on the monthly plan (R63), reviewed weekly. Replaces the per paid job ceiling | Phase 8 measurement; speed-to-scale plan, section 8 |
