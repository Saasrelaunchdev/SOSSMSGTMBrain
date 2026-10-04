# Cross-side check: SOS SMS supply and demand runs

Both briefs end with the same rule: neither side's copy may promise something the other side's terms do not deliver. This file runs that check across both completed runs, row by row against `GTM-BRIEF.md` Section 6, then lists the conflicts the runs uncovered that Section 6 did not anticipate.

Inputs: `../run-1-supply-contractors/output/` and `../run-2-demand-customers/output/`, both 2026-10-01. Every decision in Part 3 was decided on 2026-10-03; the values and their basis are in `resolution-register.md`.

## Part 1. The eight Section 6 rows, after both runs

| # | Customer-side promise | Run 1 (contractors) | Run 2 (customers) | Status | What closes it |
|---|---|---|---|---|---|
| 1 | 90-minute guarantee, refund on a miss | Phase 9 sets a fault-based late-arrival rule (option C): a contractor who misses their own committed time funds the refund from their trip charge; SOS SMS pays for misses it causes | Phase 6 drill 3 states the scope: 90 minutes from the confirming text, the $99 trip charge back, in the zone's covered areas and hours; Phase 9 sizes the fee against SOS-caused misses | **Closed, decision 3** | Option C and the guarantee scope adopted together, with the rule in Part 2, item B: a contractor can never accept with an arrival time outside the window |
| 2 | Relaunch guarantee | Not referenced in any contractor copy | Excluded from all customer copy | **Closed, kept out of copy until built** | SOS SMS pays the second contractor's trip charge from the SOS SMS fee, so the first contractor's guarantee is not affected (resolution register, R17) |
| 3 | One text reaches every matched contractor | Drill 2 states the shared request openly: "Lose the race, lose nothing" | Drill 1: "all at once, the first who can come accepts" | **Consistent** | Dispatch rule decided (decision 4): all matched at once, first to accept |
| 4 | Private by design | Drills 7 and 9 tell contractors they see the problem and any photos before accepting | Drill 5 promises the broadcast carries no name, number, or address until acceptance | **Consistent, decision 4** | Part 2, item C, adopted: contractors see the problem, photos, and an approximate distance, never the address, before acceptance |
| 5 | Trip charge credited to the job | Drill 6 states the obligation to the contractor in the copy itself | Drill 7 promises it to the customer | **Consistent** | Put it in the founding contractor agreement (Run 1 Phase 8) |
| 6 | Known arrival time | Commitment on acceptance, in the terms on one page | Drill 2: "we text you their name and when they'll arrive" | **Consistent** | The terms on one page (Run 1, first asset in production order) |
| 7 | License and insurance verified | Onboarding step (Run 1 Phase 7, stage 4) | Drill 8: checked at sign-up, every 6 months, and on each policy's expiry date | **Closed, decision 7** | The same cadence in both places: at sign-up, every 6 months, and on each policy's expiry date |
| 8 | Zero cost to join | $0 to join and per request; $0 a job in the founding period; then $25 per completed paid job | A $49 SOS SMS fee per dispatched request on the customer side | **Consistent, decision 2** | Decision 2 settled once, for both runs |

## Part 2. Conflicts the runs uncovered

Not in Section 6. Each is a place where one side's plan, as written, would break a promise on the other side.

| # | Conflict | Where it appears | Consequence if ignored | Resolution, decided |
|---|---|---|---|---|
| A | **Who sets the trip charge.** Run 2 recommends one SOS SMS trip charge per trade and zone, so the customer sees one price. Run 1's positioning tells contractors "your price for the work stays yours" | Run 1 Phase 3; Run 2 Phase 9 decision 3 | A contractor who expects to set their own trip charge feels misled | Adopt one trip charge per trade and zone, and say so in the terms on one page. Contractor copy keeps "your price for the work" and never says "your trip charge" |
| B | **Accepting with an arrival time outside the window.** The guarantee runs from the customer's text; a contractor accepting late in the window can only commit to a time past it | Run 1 Phase 9 option C; Run 2 drill 3 | Fault-based refunds become unfair to contractors, or the guarantee breaks at the moment of acceptance | Dispatch only lets a contractor accept with an arrival time inside the remaining window. When no contractor can, the miss is SOS-caused and SOS SMS pays |
| C | **Address before acceptance.** Contractors need to judge distance before they accept; customers are promised that only the accepting contractor gets their address | Run 1 drills 7 to 9; Run 2 drill 5 | Either the privacy promise or the contractor's ability to commit to a time fails | Show an approximate distance or cross-street area before acceptance, the full address after |
| D | **Customers without a card.** Run 2 suggests a pay-on-arrival path for customers who cannot pay by text | Run 2 Phase 9 decision 5; Run 1 VP2 | "Paid to show up" is false for those jobs | No pay-on-arrival path. Dispatch needs a card or a phone wallet through the payment link; without one, the customer gets the free help by text and pays nothing (R16) |
| E | **A contractor's own customers.** Run 2 suggests founding contractors give SOS SMS as their after-hours line; Run 1 promises the customer relationship stays with the contractor | Run 2 Phase 7 acceleration; Run 1 item 7 | A contractor's own customer could be accepted by a rival, which ends that contractor's participation | Do not use this acceleration until dispatch can give the referring contractor first refusal on their own customers' requests for 5 minutes. Until then, drop it |
| F | **Gas and other life-safety texts.** The customer side holds them for the safety reply first | Run 2 rules; Run 1 dispatch | A plumber may be dispatched into a gas leak | Requests mentioning gas, smoke, fire, or injury get the safety reply and are not broadcast until the customer confirms it is safe and the utility or 911 has been called |
| G | **Paid search ahead of density.** Paid search is now the primary customer channel (product-led revision, 2026-10-01) | Run 2 Phase 8 | Ads produce requests nobody can reach in time, and refunds | Geofence campaigns to zones at Run 1's density number and schedule them to covered hours; pause automatically when acceptance falls |
| H | **Payment hold timing.** Run 1 promises the trip charge is collected before the contractor rolls; card authorizations usually last 7 days online (S30) | Run 1 drill 4; Run 2 Phase 7 stage 4 | Mismatch between hold, capture, and payout produces disputes | Stripe Connect: authorize when the customer confirms, capture at acceptance, hold for release on arrival, payout within 2 business days; refunds per the late-arrival rule |

## Part 3. Decisions before launch, both sides, in order

Merged from both briefs' open decisions, Part 2, and the product-led revision (decisions 11 and 12). Each decision is listed once; it unblocks work on both sides. All twelve were decided on 2026-10-03; the basis for each is in `resolution-register.md`.

| # | Decision | Decided | Unblocks |
|---|---|---|---|
| 1 | Launch metro, first zone, and trades | The United States; the founders' home metro; one founding zone, a 10-mile radius around the founding contractors' shops; plumbing and water emergencies | Local research; every Phase 8 asset |
| 2 | Revenue model | A $49 SOS SMS fee per dispatched request; $0 to contractors to join and per request, and $0 a job during the founding period (the founding zone's first 6 months open); then $25 per completed paid job, deducted from the trip charge payout; founding contractors keep $0 a job for 12 months after the founding period. Paid search is not paid back by the customer fee alone (`speed-to-scale-plan.md`, section 5) | Run 1 drills 1 to 3; Run 2 Phase 9 |
| 3 | Late-arrival rule and guarantee scope, together | Fault-based (Run 1 option C) plus Part 2 item B; the 90 minutes start at the customer's confirming text; the refund is the $99 trip charge, automatic; covered areas and hours are the zone's, named on the zone page; with no acceptance, the customer is told within 15 minutes and pays nothing | Run 1 drills 4 and 5; Run 2 drill 3 and the guarantee page |
| 4 | Dispatch rule and what contractors see before accepting | All matched at once, first to accept with an arrival time inside the remaining window; the problem, photos, and an approximate distance, not the address (Part 2 item C); a 10-minute response window | Run 1 drill 2; Run 2 drills 1 and 5 |
| 5 | Who sets the trip charge | SOS SMS, one per trade and zone (Part 2 item A): $99 for plumbing, day or night, credited to the repair | The first reply; the terms on one page |
| 6 | Payment provider, hold, capture, and payout timing | Stripe Connect; capture at acceptance, release on arrival, payout within 2 business days of arrival (Part 2 item H) | Run 1 drill 5; Run 2 Phase 7 stage 4 |
| 7 | Verification and recheck cadence | At sign-up, every 6 months, and on each policy's expiry date; the same value on both sides | Run 1 onboarding; Run 2 drill 8 |
| 8 | Safety handling | Part 2 item F: the safety reply first, no broadcast until the customer confirms they are safe | Both sides' first messages |
| 9 | Carrier registration of the SOS SMS number | One local number in the launch metro's area code, registered for A2P 10DLC before any test (S32) | Every text on both sides |
| 10 | Name collision | A US trademark search and a search check in the zone, in Stage 0, before any ad, page, or email | Every ad, page, and email |
| 11 | Paid search eligibility | Standard search ads only, after Google confirms in writing that a dispatch service may run them for plumbing; never Local Services Ads (S70, S71); message assets only with verified business details (S72) | Run 2 Phase 8, Channel 1 |
| 12 | Paid search ceiling per zone | $275 per paid job while proving a zone, falling to $192 by the end of month 6 and to $137 by the end of month 12 | Run 2 Phase 9; `speed-to-scale-plan.md`, section 8 |

## Result

All eight Section 6 rows are consistent or closed: rows 1 and 7 closed with decisions 3 and 7, not rewrites, and row 2 stays out of copy until the relaunch is built. The eight conflicts in Part 2 are resolved, each keeping both sides' copy as written in Phase 6. With the twelve decisions made, every line that waited on one carries the decided words; contractor recruiting copy stays in the future tense, and customer copy stays held until its zone opens.
