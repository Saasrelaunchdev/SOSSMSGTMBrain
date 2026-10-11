# Resolution register

Every unknown and every open founder decision in the SOS SMS go-to-market, resolved in one place. Written 2026-10-03 by the GTM consultant, at the instruction to resolve everything that public data, the research, and the GTM itself can resolve, and to leave no unknown and no decision open in any deliverable. Every file in this repository, the GTM brain, the walkthrough deck, and the Google folder now uses these values.

**What this changes.** The twelve decisions in `cross-side-check.md` Part 3 are decided, and copy that waited on them carries the decided words. Every unknown number has a value with its basis, or the method and the moment that produce it.

**Revised 2026-10-11, the membership revision.** The demand side is a monthly or annual membership, joined before the need, with the card and home address on file, so in an emergency a member sends one text and dispatch starts. Decisions 2, 3, 6, 8, and 11 carry revised words, and decision 12 is replaced by an acquisition ceiling per new paid member. R02 (the SOS SMS fee) and R30 (first text to paid) are retired; their rows stay, marked Retired, so earlier references still resolve. R01, R06, R09, R11, R15 to R19, R21, R23 to R25, R31, R32, R34, R39, R42, R43, R46, R49, and R50 are revised; R51 to R64 are new; the merge fields add `{{monthly price}}`, `{{annual price}}`, and `{{renewal date}}`. The contractor side is unchanged.

**What this does not change.** SOS SMS is pre-launch: nothing is live, and nothing here is a result. No member, contractor, job, arrival time, testimonial, or proof point is invented. Grade C figures stay internal. Contractor recruiting copy stays in the future tense, and member copy stays held until memberships open in its zone.

## Five kinds of resolution

| Kind | What it means | How copy treats it |
|---|---|---|
| **Decided** | A choice SOS SMS makes: a price, a rule, a term. Set here, with its basis | Used as written, in copy on the side it belongs to |
| **Planning value** | A number SOS SMS plans with: a target, a threshold, or an operating assumption, with its basis | Used in planning and internal math. Never presented as a measured result. The measured figure replaces it once a zone runs |
| **Counted at** | A fact that cannot exist before launch, resolved to the method that produces it and the stage when it is produced | The method is stated; no number is written until it is counted |
| **Merge field** | A value that differs per zone, per contractor, per member, or per message, written `{{field}}` and filled from a named record when the message is sent | Never typed by hand; the field list is below |
| **Retired** | A value a later decision removed. The row stays, with the date and what replaced it, so earlier references still resolve | Never used in copy |

## The twelve decisions, decided 2026-10-03, revised 2026-10-11

| # | Decision | Decided | Basis |
|---|---|---|---|
| 1 | Launch metro, first zone, and trades | The United States. Launch in the founders' home metro, in one founding zone: a 10-mile radius drawn around the founding contractors' shops. Plumbing and water emergencies first (burst pipes, leaks, backups, water heaters) | Every source in the research is US (S62, S31, S32, S70). In Stage A the founders cover dispatch gaps and contractor support by hand, which needs them in the metro. The radius is R27. The city's name is the one input no data can supply, so the rule decides it |
| 2 | Revenue model | Revised 2026-10-11, the membership revision. Members pay a monthly or annual membership, billed to the card on file: planning values $10 a month or $100 a year (R51, R52) until the launch price is set in Stage 0, shown in copy as `{{monthly price}}` and `{{annual price}}`. No fee per request; the $99 trip charge on use (decision 5). Contractors pay $0 to join, $0 per request seen or declined, and no subscription or seat fee. After the founding period, contractors pay $25 per completed paid job, deducted from the trip charge payout; founding contractors keep $0 a job for 12 months after the founding period. SOS SMS takes no share of the repair | The pricing model (`../pricing/pricing-model.md`): the membership at the value ceiling of the closest analog, a plumber's club at $10 a month (S75), far above its cost floor of about $3.75 a month; the subsidized side priced from the floor up and held far under the market. Members join before the need, so the emergency is one text. Replaces the $49 SOS SMS fee per request (R02, retired) |
| 3 | Late-arrival rule and guarantee scope, together | Fault-based (Run 1 option C) plus item B. A contractor can accept only with an arrival time inside the remaining window. The 90 minutes start at the member's request text (revised 2026-10-11). If no one is there in time, the $99 trip charge comes back automatically: from the contractor's trip charge when the contractor missed the time they committed to, from SOS SMS when SOS SMS caused the miss. Covered areas: the zone, named by its neighborhoods on the membership page. Covered hours: the hour bands where the zone meets its density number, listed on the membership page. If no contractor accepts, the member is told within 15 minutes and pays nothing | Run 1 Phase 9 option C; Part 2 item B; Run 2 Phase 9 decision 2. A member's card and address are on file, so the request text is the whole request and the window runs from it. Before 2026-10-11 the clock started at the confirming text of the pay per request flow |
| 4 | Dispatch rule and what contractors see before accepting | Every matched contractor receives the request at once; the first to accept with an arrival time inside the remaining window gets the job. Before accepting, contractors see the problem, any photos or video, and an approximate distance and cross-street area. The address goes only to the contractor who accepts | Part 2 item C; both runs' privacy and "lose the race, lose nothing" copy |
| 5 | Who sets the trip charge | SOS SMS sets one trip charge per trade and zone: $99 for plumbing in the founding zone, day or night. It is charged to the member's card on file when a contractor accepts, paid to the contractor, and credited to the repair if the member goes ahead | Part 2 item A. $99 sits inside the plumbing trip charge band of $75 to $100 (S28, C) and under the $150 to $250 after-hours call fee (S50, C) |
| 6 | Payment provider, hold, capture, and payout | Stripe Connect. The card is saved when the member joins and billed monthly or annually for the membership. The trip charge is authorized on the card on file when the member's request text arrives, captured when a contractor accepts, held, and released to the contractor on arrival. Payout to the contractor's bank within 2 business days of arrival, on the provider's standard schedule (revised 2026-10-11) | Part 2 item H. Online card authorizations are valid about 7 days (S30), far longer than a 90-minute job. Card processing 2.9% plus $0.30 a charge, the planning value in the pricing model |
| 7 | Verification and recheck cadence | License and insurance checked at sign-up, before the first request; rechecked every 6 months and on each policy's expiry date. The same words on both sides | Section 6 row 7. Policies run for a year, so a 6-month check plus the expiry date catches every lapse |
| 8 | Safety handling | Texts that mention gas, smoke, fire, or injury get the safety reply first and are not broadcast until the member confirms they are safe and the utility or 911 has been called. A text from a non-member gets the same safety reply (R57) | Part 2 item F (S60) |
| 9 | Carrier registration of the SOS SMS number | One local number in the launch metro's area code, registered for A2P 10DLC (brand and campaign) through the messaging provider before any test text. The same number serves every zone | S32: US carriers block unregistered business texting from local numbers |
| 10 | Name collision | A US trademark search and a search check in the zone, done in Stage 0, before any ad, page, or email. Always the full name SOS SMS; no bids on "SOS plumbing" | Unrelated local plumbing companies use "SOS" |
| 11 | Paid search, and what it is for | Revised 2026-10-11. Paid search sells memberships before the need, never dispatch during an emergency: standard Google search ads only, after Google confirms in writing that SOS SMS may advertise its membership this way; never Local Services Ads; emergency dispatch searches are negative keywords. Microsoft Ads runs in every open zone alongside | S70, S71, S74. A homeowner searching mid-emergency is better served by calling a contractor from the results than by joining anything |
| 12 | Acquisition ceiling per new paid member (replaces the paid search ceiling per paid job) | Replaced 2026-10-11. By channel and zone, at most the first 6 months of contribution on the monthly plan: about $43 at the planning price (R63), reviewed weekly. Affiliate commissions count in it. Replaces the per paid job ceiling of $275, falling to $192 and $137 | $8.51 of contribution a month in the founding period (R51, R31, R58) over the first 6 months at 6.5 percent monthly churn (R59): about $43.4, about $43 (pricing model). The affiliate commission, $20 (R61), sits under it |

## Every value

| ID | Kind | What | Resolved to | Basis |
|---|---|---|---|---|
| R01 | Decided | Trip charge | $99 per request, one per trade and zone, day or night; charged to the member's card on file when a contractor accepts; paid to the contractor; credited to the repair if the member goes ahead | Decision 5; decision 6 (revised 2026-10-11) |
| R02 | Retired | SOS SMS fee | Retired 2026-10-11 by the membership revision: no fee per request. Was: $49 per dispatched request | Decision 2, revised; replaced by the membership (R51, R52) |
| R03 | Decided | Contractor fee | $25 per completed paid job after the founding period, deducted from the trip charge payout. Never per request, never to join, never for a declined or lost request | Decision 2. At the value ceiling: 20 percent of the about $125 cheapest per-lead cost per booked job (S03, S06, C, internal only). Floor about $10 |
| R04 | Decided | SOS SMS share of the repair, or a rate discount | $0. The price for the work stays the contractor's | Run 1 Phase 9; Part 2 item A |
| R05 | Decided | Founding terms | Founding contractors pay $0 a job through the founding period and for 12 months after it, written into the founding agreement from day one | Decision 2; pricing model |
| R06 | Decided | Founding period | The founding zone's first 6 months open to members. Every contractor pays $0 a job during it | Long enough for the 4-week proving gate (R33) and a full season of member churn and renewal to be measured |
| R07 | Decided | Founding list | Opens with the first cold email in the founding zone and closes 60 days after it. Everyone on the list by then is a founding contractor | Four cold emails run 12 days; 60 days leaves room for partners and referrals, and gives the last email a real date |
| R08 | Planning value | Founding cohort target | 9 contractors for plumbing in the founding zone | The density number at acceptance 0.30 for a 95 percent chance that at least one accepts, which buffers nights and freeze spikes (Run 1 Phase 5) |
| R09 | Decided | Take per job | $0 in the founding period: the trip charge goes to the contractor. After it, $25 per completed paid job from the contractor fee (R03). SOS SMS's revenue is the membership (R51, R52) | Decision 2, revised 2026-10-11. Contribution per member about $8.51 a month in the founding period and $9.03 after it (pricing model, illustrative) |
| R10 | Decided | Refund on a late arrival | The $99 trip charge, back to the card automatically | Decision 3 |
| R11 | Decided | Member told when no one accepts | Within 15 minutes; the card is never charged | The 10-minute response window plus one rebroadcast |
| R12 | Decided | Contractor response window | 10 minutes, when marked available | Acceptance has to fit the start of the 90-minute window and leave the rest for the drive (R27) |
| R13 | Decided | First refusal on a contractor's own customers | 5 minutes. The after-hours-line acceleration runs only once dispatch supports it | Part 2 item E |
| R14 | Decided | Payout timing | Within 2 business days of arrival | Decision 6 |
| R15 | Decided | Requests outside covered hours | Not dispatched. The member gets the stop-the-water steps and the safety line, is told no contractor is covering that hour, and pays nothing. The membership page names the covered hours | The guarantee and sign-ups run only for covered hours (Part 2 item G) |
| R16 | Decided | No card | Joining puts a card on file. A text from someone without a membership gets the free help by text (R57) and pays nothing | Keeps "paid to show up" true for every contractor job (Part 2 item D) |
| R17 | Decided | Second contractor after a miss (the relaunch) | SOS SMS pays the second contractor's trip charge from membership revenue. Kept out of copy until dispatch supports it | Section 6 row 2; the first contractor's guarantee is not affected |
| R18 | Decided | Supply partner referral fee and contractor referral reward | None at launch. Supply partners and contractors are thanked by text; no reward is promised. Member affiliates are paid per R61 | Run 1 Phase 8 |
| R19 | Decided | Household membership | The demand-side product: a monthly or annual membership, joined before the need (decision 2, revised 2026-10-11) | The membership revision |
| R20 | Decided | After-hours surcharge | None: one trip charge, day or night | Run 2 Phase 9: the after-hours premium is the surprise fee customers complain about (S50, S51) |
| R21 | Decided | Guarantee on the repair | Not offered. The guarantee covers the arrival window; the repair is between the member and the contractor, whose license and insurance SOS SMS checks. The membership does not pay for repairs or parts (R53) | Run 2 Phase 3 |
| R22 | Decided | Market and country | The United States | Decision 1 |
| R23 | Decided | Website | One site: the contractor page, the readiness scorecard, and the launch list from Stage 1; the membership page (with a ZIP check), the guarantee page, and five problem and prevention guides from Stage 2 | Launch sequence, Stages 1 and 2 |
| R24 | Decided | Taglines and sub tags | Contractors: "Emergency jobs you choose, with the trip paid before you roll." Sub tag: "No lead fees. Paid to show up." Members: "One text, and help is on the way." Sub tag: "Join before you need it." | Run 1 and Run 2 Step 6.1 brand promises; the member lines revised 2026-10-11 |
| R25 | Decided | Founder roles | Two roles: a supply lead (recruiting, onboarding, dispatch backup) and a demand lead (memberships: affiliates, email, search for sign-ups, the member line). Both founders work supply first in Stage 1, while the demand lead also signs the zone's affiliates and grows its launch list; the roles split fully when memberships open in Stage 2 | Mirrors the two runs and the launch sequence |
| R26 | Decided | The unattributed matrix rows | Excluded for good. The source matrix as written, with its attributed rows, is the input | No item text exists to attribute them to |
| R27 | Planning value | Zone radius | 10 miles | 90 minutes less up to 15 to accept and about 20 to get on the road leaves about 55 to drive; a 10-mile radius keeps the longest crossing, 20 miles, inside it |
| R28 | Planning value | Acceptance rate per contractor (a) | 0.30 | The density table: 7 contractors for 90 percent coverage, 9 for 95. Measured per hour band with test requests in Stage 1 |
| R29 | Planning value | Share of requests with a miss SOS SMS causes | 5 percent | The pricing model's refund reserve |
| R30 | Retired | First text to paid request | Retired 2026-10-11: a member does not confirm a request, so there is no first text to convert. Was: 50 percent | Decision 2, revised |
| R31 | Planning value | Card processing and operations | 2.9 percent plus $0.30 a charge. Per request: operations $5.30 (support and disputes $3, platform $2, about 30 texts at $0.01). Per completed job, contractor side: payout $0.50, license and insurance checks $1.00, contractor support $2.00. Per member a month: messaging $0.05, support and platform $0.50 | Stripe's standard US card price; the pricing model inputs |
| R32 | Planning value | Zone signal thresholds | Acceptance inside the remaining window 90 percent or more; arrival inside the window 95 percent or more; SOS-caused refunds 5 or fewer per 100 requests; monthly plan churn 6.5 percent or less a month (R59); cost per new paid member at or under the ceiling (R63), by channel; contractor activity 60 percent or more accepting at least one job in 30 days | Acceptance matches the 90 percent coverage target; refunds match R29; churn matches R59; cost per member matches decision 12 |
| R33 | Planning value | Weeks at threshold to prove a zone | 4 consecutive weeks | Long enough to include weekends and one weather swing |
| R34 | Planning value | Sign-up pause | Sign-ups pause automatically in a zone when acceptance falls below 90 percent over the trailing 7 days: ads stop, and affiliate links show the launch list | R32 |
| R35 | Planning value | Runway | At least 18 months at Stage A spending | Covers the founding zone's proving and two more zones proving at once, with margin for them taking longer (`speed-to-scale-plan.md`, section 5) |
| R36 | Planning value | Contractor sign-up time | About 5 minutes by text: trades, area, documents, payout details | Run 1 Phase 7, stage 4 |
| R37 | Planning value | First paid trip | Within 30 days of the zone opening, or of joining if later | Run 1 Phase 5 success metric |
| R38 | Planning value | ICP revenue bands (contractors) | Level 1, the owner-operator: under $500,000 a year. Level 2, the owner with one to five technicians: $500,000 to $3 million a year | Drawn from the team sizes in the ICP; checked in the founding contractors' sign-up survey |
| R39 | Decided | Household income (members) | Not a targeting criterion. Members are targeted by zone and by readiness triggers | No research ties income to joining a home repair membership |
| R40 | Counted at | Licensed plumbing businesses in the launch metro | Counted from the state license list in Stage 0 | Public license lists |
| R41 | Counted at | Owner-occupied homes in the founding zone | Counted from Census tract data (ACS) when the zone is drawn in Stage 0 | S62 method, at tract level |
| R42 | Counted at | Requests per month in a zone | Measured over the zone's first 8 weeks open; planned at 0.25 a member a year until then (R58) | The trigger rate cannot be taken from insurance claim frequency |
| R43 | Counted at | Every SOS SMS result: acceptance, arrival, refunds, joins, churn, renewal, cost per new paid member, earnings | Measured from the first member and the first request in the founding zone, weekly, against R32 | Nothing is live |
| R44 | Decided | Social-proof headlines | The method line in each drill, which describes how the process works. A result replaces it only when it is real, measured, and permissioned | The fabrication rule in both Phase 6 files |
| R45 | Decided | Supporting proof points | The named record or document in each drill that will show the claim is true from the first job (lists below) | Run 1 and Run 2 Phase 6 |
| R46 | Decided | SOS SMS strengths and weaknesses in the competitive tables | Stated by design, with the weaknesses written plainly: no track record yet; open only in zones at density; a fee every month or year, before anything breaks | Nothing is live |
| R47 | Counted at | Warranty network discount | Set by each warranty company's rate card | A competitor's terms, not an SOS SMS number |
| R48 | Decided | Team, burn, and channels tried (the briefs' company snapshot) | Team: two founders, Bryan and Ali, roles per R25. Channels tried: none; SOS SMS is pre-launch. Burn and runway: the founders' own figures stay out of the GTM, which sets the requirement instead (R35) | Pre-launch facts |
| R49 | Decided | Price or price range for the work before arrival (Run 2 item 11) | Not offered at launch. The $99 trip charge is stated on the membership page before joining; the price for the work is set by the contractor on site, before any work starts | Run 2 Phase 1 rates it a Hero (wanted by all, offered by few: S42, S47, S53). One emergency product first; a price range needs per-trade price data the founding zone does not yet have. Kept in the matrix, out of copy |
| R50 | Decided | Reaching a person | Text HELP: a person from SOS SMS replies by text within 15 minutes in covered hours; STOP ends all texts. The welcome texts, the first reply, and every message say so | S72: automated replies identify themselves, state a response time, and hand off to a person; carrier messaging rules require HELP and STOP replies. 15 minutes matches R11 |
| R51 | Planning value | Membership, monthly | $10 a month, billed to the card on file, until the launch price is set in Stage 0. Copy: `{{monthly price}}` | Plumber clubs $8.25 to $19.99 a month (S75 to S77); utility-partner plumbing plans $16.99 to $22.99 (S78). At the closest analog's price, $10 (S75), the value ceiling in the pricing model |
| R52 | Planning value | Membership, annual | $100 a year: two months free. Copy: `{{annual price}}` | The most common annual discount is 16.7 percent, two months free (S90) |
| R53 | Decided | What membership includes | One-text dispatch to the matched contractors; an arrival time on acceptance; the 90-minute guarantee (decision 3); a person by text (R50); the readiness kit (the shutoff guide, Text READY, the contact card). Not included: the repair, parts, or a guarantee on the work (R21). Paid on use: the $99 trip charge, credited to the repair | Decision 2, revised 2026-10-11 |
| R54 | Decided | Joining | On the membership page, or from Text READY; about 3 minutes (planning value); the card, the home address, and consent to the member terms on file; one address per membership; the contact card sent at once | Decision 6; the welcome texts in Run 2 Phase 8 |
| R55 | Decided | When memberships open | Per zone, once the density number is met for the first trade and the covered hours are named. Before then, the launch list: email, no charge, no service promised | Run 1 Phase 5; the launch sequence, Stage 2 |
| R56 | Decided | Cancelling and renewal | Cancel any time, on the membership page, or by texting HELP to reach a person. A monthly membership ends at the end of the paid month; annual members get a renewal reminder before `{{renewal date}}` | ROSCA and state automatic renewal laws (S87). Not a CANCEL keyword: carriers treat stop words as an opt-out from texts |
| R57 | Decided | A text from a non-member | The safety line, the stop-the-water steps, and how to join. Dispatch is for members; nothing is charged | Decision 8; R16 |
| R58 | Planning value | Requests per member | 0.25 a year | 26 percent of homeowners reported a blocked or overflowing toilet emergency in a year (S82); about 20 percent in 2024 (S83). Measured from the first members (R42) |
| R59 | Planning value | Monthly plan churn | 6.5 percent a month | Consumer subscription benchmarks, about 5 to 7 percent; Recurly consumer about 6.5 percent (S89, C) |
| R60 | Planning value | Annual renewal | 75 percent | Annual plans churn about 2.1 percent a month (S89, C), about 77 percent kept over a year, rounded down |
| R61 | Planning value | Affiliate commission | $20 per new paid member, paid after the member's first paid month. Never to a real estate agent, lender, title or settlement agent, or anyone referring at a home purchase settlement. Every affiliate discloses that they are paid | Home warranty affiliate programs pay $4 to $56 an enrollment (S85, C). RESPA Section 8 (S86, S94); FTC Endorsement Guides (S88). Under the ceiling (R63) |
| R62 | Decided | Member referral reward | None at launch. Members who share the contact card are thanked by text | Mirrors R18 |
| R63 | Planning value | Acquisition ceiling per new paid member | About $43, by channel and zone, reviewed weekly: the first 6 months of contribution on the monthly plan | $8.51 a month (R51, R31, R58) over 6 months at 6.5 percent churn (R59): about $43.4 (pricing model). Decision 12 |
| R64 | Planning value | Member base per zone | About 430 members, enough for about one request a month for each founding contractor | 9 founding contractors (R08) × 12 months ÷ 0.25 requests a member a year (R58) = 432 |

## Proof points per copy drill (R45)

| Drill | Contractors | Members |
|---|---|---|
| 1 | The terms on one page: $0 to receive a request, in writing before sign-up | Each request's log: who received it and when the first contractor accepted |
| 2 | The dispatch rule in the terms: every matched contractor sees the request at once | Every acceptance text carries the contractor's name, the committed arrival time, and their Google rating where they have one |
| 3 | Declines carry no penalty, written in the terms; the request history shows what reached you | The guarantee page, published before memberships open in the zone; refunds paid automatically |
| 4 | Every job record shows the trip charge captured before you roll | The member record: the card and home address saved at joining, with consent to the member terms |
| 5 | The payout timeline in the terms: within 2 business days of arrival | The contact card, sent in the welcome texts and again after every job |
| 6 | Every request carries the member's agreement to the trip charge, from the member terms, and the time it was charged | The membership page and the member terms: price, renewal, and how to cancel, stated before the card is taken |
| 7 | Every request carries the time of the member's request text | The trip charge on the membership page and in every acceptance text: $99, credited to the repair |
| 8 | Your trades and area, set at sign-up, shown on every request | License and insurance checked at sign-up, every 6 months, and on each policy's expiry date |
| 9 | The member's photos and video attached to the request before you accept | The broadcast text contractors receive, shown on the privacy page; the privacy policy in plain words, linked from the welcome texts |

## Merge fields

Written `{{field}}` in templates and filled automatically when the message, page, or ad is produced. None is typed by hand.

| Field | Filled from |
|---|---|
| `{{first name}}`, `{{name}}`, `{{business}}` | The contractor list record (cold email), the contractor's sign-up record, or the member record |
| `{{SOS SMS number}}`, `{{number}}` | The registered SOS SMS number (decision 9) |
| `{{zone}}`, `{{zone name}}`, `{{zone neighborhoods}}`, `{{launch metro}}` | The zone record (decision 1) |
| `{{covered hours}}` | The zone record: the hour bands at the density number (decision 3) |
| `{{trade}}`, `{{trades}}` | The contractor's sign-up, or the zone's open trades |
| `{{url}}`, `{{link}}`, `{{terms link}}`, `{{contractor page}}` | The page addresses on the SOS SMS site (R23) |
| `{{code}}` | The partner's or affiliate's code, from the partnership program or the affiliate agreement |
| `{{founding close date}}` | The founding list's close date: 60 days after the first email (R07) |
| `{{score}}`, `{{top two}}`, `{{top three}}`, `{{top-scoring question}}`, `{{result}}`, `{{cost per lead ÷ close rate}}` | The contractor's own answers in the Job Leak Scorecard or the Lead Cost Check |
| `{{their number}}` | The member's own phone number, for the contact card |
| `{{partner}}` | The partner's or affiliate's name, from the signed partner or affiliate agreement |
| `{{share}}`, `{{estimate from your answers}}` | Computed from the survey's own responses, or the respondent's own answers |
| `{{sender name}}`, `{{postal address}}`, `{{opt-out link}}` | The email sending setup: the sending founder, SOS SMS's postal address, and the platform's one-click opt-out (S73) |
| `{{contractor name}}`, `{{arrival time}}`, `{{rating}}` | The request record: the accepting contractor's sign-up, their committed arrival time, and their Google rating where they have one |
| `{{monthly price}}`, `{{annual price}}` | The zone's price record, set in Stage 0 (planning values R51, R52) |
| `{{renewal date}}` | The member record: the annual membership's next renewal date (R56) |

## Arithmetic, checked

- A member pays the membership, `{{monthly price}}` a month or `{{annual price}}` a year (planning values $10 and $100), and the $99 trip charge only on use, credited to the repair. Never shown as one total in copy.
- Per-request costs, both sides: refund reserve 0.05 × $99 = $4.95; card processing on the trip charge 2.9% × $99 + $0.30 = $3.17; messages 30 × $0.01 = $0.30; member support and platform $5.00; contractor payout, checks, and support $3.50. Total $16.92 a request; at 0.25 requests a member a year, $16.92 × 0.25 ÷ 12 = $0.35 a member a month.
- Membership cost floor: fixed costs a member a month $0.30 (the processing fee) + $0.05 (messages) + $0.50 (support and platform) + $0.35 (requests) = $1.20, ÷ (1 - 0.65 - 0.029) = $3.75. The planning price is $10.
- Contribution a member a month at $10: $10 - $0.59 - $0.05 - $0.50 - $0.35 = $8.51 in the founding period; plus $25 × 0.25 ÷ 12 = $0.52 after it, $9.03.
- Annual at $100: $3.20 processing + $0.60 messages + $6.00 support and platform + $4.23 requests = $14.03 a year; contribution about $85.97 a year, about $7.16 a month.
- Acquisition ceiling: $8.51 × (1 - 0.935^6) ÷ 0.065 = about $43.4, about $43. Lifetime contribution: $8.51 ÷ 0.065 = about $131.
- Members per zone: 9 × 12 ÷ 0.25 = 432, about 430.
- Take per job: $0 in the founding period; $25 after it.
- Density at a = 0.30: n ≥ ln(1 - 0.90) ÷ ln(0.70) = 6.5, so 7; n ≥ ln(1 - 0.95) ÷ ln(0.70) = 8.4, so 9.
- Zone radius: 90 - 15 - 20 = 55 minutes to drive; a 20-mile crossing at 25 miles an hour takes 48 minutes.
