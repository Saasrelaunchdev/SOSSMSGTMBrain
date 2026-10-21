# Phase 8. Assets and Collaterals Library Dashboard, contractor side

Revised 2026-10-01 for the product-led motion: no sales team, no calls, no shop visits. Contractors find SOS SMS through email or a partner and sign themselves up by text. Revised 2026-10-20, the tiers revision: recruiting runs in three trades at once, plumbing, HVAC, and electrical, and the late-arrival rule keeps the trip charge on a late arrival.

## The three channels

<!-- sheet: Channel_Choice -->
| Skill default | Used for SOS SMS | Why |
|---|---|---|
| Cold email (Instantly) | 1. Cold email, kept | Cheap, scales zone by zone, and needs no salesperson: the email sends a contractor to the Lead Cost Check and to self-serve sign-up |
| LinkedIn outreach | 2. Partnership program | Supply houses for each trade, the trade associations (PHCC for plumbing, ACCA for HVAC, NECA and IEC for electrical), trade schools, and tools contractors already use put SOS SMS in front of contractors where they already are |
| LinkedIn Ads | 3. In-product referral loop | The product asks a contractor who just got paid which other trade they trust. Not a sales channel; it costs nothing to run |

**Self-serve rule.** Every call to action ends in a contractor signing up on their own, by text (JOIN) or on the contractor page. No asset asks for a meeting.

**Email rule.** Commercial email law applies to business email too: accurate sender details, an honest subject line, a valid postal address, and an opt-out honored within 10 business days (S73).

**Texting rule.** Marketing texts need prior written consent (S31). A contractor receives texts only after starting sign-up themselves.

The demand driver from Phase 1, the Lead Cost Check, is the top-of-funnel asset in all three channels.

## Step 8.1. Full-funnel asset map

<!-- sheet: Assets -->
| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specs and QA | Contributors | Inputs Required | Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **CHANNEL 1. COLD EMAIL** | | | | | | | | | |
| Top of Funnel | Zone contractor list | Every licensed plumbing, HVAC, and electrical business in the zone, with a business email where one is published | Spreadsheet or email tool import | Business name, trade, license number, website, email, whether it advertises on lead platforms | Licenses from public lists; emails only from the business's own site or a reputable data provider; verify before sending | Growth lead | The launch zone, drawn in Stage 0 (decision 1) | 1 week per zone | Lead-platform advertisers (ICP Level 2) go first; each trade's list fills toward its own 9 places (R08) |
| Top of Funnel | Email 1: the Lead Cost hook | First email: one question about cost per booked job, and a link to the Lead Cost Check | Email, plain text | Draft below | Under 120 words; no claims about SOS SMS results; postal address and opt-out (S73) | Growth lead | Lead Cost Check web version | 2 days | Measure clicks to the check, not opens |
| Top of Funnel | Lead Cost Check, web version | The demand driver as a self-serve page: four numbers in, cost per booked job out | Web page | Lead spend; leads paid for; jobs booked; unpaid trips. Result: cost per booked job, spend on requests that never became work | Uses only the contractor's numbers; nothing stored without consent | Product | Phase 1 Step 1.6; the calculator in `pricing_dashboard.xlsx` | 1 week | The same page serves all three channels |
| Middle of Funnel | Email 2: how a job works in three texts | The mechanics, including the shared request stated openly | Email with one image | Draft below | Mock-up labeled as such until the product exists | Growth lead, designer | Message design | 3 days | |
| Middle of Funnel | Email 3: the terms on one page | What the contractor pays, when they are paid, what they commit to, what happens if they are late | Email linking to the terms page | Draft below | Written to decisions 2, 3, and 6; counsel-reviewed before sending | Founders, counsel | The terms on one page | 1 week | The most important supply-side asset |
| Middle of Funnel | Contractor page | The page every email and partner links to: how it works, the terms, FAQ, sign-up | Web page | How it works; terms; FAQ (who else sees a request, what if I'm late, how many requests to expect in my trade, how disputes work); text JOIN | Narrowed claims only (brief Section 5) | Founders, product | The terms on one page | 1 week | Shared with Channels 2 and 3 |
| Bottom of Funnel | Email 4: when the zone opens | When {{zone}} opens to members, and how to be on SOS SMS by then | Email | Draft below | No urgency of any kind: there is no deadline to invent | Growth lead | The terms on one page (R03) | 1 day | Ends the sequence; no further emails without engagement |
| Bottom of Funnel | Sign-up by text | The self-serve path from JOIN to available | Text sequence | Trades and area; license and insurance upload; payout setup; availability hours; the agreement with the permission clause; a test request | One step per text; progress shown; help by text, not by phone | Product | Payment provider; verification process | 2 weeks to build | Track the drop-off step (Phase 7 Stage 4) |
| Bottom of Funnel | Contractor agreement | The agreement, signed inside the sign-up flow | E-signature | The terms made binding: the $25 contractor fee per completed paid job from the first job, the same for every contractor; permission clause for citing outcomes and names | Counsel-reviewed; permission asked before the first job | Founders, counsel | Terms on one page | 2 weeks | |
| **CHANNEL 2. PARTNERSHIP PROGRAM** | | | | | | | | | |
| Top of Funnel | Counter card | Card at supply house counters with a QR code to the Lead Cost Check and a partner code | Printed card | "What did your leads really cost last month?"; QR code; "text JOIN-{{code}}" | Partner approves wording and placement; no endorsement implied unless given in writing | Growth lead, designer | Partner agreement | 1 week | One code per partner location, so sign-ups are attributed |
| Top of Funnel | Member newsletter and job-board listings | A short listing in association newsletters, trade school job boards, and partner emails | Text blurb and link | Two sentences on how SOS SMS works; the Lead Cost Check link; the partner code | Partner edits allowed; claims stay narrowed | Growth lead | Partner agreement | 2 days per partner | Trade schools reach newly licensed contractors |
| Top of Funnel | Emergency rate card template | Free template for stating after-hours trip charges and rates up front | One-page PDF | Trip charge; after-hours rates; what is credited if the work goes ahead | Useful on its own; SOS SMS footer only | Growth lead | Phase 1 variant | 3 days | A giveaway partners are glad to hand out |
| Middle of Funnel | Partner kit | Everything a partner needs to explain SOS SMS without calling the founders | One-pager, FAQ for counter staff, co-branded contractor page | What it is; who it is for; what it costs; how to join; the partner's code | Accurate and short; counter staff should never have to guess | Growth lead | Contractor page | 1 week | Counter staff are the channel |
| Middle of Funnel | Ten-minute explainer video | Recorded walk-through partners can play at member meetings or share | Video | The lead cost problem; how a job works in three texts; the terms; how to join | No volume or earnings claims; replaces in-person talks | Founders | Contractor page; message mock-ups | 1 week | |
| Bottom of Funnel | Partner-code sign-up | The self-serve sign-up, opened with the partner's code | Text sequence | Same as Channel 1, with the partner credited | Same QA as Channel 1 | Product | Sign-up by text | Uses Channel 1 build | Measures sign-ups per partner |
| Bottom of Funnel | Partner member offer | The contractor terms presented to a partner's members, if the partner wants it | One-page offer | The terms on one page; how to join; the partner's role, only if agreed | Partner sign-off on any use of their name. No partner referral fee (R18) | Founders, partner | Partner agreement | 1 week | Optional |
| **CHANNEL 3. IN-PRODUCT REFERRAL LOOP** | | | | | | | | | |
| Top of Funnel | Fifth-trip referral prompt | Automated text after a contractor's fifth paid trip: which other trade do you trust? | Text | One question, then a personal link to send | Sent once; easy to ignore | Product | Phase 7 Stage 5 data | 2 days | Cross-trade referrals fill coverage gaps |
| Top of Funnel | Forwardable Lead Cost Check | The check as a link a contractor can send to a peer | Link | One line from the contractor; the link | The contractor decides whether to send | Product | Web version | 1 day | |
| Middle of Funnel | Referred contractor intro | The first message a referred contractor receives, by email | Email | Who referred them; the contractor page; how to join | Sent once; postal address and opt-out (S73) | Product | Contractor page | 1 day | |
| Middle of Funnel | Add-a-technician flow | Lets a shop add its technicians without anyone from SOS SMS | Text sequence | Owner invites a technician; technician confirms; documents linked to the shop | Owner controls who receives requests (Phase 5 Manager blocker) | Product | Sign-up by text | 1 week | Expansion inside a shop |
| Bottom of Funnel | Referred sign-up | Sign-up opened with the referrer's name | Text sequence | Same as Channel 1 | Same QA | Product | Sign-up by text | Uses Channel 1 build | Track referred versus cold completion |
| Bottom of Funnel | Referral thank-you | How the referring contractor is thanked | Text | Thanks; what happened with the referral | No cash reward at launch (R18) | Product | The referral prompt | 1 day | Promise no reward |

## Cold email sequence, draft copy

Merge fields are filled from the contractor list record before anything is sent (resolution register, merge fields). Every email ends with the sender's name, SOS SMS's postal address, and a one-click opt-out (S73).

<!-- sheet: Email_Copy -->
| Email | Send | Subject | Body |
|---|---|---|---|
| 1 | Day 0 | What did each job from your leads cost? | Hi {{first name}}, one question for {{business}}: what did each booked job from your lead platforms cost last month, counting the leads that never answered? This two-minute check works it out from four numbers you already know: {{link}}. Your answers stay yours. We're building SOS SMS, emergency jobs by text in {{zone}}, with no lead fees and the trip charge collected before you roll. SOS SMS will be paid by members' monthly or annual fees, and by you only per completed paid job. |
| 2 | Day 3 | How a job works in three texts | An SOS SMS member texts what broke. Every matched contractor in the area sees it at once, and the first to accept gets the job. Everyone else pays nothing, because nobody pays to look. The trip charge is on the member's card before you roll. (Image: the three texts.) See how it works: {{contractor page}}. |
| 3 | Day 7 | The terms, on one page | What you'll pay: nothing to join or to see a request; $25 per completed paid job, taken from the $99 trip charge, so $74 of it reaches you. When you're paid: the trip charge is released when you arrive and reaches your bank within two business days. What you commit to: an arrival time when you accept, crediting the trip charge to the work if the member goes ahead, and current license and insurance. If you're late: you keep the trip charge, the late arrival is recorded, and two in 90 days pause your requests until we review them; if you accept and don't come, the trip charge goes back to the member. All of it in writing: {{terms link}}. |
| 4 | Day 12 | When SOS SMS opens in {{zone}} | We're opening memberships in {{zone}} once enough plumbing, HVAC, and electrical contractors have joined to cover every hour of the day. Every contractor joins on the same terms, written on one page. To join, text JOIN to {{number}}; it takes about 5 minutes, with no call. Last email unless you reply. |

## Production order

1. The terms on one page, then the contractor page. Nothing else is honest without them; they carry decisions 2, 3, 4, and 6.
2. The Lead Cost Check web version and sign-up by text.
3. The zone contractor list and emails 1 to 4, with the sending setup (a separate sending domain, warm-up, daily caps, opt-out handling).
4. The partner kit, counter cards, and explainer video, once one partner says yes.
5. The referral prompt and add-a-technician flow, once contractors reach five paid trips.

## Optional later test, not one of the three

Search ads aimed at contractors looking for work ("plumbing leads", "HVAC leads", "electrician jobs"). Product-led, but not part of the founders' channel decision, and SOS SMS runs no paid search at launch on either side (decision 11). Revisit only if email and partners do not reach the density target in a trade in time.

## Name collision note

A web search for "SOS SMS" returns several unrelated local plumbing companies with "SOS" in their names (decision 10: a US trademark search and a search check in the zone, in Stage 0). In email it matters for deliverability and trust: always use the full name, the sending domain, and the zone, never "SOS" alone.
