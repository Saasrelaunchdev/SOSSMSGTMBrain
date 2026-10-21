# Launch sequence: how the two GTMs fit together

The order the two GTMs execute in, and the gates between steps. Revised 2026-10-01 for the product-led motion: no sales team, contractors sign themselves up after cold email or a partner. Revised 2026-10-11, the membership revision: homeowners join as members before anything breaks, reached through affiliates and email first, with search and social for sign-ups, and a member's one text starts dispatch. Revised 2026-10-20, the tiers revision: one membership covers plumbing, HVAC, and electrical, so supply fills all three trades before a zone opens; members choose Basic, Plus, or Premier; no paid search at launch, so affiliates, email, and paid social carry sign-ups. Every element comes from the run outputs or from `speed-to-scale-plan.md`, cited by phase.

The organizing rule from both runs: **supply leads, memberships follow, zone by zone.** The member side's headline promises are only true where the contractor side has reached density (Run 1 Phase 5; Run 2 Phase 5), so memberships open only where they are true (R55). Before then, the zone's launch list grows: email, no charge, no service promised.

## Stage 0. Decisions and plumbing (both sides)

| Work | Source | Gate to leave this stage |
|---|---|---|
| Write the twelve decisions (decided 2026-10-03, revised 2026-10-11 and 2026-10-20, `cross-side-check.md` Part 3) into the member terms, the guarantee on Plus and Premier, the terms on one page, and the contractor agreement | `resolution-register.md` | Each decision appears, in the same words, in every document that carries it |
| Load the decided prices into billing: Basic $10 a month and $100 a year, Plus $15 and $150, Premier $35 and $350, Plus on the annual plan shown first (R51, R52, R65, R66, R19) | Run 2 Phase 9; the pricing model | All six prices billable in a test |
| Membership billing: card on file with an optional backup card, monthly and annual billing, the 30-day start of dispatch on the monthly plan (R54), upgrades and downgrades (R54), the late-arrival credit applied to the next bill on Plus and Premier (R65), Premier's covered trip charge after 6 paid months on monthly (R66), renewal reminders before `{{renewal date}}`, failed payments retried for 7 days and then paused, cancel any time on the membership page or by texting HELP, no partial refunds (R56) | Run 2 Phase 9; decision 6 | A test member on each plan joined, billed, upgraded, credited, reminded, paused after a failed payment, and cancelled |
| Counsel review of the member terms: the automatic renewal disclosures, the 30-day start on the monthly plan, the late-arrival credit, and the no-partial-refund term | Run 2 Phase 8 (S87) | Counsel-reviewed |
| The affiliate program terms: the disclosure every affiliate makes, the $20 commission paid once the member's second monthly payment or first annual payment clears, and no payments at a home purchase settlement (R61) | Run 2 Phase 8 (S86, S88, S94) | Counsel-reviewed; the affiliate program page and the kit ready |
| Start signing affiliates for the launch zone, fastest categories first (local publications and newsletters, home content creators, associations, retailers); utilities, cities, and employers in parallel, never on the critical path (R25) | Run 2 Phase 8, Channel 1 | Partners signing; codes issued as each signs |
| Email sending setup for the launch list and member email | Run 2 Phase 8 (S73) | A test send with the postal address and a working opt-out |
| Set up paid social for sign-ups before the need, limited to the launch zone's map, paused with sign-ups (R34); no paid search at launch (decision 11) | Run 2 Phase 8, Channel 3 | Audiences built; nothing runs before the zone opens |
| Register the SOS SMS number for A2P 10DLC: one local number in the launch metro's area code (decision 9) | Run 2 Phase 7 blocker (S32) | Test texts deliver on the three major carriers |
| Set up Stripe Connect: the card saved at joining, with the backup card tried on a decline; the trip charge authorized when a member's request text arrives, captured at acceptance, released on arrival; payout within 2 business days, less the $25 contractor fee; no dispatch without an authorized trip charge (decision 6, R16) | Cross-side check, item H | A test trip charge authorized, captured, held, released, and paid out; a declined card stops dispatch and starts it again on authorization |
| Build the self-serve paths: contractor sign-up by text; joining on the membership page or from Text READY; the welcome texts; the first reply to a request text with the first steps for the problem; NEXT after a miss (R17); the reply to a non-member (R57); the safety reply for gas, smoke, fire, sparks, a burning smell, a shock, or injury (decision 8) | Run 1 Phase 8; Run 2 Phase 8 | All tested end to end with no person involved |
| Write the terms on one page (contractor, with the late-arrival rule, R67), the membership page with the three plans, and the guarantee in full (member, Plus and Premier) | Run 1 Phase 8; Run 2 Phase 8 | Counsel-reviewed; every Phase 6 drill carries the decided terms |
| Put the zone signal thresholds (R32) into the weekly review before launch | `speed-to-scale-plan.md`, section 3 | Thresholds written down and visible to both founders, so results cannot be argued after the fact |
| Draw the launch zone (a 10-mile radius around the first contractors' shops in the founders' home metro) and run its local research; count licensed plumbing, HVAC, and electrical businesses from the state license lists and owner-occupied homes from Census tract data | `../research/step-0-competitor-slates.md`, local list | Local slate recorded |

## Stage 1. Supply fills the launch zone; the launch list grows

| Work | Source | Measure |
|---|---|---|
| Build the zone contractor list in all three trades; send cold emails 1 to 4 | Run 1 Phase 8, Channel 1 (S73) | Lead Cost Checks completed; contractor page visits; JOIN texts |
| Sign one supply house per trade and the local association chapters (PHCC, ACCA, NECA or IEC) to the partnership program | Run 1 Phase 8, Channel 2 | Sign-ups per partner code |
| Self-serve sign-up by text, with the agreement and permission clause | Run 1 Phase 7 stage 4 | Verified, payout-ready, available contractors per trade |
| Measure acceptance with test requests by trade and hour band | Run 1 Phase 5 density model | Acceptance rate per trade and hour band; recompute the density number |
| In parallel: the readiness scorecard, the first prevention guides, and the launch list sequence | Run 2 Phase 8, Channels 2 and 3 | Launch list joins in the zone; no charge, no service promised |
| In parallel: more affiliates signed for the zone, with codes ready before it opens | Run 2 Phase 8, Channel 1 | Partners signed; codes issued |

**Gate to Stage 2:** the density number is met for each of the three trades, in the first zone, in every hour band, every day: 27 places in the first cohort (R08, R15, R55). The zone opens at that point, whether or not a utility or city has signed.

## Stage 2. Memberships open in the zone

| Work | Source | Measure |
|---|---|---|
| The opening email to the zone's launch list | Run 2 Phase 8, Channel 2 | New paid members from the launch list |
| Affiliates go live with their codes | Run 2 Phase 8, Channel 1 | New paid members and commissions by code |
| The membership page with the ZIP check, the guarantee page, and the first five problem and prevention guides | Run 2 Phase 8, Channel 3 | ZIP checks; membership page to join rate |
| The welcome texts, the first-steps reply, the reply to a non-member, automatic credits and no-show refunds | Run 2 Phase 8, member loops | Time from request text to acceptance; credits applied without being asked |
| Member loops: the contact card, the forwardable card, Text READY, the two questions after a job | Run 2 Phase 8, member loops | Referrals per member |
| Paid social for sign-ups, limited to the zone's map; no paid search at launch (decision 11) | Run 2 Phase 8, Channel 3 | Cost per new paid member against the plan's ceiling, about $47 Basic, $70 Plus, $151 Premier (R63) |

**Measures watched weekly, both sides together:**

| Measure | Side | Why it matters |
|---|---|---|
| Active contractors per trade, zone, and hour band against the density target | Supply | Decides whether sign-ups stay open in the zone (R34) and which hour bands recruiting serves first |
| Time from the request text to acceptance, by trade; share with no acceptance in time | Both | What the arrival time is worth |
| Share arriving within the window; late arrivals and no-shows per 100 accepted requests | Both | Prices the late-arrival credit on Plus and Premier (R29) |
| Cost per new paid member by channel and plan; the plan mix; members against about 410 (R64) | Members | Decides which channels grow (speed-to-scale plan, section 5) |
| Monthly churn; annual renewal | Members | Decides what a member is worth, and so the ceiling (R59, R60, R63) |
| Days to first paid trip; share of trips paid before rolling | Supply | Keeps contractors active (Run 1 Phase 7) |

## Stage 3. Prove the zone, then accelerate

Use the gates in `speed-to-scale-plan.md`, section 8:

1. **Zone proven:** every zone signal at its threshold for 4 consecutive weeks. Then raise affiliate and paid social spend in the zone while cost per new paid member holds under the ceiling and acceptance holds in every trade and hour band. Count search volume for SOS SMS by name once the zone has been open 6 months (R68).
2. **Zone full:** every trade and hour band holding the density number and members growing toward about 410 (R64). Then open the adjacent zone from the template: contractor list and emails, partner kit, launch list, affiliates, membership page.
3. **Metro proven:** three zones pass without founders stepping in. Then a second metro.
4. **Trade added:** plumbing, HVAC, and electrical density hold and a referred trade (water damage, then locksmith) reaches its own density. Then a fourth trade behind the same membership.

**Slow down** in any zone when late arrivals, acceptance, monthly churn, cost per new paid member, or contractor activity cross their thresholds. Sign-ups pause automatically when acceptance in any trade falls: paid social stops and affiliate links show the launch list (R34).

## What would change this sequence

| If the plan changes to | Then |
|---|---|
| Memberships first, recruiting contractors to meet them | The arrival time and the guarantee on Plus and Premier cannot launch with memberships, and members would pay for a promise nobody can keep. Launch Basic only and rewrite Run 2 Phase 6 VP1 |
| Opening a zone with plumbing alone | Members pay for three trades they cannot all use; sell the membership as plumbing only in that zone and rewrite the membership page |
| Paid search at launch | Each zone needs Google's written confirmation that SOS SMS may advertise its membership (S70, S71), and measured cost must sit under the plan's ceiling, about 3 times lower than the benchmark (decision 11) |
| Property managers as a demand segment | A third run, with a B2B buying committee and contracted-vendor competitors |
