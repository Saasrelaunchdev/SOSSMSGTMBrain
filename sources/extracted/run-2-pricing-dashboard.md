# Source: run-2-pricing_dashboard.xlsx

Original path: `Fit137/SOSSMSGTMBuild`, `gtm/run-2-demand-customers/output/pricing_dashboard.xlsx`
Type: xlsx
Size: 23,320 bytes

## Sheet: README

| Phase 9. Pricing and Packaging Dashboard, member side |
| A member pays to be ready before anything breaks. Per ../SKILL-ADAPTATION.md, the skill's subscription logic fits, narrowed to one membership billed monthly or annually. The prices here are planning values set by the membership revision on 2026-10-11 (decision 2, revised; ../../marketplace/resolu... |
| The live model is SOS_SMS_Pricing_Model.xlsx in the Google folder; the calculators in pricing_dashboard.xlsx follow this file. |
| Generated from gtm/run-2-demand-customers/output/phase-9-pricing.md by gtm/tools/render.py. The Markdown file is the source of truth; edit it, then re-render. |
| Source IDs (S01, S02, ...) refer to gtm/research/SOURCES.md, which gives each source's URL and evidence grade (A primary, B secondary, C vendor estimate). |
| SOS SMS values are decided, planning values with their basis, or counted at a named stage (gtm/marketplace/resolution-register.md). SOS SMS is pre-launch: no figure in this workbook is an SOS SMS result. |

## Sheet: Calculators

| Member-side calculators (live formulas) |
| Legend: yellow cells with blue text are inputs. The defaults are the planning values of the membership revision (2026-10-11): $10 a month or $100 a year (R51, R52), the $99 trip charge on use (decision 5), and R29, R31, R58 to R61. Copy uses {{monthly price}} and {{annual price}} until the launch... |
| 1. Member economics: contribution a member, and the acquisition ceiling |
| Membership, a month (M) | 10 | Planning value (R51) |
| Membership, a year (A) | 100 | Planning value (R52): two months free (S90) |
| Card processing rate | 0.029 | Stripe's standard US card price (decision 6) |
| Card processing fixed fee per charge | 0.3 | Stripe's standard US card price |
| Messaging, support, and platform per member a month | 0.55 | Planning value: $0.05 messages and $0.50 support and platform (R31) |
| Trip charge per request (T) | 99 | Decided (decision 5) |
| Share of requests with an SOS-caused miss | 0.05 | Planning value (R29) |
| Support, platform, and texts per request | 5.3 | Planning value (R31): $3 + $2 + 30 texts at $0.01 |
| Contractor-side cost per completed job | 3.5 | Planning value (R31): payout $0.50, checks $1, support $2 |
| Requests per member a year | 0.25 | Planning value (R58); S82, S83 |
| Monthly plan churn, a month | 0.065 | Planning value (R59); S89, grade C |
| Contractor fee per completed paid job, after the founding period | 25 | Decided (decision 2) |
| Refund reserve per request | 4.95 |
| Card processing on the trip charge | 3.171 |
| Cost per request, both sides | 16.921 |
| Requests, a member a month | 0.352520833333333 |
| Contribution a member a month, founding period | 8.50747916666667 |
| Contribution a member a month, after the founding period | 9.0283125 |
| Months of contribution kept in the first 6 months | 5.10548656845937 |
| Acquisition ceiling per new paid member (R63) | 43.4348206168646 |
| Lifetime contribution, monthly plan | 130.884294871795 |
| Contribution a member a year, annual plan, founding period | 85.96975 |
| 2. Guarantee economics: refund reserve by SOS-caused miss share |
| SOS-caused miss share | Reserve per request | Reserve a member a month |
| 0.02 | 1.98 | 0.04125 |
| 0.05 | 4.95 | 0.103125 |
| 0.1 | 9.9 | 0.20625 |
| 0.2 | 19.8 | 0.4125 |
| 3. Acquisition per new paid member, by channel (illustrative) |
| Affiliate commission per new paid member | 20 | Planning value (R61); market $4 to $56, S85, grade C |
| Cost per click, plumbing search | 10.49 | S15, grade B |
| Click to new paid member | 0.0763 | Assumed equal to the plumbing click-to-lead rate (S15, grade B) |
| Affiliate: under the ceiling by | 23.4348206168646 |
| Affiliate: months of contribution to pay back, before churn | 2.35087263902596 |
| Paid search cost per new paid member | 137.483617300131 |
| Paid search against the ceiling, times | 3.16528571656515 |
| 4. What a household pays for readiness elsewhere, a month (Phase 9, Anchor 2) |
| Option | Low | High | Source |
| Plumber club memberships | 8.25 | 19.99 | S75, S76, A; S77, C |
| Utility-partner plumbing plans | 16.99 | 22.99 | S78, A |
| Home warranties | 47 | 82 | S79, B |
| SOS SMS membership, a month (planning value) | 10 |
| Plus the trip charge on use, credited to the repair | 99 |

## Sheet: Value_Metric

| Step 9.1. Value metric selection |
| Denominator | Correlation to Value | Scalability | Ease of Measurement | Score (1 to 10) | Verdict |
| Per household, monthly or annual (membership) | High. The member pays to be ready before anything breaks, and every month they are | High | High | 8.2 | Primary |
| Per outcome: the guarantee refunds the trip charge on a miss | High. The member pays for arrival inside the window | High | Medium. Needs arrival logging | 7.1 | Built into the primary: the guarantee is part of the membership |
| Per completed repair, as a percentage | Medium. SOS SMS does not control the repair or its price | Medium | Low unless payment for the work flows through SOS SMS | 4.6 | Reject |
| Per request, an SOS SMS fee at the moment of need | Medium. Charged at the worst moment, after a search a member would rather not make | High | High | 4.2 | Replaced by the membership (decision 2, revised 2026-10-11) |
| Per capability (priority, after-hours premium) | Medium | Medium | High | 3.2 | Reject. An after-hours premium is the surprise fee customers complain about (S50, S51) |
| Decided (decision 2), revised 2026-10-11 by the membership revision: |
| Primary value metric: per household, monthly or annual. The member pays {{monthly price}} a month or {{annual price}} a year (planning values $10 and $100, R51, R52), billed to the card on file. No fee per request. |
| The use charge: the $99 trip charge, on the card on file when a contractor accepts, paid to the contractor and credited to the repair (decision 5). |
| Secondary usage metrics, for tracking: requests per member per year (planning value 0.25, R58), and members per zone against about 430 (R64). |
| Rationale: the member pays to be ready, so the emergency is one text with nothing to agree to at the worst moment. A flat monthly or annual price, stated before joining, avoids the after-hours surprise the research found customers resent, and the guarantee's cost sits inside the membership. |

## Sheet: Packaging

| Step 9.2. Packaging: the member price structure |
| Plan | Price | What it covers | Guarantee | Position | Target share |
| Monthly membership | {{monthly price}} a month (planning value $10, R51) | One-text dispatch to the matched contractors; an arrival time on acceptance; a person by text; the readiness kit (R53) | 90 minutes from the member's request text; the $99 trip charge back on a miss | Default | Measured from the first members |
| Annual membership | {{annual price}} a year (planning value $100: two months free, R52) | The same | The same | The second shape; renews each year with a reminder before {{renewal date}} (R56) | Measured from the first members |
| The trip charge, on use | $99 per request, on the card on file when a contractor accepts | The contractor's trip, credited to the repair if the member goes ahead | Refunded on a miss | Every request | n/a |
| Request outside covered hours | Not dispatched | Stop-the-water steps and the safety line by text, free | None | The membership page names covered hours (R15) | 0 |
| A text from a non-member | Not dispatched | The safety line, the stop-the-water steps, and how to join, free (R57) | None | Dispatch is for members | 0 |
| Not offered: memberships outside open zones. Homeowners there are told plainly that SOS SMS does not cover their area yet, and may join the launch list (R55). The membership does not pay for the repair or parts and carries no guarantee on the work (R21, R53). |

## Sheet: Guarantee_Economics

| Guarantee economics |
| Share of requests with an SOS-caused miss | Refund cost per request, as a share of the trip charge | Reserve per request to cover refunds alone |
| 2 percent | 0.02 × T | 2 percent of T |
| 5 percent | 0.05 × T | 5 percent of T |
| 10 percent | 0.10 × T | 10 percent of T |
| 20 percent | 0.20 × T | 20 percent of T |
| Under option B (SOS SMS absorbs every miss), replace "SOS-caused" with all misses, and the reserve must cover the full miss rate. The SOS-caused miss share is planned at 5 percent (R29) until the founding zone runs: $4.95 of reserve per request on the $99 trip charge, or about $0.10 a member a mo... |

## Sheet: Acquisition

| Acquisition economics per member |
| Channel | Cost basis | Cost per new paid member | Against the ceiling of about $43 | Source and grade |
| Affiliates | $20 commission per new paid member, paid after the first paid month (planning value) | $20 | Under, by about $23 | R61; market $4 to $56 an enrollment, S85, C |
| Email, SOS SMS's own list | The sending tool and the scorecard; almost no cost per send | Counted from the first opening email (Stage 2) | Measured | S92, C (open and click benchmarks only) |
| Paid search, plumbing benchmark | $10.49 a click; 7.63 percent of clicks converting, assumed equal for sign-ups | about $137 | Over, about 3 times | S15, B |
| Paid search, Microsoft, 30 to 60 percent cheaper clicks | $4.20 to $7.34 a click, the same conversion | about $55 to $96 | Over | S74, C |
| Acquisition economics per member |
| Plan, at the planning price | Contribution a month | Churn or renewal | First 6 months of contribution | Lifetime contribution |
| Monthly at $10, founding period | $8.51 | 6.5 percent a month (R59) | about $43, the ceiling (R63) | about $131 |
| Monthly at $10, after the founding period | $9.03, with the $25 contractor fee | 6.5 percent a month | about $46 | about $139 |
| Annual at $100, founding period | about $7.16, paid as about $85.97 a year | 75 percent renewal (R60) | paid up front | about $85.97 a year while renewed |
| What it means. Affiliates at the planning commission come in under the ceiling, and SOS SMS's own email list costs almost nothing per send. Paid search at plumbing benchmarks does not pay back inside 6 months on one new member, which is why it supports sign-ups in open zones and never leads: each... |

## Sheet: ROI_Anchors

| Anchor 1. Cost of the problem |
| Problem Scenario | Cost Without Solution | SOS SMS Cost | ROI Multiple |
| Water damage that becomes an insurance claim | Average water damage and freezing claim $13,954 (2018 to 2022) (S57, B) | {{monthly price}} a month (planning value $10), plus the $99 trip charge on use, credited to the repair | Not computed. SOS SMS gets a contractor there; it does not claim to prevent the damage |
| Waiting until morning | EPA: dry water-damaged areas within 24 to 48 hours to prevent mold (S58, A) | Same | Not computed, same reason |
| Anchor 2. Alternative comparison |
| Alternative | Price in Advance | Cost When Something Breaks | What They Promise on Arrival | SOS SMS | Source and grade |
| D1 Search and call, no plan | Nothing | Service call fees commonly $150 to $250 after hours; labor 1.5 to 3 times standard rates | Nothing, unless the business offers it | {{monthly price}} a month; the $99 trip charge on use, credited to the repair | S50, C |
| D2 Plumber clubs | $8.25 to $19.99 a month (Benjamin Franklin: $10 a month or $120 a year) | Club trip charge $49 instead of $89; 10 percent off repairs; no after-hours fees (Benjamin Franklin) | Priority scheduling; $5 a minute late, up to $300, on scheduled appointments | Same; the $99 trip charge back if no one is there within 90 minutes of the text | S40, S75, S76, A; S77, C |
| D3 Home warranties | $47 to $82 a month | Service fee $75 to $125 a visit, for covered failures | Contractor contacted within 4 business hours, or 48 hours on weekends and holidays; no guarantee of timely emergency service | Same | S20, S79, B |
| D4 Utility-partner plans | $16.99 to $22.99 a month | Covered repairs up to $2,500 a call, after a 30-day waiting period | None found | Same | S78, A |
| D5 Frontdoor | $25 to $149 a year | Video help; a visit is arranged separately | Not applicable | Same | S81, A, B |
| D6 Marketplaces | Nothing | Free to request; booking prices vary | No arrival guarantee found; guarantees cover the work | Same | S44 to S46, A |
| Against D1, a member pays {{monthly price}} a month (planning value $10) before anything breaks, and $99 when they use it, credited to the repair; a household with no plan pays nothing in advance and an after-hours call fee of $150 to $250 when it happens (S50, C, internal only). Against D2, the ... |
| Anchor 3. Breakeven |
| Plan | Price | Cost Components SOS SMS Must Cover | Breakeven | Payback Period |
| Monthly membership | {{monthly price}} a month (planning value $10) | Processing, messaging, support and platform, per-request costs including the refund reserve | M × (1 − 0.029) ≥ $0.30 + $0.05 + $0.50 + $0.35 a month: about $1.24 against $10 | An affiliate's $20 is paid back in the third month at $8.51 a month |
| Annual membership | {{annual price}} a year (planning value $100) | The same, for a year | A × (1 − 0.029) ≥ $0.30 + $0.60 + $6.00 + $4.23 a year: about $11.46 against $100 | Paid back at joining at the $20 commission |
| "One outcome" message, adapted |
| Outcome | Message |
| The window is missed | "If your contractor isn't there within 90 minutes of your text, the $99 trip charge comes back to you, automatically." |
| The work goes ahead | "Your $99 trip charge counts toward the bill, so you don't pay twice." |
| Nothing breaks this month | "Most months nothing breaks. Your membership is there for the night something does, and you can cancel any time." |

## Sheet: Decisions

| Pricing decisions, decided 2026-10-03, revised 2026-10-11 |
| # | Decision | Decided | Where it shows |
| 1 | Where SOS SMS revenue comes from (shared with Run 1) | Members pay a monthly or annual membership, billed to the card on file: planning values $10 a month or $100 a year (R51, R52), no fee per request. Contractors pay $0 in the founding period, then $25 per completed paid job (decision 2, revised 2026-10-11) | Phases 6 and 8, both runs |
| 2 | The guarantee scope (decision 3) | 90 minutes from the member's request text; the refund is the $99 trip charge, automatic; covered areas and hours named on the membership page; when no one accepts, the member is told within 15 minutes and pays nothing | Phase 6 drill 3; the guarantee page |
| 3 | Who sets the trip charge | SOS SMS: one $99 trip charge per trade and zone, stated on the membership page before joining | Membership page; Run 1 terms |
| 4 | What the membership includes | One-text dispatch; an arrival time on acceptance; the 90-minute guarantee; a person by text; the readiness kit. Not included: the repair, parts, or a guarantee on the work (R53) | Membership page; Phase 6 drill 6 |
| 5 | Cancelling and renewal | Cancel any time, on the membership page or by texting HELP; a monthly membership ends at the end of the paid month; annual members get a reminder before {{renewal date}} (R56) | Member terms; member emails |
| 6 | The acquisition ceiling | About $43 per new paid member, by channel: the first 6 months of contribution on the monthly plan (R63), reviewed weekly. Replaces the per paid job ceiling | Phase 8 measurement; speed-to-scale plan, section 8 |
