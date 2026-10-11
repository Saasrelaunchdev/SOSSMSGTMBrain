# Phase 8. Assets and Collaterals Library Dashboard, member side

Revised 2026-10-11, the membership revision. Homeowners join before the need, so SOS SMS meets them where they already trust someone, through partners and email, long before anything breaks. Search and social sell sign-ups in open zones, never dispatch during an emergency. No sales team and no calls to households: partners join an affiliate program, and the product does the converting.

## The three channels

<!-- sheet: Channel_Choice -->
| Skill default | Used for SOS SMS | Why |
|---|---|---|
| LinkedIn Ads | 1. Affiliates, before the need | Partners who already reach homeowners pass SOS SMS on with a code and a disclosed commission per new paid member (R61): utilities and cities, homeowner and neighborhood associations, local publications and newsletters, home content creators, home improvement retailers, insurance agents for existing policyholders, and employers' benefit platforms. The partner-led model already reaches millions of households (S93) |
| Cold email | 2. Email, before the need | SOS SMS's own homeowner list, built from the readiness scorecard and the launch list; partner sends; member email (welcome, seasonal notes, renewal). It reaches people before the need, at almost no cost per send (CAN-SPAM, S73) |
| LinkedIn outreach | 3. Search and SEO pages, for sign-ups | Prevention and problem guides read before the need, the membership page, and zone pages; paid search (Google, then Microsoft) and paid social for sign-ups, geofenced to open zones, with no retargeting and no pixels |

Plus the **member loops**: the saved contact card, Text READY, the forwardable card, the two questions after a job, and renewal.

**What was dropped, and why.** Ads that sell dispatch during an emergency: a homeowner searching mid-emergency is better served by calling a contractor from the results than by joining anything, so search sells memberships before the need instead (decision 11, revised 2026-10-11). Also out: sales calls, demos, meetings, and door-to-door; marketing texts without written consent (S31); retargeting and ad pixels; Local Services Ads (S70); payments to anyone referring at a home purchase settlement (RESPA, S86, S94); LinkedIn.

### Rules for affiliates

<!-- sheet: Affiliate_Rules -->
| Rule | Detail |
|---|---|
| Zones first | Every affiliate link lands on the ZIP check: in an open zone, the membership; in a zone not yet open, the launch list; outside, the readiness steps alone. Partners are signed for a zone before it opens, with codes ready |
| A disclosed commission | $20 per new paid member, paid after the member's first paid month (planning value, R61). Every affiliate discloses that they are paid, clearly and next to the mention (FTC Endorsement Guides, S88) |
| No payment at a home purchase | No commission, fee, or thing of value to a real estate agent, lender, title or settlement agent, or anyone referring at a home purchase settlement (RESPA Section 8, S86, S94). They may share SOS SMS without payment |
| Insurance agents | Commission only for existing policyholders, outside any home purchase settlement; hazard insurance is a settlement service (S94) |
| The kit | Each affiliate gets one kit: a paragraph, how it works in one text, the prices as merge fields, the guarantee with its scope, the safety line, the disclosure line, and what not to claim |
| Claims | Affiliates use the kit's words only: never "covers repairs", "warranty", or "insurance"; no "24/7" without the zone's hours; no arrival averages |

### Rules for email

<!-- sheet: Email_Rules -->
| Rule | Detail |
|---|---|
| Identity and opt-out | Every email carries the full name SOS SMS, a valid postal address, and an opt-out honored within 10 business days (CAN-SPAM, S73) |
| The launch list | Joining it charges nothing and promises no service. When memberships open in its zone, the opening email goes to the launch list first |
| Member email | The welcome, seasonal notes (opt-in), and the renewal reminder before {{renewal date}} (R56) |
| Partner sends | A partner's email to its own list uses the kit's words and carries the partner's disclosure (S88) |
| Not by text | Marketing goes by email. A marketing text needs separate written consent (S31); transactional texts stay transactional |

### Rules for paid search

<!-- sheet: Paid_Search_Rules -->
| Rule | Detail |
|---|---|
| Density first | Ads run only in open zones, where Run 1's density number is met (R55). Acceptance below 90 percent over 7 days pauses sign-ups in the zone automatically: ads stop and affiliate links show the launch list (R34) |
| Sign-ups, never dispatch | Ads sell the membership before the need. No ad offers dispatch during an emergency, and emergency dispatch searches are negative keywords (decision 11) |
| Local Services Ads are not an option | Google's Local Services policy bars reselling leads and re-routing requests to businesses not listed in the ad (S70) |
| Standard search ads | Plumbing is not on Google's US list of restricted local services (S71; locksmith and garage door are). Confirm with Google, in writing, that SOS SMS may advertise its membership this way before spending (decision 11) |
| Never pose as the plumber | Every ad and page says SOS SMS is a membership that dispatches licensed, insured contractors; the contractor does the work |
| No retargeting, no pixels | Search and social are targeted by location only, to open zones: no ad pixels, retargeting, or uploaded lists (Phase 6 drill 9) |
| Claims | No superlatives, no arrival averages, no "24/7" unless the zone's covered hours are 24/7. The guarantee appears in an ad only with its scope on the membership page (decision 3) |
| Safety | The 911 line appears on the membership page and in one ad description |
| Brand terms | The name collision (decision 10) means people searching "SOS plumbing" may be looking for someone else. Do not bid on "SOS plumbing" until the trademark and search check is done |

### Measurement

The conversion to optimize for is a **new paid member**, not a click, a ZIP check, or a launch list sign-up; those are imported as secondary conversions. Cost per new paid member by channel and zone, with affiliate commissions counted in it, is measured against the ceiling of about $43 (R63) and decides whether a channel's spend grows or shrinks. Monthly churn and annual renewal by channel show which channels bring members who stay (`../../marketplace/speed-to-scale-plan.md`, sections 5 and 8).

## Step 8.1. Full-funnel asset map

<!-- sheet: Assets -->
| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specs and QA | Contributors | Inputs Required | Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **CHANNEL 1. AFFILIATES** | | | | | | | | | |
| Top of Funnel | Affiliate program page | Where partners join: who may join, the commission, the disclosure rule, the kit, the codes | Web page | What SOS SMS is; who may join; the commission and when it is paid (R61); the disclosure line; who may not be paid (RESPA) | Counsel-reviewed; plain words; no claims beyond the kit | Demand lead, counsel | Affiliate terms (Stage 0) | 1 week | Partners sign up here; no calls |
| Top of Funnel | Partner kit | The words a partner uses | One page, plus email and newsletter blocks | A paragraph; how it works in one text; the prices as merge fields; the guarantee with its scope; the safety line; the disclosure line; what not to claim | Every claim from Phase 6; the partner's code in every link | Demand lead | Phase 6 drills; affiliate terms | 1 week | One kit, a code per partner |
| Middle of Funnel | New-account insert | A note in the welcome a utility or city sends to a new account | Insert or email block | "New home? Save one number before anything breaks"; the readiness scorecard; the code | The partner's own approval; the disclosure | Demand lead | Partner agreement | 2 weeks per partner | Reaches Level 1 at moving in (Phase 4) |
| Middle of Funnel | Association and newsletter feature | A short feature for a homeowner association's or a local publication's newsletter | Article and email block | The first-freeze readiness steps; how membership works; the code | Same QA as the kit | Demand lead | Partner agreement | 1 week per partner | Reaches Level 2 (Phase 4) |
| Bottom of Funnel | Partner landing page | The membership page with the partner's name and code | Web page | The partner's welcome line; the ZIP check; the membership; the disclosure | Same QA as the membership page | Product | Partner code | 1 day per partner | Commission tracked by code |
| Bottom of Funnel | Commission statement | A monthly statement of new paid members by code | Email | Members joined; first month paid; commission due | Paid only after the member's first paid month (R61) | Product | Billing records | 2 days | |
| **CHANNEL 2. EMAIL** | | | | | | | | | |
| Top of Funnel | Scorecard results emails | The readiness scorecard's tiered results, by email | Email sequence | See `lead-magnet-spec.md` | CAN-SPAM (S73) | Demand lead | ScoreApp | 1 week | Builds SOS SMS's own homeowner list |
| Middle of Funnel | Launch list sequence | For zones not yet open: what SOS SMS is, readiness steps, and the opening when it comes | Email sequence | Three emails: how it works in one text; the shutoff guide; the opening email | No charge, no service promised; an opt-out in every email | Demand lead | Zone record | 1 week | The opening email goes first to the launch list (Stage 2) |
| Middle of Funnel | Seasonal readiness notes | Before the first freeze, and before summer storms | Email | One problem, the steps, the membership | Opt-in for members; CAN-SPAM | Demand lead | Prevention guides | 2 days per season | |
| Bottom of Funnel | Opening email | Memberships are open in your zone | Email | The zone is open; the prices; how it works in one text; the guarantee with its scope; join | Sent only once the density number is met (R55) | Demand lead | Zone open | 1 day per zone | |
| Bottom of Funnel | Member emails | The welcome, the renewal reminder before {{renewal date}}, and the cancellation confirmation | Emails | What membership includes; how to cancel; the renewal terms | ROSCA and state automatic renewal laws (S87); counsel-reviewed | Product, counsel | Member terms | 1 week | Retention |
| **CHANNEL 3. SEARCH AND SEO PAGES** | | | | | | | | | |
| Top of Funnel | Prevention guides | "How to prevent frozen pipes", "Where is my main water shutoff?" | Web pages | Steps; when to call a plumber; the readiness scorecard; the membership | Accurate and general; no product claims | Demand lead, a founding contractor reviewer | Founding contractor review | 1 week for the first five | Read before the need |
| Top of Funnel | Home Emergency Readiness Scorecard | The lead magnet, as a page | ScoreApp scorecard | See `lead-magnet-spec.md` | Same as the spec | Demand lead | ScoreApp | 1 week | |
| Middle of Funnel | Problem guides | "Water leaking through the ceiling: what to do first", "Sewer backup: what to do now", "Water heater leaking" | Web pages | Stop-the-water steps first; safety; when it needs a plumber tonight; for next time, the membership | Steps limited to shutoff and safety, not repairs; the 911 line; reviewed by a licensed plumber | Demand lead, a founding contractor reviewer | Founding contractor review | 1 week for the first five | Help first: a reader mid-emergency gets the steps and the safety line, never a sign-up first |
| Middle of Funnel | Sign-up ad groups | Paid search on readiness and plan searches ("plumbing protection plan", "home warranty alternatives", "plumber membership", "how to prevent frozen pipes") | Responsive search ads | Drafts below | Geofenced to open zones; emergency dispatch searches excluded | Demand lead | Membership page | 1 week per zone | Sells memberships before the need (decision 11) |
| Middle of Funnel | Paid social for sign-ups | Short readiness posts, promoted to homeowners in open zones | Image or video ads | The first freeze; where the shutoff is; one text | Location targeting only; no pixels, retargeting, or uploaded lists | Demand lead | Prevention guides | 1 week per zone | |
| Bottom of Funnel | Membership page | The page every channel lands on | Web page | The ZIP check; {{monthly price}} or {{annual price}}; the $99 trip charge on use, credited to the repair; how it works in one text; the guarantee in full with its scope; what is not included; cancel any time; privacy; the 911 line | Loads fast on a phone; join above the fold; says SOS SMS dispatches and is not the plumber; renewal terms counsel-reviewed | Product, counsel | Decisions 2, 3, 4, and 6; R51 to R56 | 1 week | One template, one per zone |
| Bottom of Funnel | Zone pages | "Plumbing emergency membership in {{zone name}}" | Web pages | Same as the membership page, written for search | Same QA | Product | Zone | 2 days per zone | Shared template with the membership page |
| Bottom of Funnel | Negative keyword list | Searches to exclude | List | Emergency dispatch searches ("emergency plumber near me", "24 hour plumber", "burst pipe repair"); jobs and careers; DIY parts and tools; other cities; competitor brand names | Reviewed weekly against search terms | Demand lead | Search term reports | Ongoing | Keeps spend on sign-ups before the need |
| Bottom of Funnel | Microsoft Ads import | The Google campaigns imported to Microsoft Ads | Search campaigns | Same structure, same rules | Same QA | Demand lead | Google campaigns running | 2 days | Clicks reported 30 to 60 percent cheaper; audience skews older homeowners (S74, C) |
| **MEMBER LOOPS** | | | | | | | | | |
| Top of Funnel | Forwardable contact card | Sent in the welcome texts and after a completed job: "save this, and share it with a neighbor if you like" | Text with a contact file | One line; the contact card; the membership page | Sent once; no follow-ups without opt-in (S31) | Product | Members | 2 days | Referrals per member is the loop's KPI; no reward at launch (R62) |
| Top of Funnel | Text READY | The readiness keyword on every page and card | Text sequence | Five-question home check; the shutoff guide; the membership page | Informational only | Product | Message design | 1 week | A path to joining (R54) |
| Middle of Funnel | Welcome texts | Sent the moment a member joins | Texts | Membership active; save the contact card; how it works in one text; the safety line; text HELP for a person | Transactional only; full name "SOS SMS", never "SOS" alone (name collision) | Product | Join flow | 3 days | The contact card is how members reach SOS SMS, not the name |
| Bottom of Funnel | Stop-the-water first reply | The product's answer to a member's request text: it is going to the contractors now, then the steps to stop the water for the problem described | Text | Automated-reply disclosure; that it is going to the licensed, insured contractors on SOS SMS now; text HELP for a person; the safety line; then the shutoff steps | No offer, no link, nothing to confirm; gas, smoke, fire, or injury: the safety reply first and no broadcast until safe (decision 8); steps limited to shutoff and safety | Product, founding contractor reviewer | Decisions 3, 4, and 8 | 2 weeks, tested with 20 people | The demand driver (Phase 1) and the moment the membership proves itself |
| Bottom of Funnel | Reply to a non-member | The answer to a text from a number that is not a member | Text | The safety line; the stop-the-water steps; how to join | Dispatch is for members (R57); never charged | Product | R57 | 2 days | |
| Bottom of Funnel | Automatic refund text | When the window is missed, the refund and an explanation arrive without the member asking | Text | What happened; the refund; what happens next | Sent automatically; plain words | Product | Guarantee rule | 3 days | Trust that keeps the membership |
| Bottom of Funnel | Permission request | After the job, a separate request to quote the member's words | Text | One question; how the quote would be used | Explicit and separate from the review question | Product | Member terms clause | 1 day | Feeds the proof table only with permission |

## Search ad drafts, sign-ups, zone template

Lengths checked: headlines at most 30 characters, descriptions at most 90. Merge fields are filled per zone from the zone record. Ads run only in open zones, and the guarantee headline runs only where the zone's covered hours are on the membership page.

<!-- sheet: Ad_Copy -->
| Type | Text | Length | Note |
|---|---|---|---|
| Headline | Join Before Your Pipes Burst | 28 | |
| Headline | One Text When Something Breaks | 30 | |
| Headline | Plumbing Emergency Membership | 29 | |
| Headline | Dispatch to Licensed Plumbers | 29 | Says SOS SMS dispatches |
| Headline | One Text Reaches Local Pros | 27 | Holds only in zones at density |
| Headline | Trip Charge Only When Used | 26 | |
| Headline | Arrival Time When They Accept | 29 | |
| Headline | No App. No Phone Tree. | 22 | |
| Headline | No Forms at 2 a.m. | 18 | The card and address are on file |
| Headline | Cancel Any Time | 15 | |
| Headline | Ready Before the First Freeze | 29 | Seasonal |
| Headline | Only One Pro Gets Your Info | 27 | Only once the broadcast hides identity (Phase 6 drill 9) |
| Headline | Membership in {{zone name}} | 14 plus the zone name | Per zone; at most 30 once filled |
| Headline | 90 Minutes or Trip Charge Back | 30 | The guarantee (decision 3); scope on the membership page |
| Description | Join before you need it. In an emergency, one text reaches vetted local plumbers at once. | 89 | |
| Description | Your card and address are on file, so the emergency is one text. Cancel any time. | 81 | |
| Description | The $99 trip charge applies only when you use it, and counts toward the repair. | 79 | |
| Description | Not a warranty. We get a vetted plumber to your door; they price the repair on site. | 84 | |
| Description | We dispatch local licensed, insured plumbers. Only the one who accepts gets your address. | 89 | Second sentence only once the broadcast hides identity |
| Description | Fire, gas smell, or anyone hurt? Call 911 first. For leaks and backups, members text us. | 88 | The safety line |

## Production order

1. Stage 0 first: the member terms and the automatic renewal disclosures reviewed by counsel (S87); membership billing tested; the affiliate terms (disclosure, S88; no settlement-service payments, S86, S94); email sending set up (S73); the number registered for A2P 10DLC (decision 9, S32). Without them, nothing can sell a membership.
2. The membership page, the guarantee in full, and how it works in one text. They carry decisions 2, 3, 4, and 6.
3. During Stage 1, while supply fills the zone: the readiness scorecard, the first five prevention and problem guides, and the launch list sequence.
4. The affiliate program page and the partner kit; the first partners signed for the founding zone, with codes ready before it opens.
5. Member loops: the welcome texts, the stop-the-water first reply, the reply to a non-member, the contact card, the refund text, READY.
6. When the zone opens: the opening email to the launch list; affiliates go live; then the sign-up ad groups after Google's written confirmation (decision 11), paid social, and the Microsoft Ads import.

## Name collision note

A web search for "SOS SMS" returns several unrelated local plumbing companies with "SOS" in their names (decision 10: a US trademark search and a search check in the zone, in Stage 0). In paid search this has a direct cost: brand searches for "SOS" may belong to someone else, and an ad that reads like theirs invites confusion. Use the full name in every ad, email, and page, and make the saved contact card, not the name, the way members reach SOS SMS.
