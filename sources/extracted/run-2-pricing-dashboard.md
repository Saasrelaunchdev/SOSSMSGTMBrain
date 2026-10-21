# Source: run-2-pricing_dashboard.xlsx

Original path: `Fit137/SOSSMSGTMBuild`, `gtm/run-2-demand-customers/output/pricing_dashboard.xlsx`
Type: xlsx
Size: 26,488 bytes

## Sheet: README

| Phase 9. Pricing and Packaging Dashboard, member side |
| A member pays to be ready before anything breaks. Per ../SKILL-ADAPTATION.md, the skill's subscription logic fits: three plans, each billed monthly or annually. The prices here were decided by the membership revision on 2026-10-11 and the tiers revision on 2026-10-20 (decision 2, revised; ../../marketplace/resolution-register.md, R51 to R68) and are computed in the pricing model (../../pricing/pricing-model.md): Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350, with Plus on the annual plan shown first, plus the $99 trip charge on use (decision 5). Every plan covers plumbing, HVAC, and electrical. Contractors pay $25 per completed paid job from their first job, the same for every contractor (Run 1 Phase 9). |
| The live model is SOS_SMS_Pricing_Model.xlsx in the Google folder; the calculators in pricing_dashboard.xlsx follow this file. |
| Generated from gtm/run-2-demand-customers/output/phase-9-pricing.md by gtm/tools/render.py. The Markdown file is the source of truth; edit it, then re-render. |
| Source IDs (S01, S02, ...) refer to gtm/research/SOURCES.md, which gives each source's URL and evidence grade (A primary, B secondary, C vendor estimate). |
| SOS SMS values are decided, planning values with their basis, or counted at a named stage (gtm/marketplace/resolution-register.md). SOS SMS is pre-launch: no figure in this workbook is an SOS SMS result. |

## Sheet: Calculators

| Member-side calculators (live formulas) |
| Legend: yellow cells with blue text are inputs. The defaults are the decided plans of the pricing revision (2026-10-21): Basic $10 a month, Plus $15, Premier $35, with their entitlements (R51, R52, R65, R66, R69), the $99 trip charge on use (decision 5), the $25 contractor fee (decision 2), and the planning values R29, R31, R58 to R61, R70. The full model, with every input on its first sheet, is google-folder/SOS_SMS_Pricing_Model.xlsx. |
| 1. The plans (inputs) |
| Input | Basic | Plus | Premier | Basis |
| Price, a month | 10 | 15 | 35 | Decided (R51, R65, R66) |
| Late-arrival credit, months of membership | 0 | 6 | 12 | Decided (decision 3, R65, R66) |
| Phones that can text for the home | 1 | 5 | 10 | Decided (R69) |
| Homes covered | 1 | 1 | 2 | Decided (R66) |
| Trip charges paid by SOS SMS, a membership year (0 to 3) | 0 | 0 | 1 | Decided (R66) |
| Plan mix | 0.1 | 0.8 | 0.1 | Planning value (R70) |
| 2. Shared inputs |
| Months free on an annual plan | 2 | Decided (R52) |
| Requests from a second home, share of the first | 0.5 | Planning value (R58) |
| Requests per member a year, plumbing | 0.25 | Planning value (R58) |
| Requests per member a year, HVAC | 0.2 | Planning value (R58) |
| Requests per member a year, electrical | 0.05 | Planning value (R58) |
| Trip charge per request, every trade | 99 | Decided (decision 5) |
| Share of requests no contractor accepts | 0.1 | Planning value (the 90 percent acceptance threshold, R32) |
| Share of accepted requests late or not at all | 0.05 | Planning value (R29) |
| Card processing rate | 0.029 | Stripe's standard US card price (decision 6) |
| Card processing fixed fee per charge | 0.3 | Stripe's standard US card price |
| Request handling: support, platform, and texts | 5.3 | Planning value (R31): $3 + $2 + 30 texts at $0.01 |
| Contractor-side cost per completed job | 3.5 | Planning value (R31): payout $0.50, checks $1, support $2 |
| Messaging per phone on file, a month | 0.05 | Planning value (R31) |
| Support and platform per member, a month | 0.5 | Planning value (R31) |
| Monthly plan churn, a month | 0.065 | Planning value (R59); S89, grade C |
| Months before SOS SMS pays a trip charge, monthly plan | 6 | Decided (R66) |
| Contractor fee per completed paid job, from the first job | 25 | Decided (decision 2) |
| Months of contribution in the acquisition ceiling | 6 | Decided (decision 12) |
| Affiliate commission per new paid member | 20 | Decided (R61); market $4 to $56, S85, grade C |
| Cost per click, plumbing search | 10.49 | S15, grade B; no paid search at launch (decision 11) |
| Click to new paid member | 0.0763 | Assumed equal to the plumbing click-to-lead rate (S15, grade B) |
| 3. Member economics by plan, a month on the monthly plan (illustrative) |
| Basic | Plus | Premier |
| A year, annual plan | 100 | 150 | 350 |
| Requests a member a year | 0.5 | 0.5 | 0.75 |
| Accepted requests a year | 0.45 | 0.45 | 0.675 |
| Completed paid jobs a year | 0.4275 | 0.4275 | 0.64125 |
| Trips SOS SMS pays, expected a year | 0 | 0 | 0.47336627971139 |
| Card processing on the membership | 0.59 | 0.735 | 1.315 |
| Messaging for the phones on file | 0.05 | 0.25 | 0.5 |
| Support and platform | 0.5 | 0.5 | 0.5 |
| Request handling | 0.220833333333333 | 0.220833333333333 | 0.33125 |
| Card processing on trip charges | 0.1189125 | 0.1189125 | 0.17836875 |
| Contractor-side costs | 0.1246875 | 0.1246875 | 0.18703125 |
| Contractor fee earned | 0.890625 | 0.890625 | 1.3359375 |
| Late-arrival credit | 0 | 0.16875 | 1.18125 |
| Trip charges SOS SMS pays | 0 | 0 | 2.52570540178141 |
| Contribution a member a month | 9.28619166666667 | 13.7724416666667 | 29.6173320982186 |
| Margin | 0.928619166666667 | 0.918162777777778 | 0.846209488520532 |
| Months of contribution kept in the first 6 | 5.10548656845937 | 5.10548656845937 | 5.10548656845937 |
| Acquisition ceiling per new paid member (R63) | 47.410526826306 | 70.3150159440569 | 151.210891221056 |
| Affiliate: under the ceiling by | 27.410526826306 | 50.3150159440569 | 131.210891221056 |
| Paid search at the benchmark, cost per new paid member | 137.483617300131 | 137.483617300131 | 137.483617300131 |
| Paid search against the ceiling, times (not run at launch) | 2.89985424131266 | 1.95525259369228 | 0.909217690537537 |
| Contribution a member a month at the plan mix | 14.9083057098219 |
| 4. One request, by how it ends: SOS SMS net, monthly plan (decision 3) |
| Basic | Plus | Premier |
| Arrives inside the 90 minutes | 13.029 | 13.029 | 13.029 |
| Arrives late: the trip charge stands; Plus and Premier credit | 13.029 | -76.971 | -406.971 |
| Accepts and does not come, or NEXT: the $99 back, the contractor paid nothing | -8.471 | -98.471 | -428.471 |
| No contractor accepts: nobody pays, nobody is paid | -5.3 | -5.3 | -5.3 |
| 5. What a household pays for readiness elsewhere, a month (Phase 9, Anchor 2) |
| Option | Low | High | Source |
| Plumber club memberships | 8.25 | 19.99 | S75, S76, A; S77, C |
| Utility-partner plumbing plans | 16.99 | 22.99 | S78, A |
| HVAC club plans, the top plans | 30.3 | 36.95 | S100, C |
| Home warranties | 47 | 82 | S79, B |
| SOS SMS plans, a month: Basic, Plus, Premier | 10 | 15 | 35 |
| Plus the trip charge on use, credited to the repair | 99 |

## Sheet: Value_Metric

| Step 9.1. Value metric selection |
| Denominator | Correlation to Value | Scalability | Ease of Measurement | Score (1 to 10) | Verdict |
| Per household, monthly or annual, on three plans (membership) | High. The member pays to be ready before anything breaks, and every month they are | High | High | 8.2 | Primary |
| Per outcome: the guarantee credits the membership on a late arrival | High. The member pays for arrival inside the window | High | Medium. Needs arrival logging | 7.1 | Built into Plus and Premier: the guarantee is part of those plans |
| Per completed repair, as a percentage | Medium. SOS SMS does not control the repair or its price | Medium | Low unless payment for the work flows through SOS SMS | 4.6 | Reject |
| Per request, an SOS SMS fee at the moment of need | Medium. Charged at the worst moment, after a search a member would rather not make | High | High | 4.2 | Replaced by the membership (decision 2, revised 2026-10-11) |
| Per capability (priority, after-hours premium) | Medium | Medium | High | 3.2 | Reject. An after-hours premium is the surprise fee customers complain about (S50, S51), and priority would break dispatch to every matched contractor at once |
| Decided (decision 2), revised 2026-10-11 by the membership revision and 2026-10-20 by the tiers revision: |
| Primary value metric: per household, monthly or annual, on one of three plans. Basic $10 a month or $100 a year (R51, R52); Plus $15 or $150 (R65); Premier $35 or $350 (R66), billed to the card on file. No fee per request. Dispatch starts 30 days after joining on the monthly plan and at once on the annual plan, which is paid in advance (R54). |
| The use charge: the $99 trip charge, the same in all three trades, on the card on file when a contractor accepts, paid to the contractor and credited to the repair (decision 5). |
| Secondary usage metrics, for tracking: requests per member per year by trade (planning value 0.50 in all, R58), the plan mix, and members per zone against about 410 (R64). |
| Rationale: the member pays to be ready, so the emergency is one text with nothing to agree to at the worst moment. A flat monthly or annual price, stated before joining, avoids the after-hours surprise the research found customers resent. The plans differ by what stands behind the arrival time, never by how fast a request goes out. |

## Sheet: Packaging

| Step 9.2. Packaging: the member price structure |
| Plan | Price | What it covers | Guarantee | Position | Target share |
| Plus | $150 a year or $15 a month (R65) | Everything in Basic, plus the 90-minute guarantee and up to 5 phones that can text for the home (R69) | On a late arrival or a no-show, the membership paid in the 6 months before the request is credited to the next bills: up to $90 monthly, $75 annual | Shown first, on the annual plan, selected by default, and flagged most popular; the Hero | 80 percent (R70), measured from the first members |
| Basic | $100 a year or $10 a month (R51, R52) | One-text dispatch to the matched contractors in plumbing, HVAC, and electrical, at any hour; an arrival time on acceptance, inside 90 minutes; never charged if no one accepts; NEXT after a miss; a person by text; the readiness kit and a yearly readiness check; the member's phone (R53, R69) | None: a late arrival keeps its trip charge; a no-show returns it in full | The entry plan | 10 percent (R70), measured from the first members |
| Premier | $350 a year or $35 a month (R66) | Everything in Plus, plus one trip charge a membership year paid by SOS SMS (annual: from joining; monthly: after 6 paid months), a second home in an open zone, and up to 10 phones across both homes | The membership paid in the 12 months before the request: up to $420 monthly, $350 annual | Shown third; the Anchor, 2.33 times Plus | 10 percent (R70), measured from the first members |
| The trip charge, on use | $99 per request, every trade, on the card on file when a contractor accepts | The contractor's trip, credited to the repair if the member goes ahead | Stands on a late arrival; back in full on a no-show | Every request | n/a |
| A declined card at a request | Not dispatched until a card authorizes | The backup card is tried at once; the member is told at once and can update the card on the membership page or by texting HELP | The 90 minutes run from the moment a card authorizes | No dispatch without an authorized trip charge (R16) | 0 |
| A text from a non-member | Not dispatched | The safety line, the first steps for the problem, and how to join, free (R57) | None | Dispatch is for members | 0 |
| Not offered: memberships outside open zones, and faster dispatch on any plan. Homeowners outside an open zone are told plainly that SOS SMS does not cover their area yet, and may join the launch list (R55). No plan pays for the repair or parts or carries a guarantee on the work (R21, R53). |

## Sheet: Guarantee_Economics

| Guarantee economics |
| Share of accepted requests late or not at all | Plus, credit cost a member a month | Premier, credit cost a member a month | Basic |
| 2 percent | about $0.07 | about $0.47 | No credit |
| 5 percent | about $0.17 | about $1.18 | No credit |
| 10 percent | about $0.34 | about $2.36 | No credit |
| 20 percent | about $0.68 | about $4.73 | No credit |
| Computed at 0.50 requests a member a year (0.75 on Premier, with a second home; R58), 90 percent accepted (R32), against $15 and $35 a month. The late share is planned at 5 percent (R29), the arrival threshold (R32), until the launch zone runs: about $0.17 a Plus member a month for a plan that keeps about $4.49 more than Basic. The credit never returns more than the membership already paid. The table is arithmetic, not a forecast. |

## Sheet: Acquisition

| Acquisition economics per member |
| Channel | Cost basis | Cost per new paid member | Against the ceilings (about $47, $70, $151) | Source and grade |
| Affiliates | $20 commission per new paid member on any plan, paid once the second monthly payment or the first annual payment clears (R61) | $20 | Under every plan's ceiling; by about $27 on Basic and $50 on Plus | R61; market $4 to $56 an enrollment, S85, C |
| Email, SOS SMS's own list | The sending tool and the scorecard; almost no cost per send | Counted from the first opening email (Stage 2) | Measured | S92, C (open and click benchmarks only) |
| Paid social, sign-ups before the need | Audiences limited to the open zone's map | Counted in each open zone | Scales only at or under the plan's ceiling; pauses with sign-ups (R34) | Measured |
| Paid search, plumbing benchmark | $10.49 a click; 7.63 percent of clicks converting, assumed equal for sign-ups | about $137 | Over, about 3 times Basic's; not run at launch (decision 11) | S15, B |
| Acquisition economics per member |
| Plan, at the decided price | Contribution | Churn or renewal | First 6 months of contribution | Lifetime contribution |
| Plus, annual at $150 | about $139.78 a year | 75 percent renewal (R60) | about $70, paid up front | about $559 |
| Plus, monthly at $15 | about $13.77 a month | 6.5 percent a month (R59) | about $70 | about $212 |
| Basic, annual at $100 | about $95.31 a year | 75 percent renewal (R60) | about $48, paid up front | about $381 |
| Basic, monthly at $10 | about $9.29 a month | 6.5 percent a month (R59) | about $47 | about $143 |
| Premier, annual at $350 | about $278.05 a year | 75 percent renewal (R60) | about $139, paid up front | about $1,112 |
| Premier, monthly at $35 | about $29.62 a month | 6.5 percent a month (R59) | about $151 | about $456 |
| What it means. Affiliates at the planning commission come in under every plan's ceiling, and SOS SMS's own email list costs almost nothing per send. Paid search at plumbing benchmarks does not pay back inside 6 months on one new member, so SOS SMS runs none at launch (decision 11): each zone fills through affiliates, the launch list, and paid social, and search volume for SOS SMS by name is counted once the zone has been open 6 months (R68). Plus on the annual plan, shown first, upgrades, referrals, three trades behind one membership, and the contractor fee from the first job all raise the contribution the ceilings are drawn from. Every request also pays for itself: the $25 contractor fee against about $11.97 of costs on both sides, about $13.03 net. The live model is the Pricing Model tab in SOS_SMS_Pricing_Model.xlsx. |

## Sheet: ROI_Anchors

| Anchor 1. Cost of the problem |
| Problem Scenario | Cost Without Solution | SOS SMS Cost | ROI Multiple |
| Water damage that becomes an insurance claim | Average water damage and freezing claim $13,954 (2018 to 2022) (S57, B) | From $10 a month on Basic, plus the $99 trip charge on use, credited to the repair | Not computed. SOS SMS gets a contractor there; it does not claim to prevent the damage |
| Waiting until morning | EPA: dry water-damaged areas within 24 to 48 hours to prevent mold (S58, A) | Same | Not computed, same reason |
| Anchor 2. Alternative comparison |
| Alternative | Price in Advance | Cost When Something Breaks | What They Promise on Arrival | SOS SMS | Source and grade |
| D1 Search and call, no plan | Nothing | Service call fees commonly $150 to $250 after hours; labor 1.5 to 3 times standard rates | Nothing, unless the business offers it | From $10 a month for plumbing, HVAC, and electrical; the $99 trip charge on use, credited to the repair | S50, C |
| D2 Plumber and HVAC clubs | $8.25 to $19.99 a month for plumbing (Benjamin Franklin: $10 a month or $120 a year); HVAC clubs $15.95 to $36.95 | Club trip charge $49 instead of $89; 10 percent off repairs; no after-hours fees (Benjamin Franklin) | Priority scheduling with one company; $5 a minute late, up to $300, on scheduled appointments | Same; 6 months of membership credited on Plus, 12 on Premier, if the contractor is late | S40, S75, S76, A; S77, S100, C |
| D3 Home warranties | $47 to $82 a month | Service fee $75 to $125 a visit, for covered failures | Contractor contacted within 4 business hours, or 48 hours on weekends and holidays; no guarantee of timely emergency service | Same | S20, S79, B |
| D4 Utility-partner plans | $16.99 to $22.99 a month | Covered repairs up to $2,500 a call, after a 30-day waiting period | None found | Same | S78, A |
| D5 Frontdoor | $25 to $149 a year | Video help; a visit is arranged separately | Not applicable | Same | S81, A, B |
| D6 Marketplaces | Nothing | Free to request; booking prices vary | No arrival guarantee found; guarantees cover the work | Same | S44 to S46, A |
| Against D1, a Basic member pays $10 a month before anything breaks, and $99 when they use it, credited to the repair; a household with no plan pays nothing in advance and an after-hours call fee of $150 to $250 when it happens (S50, C, internal only). Against D2, Basic matches the plumber club's $10 a month (S75) and covers HVAC and electrical too: the club gives one company's priority, a lower trip charge, and repair discounts; SOS SMS gives many contractors at once, an arrival time from the text, and on Plus and Premier a credit when the contractor is late. Against D3 and D4, a covered failure is usually cheaper through the warranty or the plan, and SOS SMS should say so: they pay for repairs, SOS SMS gets someone there. |
| Anchor 3. Breakeven |
| Plan | Price | Cost Components SOS SMS Must Cover | Breakeven | Payback Period |
| Basic, monthly | $10 a month | Processing, messaging, support and platform, per-request costs | M × (1 − 0.029) ≥ $1.31 a month: about $1.35 against $10 | An affiliate's $20 is paid back in the third month at $9.29 a month; dispatch starts after two payments, so a member who joins, uses it once, and cancels still leaves about $30.75 |
| Plus, monthly | $15 a month | The same, plus 5 phones and the late-arrival credit, about $0.17 a month | M × (1 − 0.029) ≥ $1.51 + $0.17 a month: about $1.73 against $15 | Six payments in, one late arrival with the credit used in full still leaves about $4.12 |
| Premier, monthly | $35 a month | The same, plus 10 phones, the 12-month credit, and the covered trip charge after 6 paid months, about $3.71 a month | M × (1 − 0.029) ≥ $2.00 + $3.71 a month: about $5.87 against $35 | Six payments, the covered trip charge, then cancel still leaves about $113.31. Twelve payments, then a late arrival with the 12-month credit used in full, costs about -$14.75: rare, and inside the plan's contribution |
| Annual plans | $100, $150, $350 a year | The same, for a year; Premier's covered trip charge from joining | About $5, $10, and $72 a year against the price | Paid back at joining at the $20 commission |
| "One outcome" message, adapted |
| Outcome | Message |
| The contractor is late, on Plus or Premier | "If your contractor gets there after 90 minutes from your text, we credit the membership you paid for the 6 months before (12 on Premier), on your next bills. The trip charge still pays for the work." |
| The work goes ahead | "Your $99 trip charge counts toward the bill, so you don't pay twice." |
| Nothing breaks this month | "Most months nothing breaks. Your membership is there for the night something does, and you can cancel any time." |

## Sheet: Decisions

| Pricing decisions, decided 2026-10-03, revised 2026-10-11 and 2026-10-20 |
| # | Decision | Decided | Where it shows |
| 1 | Where SOS SMS revenue comes from (shared with Run 1) | Members pay a plan, billed to the card on file: Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350 (R51, R52, R65, R66), no fee per request. Contractors pay $25 per completed paid job from the first job (decision 2, revised 2026-10-20) | Phases 6 and 8, both runs |
| 2 | The guarantee scope (decision 3) | 90 minutes from the member's request text, anywhere in the zone's neighborhoods, at any hour (R15). No acceptance: told within 15 minutes, never charged. A late arrival keeps its trip charge; on Plus and Premier, the membership paid in the 6 months (Plus) or 12 months (Premier) before the request is credited (R65, R66). A no-show returns the trip charge in full; NEXT after the 90 minutes (R17) | Phase 6 drill 3; the guarantee page |
| 3 | Who sets the trip charge | SOS SMS: one $99 trip charge per trade and zone, the same for plumbing, HVAC, and electrical, stated on the membership page before joining | Membership page; Run 1 terms |
| 4 | What every plan includes | One-text dispatch in plumbing, HVAC, and electrical, at any hour; an arrival time on acceptance; never charged if no one accepts; NEXT after a miss; a person by text; the readiness kit and a yearly readiness check. Plus adds the guarantee and up to 5 phones; Premier a 12-month credit, a trip charge a year on SOS SMS, a second home, and up to 10 phones (R69). Not included: the repair, parts, a guarantee on the work, or faster dispatch (R53) | Membership page; Phase 6 drill 6 |
| 5 | Cancelling, renewal, and changing plans | Cancel any time, on the membership page or by texting HELP; a monthly membership ends at the end of the paid month and an annual one at the end of the paid year, with no partial refunds; annual members get a reminder before {{renewal date}}; a failed payment is retried for 7 days, then the membership pauses (R56). Upgrades at once on annual, 30 days after on monthly; downgrades at the end of the paid period (R54) | Member terms; member emails |
| 6 | The acquisition ceiling | One per plan, the first 6 months of contribution: about $47 Basic, $70 Plus, $151 Premier (R63), reviewed weekly by channel, plan, and zone; every channel scales while at or under it. No paid search at launch (decision 11) | Phase 8 measurement; speed-to-scale plan, section 8 |
