# Phase 1. Product Feature Matrix Dashboard, contractor side

Rates only the contractor items (`../GTM-BRIEF.md` Section 3). Bryan's ratings from the source matrix are the starting hypotheses. The research in `../../research/supply-research.md` (Step 1.1) moved them where evidence supported it.

## Step 1.1. Research

Done, see `../../research/supply-research.md`, Step 1.1. Competitors researched: C1 Angi Leads, C2 Thumbtack, C3 Google Local Services Ads, C4 Service Direct, C5 home warranty network, C6 status quo.

## Step 1.2. Demand and competitiveness

Demand scale: Wanted by one, some, most, all. Competitiveness scale: Commodity (should be free), Most vendors can do this, A few others can do this, Unique to us.

<!-- sheet: Scoring -->
| # | Feature | Source | Demand | Competitiveness | Bryan's hypothesis | Changed? | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | Zero cost to join: no subscription, no lead fees | stated | Wanted by all | A few others can do this | All / Unique To Us | Yes, competitiveness down | Free sign-up is common (S05, S36); Jiffy has no lead fee but takes 20 to 30 percent (S16); warranty networks charge no join fee (S33). Step 1.5 rule also forbids All with Unique |
| 2 | High-urgency leads: active emergencies | stated | Wanted by most | A few others can do this | Most / A few others | No | Service Direct and eLocal sell emergency calls (S10, S11) |
| 3 | Pre-qualified leads: matched to service area and trade | stated | Wanted by all | Most vendors can do this | All / Most vendors | No | Every platform claims it; FTC found HomeAdvisor's claims false or unsubstantiated (S01) |
| 4 | Guaranteed trip charge, collected before the contractor rolls | stated | Wanted by most | A few others can do this | All / Most vendors | Yes, demand down one level, competitiveness up | No lead platform in the set collects a trip charge for the contractor; many plumbers waive trip fees and recover them in labor (S28), so not all want it |
| 5 | Photos and video before you roll | inferred | Wanted by some | A few others can do this | Most / A few others | Yes, demand down | No source evidences contractor demand; the source matrix marks it as implied by a memo |
| 6 | Accept or decline freely | stated | Wanted by most | Most vendors can do this | Most / Most vendors | No | Thumbtack opportunities and Service Direct pausing give similar control (S05, S10) |
| 7 | Customer relationship stays with the contractor | candidate | Wanted by most | Most vendors can do this | not rated | New | Lead platforms hand over the customer (S03, S05); booking and warranty networks keep the customer (S16, S20) |
| 8 | Fast trip charge payout | candidate | Wanted by most | A few others can do this | not rated | New | Only platforms that collect payment can offer it (S16, S17); unverified |
| 9 | Jobs received and accepted by text, no app | candidate | Wanted by some | A few others can do this | not rated | New | Text notifications are common (S05); accepting by text is not documented |

## Step 1.3. Scatter plot scores

Demand and competitiveness from -20 to +20, with decimals. Bands used: Wanted by all +14 to +19, most +6 to +13, some -6 to +3. Unique +14 to +19, A few others +3 to +12, Most vendors -4 to -12, Commodity -13 to -19.

<!-- sheet: Scoring -->
| Feature | Demand Score | Competitiveness Score |
|---|---|---|
| 1. Zero cost to join | 17.6 | 6.3 |
| 2. High-urgency leads | 11.2 | 7.9 |
| 3. Pre-qualified leads | 16.4 | -8.7 |
| 4. Guaranteed trip charge, collected up front | 10.6 | 11.8 |
| 5. Photos and video before you roll | -1.8 | 5.4 |
| 6. Accept or decline freely | 8.1 | -6.2 |
| 7. Customer relationship stays with the contractor | 9.4 | -9.3 |
| 8. Fast trip charge payout | 6.8 | 3.1 |
| 9. Jobs by text, no app | -4.2 | 5.9 |

## Step 1.4. Quadrant assignment

<!-- sheet: Quadrants -->
| Feature | Quadrant | Rationale |
|---|---|---|
| 1. Zero cost to join | Q1 Hero Feature | Every contractor wants it, and only a few alternatives combine no lead fee with no commission. Decision 2 keeps it there: joining and requests stay free, and the $25 fee applies only to completed paid jobs after the founding period |
| 2. High-urgency leads | Q1 Hero Feature | Emergency-only requests answer the "just exploring" complaint (S05). Service Direct is the only close peer |
| 3. Pre-qualified leads | Q4 Table Stakes | Expected from any platform, and the FTC order (S01) means contractors discount the claim. Must be present, cannot lead |
| 4. Guaranteed trip charge, collected up front | Q1 Hero Feature | The strongest competitive score on the list. No lead platform in the set does it, and it changes the economics from paying to receive a request to being paid to show up |
| 5. Photos and video before you roll | Q2 Differentiator | Few offer it, but demand is not evidenced. Useful as a reason to believe, not a headline |
| 6. Accept or decline freely | Q4 Table Stakes | Contractors expect control; similar control exists elsewhere |
| 7. Customer relationship stays with the contractor | Q4 Table Stakes | Lead platforms already hand over the customer, so it is expected. Its value is defensive: SOS SMS must not look like a booking network that keeps the customer |
| 8. Fast trip charge payout | Q1 Hero Feature, payout set by decision 6 | Only meaningful because SOS SMS collects the trip charge. Set at within 2 business days of arrival through Stripe Connect (decision 6), built in Stage 0; the payout log shows it from the first job |
| 9. Jobs by text, no app | Q2 Differentiator | Low evidenced demand, some differentiation. Matters for onboarding friction rather than for the pitch |

Quadrant reference: Q1 Hero Features (high demand, high competitive advantage), Q2 Differentiators (low demand, high advantage), Q3 Commodities (low demand, low advantage), Q4 Table Stakes (high demand, low advantage). No contractor item falls in Q3.

## Step 1.5. Entry validation

<!-- sheet: Validation -->
| Rule | Check | Result |
|---|---|---|
| If "Wanted by some", exclude "Most vendors can do this" | Items 5 and 9 are Wanted by some and rated A few others | Pass |
| If "Wanted by all", exclude "Unique to us" | Bryan rated item 1 Wanted by all and Unique To Us | **Violation in the source matrix.** Corrected to A few others, which the research also supports |
| If "Wanted by one", exclude "Commodity" | No item is Wanted by one | Pass |
| Source matrix residue | The "CONTRACTOR FEATURES" header row carries a rating (Most / Unique), and four rated rows have no item text (Most / A few others, then three of Some / Unique) | Excluded. Three blank rows rated Unique suggest items Bryan meant to add. Ask him what they were |
| Ali's ratings | 18 rated rows, no item text | Excluded. Cannot be attributed |

## Step 1.6. Demand driver

One top-of-funnel entry for contractors. Rule check: it must give immediate value, and reveal a problem SOS SMS is built to solve. The skill's wording is "only SOS SMS"; the narrowed form used here is the specific combination SOS SMS offers, no lead fee plus a trip charge collected before the contractor rolls, which no alternative in the set offers together.

<!-- sheet: Demand_Drivers -->
| Attribute | Description |
|---|---|
| What it is | **The Lead Cost Check.** A two-minute calculator. The contractor enters last month's lead spend, how many leads they paid for, how many became booked jobs, and how many trips they made without getting paid. It returns their true cost per booked job and the share of spend that went to requests that never became work |
| Immediate value | A number most contractors have never calculated, from their own data, with nothing to sign up for. The output belongs to them whether or not they ever join |
| How it helps in problem identification | It separates the price of a lead from the cost of a job. A $40 lead that closes one time in six is a $240 job before the truck leaves (illustrative arithmetic using the ranges in S03 and S06) |
| How it exposes the need for SOS SMS | The two leaks it measures, paying for requests that never convert and driving out without getting paid, are the two things SOS SMS's model removes: no lead fee, and the trip charge collected before rolling |
| ICP fit | ICP Level 2: contractors already paying for leads. Level 1 contractors with no lead spend get a short path to the unpaid-trips question instead |
| Conversion lever | The result screen ends with one question: "Want emergency jobs where you pay nothing to see the request and the trip charge is collected before you roll?" Reply by text to join the founding contractor list |
| Top-of-funnel use case | The hook in cold email 1, on supply house counter cards and partner newsletters, and forwarded contractor to contractor. No calls: the check runs itself |

## Step 1.7. Demand driver variants

<!-- sheet: Demand_Drivers -->
| Variant Name | Perceived Value | Ease of Delivery | Delivery Type | Description | TOFU Use Case |
|---|---|---|---|---|---|
| Automated lead spend report | High | Medium | Light tool | The contractor forwards or uploads three months of lead platform receipts; a report by email shows cost per booked job by platform. Replaces the white-glove audit, since there is no sales team | Follow-up for contractors who complete the Lead Cost Check from cold email |
| The Lead Cost Check | Medium | Easy | Light tool | The calculator above, web page or text-based | Cold email, supply house QR cards, partner newsletters |
| After-Hours Readiness Scorecard | Medium | Easy | Self-assessment scorecard (ScoreApp) | Seven questions on after-hours response, trip charge policy, lead spend, and unpaid trips, scored 0 to 100 | The lead magnet, specified in `lead-magnet-spec.md` |
| Emergency rate card template | Low | Easy | Light tool | A one-page template for stating after-hours trip charges and rates up front | Giveaway at supply counters and association meetings; builds familiarity with the trip charge idea |
| Founding contractor test week | High | Medium | Value using the product itself | Once the product exists: a week of live requests in the launch area with no fee of any kind | Converts interested contractors into active ones. Not available until launch |

## What Phase 1 tells the rest of the run

- **Lead with item 4, the trip charge collected up front.** It has the highest competitive score and is the one thing no lead platform does. Item 1, no lead fees, is the door opener but not unique, and its strength depends on how SOS SMS earns money.
- **Answer the shared-request weakness explicitly.** Item 3 sits in Table Stakes and carries a trust penalty from the FTC order. Phase 3 has to address that SOS SMS sends each request to several contractors.
- **Rate the obligations, too.** Joining asks the contractor to commit to an arrival time, credit the trip charge to the job, and keep license and insurance current (`../GTM-BRIEF.md` Section 3). These are costs in the contractor's eyes. Phase 6 states them; Phase 7 places them in onboarding.
