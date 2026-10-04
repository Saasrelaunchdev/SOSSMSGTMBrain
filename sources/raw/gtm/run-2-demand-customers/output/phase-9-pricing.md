# Phase 9. Pricing and Packaging Dashboard, customer side

A customer buys one emergency call, rarely. The skill's subscription tiers describe nothing they buy, so per `../SKILL-ADAPTATION.md` this phase builds the customer side of the take rate. The prices here were decided on 2026-10-03 (decisions 2 and 5, `../../marketplace/resolution-register.md`), from the pricing model in `../../pricing/pricing-model.md`: a $99 trip charge and a $49 SOS SMS fee per dispatched request. Run 1 Phase 9 recommended that SOS SMS's revenue come from this side and that contractors pay nothing at launch; the decision adopted it, with a contractor fee after the founding period.

Live calculators are in `pricing_dashboard.xlsx`.

## Step 9.1. Value metric selection

<!-- sheet: Value_Metric -->
| Denominator | Correlation to Value | Scalability | Ease of Measurement | Score (1 to 10) | Verdict |
|---|---|---|---|---|---|
| Per request, flat (trip charge plus an SOS SMS fee) | High. One request is one emergency handled | High | High | 8.2 | Primary |
| Per outcome: the fee is what the guarantee refunds on a miss | High. The customer pays for arrival inside the window | High | Medium. Needs arrival logging | 7.1 | Built into the primary: the guarantee makes the request price outcome-backed |
| Per completed repair, as a percentage | Medium. SOS SMS does not control the repair or its price | Medium | Low unless payment for the work flows through SOS SMS | 4.6 | Reject at launch |
| Per household per year (membership) | Low to medium. Emergencies are rare for any one household | Medium | High | 3.9 | Later option only; competes with home warranties (D6) |
| Per capability (priority, after-hours premium) | Medium | Medium | High | 3.2 | Reject. An after-hours premium is the surprise fee customers complain about (S50, S51) |

**Decided (decision 2):**

- **Primary value metric: per request.** The customer sees two lines before anyone is sent: the trip charge, credited to the repair if they go ahead, and the SOS SMS fee, which pays for dispatch and the guarantee.
- **Secondary usage metric, for tracking:** requests per 1,000 owner-occupied homes in the zone per month.
- **Rationale:** the customer is paying for speed and certainty. A flat, stated price matches that, avoids the after-hours surprise the research found customers resent, and puts the guarantee's cost where its value is felt.

## Step 9.2. Packaging: the customer price structure

<!-- sheet: Packaging -->
| Plan | Price | What it covers | Guarantee | Position | Target share of requests |
|---|---|---|---|---|---|
| Standard request | Trip charge $99 plus SOS SMS fee $49, two lines | Dispatch to the matched contractors; the trip; the trip charge credited to the repair if the customer goes ahead | 90-minute guarantee: 90 minutes from the confirming text; the $99 trip charge back on a miss | Default | About all requests at launch |
| Request outside covered hours | Not dispatched | Stop-the-water steps and the safety line by text, free | None | Not offered at launch: the guarantee and the ads run only in covered hours (R15) | 0 |
| Household membership | Not offered at launch | n/a | n/a | A later option only; competes with home warranties (R19) | 0 |

Not offered: requests outside the founding zone. Those customers are told plainly that SOS SMS does not cover their area yet.

### Expansion levers

1. More trades behind the same number: water damage first, then electrical, HVAC, and locksmith, each opened only when Run 1 reaches density for that trade.
2. Neighbor referral through the forwardable contact card.
3. Repeat use by the same household, rare by nature.
4. A household membership, later, if repeat use and saved-number rates show it would be valued.
5. Property managers, as a separate future run (the demand side is homeowners, brief decision 1).

## Guarantee economics

What the 90-minute guarantee costs SOS SMS depends on Run 1's late-arrival rule. Under the decided fault-based rule (Run 1, option C; decision 3), a contractor who misses their own committed time funds the refund from their trip charge, and SOS SMS pays only for misses it causes: no acceptance in time, or dispatch failure.

Expected refund cost per request = (share of requests where SOS SMS causes a miss) × (refund amount). With the refund equal to the trip charge T, the SOS SMS fee must cover at least that share of T before processing and operations.

<!-- sheet: Guarantee_Economics -->
| Share of requests with an SOS-caused miss | Refund cost per request, as a share of the trip charge | Minimum fee to cover refunds alone |
|---|---|---|
| 2 percent | 0.02 × T | 2 percent of T |
| 5 percent | 0.05 × T | 5 percent of T |
| 10 percent | 0.10 × T | 10 percent of T |
| 20 percent | 0.20 × T | 20 percent of T |

Under option B (SOS SMS absorbs every miss), replace "SOS-caused" with all misses, and the fee must cover the full miss rate. The SOS-caused miss share is planned at 5 percent (R29) until the founding zone runs: $4.95 of reserve per request on the $99 trip charge. The table is arithmetic, not a forecast.

## Paid acquisition economics

Added 2026-10-01 for the product-led motion, where paid search is the first customer channel. The question this answers: what does one paid job cost to acquire, and what has to be true for the take per job to cover it.

**Paid cost per paid job = cost per click ÷ click-to-first-text rate ÷ first-text-to-paid rate**

**Blended cost per paid job = (1 - owned share of requests) × paid cost per paid job**, where the owned share is requests from saved numbers, shares, and organic pages.

Illustrative, using market benchmarks and a planned 50 percent first-text-to-paid rate (R30), replaced by the measured rate once the zone runs:

<!-- sheet: Paid_Acquisition -->
| Basis | Cost per click | Click to first text | Cost per first text | Paid cost per paid job at 50 percent | Source and grade |
|---|---|---|---|---|---|
| Plumbing search benchmark | $10.49 | 7.63 percent | about $137 | about $275 | S15, B |
| Emergency plumbing dataset | $66.82 | 31 percent | about $216 | about $431 | S69, C |
| Microsoft Ads, 30 to 60 percent cheaper clicks on the benchmark basis | $4.20 to $7.34 | 7.63 percent, assumed equal | about $55 to $96 | about $110 to $192 | S74, C |

<!-- sheet: Paid_Acquisition -->
| Owned share of requests | Blended cost per paid job, benchmark basis |
|---|---|
| 0 percent | about $275 |
| 30 percent | about $192 |
| 50 percent | about $137 |
| 70 percent | about $82 |

**What it means.** A customer fee on its own will not pay back a paid-search job on the first request: the trip charge benchmarks are $75 to $100 (S28) and after-hours call fees $150 to $250 (S50). Four levers close the gap, and Phase 9 of Run 1 and the speed-to-scale plan carry them: a rising owned share, more jobs per household (repeats and more trades), cheaper paid sources (Microsoft Ads, problem keywords), and revenue from both sides after the founding period. The live calculator is the Calculators sheet, section 3, in `pricing_dashboard.xlsx`.

## Step 9.3. ROI anchoring

### Anchor 1. Cost of the problem

Context the customer already feels. SOS SMS does not claim to prevent damage, so no ROI multiple is computed against it.

<!-- sheet: ROI_Anchors -->
| Problem Scenario | Cost Without Solution | SOS SMS Cost | ROI Multiple |
|---|---|---|---|
| Water damage that becomes an insurance claim | Average water damage and freezing claim $13,954 (2018 to 2022) (S57, B) | Trip charge $99 plus SOS SMS fee $49, the trip charge credited to the repair | Not computed. SOS SMS gets a contractor there; it does not claim to prevent the damage |
| Waiting until morning | EPA: dry water-damaged areas within 24 to 48 hours to prevent mold (S58, A) | Same | Not computed, same reason |

### Anchor 2. Alternative comparison

What the customer pays or risks before the repair starts. The anchor that closes is usually the after-hours service call fee, because it is the price the customer would otherwise meet at the door.

<!-- sheet: ROI_Anchors -->
| Alternative | Their Cost Before the Repair | What They Promise on Arrival | SOS SMS | Source and grade |
|---|---|---|---|---|
| D1 Search and call, after hours | Service call fees commonly $150 to $250 after hours; labor 1.5 to 3 times standard rates | Nothing, unless the business offers it | Trip charge $99, credited to the repair; SOS SMS fee $49 | S50, C |
| D2 Roto-Rooter | No extra charge for nights, weekends, holidays; job price varies | Typically within two hours for true emergencies, no refund promise (C) | Same | S41, A and C |
| D3 Benjamin Franklin | Varies by franchise | $5 a minute late, up to $300, on scheduled appointments | Same; the $99 trip charge back if no one is there within 90 minutes of the request | S40, A |
| D4 Angi, D5 Thumbtack | Free to request; booking prices vary | No arrival guarantee found; guarantees cover the work | Same | S44 to S46, A |
| D6 American Home Shield | Service fee typically $75 to $125, for covered failures | Contractor contacted within 4 business hours, or 48 hours on weekends and holidays; no guarantee of timely emergency service | Same | S20, B; S56, C |
| Do it yourself, or wait | $0 tonight | n/a; the damage keeps going | Same | S57, S58 |

Against D1, the customer pays $148 before the repair, as two lines ($99 trip charge, credited to the repair, plus the $49 SOS SMS fee), at or under the $150 to $250 after-hours call fee: about 1 to 41 percent less. Internal only, because S50 is grade C, and never shown to a customer as one total. Two honest positions SOS SMS can take: against D6, a covered failure is usually cheaper through the warranty, and SOS SMS should say so; against D1, the comparison is the after-hours service call fee against the trip charge, which is credited if the work goes ahead.

### Anchor 3. Breakeven

**Customer view.** If the customer goes ahead with the repair, the trip charge is credited, so the extra cost of using SOS SMS instead of reaching a plumber directly is the SOS SMS fee, plus any difference between SOS SMS's trip charge and the plumber's own after-hours call fee. Breakeven: the fee is worth paying when not having to find someone at night, plus the guarantee, is worth more to the customer than the fee. That is a judgment, not a number, and the first reply should make it easy by stating both lines.

**SOS SMS view.** The fee must at least cover refund cost per request (guarantee economics, above), payment processing (2.9 percent plus $0.30 a charge, R31), and operations ($5.30 a request, R31). At a 5 percent SOS-caused miss share and a 65 percent target margin, the floor is about $42, and the $49 fee clears it (pricing model).

<!-- sheet: ROI_Anchors -->
| Plan | Price per Request | Cost Components SOS SMS Must Cover | Breakeven Condition | Payback Period |
|---|---|---|---|---|
| Standard request | Trip charge T of $99 plus fee F of $49 | Refunds (share × T), processing, operations | F ≥ (SOS-caused miss share × T) + processing + operations per request: $49 against a floor of about $42 | n/a for a per-request price |

### "One outcome" message, adapted

The skill's "one outcome pays for X years" does not apply to a single emergency call. The adapted message, for the guarantee page, written to decision 3:

<!-- sheet: ROI_Anchors -->
| Outcome | Message |
|---|---|
| The window is missed | "If your contractor isn't there within 90 minutes of your request, the $99 trip charge comes back to you, automatically." |
| The work goes ahead | "Your $99 trip charge counts toward the bill, so you don't pay twice." |

## Pricing decisions, decided 2026-10-03

<!-- sheet: Decisions -->
| # | Decision | Decided | Where it shows |
|---|---|---|---|
| 1 | Where SOS SMS revenue comes from (shared with Run 1) | A $49 SOS SMS fee per dispatched request on the customer side; $0 to contractors during the founding period, then $25 per completed paid job, because paid search costs are not covered by the customer fee alone | Phases 6 and 8, both runs |
| 2 | The guarantee scope (decision 3) | 90 minutes from the customer's confirming text; the refund is the $99 trip charge, automatic; covered areas and hours named on the zone page; when no one accepts, the customer is told within 15 minutes and pays nothing | Phase 6 drill 3; the guarantee page |
| 3 | Who sets the trip charge | SOS SMS: one $99 trip charge per trade and zone, so the customer sees one price before dispatch | First reply; Run 1 terms |
| 4 | Is the SOS SMS fee refunded on a miss too | No. The refund is the $99 trip charge; the SOS SMS fee carries the guarantee's refund reserve. One amount keeps the promise simple to state | Guarantee page |
| 5 | What happens for customers without a card | No pay-on-arrival path at launch: dispatch needs a card or a phone wallet through the payment link; without one, the customer gets the free help by text and pays nothing | Phase 7 blocker |
| 6 | The paid search ceiling per zone | $275 per paid job while proving a zone, falling to $192 by the end of month 6 and to $137 by the end of month 12 | Phase 8 Channel 1 budgets; speed-to-scale plan, section 8 |
