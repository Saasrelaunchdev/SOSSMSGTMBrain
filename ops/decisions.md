# Decision log

What was decided and why, so settled strategy is not relitigated. Newest at the top. Every entry is DECIDED: nothing waits on a founder. Decision numbers 1 to 12 are the merged list in `sources/raw/gtm/marketplace/cross-side-check.md` Part 3, all decided 2026-10-03; every other value is in `reference/resolution-register.md`. The per-brief numbers in the runs differ (crosswalk at the end).

---

## 2026-10-04 Every unknown and founder decision resolved (DECIDED)
At the user's instruction ("The final walkthrough and every deliverable we have shouldn't include any TBDs or decisions left for the founder. Everything should be resolved"), the GTM consultant resolved every former unknown and every founder decision, from public data, the research, and the GTM itself. Each value is now decided, a planning value with its basis, counted at a named stage, or a `{{merge field}}` (`reference/resolution-register.md`, R01 to R50). Nothing that cannot exist before launch is guessed: results, arrival times, and counts are resolved to how and when they are counted.

**Rationale:** copy that waited on decisions could not ship, and every value needed for launch can be set from the research and the pricing model. Planning values are labelled, so no planning number is ever mistaken for a result.
**What this does not change:** nothing is live; no customer, contractor, job, testimonial, or result exists; grade C figures stay internal; contractor recruiting copy stays in the future tense; customer copy stays held until its zone opens.
**Downstream:** every file in `rules/`, the master context, `reference/`, `templates/`, `examples/`, `adapters/`, and `tools/check_sos_sms.py` (which now fails on any placeholder); the GTM build repo, the Google folder, and the walkthrough deck. Done 2026-10-04.

## 2026-10-03 The twelve decisions (DECIDED)

| # | Decision | Decided |
|---|---|---|
| 1 | Launch metro, first zone, trades | The United States; the founders' home metro; one founding zone, a 10-mile radius around the founding contractors' shops; plumbing and water emergencies first |
| 2 | Revenue model | Customer: a $49 SOS SMS fee per dispatched request. Contractors: $0 to join, $0 per request seen or declined, no subscription; $0 a job in the founding period (the zone's first 6 months open), then $25 per completed paid job, deducted from the payout; founding contractors keep $0 a job for 12 months after it. No share of the repair |
| 3 | Late-arrival rule and guarantee scope, together | Fault-based (option C); acceptance only with an arrival time inside the remaining window; 90 minutes from the customer's confirming text; the $99 trip charge back automatically, from the contractor's trip charge when they missed their time, from SOS SMS when SOS SMS caused the miss; covered areas and hours named on the zone page; with no acceptance, the customer is told within 15 minutes and pays nothing |
| 4 | Dispatch rule, and what contractors see first | All matched at once; first to accept with an arrival time inside the remaining window; the problem, photos or video, and an approximate distance and cross-street area before accepting; the address only to the contractor who accepts |
| 5 | Who sets the trip charge | SOS SMS, one per trade and zone: $99 for plumbing in the founding zone, day or night, credited to the repair |
| 6 | Payments | Stripe Connect: authorize at the confirming text, capture at acceptance, hold, release on arrival; payout within 2 business days of arrival |
| 7 | Verification recheck cadence | At sign-up, every 6 months, and on each policy's expiry date; the same words on both sides |
| 8 | Safety handling | Gas, smoke, fire, injury: the safety reply first; no broadcast until the customer confirms they are safe and the utility or 911 has been called |
| 9 | Carrier registration | One local number in the launch metro's area code, registered for A2P 10DLC before any test text (S32) |
| 10 | Name collision | US trademark search and search check in the zone in Stage 0; the full name always; no bids on "SOS plumbing" |
| 11 | Paid search eligibility | Standard Google search ads only, after Google's written confirmation; never Local Services Ads; message assets only once verified; Microsoft Ads alongside (S70 to S72, S74) |
| 12 | Paid search ceiling per zone | $275 per paid job while proving; $192 by the end of month 6; $137 by the end of month 12 |

**Rationale:** the GTM consultant's resolution at the user's instruction, from the research, both runs, the cross-side check, and the pricing model (basis per decision in `sources/raw/gtm/marketplace/resolution-register.md`).
**What this does not change:** nothing is live. The guarantee, the fees, and the payout are launch-day terms, held in customer copy until the zone opens.
**Downstream:** done 2026-10-04 (entry above).

## 2026-10-03 Pricing direction: contractors join free, SOS SMS earns on transactions (DECIDED with decision 2)
The GTM consultant set the direction for the pricing model: the lowest barrier of entry for contractors, and revenue from transactions, not from joining. Contractors pay $0 to join, $0 per request seen or declined, and no subscription or seat fee. SOS SMS earns an SOS SMS fee on each customer request, and a contractor fee per completed paid job once the founding period ends; founding contractors keep $0 a job for a held period after it. Decision 2 took this direction the same day.

**Rationale:** supply is the constrained side and every customer promise depends on density, so contractors are subsidized; the customer pays for speed and the guarantee. A customer fee alone does not pay back paid search on the first job, so the contractor fee after the founding period is planned from the start (`reference/pricing-and-economics.md`).
**What this does not change:** grade C figures stay internal. No claim, channel, or status changes. The amounts became decided with decisions 2 and 5 (above).
**Downstream:** `reference/pricing-and-economics.md` (the price points), `rules/do-not-say.md` (the two lines are never merged into one total), `adapters/portable-control-layer.md`, `ops/asset-index.md`; the pricing model and handoff in `Fit137/SOSSMSGTMBuild` (`google-folder/SOS_SMS_Pricing_Model.xlsx`, `gtm/pricing/pricing-handoff.md`). Done 2026-10-03.

## 2026-10-03 Pre-launch framing for contractor recruiting (DECIDED, build rule)
Contractor recruiting copy goes out before launch and describes what SOS SMS is building, in the future tense ("when it opens in {{zone}}"). Customer copy stays held until the zone opens.

**Rationale:** the live test (`pages/partner-counter-card.md`) found that "held until it ships" and Stage 1 recruiting before launch could not both be followed. This is a wording rule derived from decided strategy (supply first, pre-launch), not a new strategic choice.
**What this does not change:** no claim, no number, no channel. Nothing is described as live.
**Downstream:** `rules/writing-rules.md`, the master context Section 0, `ops/QA-checklist.md`, `adapters/portable-control-layer.md`. Done 2026-10-03.

## 2026-10-02 Built the GTM brain from both runs and the walkthrough (DECIDED)
This repository is the single source of truth for SOS SMS go-to-market work. Where a source and the brain disagree, the brain records the conflict and the decided verdict wins.

**What this does not change:** no strategy, claim, or number.

## 2026-10-01 Brand identity v1: green and white (DECIDED)
Logo, mark (round customer, square contractor), Inter, the twelve colour roles, and the brand book, built in the walkthrough repo at the user's request. The dark (projector) palette is kept as validated (2026-10-04): three roles sit brighter than the chart band so every role clears 5:1 on the dark surface.

**What this does not change:** the voice rules, and the rule that the name is always SOS SMS.

## 2026-10-01 Product-led motion, no sales team (DECIDED)
No calls, demos, meetings, shop visits, or audits on either side. Contractors: cold email, a partnership program, an in-product referral loop, self-serve sign-up by text. Customers: bottom-of-funnel paid search (Google, then Microsoft), problem-solving pages, product loops. No outreach to homeowners. The white-glove audit became the automated lead spend report.

**Rationale:** the founders chose it after the first runs; paid search sits where emergency demand already searches, and a text-only product can convert without people.
**What this does not change:** the two-run structure, supply first, the claim ledger.
**Downstream:** stale lines in two sources still mention calls (`reference/lead-magnets.md`, source conflict). This entry governs.

## 2026-10-01 Two runs, never blended (DECIDED)
One value proposition, ICP, journey, and channel plan per side. No asset speaks to both.

## 2026-10-01 Supply leads, demand follows, zone by zone (DECIDED)
Demand opens only at the density number, for covered hours. Paid search is geofenced and scheduled to match.

## 2026-10-01 Where SOS SMS fights (DECIDED)
Contractors: no charge for requests that never become work; paid to show up. Customers: a guaranteed arrival window; many contractors reached with one reply. Do not contest volume, exclusivity, brand familiarity, or guarantees on the work.

## 2026-10-01 Claims follow the narrowed forms; nothing invented (DECIDED)
Every source "only" and "unique" was narrowed or dropped. No result exists before launch: social proof is the method line and proof is the named record (R44, R45) until permissioned results exist.

## 2026-10-01 Speed only inside proven zones (DECIDED)
Accept inefficiency in proving zones; never trade claim accuracy, safety, payouts, refunds, privacy, or law. Zone thresholds are set before launch (R32).

## Closed 2026-10-04 (formerly open, owned elsewhere)
- **Customer data rule:** name, address, phone, and photos go to the accepting contractor only (decision 4); no marketing texts without a separate written opt-in (S31). Decided in the Run 2 brief.
- **Demand-side scope:** homeowners. Property managers would be a third run (Run 2 brief).
- **Build status of every capability:** every capability is PLANNED, built in Stage 0 or at its named stage, and claimable only once it ships (`rules/feature-status.md`).
- **The founder memo and unattributed matrix rows:** excluded for good (R26).
- **Dispute rules:** founders handle each dispute by text in Stage A, decided from the request log (confirming text, acceptance, committed arrival time, arrival); written rules and a queue before scaling (speed-to-scale plan, operations table).
- **Founder roles, team, runway, channels tried:** a supply lead and a demand lead (R25); at least 18 months of runway at Stage A spending (R35); no channels tried before launch (R48).
- **Customers without a card (conflict D)** and **first refusal on a contractor's own customers (conflict E):** R16 and R13.
- **Walkthrough deck:** the Vercel config is checked on the first deploy, with Deployment Protection on; S08 has 6 bands.
- **Review cadence and corroboration thresholds:** adopted as set in `review-cadence.md`.

## Numbering crosswalk
Run 1 brief: 1 metro = 1; 2 revenue = 2; 3 late arrival = 3; 4 dispatch = 4; 7 name collision = 10. Run 2 brief: 2 metro = 1; 3 customer price = 2 and 5; 4 guarantee scope = 3; 7 name collision = 10; 8 paid search eligibility = 11.
