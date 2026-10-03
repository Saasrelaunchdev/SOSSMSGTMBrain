# Cross-side check: SOS SMS supply and demand runs

Both briefs end with the same rule: neither side's copy may promise something the other side's terms do not deliver. This file runs that check across both completed runs, row by row against `GTM-BRIEF.md` Section 6, then lists the conflicts the runs uncovered that Section 6 did not anticipate.

Inputs: `../run-1-supply-contractors/output/` and `../run-2-demand-customers/output/`, both 2026-10-01.

## Part 1. The eight Section 6 rows, after both runs

| # | Customer-side promise | Run 1 (contractors) | Run 2 (customers) | Status | What closes it |
|---|---|---|---|---|---|
| 1 | 90-minute guarantee, refund on a miss | Phase 9 recommends a fault-based late-arrival rule (option C): a contractor who misses their own committed time funds the refund from their trip charge; SOS SMS pays for misses it causes | Phase 6 drill 3 keeps the scope in brackets; Phase 9 sizes the fee against SOS-caused misses | **Open, but the two runs fit together** | Adopt option C and the guarantee scope together. Add the rule in Part 2, item B, so a contractor can never accept with an arrival time outside the window |
| 2 | Relaunch guarantee | Not referenced in any contractor copy | Excluded from all customer copy | **Parked** | Before building: decide who pays the second contractor's trip charge. Recommended: SOS SMS, from the fee, so the first contractor's guarantee is not affected |
| 3 | One text reaches every matched contractor | Drill 2 states the shared request openly: "Lose the race, lose nothing" | Drill 1: "all at once, the first who can come accepts" | **Consistent** | Confirm the dispatch rule (Run 1 open decision 4) |
| 4 | Private by design | Drills 7 and 9 tell contractors they see the problem and any photos before accepting | Drill 5 promises the broadcast carries no name, number, or address until acceptance | **Consistent if one design decision is made** | Part 2, item C: show contractors the problem, photos, and an approximate distance, never the address, before acceptance |
| 5 | Trip charge credited to the job | Drill 6 states the obligation to the contractor in the copy itself | Drill 7 promises it to the customer | **Consistent** | Put it in the founding contractor agreement (Run 1 Phase 8) |
| 6 | Known arrival time | Commitment on acceptance, in the terms on one page | Drill 2: "we text you their name and when they'll arrive" | **Consistent** | The terms on one page (Run 1, first asset in production order) |
| 7 | License and insurance verified | Onboarding step (Run 1 Phase 7, stage 4) | Drill 8, with a recheck cadence in brackets | **Open** | Set the recheck cadence; the same value goes in both places |
| 8 | Zero cost to join | Run 1 recommends $0 to contractors, any future fee per completed paid job only | Run 2 recommends a per-request SOS SMS fee on the customer side | **Consistent if the founders adopt both recommendations** | Settle open decision 2 once, for both runs |

## Part 2. Conflicts the runs uncovered

Not in Section 6. Each is a place where one side's plan, as written, would break a promise on the other side.

| # | Conflict | Where it appears | Consequence if ignored | Recommended resolution |
|---|---|---|---|---|
| A | **Who sets the trip charge.** Run 2 recommends one SOS SMS trip charge per trade and zone, so the customer sees one price. Run 1's positioning tells contractors "your price for the work stays yours" | Run 1 Phase 3; Run 2 Phase 9 decision 3 | A contractor who expects to set their own trip charge feels misled | Adopt one trip charge per trade and zone, and say so in the terms on one page. Contractor copy keeps "your price for the work" and never says "your trip charge" |
| B | **Accepting with an arrival time outside the window.** The guarantee runs from the customer's text; a contractor accepting late in the window can only commit to a time past it | Run 1 Phase 9 option C; Run 2 drill 3 | Fault-based refunds become unfair to contractors, or the guarantee breaks at the moment of acceptance | Dispatch only lets a contractor accept with an arrival time inside the remaining window. When no contractor can, the miss is SOS-caused and SOS SMS pays |
| C | **Address before acceptance.** Contractors need to judge distance before they accept; customers are promised that only the accepting contractor gets their address | Run 1 drills 7 to 9; Run 2 drill 5 | Either the privacy promise or the contractor's ability to commit to a time fails | Show an approximate distance or cross-street area before acceptance, the full address after |
| D | **Customers without a card.** Run 2 suggests a pay-on-arrival path for customers who cannot pay by text | Run 2 Phase 9 decision 5; Run 1 VP2 | "Paid to show up" is false for those jobs | If offered, these requests are labeled "pay on arrival, no trip charge collected" and go only to contractors who opt in. Customer copy states the guarantee does not apply |
| E | **A contractor's own customers.** Run 2 suggests founding contractors give SOS SMS as their after-hours line; Run 1 promises the customer relationship stays with the contractor | Run 2 Phase 7 acceleration; Run 1 item 7 | A contractor's own customer could be accepted by a rival, which ends that contractor's participation | Do not use this acceleration until dispatch can give the referring contractor first refusal on their own customers' requests for a set time ({TBD} minutes). Until then, drop it |
| F | **Gas and other life-safety texts.** The customer side holds them for the safety reply first | Run 2 rules; Run 1 dispatch | A plumber may be dispatched into a gas leak | Requests mentioning gas, smoke, fire, or injury get the safety reply and are not broadcast until the customer confirms it is safe and the utility or 911 has been called |
| G | **Paid search ahead of density.** Paid search is now the primary customer channel (product-led revision, 2026-10-01) | Run 2 Phase 8 | Ads produce requests nobody can reach in time, and refunds | Geofence campaigns to zones at Run 1's density number and schedule them to covered hours; pause automatically when acceptance falls |
| H | **Payment hold timing.** Run 1 promises the trip charge is collected before the contractor rolls; card authorizations usually last 7 days online (S30) | Run 1 drill 4; Run 2 Phase 7 stage 4 | Mismatch between hold, capture, and payout produces disputes | Capture at acceptance, hold for release on arrival; refunds per the late-arrival rule. Confirm with the payment provider |

## Part 3. Decisions before launch, both sides, in order

Merged from both briefs' open decisions, Part 2, and the product-led revision (decisions 11 and 12). Each decision is listed once; it unblocks work on both sides.

| # | Decision | Recommended | Unblocks |
|---|---|---|---|
| 1 | Launch metro, first zone, and trades | One zone in one metro; plumbing and water emergencies | Local research; every Phase 8 asset |
| 2 | Revenue model | Customer-side per-request fee; $0 to contractors during the founding period, then a per-completed-job contractor fee below Run 1's ceiling, because paid search is unlikely to be paid back by the customer fee alone (`speed-to-scale-plan.md`, section 5) | Run 1 drills 1 to 3; Run 2 Phase 9 |
| 3 | Late-arrival rule and guarantee scope, together | Fault-based (Run 1 option C) plus Part 2 item B; clock starts at the customer's text; refund equals the trip charge | Run 1 drills 4 and 5; Run 2 drill 3 and the guarantee page |
| 4 | Dispatch rule and what contractors see before accepting | All matched at once, first to accept; approximate distance, not address (Part 2 item C) | Run 1 drill 2; Run 2 drills 1 and 5 |
| 5 | Who sets the trip charge | One per trade and zone, set by SOS SMS (Part 2 item A) | The first reply; the terms on one page |
| 6 | Payment provider, hold, capture, and payout timing | Capture at acceptance, release on arrival, payout as fast as the provider allows (Part 2 item H) | Run 1 drill 5; Run 2 Phase 7 stage 4 |
| 7 | Verification and recheck cadence | {TBD}; the same value on both sides | Run 1 onboarding; Run 2 drill 8 |
| 8 | Safety handling | Part 2 item F | Both sides' first messages |
| 9 | Carrier registration of the SOS SMS number | Register before any test (S32) | Every text on both sides |
| 10 | Name collision | Trademark and search check in the zone | Every ad, page, and email |
| 11 | Paid search eligibility | Confirm with Google in writing that a dispatch service may run standard search ads for plumbing; Local Services Ads are closed to this model (S70, S71); verify message assets (S72) | Run 2 Phase 8, Channel 1 |
| 12 | Paid search ceiling per zone | {TBD}: the highest blended cost per paid job accepted while proving a zone, and the date it must fall by | Run 2 Phase 9; `speed-to-scale-plan.md`, section 8 |

## Result

Six of the eight Section 6 rows are consistent or parked. Rows 1 and 7 are open but compatible: they close with decisions, not rewrites. The eight new conflicts in Part 2 all have recommended resolutions that keep both sides' copy as written in Phase 6. Copy on either side stays held until the brackets it carries are filled by the decisions in Part 3.
