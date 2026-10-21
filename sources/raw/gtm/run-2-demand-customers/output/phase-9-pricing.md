# Phase 9. Pricing and Packaging Dashboard, member side

A member pays to be ready before anything breaks. Per `../SKILL-ADAPTATION.md`, the skill's subscription logic fits: three plans, each billed monthly or annually. The prices here were decided by the membership revision on 2026-10-11 and the tiers revision on 2026-10-20 (decision 2, revised; `../../marketplace/resolution-register.md`, R51 to R68) and are computed in the pricing model (`../../pricing/pricing-model.md`): Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350, with Plus on the annual plan shown first, plus the $99 trip charge on use (decision 5). Every plan covers plumbing, HVAC, and electrical. Contractors pay $25 per completed paid job from their first job, the same for every contractor (Run 1 Phase 9).

The live model is `SOS_SMS_Pricing_Model.xlsx` in the Google folder; the calculators in `pricing_dashboard.xlsx` follow this file.

## Step 9.1. Value metric selection

<!-- sheet: Value_Metric -->
| Denominator | Correlation to Value | Scalability | Ease of Measurement | Score (1 to 10) | Verdict |
|---|---|---|---|---|---|
| Per household, monthly or annual, on three plans (membership) | High. The member pays to be ready before anything breaks, and every month they are | High | High | 8.2 | Primary |
| Per outcome: the guarantee credits the membership on a late arrival | High. The member pays for arrival inside the window | High | Medium. Needs arrival logging | 7.1 | Built into Plus and Premier: the guarantee is part of those plans |
| Per completed repair, as a percentage | Medium. SOS SMS does not control the repair or its price | Medium | Low unless payment for the work flows through SOS SMS | 4.6 | Reject |
| Per request, an SOS SMS fee at the moment of need | Medium. Charged at the worst moment, after a search a member would rather not make | High | High | 4.2 | Replaced by the membership (decision 2, revised 2026-10-11) |
| Per capability (priority, after-hours premium) | Medium | Medium | High | 3.2 | Reject. An after-hours premium is the surprise fee customers complain about (S50, S51), and priority would break dispatch to every matched contractor at once |

**Decided (decision 2), revised 2026-10-11 by the membership revision and 2026-10-20 by the tiers revision:**

- **Primary value metric: per household, monthly or annual, on one of three plans.** Basic $10 a month or $100 a year (R51, R52); Plus $15 or $150 (R65); Premier $35 or $350 (R66), billed to the card on file. No fee per request. Dispatch starts 30 days after joining on the monthly plan and at once on the annual plan, which is paid in advance (R54).
- **The use charge:** the $99 trip charge, the same in all three trades, on the card on file when a contractor accepts, paid to the contractor and credited to the repair (decision 5).
- **Secondary usage metrics, for tracking:** requests per member per year by trade (planning value 0.50 in all, R58), the plan mix, and members per zone against about 410 (R64).
- **Rationale:** the member pays to be ready, so the emergency is one text with nothing to agree to at the worst moment. A flat monthly or annual price, stated before joining, avoids the after-hours surprise the research found customers resent. The plans differ by what stands behind the arrival time, never by how fast a request goes out.

## Step 9.2. Packaging: the member price structure

<!-- sheet: Packaging -->
| Plan | Price | What it covers | Guarantee | Position | Target share |
|---|---|---|---|---|---|
| Plus | $150 a year or $15 a month (R65) | Everything in Basic, plus the 90-minute guarantee and up to 5 phones that can text for the home (R69) | On a late arrival or a no-show, the membership paid in the 6 months before the request is credited to the next bills: up to $90 monthly, $75 annual | Shown first, on the annual plan, selected by default, and flagged most popular; the Hero | 80 percent (R70), measured from the first members |
| Basic | $100 a year or $10 a month (R51, R52) | One-text dispatch to the matched contractors in plumbing, HVAC, and electrical, at any hour; an arrival time on acceptance, inside 90 minutes; never charged if no one accepts; NEXT after a miss; a person by text; the readiness kit and a yearly readiness check; the member's phone (R53, R69) | None: a late arrival keeps its trip charge; a no-show returns it in full | The entry plan | 10 percent (R70), measured from the first members |
| Premier | $350 a year or $35 a month (R66) | Everything in Plus, plus one trip charge a membership year paid by SOS SMS (annual: from joining; monthly: after 6 paid months), a second home in an open zone, and up to 10 phones across both homes | The membership paid in the 12 months before the request: up to $420 monthly, $350 annual | Shown third; the Anchor, 2.33 times Plus | 10 percent (R70), measured from the first members |
| The trip charge, on use | $99 per request, every trade, on the card on file when a contractor accepts | The contractor's trip, credited to the repair if the member goes ahead | Stands on a late arrival; back in full on a no-show | Every request | n/a |
| A declined card at a request | Not dispatched until a card authorizes | The backup card is tried at once; the member is told at once and can update the card on the membership page or by texting HELP | The 90 minutes run from the moment a card authorizes | No dispatch without an authorized trip charge (R16) | 0 |
| A text from a non-member | Not dispatched | The safety line, the first steps for the problem, and how to join, free (R57) | None | Dispatch is for members | 0 |

Not offered: memberships outside open zones, and faster dispatch on any plan. Homeowners outside an open zone are told plainly that SOS SMS does not cover their area yet, and may join the launch list (R55). No plan pays for the repair or parts or carries a guarantee on the work (R21, R53).

### Expansion levers

1. Upgrades from Basic to Plus and Premier, at once on the annual plan and 30 days after the upgrade on the monthly plan (R54).
2. More trades behind the same membership: water damage first, then locksmith, each opened only when Run 1 reaches density for that trade.
3. More zones, opened behind supply (launch sequence, Stage 3).
4. Annual memberships, which churn far less than monthly ones (R60).
5. Member referral through the forwardable contact card; no reward at launch (R62).
6. Affiliates who reach a whole zone at once: utilities, cities, and associations (S93).
7. Property managers, as a separate future run (the demand side is homeowners, brief decision 1).

## Guarantee economics

What the 90-minute guarantee costs SOS SMS, under decision 3 as revised on 2026-10-20 and 2026-10-21. A late arrival keeps its trip charge, because it pays for the work, so no trip charge is refunded for lateness. A no-show returns the trip charge in full, but the contractor is paid nothing, so SOS SMS loses nothing on the trip. What the guarantee costs is the credit, on a sliding scale: none on Basic, the membership paid in the 6 months before the request on Plus, and in the 12 months before it on Premier.

Expected credit cost a member a month = (share of accepted requests late or not at all) × (accepted requests a member a month) × (the plan's credit months × its price).

<!-- sheet: Guarantee_Economics -->
| Share of accepted requests late or not at all | Plus, credit cost a member a month | Premier, credit cost a member a month | Basic |
|---|---|---|---|
| 2 percent | about $0.07 | about $0.47 | No credit |
| 5 percent | about $0.17 | about $1.18 | No credit |
| 10 percent | about $0.34 | about $2.36 | No credit |
| 20 percent | about $0.68 | about $4.73 | No credit |

Computed at 0.50 requests a member a year (0.75 on Premier, with a second home; R58), 90 percent accepted (R32), against $15 and $35 a month. The late share is planned at 5 percent (R29), the arrival threshold (R32), until the launch zone runs: about $0.17 a Plus member a month for a plan that keeps about $4.49 more than Basic. The credit never returns more than the membership already paid. The table is arithmetic, not a forecast.

## Acquisition economics per member

Revised 2026-10-20, the tiers revision. The question this answers: what one new paid member costs to acquire, by channel, and what each plan pays back to cover it.

**Cost per new paid member = channel cost ÷ new paid members from it**, by channel, plan, and zone, with affiliate commissions counted in.

**Ceiling per new paid member = the first 6 months of the plan's contribution (R63)**: about $47 on Basic, $70 on Plus, and $151 on Premier on the monthly plan, at 6.5 percent monthly churn (R59); about $48, $70, and $139 on the annual plan. Every channel scales while its measured cost is at or under the ceiling of the plan joined, and stops when it is not (decision 12).

Illustrative, using the decided prices, the planning values, and market benchmarks, replaced by measured costs once the zone runs:

<!-- sheet: Acquisition -->
| Channel | Cost basis | Cost per new paid member | Against the ceilings (about $47, $70, $151) | Source and grade |
|---|---|---|---|---|
| Affiliates | $20 commission per new paid member on any plan, paid once the second monthly payment or the first annual payment clears (R61) | $20 | Under every plan's ceiling; by about $27 on Basic and $50 on Plus | R61; market $4 to $56 an enrollment, S85, C |
| Email, SOS SMS's own list | The sending tool and the scorecard; almost no cost per send | Counted from the first opening email (Stage 2) | Measured | S92, C (open and click benchmarks only) |
| Paid social, sign-ups before the need | Audiences limited to the open zone's map | Counted in each open zone | Scales only at or under the plan's ceiling; pauses with sign-ups (R34) | Measured |
| Paid search, plumbing benchmark | $10.49 a click; 7.63 percent of clicks converting, assumed equal for sign-ups | about $137 | Over, about 3 times Basic's; not run at launch (decision 11) | S15, B |

<!-- sheet: Acquisition -->
| Plan, at the decided price | Contribution | Churn or renewal | First 6 months of contribution | Lifetime contribution |
|---|---|---|---|---|
| Plus, annual at $150 | about $139.78 a year | 75 percent renewal (R60) | about $70, paid up front | about $559 |
| Plus, monthly at $15 | about $13.77 a month | 6.5 percent a month (R59) | about $70 | about $212 |
| Basic, annual at $100 | about $95.31 a year | 75 percent renewal (R60) | about $48, paid up front | about $381 |
| Basic, monthly at $10 | about $9.29 a month | 6.5 percent a month (R59) | about $47 | about $143 |
| Premier, annual at $350 | about $278.05 a year | 75 percent renewal (R60) | about $139, paid up front | about $1,112 |
| Premier, monthly at $35 | about $29.62 a month | 6.5 percent a month (R59) | about $151 | about $456 |

**What it means.** Affiliates at the planning commission come in under every plan's ceiling, and SOS SMS's own email list costs almost nothing per send. Paid search at plumbing benchmarks does not pay back inside 6 months on one new member, so SOS SMS runs none at launch (decision 11): each zone fills through affiliates, the launch list, and paid social, and search volume for SOS SMS by name is counted once the zone has been open 6 months (R68). Plus on the annual plan, shown first, upgrades, referrals, three trades behind one membership, and the contractor fee from the first job all raise the contribution the ceilings are drawn from. Every request also pays for itself: the $25 contractor fee against about $11.97 of costs on both sides, about $13.03 net. The live model is the Pricing Model tab in `SOS_SMS_Pricing_Model.xlsx`.

## Step 9.3. ROI anchoring

### Anchor 1. Cost of the problem

Context the member already feels. SOS SMS does not claim to prevent damage, so no ROI multiple is computed against it.

<!-- sheet: ROI_Anchors -->
| Problem Scenario | Cost Without Solution | SOS SMS Cost | ROI Multiple |
|---|---|---|---|
| Water damage that becomes an insurance claim | Average water damage and freezing claim $13,954 (2018 to 2022) (S57, B) | From $10 a month on Basic, plus the $99 trip charge on use, credited to the repair | Not computed. SOS SMS gets a contractor there; it does not claim to prevent the damage |
| Waiting until morning | EPA: dry water-damaged areas within 24 to 48 hours to prevent mold (S58, A) | Same | Not computed, same reason |

### Anchor 2. Alternative comparison

What a household pays for the same readiness elsewhere, and what it pays with no plan when something breaks.

<!-- sheet: ROI_Anchors -->
| Alternative | Price in Advance | Cost When Something Breaks | What They Promise on Arrival | SOS SMS | Source and grade |
|---|---|---|---|---|---|
| D1 Search and call, no plan | Nothing | Service call fees commonly $150 to $250 after hours; labor 1.5 to 3 times standard rates | Nothing, unless the business offers it | From $10 a month for plumbing, HVAC, and electrical; the $99 trip charge on use, credited to the repair | S50, C |
| D2 Plumber and HVAC clubs | $8.25 to $19.99 a month for plumbing (Benjamin Franklin: $10 a month or $120 a year); HVAC clubs $15.95 to $36.95 | Club trip charge $49 instead of $89; 10 percent off repairs; no after-hours fees (Benjamin Franklin) | Priority scheduling with one company; $5 a minute late, up to $300, on scheduled appointments | Same; 6 months of membership credited on Plus, 12 on Premier, if the contractor is late | S40, S75, S76, A; S77, S100, C |
| D3 Home warranties | $47 to $82 a month | Service fee $75 to $125 a visit, for covered failures | Contractor contacted within 4 business hours, or 48 hours on weekends and holidays; no guarantee of timely emergency service | Same | S20, S79, B |
| D4 Utility-partner plans | $16.99 to $22.99 a month | Covered repairs up to $2,500 a call, after a 30-day waiting period | None found | Same | S78, A |
| D5 Frontdoor | $25 to $149 a year | Video help; a visit is arranged separately | Not applicable | Same | S81, A, B |
| D6 Marketplaces | Nothing | Free to request; booking prices vary | No arrival guarantee found; guarantees cover the work | Same | S44 to S46, A |

Against D1, a Basic member pays $10 a month before anything breaks, and $99 when they use it, credited to the repair; a household with no plan pays nothing in advance and an after-hours call fee of $150 to $250 when it happens (S50, C, internal only). Against D2, Basic matches the plumber club's $10 a month (S75) and covers HVAC and electrical too: the club gives one company's priority, a lower trip charge, and repair discounts; SOS SMS gives many contractors at once, an arrival time from the text, and on Plus and Premier a credit when the contractor is late. Against D3 and D4, a covered failure is usually cheaper through the warranty or the plan, and SOS SMS should say so: they pay for repairs, SOS SMS gets someone there.

### Anchor 3. Breakeven

**Member view.** A plan is worth keeping when being one text away from a vetted plumber, HVAC technician, or electrician is worth more to the household than its price; Plus adds the guarantee behind the arrival time and lets everyone at home send the text, and Premier adds a longer credit, a trip charge a year, and a second home. That is a judgment, not a number: SOS SMS does not claim a membership pays for itself, and the membership page makes the judgment easy by stating each plan's price, the trip charge on use, and what is not included.

**SOS SMS view.** Each plan must at least cover card processing (2.9 percent plus $0.30 a charge, R31), messaging, support and platform, its share of per-request costs on both sides, and on Plus and Premier the late-arrival credit: about $1.60 a Basic member a month at the planning values. At an 80 percent target margin the floors are about $7.69, $9.48, and $32.95 a month, and every plan clears its floor; with the $25 contractor fee from the first job, about $9.29, $13.77, and $29.62 a month of contribution is left (pricing model).

<!-- sheet: ROI_Anchors -->
| Plan | Price | Cost Components SOS SMS Must Cover | Breakeven | Payback Period |
|---|---|---|---|---|
| Basic, monthly | $10 a month | Processing, messaging, support and platform, per-request costs | M × (1 − 0.029) ≥ $1.31 a month: about $1.35 against $10 | An affiliate's $20 is paid back in the third month at $9.29 a month; dispatch starts after two payments, so a member who joins, uses it once, and cancels still leaves about $30.75 |
| Plus, monthly | $15 a month | The same, plus 5 phones and the late-arrival credit, about $0.17 a month | M × (1 − 0.029) ≥ $1.51 + $0.17 a month: about $1.73 against $15 | Six payments in, one late arrival with the credit used in full still leaves about $4.12 |
| Premier, monthly | $35 a month | The same, plus 10 phones, the 12-month credit, and the covered trip charge after 6 paid months, about $3.71 a month | M × (1 − 0.029) ≥ $2.00 + $3.71 a month: about $5.87 against $35 | Six payments, the covered trip charge, then cancel still leaves about $113.31. Twelve payments, then a late arrival with the 12-month credit used in full, costs about -$14.75: rare, and inside the plan's contribution |
| Annual plans | $100, $150, $350 a year | The same, for a year; Premier's covered trip charge from joining | About $5, $10, and $72 a year against the price | Paid back at joining at the $20 commission |

### "One outcome" message, adapted

The skill's "one outcome pays for X years" is not claimed: SOS SMS does not say a membership pays for itself. The adapted message, for the membership and guarantee pages, written to decision 3:

<!-- sheet: ROI_Anchors -->
| Outcome | Message |
|---|---|
| The contractor is late, on Plus or Premier | "If your contractor gets there after 90 minutes from your text, we credit the membership you paid for the 6 months before (12 on Premier), on your next bills. The trip charge still pays for the work." |
| The work goes ahead | "Your $99 trip charge counts toward the bill, so you don't pay twice." |
| Nothing breaks this month | "Most months nothing breaks. Your membership is there for the night something does, and you can cancel any time." |

## Pricing decisions, decided 2026-10-03, revised 2026-10-11 and 2026-10-20

<!-- sheet: Decisions -->
| # | Decision | Decided | Where it shows |
|---|---|---|---|
| 1 | Where SOS SMS revenue comes from (shared with Run 1) | Members pay a plan, billed to the card on file: Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350 (R51, R52, R65, R66), no fee per request. Contractors pay $25 per completed paid job from the first job (decision 2, revised 2026-10-20) | Phases 6 and 8, both runs |
| 2 | The guarantee scope (decision 3) | 90 minutes from the member's request text, anywhere in the zone's neighborhoods, at any hour (R15). No acceptance: told within 15 minutes, never charged. A late arrival keeps its trip charge; on Plus and Premier, the membership paid in the 6 months (Plus) or 12 months (Premier) before the request is credited (R65, R66). A no-show returns the trip charge in full; NEXT after the 90 minutes (R17) | Phase 6 drill 3; the guarantee page |
| 3 | Who sets the trip charge | SOS SMS: one $99 trip charge per trade and zone, the same for plumbing, HVAC, and electrical, stated on the membership page before joining | Membership page; Run 1 terms |
| 4 | What every plan includes | One-text dispatch in plumbing, HVAC, and electrical, at any hour; an arrival time on acceptance; never charged if no one accepts; NEXT after a miss; a person by text; the readiness kit and a yearly readiness check. Plus adds the guarantee and up to 5 phones; Premier a 12-month credit, a trip charge a year on SOS SMS, a second home, and up to 10 phones (R69). Not included: the repair, parts, a guarantee on the work, or faster dispatch (R53) | Membership page; Phase 6 drill 6 |
| 5 | Cancelling, renewal, and changing plans | Cancel any time, on the membership page or by texting HELP; a monthly membership ends at the end of the paid month and an annual one at the end of the paid year, with no partial refunds; annual members get a reminder before `{{renewal date}}`; a failed payment is retried for 7 days, then the membership pauses (R56). Upgrades at once on annual, 30 days after on monthly; downgrades at the end of the paid period (R54) | Member terms; member emails |
| 6 | The acquisition ceiling | One per plan, the first 6 months of contribution: about $47 Basic, $70 Plus, $151 Premier (R63), reviewed weekly by channel, plan, and zone; every channel scales while at or under it. No paid search at launch (decision 11) | Phase 8 measurement; speed-to-scale plan, section 8 |
