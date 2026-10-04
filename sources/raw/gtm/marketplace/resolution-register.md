# Resolution register

Every unknown and every open founder decision in the SOS SMS go-to-market, resolved in one place. Written 2026-10-03 by the GTM consultant, at the instruction to resolve everything that public data, the research, and the GTM itself can resolve, and to leave no unknown and no decision open in any deliverable. Every file in this repository, the GTM brain, the walkthrough deck, and the Google folder now uses these values.

**What this changes.** The twelve decisions in `cross-side-check.md` Part 3 are decided, and copy that waited on them carries the decided words. Every unknown number has a value with its basis, or the method and the moment that produce it.

**What this does not change.** SOS SMS is pre-launch: nothing is live, and nothing here is a result. No customer, contractor, job, arrival time, testimonial, or proof point is invented. Grade C figures stay internal. Contractor recruiting copy stays in the future tense, and customer copy stays held until its zone opens.

## Four kinds of resolution

| Kind | What it means | How copy treats it |
|---|---|---|
| **Decided** | A choice SOS SMS makes: a price, a rule, a term. Set here, with its basis | Used as written, in copy on the side it belongs to |
| **Planning value** | A number SOS SMS plans with: a target, a threshold, or an operating assumption, with its basis | Used in planning and internal math. Never presented as a measured result. The measured figure replaces it once a zone runs |
| **Counted at** | A fact that cannot exist before launch, resolved to the method that produces it and the stage when it is produced | The method is stated; no number is written until it is counted |
| **Merge field** | A value that differs per zone, per contractor, or per message, written `{{field}}` and filled from a named record when the message is sent | Never typed by hand; the field list is below |

## The twelve decisions, decided 2026-10-03

| # | Decision | Decided | Basis |
|---|---|---|---|
| 1 | Launch metro, first zone, and trades | The United States. Launch in the founders' home metro, in one founding zone: a 10-mile radius drawn around the founding contractors' shops. Plumbing and water emergencies first (burst pipes, leaks, backups, water heaters) | Every source in the research is US (S62, S31, S32, S70). In Stage A the founders cover dispatch gaps and contractor support by hand, which needs them in the metro. The radius is R27. The city's name is the one input no data can supply, so the rule decides it |
| 2 | Revenue model | Contractors pay $0 to join, $0 per request seen or declined, and no subscription or seat fee. The customer pays a $49 SOS SMS fee on each dispatched request. After the founding period, contractors pay $25 per completed paid job, deducted from the trip charge payout; founding contractors keep $0 a job for 12 months after the founding period. SOS SMS takes no share of the repair | The pricing model (`../pricing/pricing-model.md`): the subsidized side is priced from the floor up and held far under the market; a customer fee alone does not pay back paid search on the first job (`speed-to-scale-plan.md`, section 5) |
| 3 | Late-arrival rule and guarantee scope, together | Fault-based (Run 1 option C) plus item B. A contractor can accept only with an arrival time inside the remaining window. The 90 minutes start when the customer confirms the request by text. If no one is there in time, the $99 trip charge comes back automatically: from the contractor's trip charge when the contractor missed the time they committed to, from SOS SMS when SOS SMS caused the miss. Covered areas: the zone, named by its neighborhoods on the zone page. Covered hours: the hour bands where the zone meets its density number, listed on the zone page. If no contractor accepts, the customer is told within 15 minutes and pays nothing | Run 1 Phase 9 option C; Part 2 item B; Run 2 Phase 9 decision 2. The clock starts at the confirming text rather than the first question, so the window runs on the request itself and not on time the customer spends reading the price |
| 4 | Dispatch rule and what contractors see before accepting | Every matched contractor receives the request at once; the first to accept with an arrival time inside the remaining window gets the job. Before accepting, contractors see the problem, any photos or video, and an approximate distance and cross-street area. The address goes only to the contractor who accepts | Part 2 item C; both runs' privacy and "lose the race, lose nothing" copy |
| 5 | Who sets the trip charge | SOS SMS sets one trip charge per trade and zone: $99 for plumbing in the founding zone, day or night. It is paid to the contractor and credited to the repair if the customer goes ahead | Part 2 item A. $99 sits inside the plumbing trip charge band of $75 to $100 (S28, C) and under the $150 to $250 after-hours call fee (S50, C) |
| 6 | Payment provider, hold, capture, and payout | Stripe Connect. The card is authorized when the customer confirms, captured when a contractor accepts, held, and released to the contractor on arrival. Payout to the contractor's bank within 2 business days of arrival, on the provider's standard schedule | Part 2 item H. Online card authorizations are valid about 7 days (S30), far longer than a 90-minute job. Card processing 2.9% plus $0.30 a charge, the planning value in the pricing model |
| 7 | Verification and recheck cadence | License and insurance checked at sign-up, before the first request; rechecked every 6 months and on each policy's expiry date. The same words on both sides | Section 6 row 7. Policies run for a year, so a 6-month check plus the expiry date catches every lapse |
| 8 | Safety handling | Texts that mention gas, smoke, fire, or injury get the safety reply first and are not broadcast until the customer confirms they are safe and the utility or 911 has been called | Part 2 item F (S60) |
| 9 | Carrier registration of the SOS SMS number | One local number in the launch metro's area code, registered for A2P 10DLC (brand and campaign) through the messaging provider before any test text. The same number serves every zone | S32: US carriers block unregistered business texting from local numbers |
| 10 | Name collision | A US trademark search and a search check in the zone, done in Stage 0, before any ad, page, or email. Always the full name SOS SMS; no bids on "SOS plumbing" | Unrelated local plumbing companies use "SOS" |
| 11 | Paid search eligibility | Standard Google search ads only, after Google confirms in writing that a dispatch service may run them for plumbing; never Local Services Ads; message assets only with verified business details. Microsoft Ads runs in every zone alongside | S70, S71, S72, S74 |
| 12 | Paid search ceiling per zone | $275 per paid job while proving a zone; it must fall to $192 by the end of month 6 and to $137 by the end of month 12 | $275 is the plumbing benchmark ($10.49 a click, 7.63 percent click to text, S15, B) at a 50 percent text-to-paid rate. $192 and $137 are the same cost at a 30 and a 50 percent owned share, the owned-share thresholds in R32 |

## Every value

| ID | Kind | What | Resolved to | Basis |
|---|---|---|---|---|
| R01 | Decided | Trip charge | $99 per request, one per trade and zone, day or night; paid to the contractor; credited to the repair if the customer goes ahead | Decision 5 |
| R02 | Decided | SOS SMS fee | $49 per dispatched request, a separate line from the trip charge, charged only when a contractor accepts | Decision 2. Clears its $42 cost floor (refund reserve, card processing, messages, support) and sits just under the $50 value ceiling (pricing model) |
| R03 | Decided | Contractor fee | $25 per completed paid job after the founding period, deducted from the trip charge payout. Never per request, never to join, never for a declined or lost request | Decision 2. At the value ceiling: 20 percent of the about $125 cheapest per-lead cost per booked job (S03, S06, C, internal only). Floor about $10 |
| R04 | Decided | SOS SMS share of the repair, or a rate discount | $0. The price for the work stays the contractor's | Run 1 Phase 9; Part 2 item A |
| R05 | Decided | Founding terms | Founding contractors pay $0 a job through the founding period and for 12 months after it, written into the founding agreement from day one | Decision 2; pricing model |
| R06 | Decided | Founding period | The founding zone's first 6 months open to customers. Every contractor pays $0 a job during it | Long enough for the 4-week proving gate (R33) and the month-6 ceiling step (decision 12) |
| R07 | Decided | Founding list | Opens with the first cold email in the founding zone and closes 60 days after it. Everyone on the list by then is a founding contractor | Four cold emails run 12 days; 60 days leaves room for partners and referrals, and gives the last email a real date |
| R08 | Planning value | Founding cohort target | 9 contractors for plumbing in the founding zone | The density number at acceptance 0.30 for a 95 percent chance that at least one accepts, which buffers nights and freeze spikes (Run 1 Phase 5) |
| R09 | Decided | Take per job | $49 per completed job in the founding period; $74 after it where the contractor fee applies | R02 plus R03. SOS SMS nets about $31 and about $56 per completed job after costs (pricing model, illustrative) |
| R10 | Decided | Refund on a late arrival | The $99 trip charge, back to the card automatically | Decision 3 |
| R11 | Decided | Customer told when no one accepts | Within 15 minutes; the card is never charged | The 10-minute response window plus one rebroadcast |
| R12 | Decided | Contractor response window | 10 minutes, when marked available | Acceptance has to fit the start of the 90-minute window and leave the rest for the drive (R27) |
| R13 | Decided | First refusal on a contractor's own customers | 5 minutes. The after-hours-line acceleration runs only once dispatch supports it | Part 2 item E |
| R14 | Decided | Payout timing | Within 2 business days of arrival | Decision 6 |
| R15 | Decided | Requests outside covered hours | Not dispatched. The customer gets the stop-the-water steps and the safety line, is told no contractor is covering that hour, and pays nothing | Paid search and the guarantee run only in covered hours (Part 2 item G) |
| R16 | Decided | Customers without a card | Dispatch needs a card or a phone wallet through the payment link. Without one, the customer gets the free help by text and pays nothing | Keeps "paid to show up" true for every contractor job (Part 2 item D) |
| R17 | Decided | Second contractor after a miss (the relaunch) | SOS SMS pays the second contractor's trip charge from the SOS SMS fee. Kept out of copy until dispatch supports it | Section 6 row 2; the first contractor's guarantee is not affected |
| R18 | Decided | Partner referral fee and contractor referral reward | None at launch. Partners and contractors are thanked by text; no reward is promised | Run 1 Phase 8 |
| R19 | Decided | Household membership | Not offered at launch | Run 2 Phase 9 lists it as a flag only; one emergency product first |
| R20 | Decided | After-hours surcharge | None: one trip charge, day or night | Run 2 Phase 9: the after-hours premium is the surprise fee customers complain about (S50, S51) |
| R21 | Decided | Guarantee on the repair | Not offered. The guarantee covers the arrival window; the repair is between the customer and the contractor, whose license and insurance SOS SMS checks | Run 2 Phase 3 |
| R22 | Decided | Market and country | The United States | Decision 1 |
| R23 | Decided | Website | One site: the contractor page from Stage 1, then the zone landing page, the guarantee page, and the first five problem guides from Stage 2 | Launch sequence, Stages 1 and 2 |
| R24 | Decided | Taglines and sub tags | Contractors: "Emergency jobs you choose, with the trip paid before you roll." Sub tag: "No lead fees. Paid to show up." Customers: "Text once, and a vetted contractor is on the way." Sub tag: "The price before anyone comes." | Run 1 and Run 2 Step 6.1 brand promises; VP1 and VP2 |
| R25 | Decided | Founder roles | Two roles: a supply lead (recruiting, onboarding, dispatch backup) and a demand lead (search, zone pages, the customer line). Both founders work supply in Stage 1; the roles split when the zone opens in Stage 2 | Mirrors the two runs and the launch sequence |
| R26 | Decided | The unattributed matrix rows | Excluded for good. The source matrix as written, with its attributed rows, is the input | No item text exists to attribute them to |
| R27 | Planning value | Zone radius | 10 miles | 90 minutes less up to 15 to accept and about 20 to get on the road leaves about 55 to drive; a 10-mile radius keeps the longest crossing, 20 miles, inside it |
| R28 | Planning value | Acceptance rate per contractor (a) | 0.30 | The density table: 7 contractors for 90 percent coverage, 9 for 95. Measured per hour band with test requests in Stage 1 |
| R29 | Planning value | Share of requests with a miss SOS SMS causes | 5 percent | The pricing model's refund reserve |
| R30 | Planning value | First text to paid request | 50 percent | The pricing model and the paid acquisition math |
| R31 | Planning value | Card processing and operations per request | 2.9 percent plus $0.30 a charge; operations $5.30 a request (support and disputes $3, platform $2, about 30 texts at $0.01) | Stripe's standard US card price; the pricing model inputs |
| R32 | Planning value | Zone signal thresholds | Acceptance inside the remaining window 90 percent or more; arrival inside the window 95 percent or more; SOS-caused refunds 5 or fewer per 100 requests; first text to paid 50 percent or more; owned share 30 percent or more by the end of month 6 and 50 percent by month 12; contractor activity 60 percent or more accepting at least one job in 30 days | Acceptance matches the 90 percent coverage target; refunds match R29; paid conversion matches R30; owned share matches the ceiling steps in decision 12 |
| R33 | Planning value | Weeks at threshold to prove a zone | 4 consecutive weeks | Long enough to include weekends and one weather swing |
| R34 | Planning value | Ad pause | A zone's campaigns pause automatically when acceptance falls below 90 percent over the trailing 7 days | R32 |
| R35 | Planning value | Runway | At least 18 months at Stage A spending | Covers the founding zone's proving and two more zones proving at once, with margin for them taking longer (`speed-to-scale-plan.md`, section 5) |
| R36 | Planning value | Contractor sign-up time | About 5 minutes by text: trades, area, documents, payout details | Run 1 Phase 7, stage 4 |
| R37 | Planning value | First paid trip | Within 30 days of the zone opening, or of joining if later | Run 1 Phase 5 success metric |
| R38 | Planning value | ICP revenue bands (contractors) | Level 1, the owner-operator: under $500,000 a year. Level 2, the owner with one to five technicians: $500,000 to $3 million a year | Drawn from the team sizes in the ICP; checked in the founding contractors' sign-up survey |
| R39 | Decided | Household income (customers) | Not a targeting criterion. Customers are targeted by zone and by the moment of need | No research ties income to willingness to pay a trip charge |
| R40 | Counted at | Licensed plumbing businesses in the launch metro | Counted from the state license list in Stage 0 | Public license lists |
| R41 | Counted at | Owner-occupied homes in the founding zone | Counted from Census tract data (ACS) when the zone is drawn in Stage 0 | S62 method, at tract level |
| R42 | Counted at | Requests per month in a zone | Measured over the zone's first 8 weeks open | The trigger rate cannot be taken from insurance claim frequency |
| R43 | Counted at | Every SOS SMS result: acceptance, arrival, refunds, conversion, owned share, earnings | Measured from the first request in the founding zone, weekly, against R32 | Nothing is live |
| R44 | Decided | Social-proof headlines | The method line in each drill, which describes how the process works. A result replaces it only when it is real, measured, and permissioned | The fabrication rule in both Phase 6 files |
| R45 | Decided | Supporting proof points | The named record or document in each drill that will show the claim is true from the first job (lists below) | Run 1 and Run 2 Phase 6 |
| R46 | Decided | SOS SMS strengths and weaknesses in the competitive tables | Stated by design, with the weaknesses written plainly: no track record yet, and open only in zones at density | Nothing is live |
| R47 | Counted at | Warranty network discount | Set by each warranty company's rate card | A competitor's terms, not an SOS SMS number |
| R48 | Decided | Team, burn, and channels tried (the briefs' company snapshot) | Team: two founders, Bryan and Ali, roles per R25. Channels tried: none; SOS SMS is pre-launch. Burn and runway: the founders' own figures stay out of the GTM, which sets the requirement instead (R35) | Pre-launch facts |
| R49 | Decided | Price or price range for the work before arrival (Run 2 item 11) | Not offered at launch. The $99 trip charge is stated before dispatch; the price for the work is set by the contractor on site, before any work starts | Run 2 Phase 1 rates it a Hero (wanted by all, offered by few: S42, S47, S53). One emergency product first; a price range needs per-trade price data the founding zone does not yet have. Kept in the matrix, out of copy |
| R50 | Decided | Reaching a person | Text HELP: a person from SOS SMS replies by text within 15 minutes in covered hours; STOP ends all texts. The first reply and every message asset say so | S72: message assets need automated-reply disclosure, a stated response time, and a defined human handoff; carrier messaging rules require HELP and STOP replies. 15 minutes matches R11 |

## Proof points per copy drill (R45)

| Drill | Contractors | Customers |
|---|---|---|
| 1 | The terms on one page: $0 to receive a request, in writing before sign-up | Each request's log: who received it and when the first contractor accepted |
| 2 | The dispatch rule in the terms: every matched contractor sees the request at once | Every acceptance text carries the contractor's name and committed arrival time |
| 3 | Declines carry no penalty, written in the terms; the request history shows what reached you | The guarantee page, published before the zone opens; refunds paid automatically |
| 4 | Every job record shows the trip charge captured before you roll | The saved contact card, sent after every job |
| 5 | The payout timeline in the terms: within 2 business days of arrival | The broadcast text contractors receive, shown on the privacy page |
| 6 | Every request carries the customer's agreement to the trip charge, by text, with its time | The privacy policy in plain words, linked from the first reply |
| 7 | Every request carries the time of the customer's confirming text | The trip charge in the first reply, $99, credited to the repair |
| 8 | Your trades and area, set at sign-up, shown on every request | License and insurance checked at sign-up, every 6 months, and on each policy's expiry date |
| 9 | Customer photos and video attached to the request before you accept | The contractor's Google rating and review link in every acceptance text, where they have one |

## Merge fields

Written `{{field}}` in templates and filled automatically when the message, page, or ad is produced. None is typed by hand.

| Field | Filled from |
|---|---|
| `{{first name}}`, `{{name}}`, `{{business}}` | The contractor list record (cold email) or the sign-up record |
| `{{SOS SMS number}}`, `{{number}}` | The registered SOS SMS number (decision 9) |
| `{{zone}}`, `{{zone name}}`, `{{zone neighborhoods}}`, `{{launch metro}}` | The zone record (decision 1) |
| `{{covered hours}}` | The zone record: the hour bands at the density number (decision 3) |
| `{{trade}}`, `{{trades}}` | The contractor's sign-up, or the zone's open trades |
| `{{url}}`, `{{link}}`, `{{terms link}}`, `{{contractor page}}` | The page addresses on the SOS SMS site (R23) |
| `{{code}}` | The partner's code in the partnership program |
| `{{founding close date}}` | The founding list's close date: 60 days after the first email (R07) |
| `{{score}}`, `{{top two}}`, `{{top three}}`, `{{top-scoring question}}`, `{{result}}`, `{{cost per lead ÷ close rate}}` | The contractor's own answers in the Job Leak Scorecard or the Lead Cost Check |
| `{{their number}}` | The customer's own phone number, for the contact card |
| `{{partner}}` | The partner's name, from the signed partner agreement |
| `{{share}}`, `{{estimate from your answers}}` | Computed from the survey's own responses, or the respondent's own answers |
| `{{sender name}}`, `{{postal address}}`, `{{opt-out link}}` | The email sending setup: the sending founder, SOS SMS's postal address, and the platform's one-click opt-out (S73) |
| `{{contractor name}}`, `{{arrival time}}`, `{{rating}}` | The request record: the accepting contractor's sign-up, their committed arrival time, and their Google rating where they have one |

## Arithmetic, checked

- Before the repair, a customer pays two lines: the $99 trip charge and the $49 SOS SMS fee. Never shown as one total in copy.
- SOS SMS fee cost floor: refund reserve 0.05 × $99 = $4.95; card processing 2.9% × $99 + $0.30 = $3.17; messages 30 × $0.01 = $0.30; support and platform $5.00. Total $13.42, ÷ (1 - 0.65 - 0.029) = $41.81, about $42. The fee is $49.
- Take per job: $49 in the founding period; $49 + $25 = $74 after it.
- Density at a = 0.30: n ≥ ln(1 - 0.90) ÷ ln(0.70) = 6.5, so 7; n ≥ ln(1 - 0.95) ÷ ln(0.70) = 8.4, so 9.
- Paid cost per paid job: $10.49 ÷ 0.0763 ÷ 0.50 = $274.97, about $275. At 30 percent owned: $275 × 0.70 = $192.50, about $192. At 50 percent owned: $275 × 0.50 = $137.50, about $137.
- Zone radius: 90 - 15 - 20 = 55 minutes to drive; a 20-mile crossing at 25 miles an hour takes 48 minutes.
