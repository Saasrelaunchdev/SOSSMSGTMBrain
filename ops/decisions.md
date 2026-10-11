# Decision log

What was decided and why, so settled strategy is not relitigated. Newest at the top. Every entry is DECIDED: nothing waits on a founder. Decision numbers 1 to 12 are the merged list in `sources/raw/gtm/marketplace/cross-side-check.md` Part 3, all decided 2026-10-03; decisions 2, 3, 6, 8, and 11 were revised and decision 12 replaced by the membership revision on 2026-10-11 (the entry below governs where the two differ). Every other value is in `reference/resolution-register.md`. The per-brief numbers in the runs differ (crosswalk at the end).

---

## 2026-10-11 The membership revision: the demand side is a membership, joined before the need (DECIDED)
The demand side of SOS SMS is a monthly or annual membership, not pay per request. Homeowners join before anything breaks, with their card and home address on file, so in an emergency a member sends one text and help is on the way: no search, no sign-up, no payment entry, nothing to confirm. Speed is the point, and membership is what makes it possible. Members are reached before the need, through lower-cost channels that only work then: affiliates and email lead, and search and SEO pages, paid search, and paid social sell sign-ups in open zones. The homeowner searching in the middle of an emergency is not the target: at that moment, calling a contractor from the results beats joining anything.

| # | Decision | Revised 2026-10-11 |
|---|---|---|
| 2 | Revenue model | Members pay a monthly or annual membership, billed to the card on file: planning values $10 a month or $100 a year (R51, R52) until the launch price is set in Stage 0; copy writes `{{monthly price}}` and `{{annual price}}`. No fee per request: the $49 SOS SMS fee is retired (R02). The $99 trip charge on use, credited to the repair. Contractors unchanged: $0 to join and per request, $0 a job in the founding period, then $25 per completed paid job; founding contractors $0 for 12 months after it |
| 3 | Guarantee clock | 90 minutes from the member's request text (there is no confirming text). Everything else in decision 3 stands: fault-based, the $99 trip charge back automatically, covered areas and hours on the membership page, no acceptance told within 15 minutes and nothing charged |
| 6 | Payments | Stripe Connect: the card saved at joining and billed monthly or annually; the trip charge authorized on the card on file when the request text arrives, captured at acceptance, held, released on arrival; payout within 2 business days of arrival |
| 8 | Safety | "customer" becomes "member"; a text from a non-member gets the same safety reply (R57) |
| 11 | Paid search | Sells memberships before the need, never dispatch during an emergency: standard Google search ads after Google's written confirmation; never Local Services Ads; emergency dispatch searches are negative keywords; Microsoft Ads alongside |
| 12 | Acquisition ceiling (replaces the paid search ceiling per paid job) | About $43 per new paid member, by channel and zone, reviewed weekly: the first 6 months of contribution on the monthly plan (R63). Replaces $275, $192, and $137 per paid job |

New values R51 to R64 (prices, what membership includes, joining, when memberships open, cancelling and renewal, a text from a non-member, requests per member, churn, renewal, the affiliate commission, the member referral reward, the acquisition ceiling, the member base per zone); R02 and R30 retired; R01, R06, R09, R11, R15 to R19, R21, R23 to R25, R31, R32, R34, R39, R42, R43, R46, R49, and R50 revised (`reference/resolution-register.md`). Vocabulary: "member" for the demand side, "homeowner" before joining; "an SOS SMS member" in contractor copy, where a contractor's own clients stay "your customers".

**Rationale:** the product thesis is readiness. An emergency should take one text, which is only possible when the card and address went on file before anything broke; and a homeowner reached before the need, through a partner or an email, costs less than one bought at the moment of the emergency, when a contractor from the search results is the faster route anyway. The membership funds the network on the demand side; the contractor side stays free to join. The economics and the channel limits are in `reference/pricing-and-economics.md` and `reference/channel-engine-members.md`.
**What this does not change:** the contractor side, entirely: free to join, $0 per request, the trip charge collected before the contractor rolls and released on arrival, the founding terms and the $25 contractor fee after the founding period, the contractor channels, the density model and the gate (supply leads; memberships open only at the density number, for covered hours), and Run 1's ICP, journey, and value proposition beyond the lines that describe the other side. Also unchanged: decisions 1, 4, 5, 7, 9, and 10; the safety line; the claim ledger's narrowed forms; product-led with no sales team; two sides never blended; the brand (round is always the member side, square always a contractor); and the pre-launch rules (nothing live, no invented number, planning values labelled, merge fields).
**Downstream:** done 2026-10-11 in this repository: every `rules/` file, the master context (v1.4), `reference/` (the member value proposition and channel engine renamed to `value-proposition-members.md` and `channel-engine-members.md`), `templates/` (the membership page, the first reply and welcome texts, sign-up ads, problem and prevention guides, the new affiliate kit and member email), `examples/`, `pages/`, `ops/`, `prompts/`, `adapters/`, the routers, and a snapshot. In `Fit137/SOSSMSGTMBuild`: `gtm/` (both runs, the research with sources S75 to S94, the marketplace files, the pricing model), the Google folder, and the deck handoff. In the walkthrough deck: the knowledge copy, the specs, the dashboards, and the build. The Miro board is updated from a prompt handed to the consultant (no access from here).

## 2026-10-04 Every unknown and founder decision resolved (DECIDED)
At the user's instruction ("The final walkthrough and every deliverable we have shouldn't include any TBDs or decisions left for the founder. Everything should be resolved"), the GTM consultant resolved every former unknown and every founder decision, from public data, the research, and the GTM itself. Each value is now decided, a planning value with its basis, counted at a named stage, or a `{{merge field}}` (`reference/resolution-register.md`, R01 to R50). Nothing that cannot exist before launch is guessed: results, arrival times, and counts are resolved to how and when they are counted.

**Rationale:** copy that waited on decisions could not ship, and every value needed for launch can be set from the research and the pricing model. Planning values are labelled, so no planning number is ever mistaken for a result.
**What this does not change:** nothing is live; no customer, contractor, job, testimonial, or result exists; grade C figures stay internal; contractor recruiting copy stays in the future tense; customer copy stays held until its zone opens.
**Downstream:** every file in `rules/`, the master context, `reference/`, `templates/`, `examples/`, `adapters/`, and `tools/check_sos_sms.py` (which now fails on any placeholder); the GTM build repo, the Google folder, and the walkthrough deck. Done 2026-10-04.

## 2026-10-03 The twelve decisions (DECIDED)

| # | Decision | Decided |
|---|---|---|
| 1 | Launch metro, first zone, trades | The United States; the founders' home metro; one founding zone, a 10-mile radius around the founding contractors' shops; plumbing and water emergencies first |
| 2 | Revenue model | Revised 2026-10-11 (above): members pay a membership; the SOS SMS fee is retired. As decided 2026-10-03: customer: a $49 SOS SMS fee per dispatched request. Contractors: $0 to join, $0 per request seen or declined, no subscription; $0 a job in the founding period (the zone's first 6 months open), then $25 per completed paid job, deducted from the payout; founding contractors keep $0 a job for 12 months after it. No share of the repair |
| 3 | Late-arrival rule and guarantee scope, together | Clock revised 2026-10-11 (above): 90 minutes from the member's request text. As decided 2026-10-03: fault-based (option C); acceptance only with an arrival time inside the remaining window; 90 minutes from the customer's confirming text; the $99 trip charge back automatically, from the contractor's trip charge when they missed their time, from SOS SMS when SOS SMS caused the miss; covered areas and hours named on the zone page; with no acceptance, the customer is told within 15 minutes and pays nothing |
| 4 | Dispatch rule, and what contractors see first | All matched at once; first to accept with an arrival time inside the remaining window; the problem, photos or video, and an approximate distance and cross-street area before accepting; the address only to the contractor who accepts |
| 5 | Who sets the trip charge | SOS SMS, one per trade and zone: $99 for plumbing in the founding zone, day or night, credited to the repair |
| 6 | Payments | Revised 2026-10-11 (above): the card on file. As decided 2026-10-03: Stripe Connect: authorize at the confirming text, capture at acceptance, hold, release on arrival; payout within 2 business days of arrival |
| 7 | Verification recheck cadence | At sign-up, every 6 months, and on each policy's expiry date; the same words on both sides |
| 8 | Safety handling | Gas, smoke, fire, injury: the safety reply first; no broadcast until the customer confirms they are safe and the utility or 911 has been called |
| 9 | Carrier registration | One local number in the launch metro's area code, registered for A2P 10DLC before any test text (S32) |
| 10 | Name collision | US trademark search and search check in the zone in Stage 0; the full name always; no bids on "SOS plumbing" |
| 11 | Paid search eligibility | Revised 2026-10-11 (above): ads sell memberships before the need. As decided 2026-10-03: standard Google search ads only, after Google's written confirmation; never Local Services Ads; message assets only once verified; Microsoft Ads alongside (S70 to S72, S74) |
| 12 | Paid search ceiling per zone | Replaced 2026-10-11 (above) by the acquisition ceiling per new paid member. As decided 2026-10-03: $275 per paid job while proving; $192 by the end of month 6; $137 by the end of month 12 |

**Rationale:** the GTM consultant's resolution at the user's instruction, from the research, both runs, the cross-side check, and the pricing model (basis per decision in `sources/raw/gtm/marketplace/resolution-register.md`).
**What this does not change:** nothing is live. The guarantee, the fees, and the payout are launch-day terms, held in customer copy until the zone opens (member copy, since 2026-10-11).
**Downstream:** done 2026-10-04 (entry above).

## 2026-10-03 Pricing direction: contractors join free, SOS SMS earns on transactions (DECIDED with decision 2)
**Revised 2026-10-11 by the membership revision (above):** SOS SMS earns on members' monthly or annual fees instead of a fee per request; the contractor half of this direction stands unchanged.

The GTM consultant set the direction for the pricing model: the lowest barrier of entry for contractors, and revenue from transactions, not from joining. Contractors pay $0 to join, $0 per request seen or declined, and no subscription or seat fee. SOS SMS earns an SOS SMS fee on each customer request, and a contractor fee per completed paid job once the founding period ends; founding contractors keep $0 a job for a held period after it. Decision 2 took this direction the same day.

**Rationale:** supply is the constrained side and every customer promise depends on density, so contractors are subsidized; the customer pays for speed and the guarantee. A customer fee alone does not pay back paid search on the first job, so the contractor fee after the founding period is planned from the start (`reference/pricing-and-economics.md`).
**What this does not change:** grade C figures stay internal. No claim, channel, or status changes. The amounts became decided with decisions 2 and 5 (above).
**Downstream:** `reference/pricing-and-economics.md` (the price points), `rules/do-not-say.md` (the two lines are never merged into one total), `adapters/portable-control-layer.md`, `ops/asset-index.md`; the pricing model and handoff in `Fit137/SOSSMSGTMBuild` (`google-folder/SOS_SMS_Pricing_Model.xlsx`, `gtm/pricing/pricing-handoff.md`). Done 2026-10-03.

## 2026-10-03 Pre-launch framing for contractor recruiting (DECIDED, build rule)
Contractor recruiting copy goes out before launch and describes what SOS SMS is building, in the future tense ("when it opens in {{zone}}"). Customer copy stays held until the zone opens.
**Revised 2026-10-11 by the membership revision:** on the member side, the readiness scorecard, prevention guides, the affiliate signing, and the launch list go out from Stage 1, in the same future tense and promising no service; membership copy stays held until memberships open in the zone (R55).

**Rationale:** the live test (`pages/partner-counter-card.md`) found that "held until it ships" and Stage 1 recruiting before launch could not both be followed. This is a wording rule derived from decided strategy (supply first, pre-launch), not a new strategic choice.
**What this does not change:** no claim, no number, no channel. Nothing is described as live.
**Downstream:** `rules/writing-rules.md`, the master context Section 0, `ops/QA-checklist.md`, `adapters/portable-control-layer.md`. Done 2026-10-03.

## 2026-10-02 Built the GTM brain from both runs and the walkthrough (DECIDED)
This repository is the single source of truth for SOS SMS go-to-market work. Where a source and the brain disagree, the brain records the conflict and the decided verdict wins.

**What this does not change:** no strategy, claim, or number.

## 2026-10-01 Brand identity v1: green and white (DECIDED)
Logo, mark (round customer, square contractor; round is the member since 2026-10-11), Inter, the twelve colour roles, and the brand book, built in the walkthrough repo at the user's request. The dark (projector) palette is kept as validated (2026-10-04): three roles sit brighter than the chart band so every role clears 5:1 on the dark surface.

**What this does not change:** the voice rules, and the rule that the name is always SOS SMS.

## 2026-10-01 Product-led motion, no sales team (DECIDED)
No calls, demos, meetings, shop visits, or audits on either side. Contractors: cold email, a partnership program, an in-product referral loop, self-serve sign-up by text. Customers: bottom-of-funnel paid search (Google, then Microsoft), problem-solving pages, product loops. No outreach to homeowners. The white-glove audit became the automated lead spend report.

**Rationale:** the founders chose it after the first runs; paid search sits where emergency demand already searches, and a text-only product can convert without people.
**Revised 2026-10-11 by the membership revision:** the demand side is reached before the need, through affiliates and email first; search and social sell sign-ups in open zones; outreach to homeowners stays out, and partners join an affiliate program rather than being sold to.
**What this does not change:** the two-run structure, supply first, the claim ledger.
**Downstream:** stale lines in two sources still mention calls (`reference/lead-magnets.md`, source conflict). This entry governs.

## 2026-10-01 Two runs, never blended (DECIDED)
One value proposition, ICP, journey, and channel plan per side. No asset speaks to both.

## 2026-10-01 Supply leads, demand follows, zone by zone (DECIDED)
Demand opens only at the density number, for covered hours. Paid search is geofenced and scheduled to match. Since 2026-10-11: memberships open per zone at the density number; before then, the launch list (R55).

## 2026-10-01 Where SOS SMS fights (DECIDED)
Contractors: no charge for requests that never become work; paid to show up. Customers: a guaranteed arrival window; many contractors reached with one reply. Since 2026-10-11, members: one text with a money-backed arrival window; many contractors reached with one reply. Do not contest volume, exclusivity, repair coverage, brand familiarity, or guarantees on the work.

## 2026-10-01 Claims follow the narrowed forms; nothing invented (DECIDED)
Every source "only" and "unique" was narrowed or dropped. No result exists before launch: social proof is the method line and proof is the named record (R44, R45) until permissioned results exist.

## 2026-10-01 Speed only inside proven zones (DECIDED)
Accept inefficiency in proving zones; never trade claim accuracy, safety, payouts, refunds, privacy, or law. Zone thresholds are set before launch (R32).

## Closed 2026-10-04 (formerly open, owned elsewhere)
- **Customer data rule:** name, address, phone, and photos go to the accepting contractor only (decision 4); no marketing texts without a separate written opt-in (S31). Decided in the Run 2 brief.
- **Demand-side scope:** homeowners. Property managers would be a third run (Run 2 brief).
- **Build status of every capability:** every capability is PLANNED, built in Stage 0 or at its named stage, and claimable only once it ships (`rules/feature-status.md`).
- **The founder memo and unattributed matrix rows:** excluded for good (R26).
- **Dispute rules:** founders handle each dispute by text in Stage A, decided from the request log (the request text, acceptance, committed arrival time, arrival; the confirming text until 2026-10-11); written rules and a queue before scaling (speed-to-scale plan, operations table).
- **Founder roles, team, runway, channels tried:** a supply lead and a demand lead (R25); at least 18 months of runway at Stage A spending (R35); no channels tried before launch (R48).
- **Customers without a card (conflict D)** and **first refusal on a contractor's own customers (conflict E):** R16 and R13.
- **Walkthrough deck:** the Vercel config is checked on the first deploy, with Deployment Protection on; S08 has 6 bands.
- **Review cadence and corroboration thresholds:** adopted as set in `review-cadence.md`.

## Numbering crosswalk
Run 1 brief: 1 metro = 1; 2 revenue = 2; 3 late arrival = 3; 4 dispatch = 4; 7 name collision = 10. Run 2 brief: 2 metro = 1; 3 member price = 2 and 5; 4 guarantee scope = 3; 7 name collision = 10; 8 paid search = 11; 9 the demand-side product (the membership revision, 2026-10-11) = 2.
