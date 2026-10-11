# Demand-side research: Steps 1.1, 2.1, and 2.7

For Run 2, the demand side. Since the membership revision (2026-10-11) the demand side is members: homeowners who join SOS SMS before they need it, on a monthly or annual membership, so an emergency takes one text. The member slate research comes first below; the pay per request research from 2026-10-01 follows it, kept because most of it still describes the emergency itself. Competitors come from `step-0-competitor-slates.md`. Source IDs and grades come from `SOURCES.md`. Everything was read through search summaries (S01 to S74 on 2026-10-01, S75 to S94 on 2026-10-11), see `README.md`.

---

## Membership revision (2026-10-11): the member slate

The question changes. A homeowner does not compare SOS SMS with other options in the middle of a flood; they compare it before anything breaks, against the other things a household can join or pay for in advance, and against doing nothing and searching when it happens. The six competitors, D1 to D6, are set in `step-0-competitor-slates.md`, member slate.

### Step 2.1. Competitor deep research, member slate

#### D1. Search and call during the emergency (the status quo)

| Attribute | Finding | Source |
|---|---|---|
| Model | No plan in advance. When something breaks, search "emergency plumber near me" and call down the list | S09, S50 |
| Price in advance | Nothing | |
| What happens in an emergency | Calls go unanswered at night; after-hours service call fees commonly $150 to $250 (C); each contractor sets its own fees | S50, S51 |
| Strengths | Costs nothing until something breaks; total choice | |
| Weaknesses | The search, the calls, and the fees all happen at the worst moment; no promise about arrival | S50, S51 |
| What it means for SOS SMS | The comparison every member makes: a fee every month or year against searching when it happens. A non-member searching mid-emergency is better served by calling a contractor from the results, so the GTM never targets that moment | |

#### D2. Plumber club memberships (Benjamin Franklin Plumbing, Roto-Rooter)

| Attribute | Finding | Source |
|---|---|---|
| Model | One plumbing company's own membership | S75, S76, S77 |
| Price | Benjamin Franklin Plumbing club $10 a month or $120 a year; the Ben Franklin Society $8.25 a month at other locations; a Roto-Rooter plan listed at $19.99 a month (C) | S75, S76, S77 |
| What a member gets | Members' trip charge $49 instead of $89; 10 percent off repairs; priority scheduling; no after-hours fees; one annual plumbing check (Benjamin Franklin) | S75 |
| What happens in an emergency | The member calls that one company and gets priority; the punctuality guarantee pays $5 a minute late, up to $300, on appointments | S40, S75 |
| Strengths | A known brand; discounts; a yearly check; priority | S40, S75 |
| Weaknesses | One company, so one schedule at 2 a.m.; recurring complaints of upselling and pressure to buy service contracts (C) | S52 |
| What it means for SOS SMS | The closest analog and the price anchor: about $10 a month. SOS SMS offers many contractors at once and a money-backed window from the text; it does not offer repair discounts or a reduced trip charge | |

#### D3. Home warranties (American Home Shield, Choice Home Warranty)

| Attribute | Finding | Source |
|---|---|---|
| Model | A service contract that pays for covered repairs and replacements | S20, S68, S79 |
| Price | $47 to $82 a month, averages of $56 and $62.33, plus a service fee of $75 to $125 a visit ($65 to $150), paid even on a denied claim | S56, S79 |
| What happens in an emergency | A claim by phone, app, or online, 24/7; contact within 4 business hours, 48 hours on weekends, by contract; the contract disclaims timely emergency service | S20, S68 |
| Strengths | Pays for covered repairs; one call for many systems | S79 |
| Weaknesses | Slow dispatch by design; denied claims still cost the fee; minimal repairs and repeat fees in complaints (C) | S20, S56 |
| What it means for SOS SMS | A different job: they pay for the repair, SOS SMS gets someone there fast. Many members will hold both. Never contest repair coverage (R21) | |

#### D4. Utility-partner plumbing plans (HomeServe)

| Attribute | Finding | Source |
|---|---|---|
| Model | Repair plans sold through utilities, cities, and associations | S78, S93 |
| Price | Interior plumbing and drainage $16.99 a month ($8.49 first-year promotion), another version $22.99; renews automatically each year | S78 |
| What a member gets | Covered repairs up to $2,500 a call and $5,000 a year; a 30-day waiting period before repairs | S78 |
| Reach | More than 1,300 municipal, utility, and association partners in the US and Canada; over 4.6 million customers | S93 |
| Strengths | Partner trust and partner channels: the plan arrives through a utility the household already pays | S93 |
| Weaknesses | Coverage caps and a waiting period; covers repairs, not speed | S78 |
| What it means for SOS SMS | Proof that home plans are sold before the need through partners, at scale. The affiliate and email channels copy the method, not the product | |

#### D5. Home app memberships (Frontdoor)

| Attribute | Finding | Source |
|---|---|---|
| Model | An app membership with video chats with home experts | S55, S81 |
| Price | Prime $99 a year with three video chats; Unlimited listed at $25 and at $149 a year; Premium $29 a month introductory in 2023. Figures conflict | S81 |
| What happens in an emergency | A video call with an expert who helps diagnose; a visit is a separate booking | S55, S81 |
| Strengths | Help in minutes, from anywhere | S55 |
| Weaknesses | Advice, not a visit; another app | S55 |
| What it means for SOS SMS | The membership most like "help now", but by screen. SOS SMS sends a contractor, by text, with no app | |

#### D6. On-demand marketplaces (Angi, Thumbtack)

| Attribute | Finding | Source |
|---|---|---|
| Model | Free to the homeowner; contractors pay per lead | S03, S06, S44, S45 |
| Price in advance | Nothing | S65, S66 |
| What happens in an emergency | One request brings calls and texts from several pros (Angi); several pros message within minutes (Thumbtack) | S46, S48 |
| Strengths | Free; guarantees on booked work (Happiness Guarantee, Thumbtack Guarantee) | S44, S45 |
| Weaknesses | Being contacted by many; the homeowner still coordinates; no arrival promise | S46, S48 |
| What it means for SOS SMS | The free alternative a member gives up. SOS SMS's answer is one reply, from the one who is coming, inside a guaranteed window | |

#### SOS SMS (ours), member side

| Attribute | Finding | Source |
|---|---|---|
| Model | A monthly or annual membership, joined before the need; card and home address on file | Membership revision, 2026-10-11 |
| Price | Planning values $10 a month or $100 a year (R51, R52); copy uses `{{monthly price}}` and `{{annual price}}` until the launch price is set in Stage 0 | `../marketplace/resolution-register.md` |
| What happens in an emergency | One text. It goes at once to the licensed, insured contractors on SOS SMS matched by trade and area; the first to accept commits to an arrival time; the $99 trip charge goes on the card on file at acceptance and counts toward the repair; if they are not there within 90 minutes of the text, the trip charge comes back (decision 3) | Decisions 3, 5, 6 |
| What it does not do | Pay for the repair, discount the repair, or guarantee the work (R21) | |
| Current state | Pre-launch; nothing is live; memberships open per zone at the density number (R55) | |

### Step 1.1. Member feature demand research

| # | Item | Who already offers it | How central | Evidence members want it | Read |
|---|---|---|---|---|---|
| 1 | A membership joined before the need, card and address on file | Plumber clubs (S75), warranties (S79), utility plans (S78), AAA for cars (S80) | Central to every plan | Strong: 4.6 million households hold one partner-sold plan alone (S93); about 81 percent had a home repair emergency in a year (S82) | Most vendors offer a plan; none offers a plan whose use is one text to many contractors |
| 2 | One text starts dispatch, no forms at the time | Not found in the set. Warranties take claims by phone, app, or online (S68); plumber clubs take calls (S75) | Not offered | Moderate to strong: the worst moment is when calls go unanswered (S50, S51) | A few others at most. The text is a mechanic, never "only we" (S64) |
| 3 | 90-minute arrival guarantee from the text, money back | Benjamin Franklin pays $5 a minute late on appointments (S40); warranties disclaim timely emergency service (S20) | Rare | Strong: no-shows and late arrivals lead the complaints (S51) | A few others |
| 4 | Many contractors reached at once, one reply | Marketplaces send to several, and several call back (S46, S48) | Peripheral as designed | Strong for speed, negative for being contacted by many (S48) | A few others |
| 5 | Arrival time on acceptance | Appointment windows and app arrival times are common (S40, S42, S53) | Common | Strong (S51) | A few others |
| 6 | Trip charge on use, credited to the repair | Plumber clubs reduce the trip charge for members (S75); warranties charge a service fee per visit (S79) | Common | Strong: surprise fees are a top complaint (S50, S51) | Most vendors |
| 7 | Cancel any time, monthly or annual | Common in consumer subscriptions; required in substance by ROSCA and state automatic renewal laws (S87) | Table stakes | Expected; the annual plan's common discount is two months free (S90) | Most vendors |
| 8 | A readiness kit: shutoff guide, home check, seasonal notes | Plumber clubs include a yearly check (S75); HomeServe reports homeowners are unprepared (S82) | Peripheral | Moderate: pipe breaks are the top worry, 49 percent (S82) | A few others |
| 9 | Private by design: no app tracking, never sold, no ad targeting | Not claimed by the set | Not claimed | Moderate (S48, S54) | A few others |
| 10 | License and insurance checked | Common (S09, S18) | Table stakes | Expected | Most vendors |
| 11 | Repair cost coverage | Warranties (S79) and utility plans (S78) | Central to them | Strong for them | Not offered by SOS SMS (R21). Do not contest |
| 12 | Member discounts on repairs, reduced trip charge | Plumber clubs (S75) | Central to clubs | Moderate | Not offered at launch. The trip charge is $99 for everyone, credited to the repair |

### Step 2.7. Review analysis, substituted, member slate

| Competitor | Top positive themes | Top negative themes | Mainly about |
|---|---|---|---|
| D1 Search and call | 1. Free until needed. 2. Choice | 1. Unanswered calls at night (n=2). 2. Surprise after-hours fees (n=2). 3. No-shows (n=1) | The worst moment |
| D2 Plumber clubs | 1. Priority and discounts (n=1, A). 2. Known brand (n=2). 3. A yearly check (n=1, A) | 1. Upselling (n=2). 2. Pressure to buy service contracts (n=1). 3. One company's schedule (inferred) | Price trust |
| D3 Home warranties | 1. Covered repairs for the fee (n=2). 2. 24/7 intake (n=1, A) | 1. Slow dispatch, 48 hours on weekends by contract (n=2). 2. Fees on denied claims (n=1, B). 3. Minimal repairs (n=1) | Speed and claims |
| D4 Utility-partner plans | 1. Arrives through a trusted utility (n=1, A). 2. Low first-year price (n=1, A) | 1. Coverage caps (n=1, A). 2. A 30-day waiting period (n=1, A). 3. Automatic renewal at a higher price (n=1, A) | Coverage limits |
| D5 Frontdoor | 1. Help in minutes by video (n=1). 2. Low annual price (n=1) | 1. Advice, not a visit (inferred). 2. Conflicting prices (n=1) | Help without a visit |
| D6 Marketplaces | 1. Free (n=2). 2. Guarantees on booked work (n=2) | 1. Contacted by many (n=2). 2. Coordination falls on the homeowner (inferred) | Being contacted by many |

### What the member research changed

1. **The plan market already exists, and it is sold before the need, through partners.** One partner-sold plan reaches 4.6 million households through more than 1,300 utilities, cities, and associations (S93). Households already pay $8.25 to $19.99 a month for a plumber's own club (S75 to S77) and $47 to $82 for a warranty (S79). The membership model sits inside known behavior.
2. **No plan in the set makes the emergency itself fast.** Warranties disclaim timely emergency service and dispatch in hours or days (S20); plumber clubs give priority with one company; utility plans cover the repair after a waiting period (S78). A plan whose use is one text, with a money-backed 90-minute window, is the open space.
3. **Emergencies are common across households, rare for each one.** About 81 percent of homeowners reported some home repair emergency in a year, and 20 to 26 percent a blocked or overflowing toilet (S82, S83). Planning value: 0.25 requests per member a year (R58). The membership is sold as readiness, not as frequent use.
4. **The law shapes the channels.** Subscriptions need clear terms, consent, and easy cancellation (S87); affiliates must disclose payment (S88); payments for referrals at a home purchase settlement are barred (S86, S94); email follows CAN-SPAM (S73); marketing texts need written consent (S31).

---

## Pay per request research (2026-10-01), kept

The research below was done for the retired pay per request model. Its findings about the emergency itself (unanswered calls, surprise fees, no-shows, being contacted by many, the national brands' arrival promises) still hold and feed the member slate above. Its competitor set and its read of what the customer pays before arrival describe the retired model.


## Step 2.1. Competitor deep research

### D1. Google search and call down the list

| Attribute | Finding | Source |
|---|---|---|
| Website | https://www.google.com | |
| Tagline | n/a. In the source's own words, the experience SOS SMS replaces: "googling, calling down a list, and scrambling while water's on the floor" | GTM-BRIEF.md |
| Description | The customer searches "emergency plumber near me", sees Local Services Ads with the Google Verified badge, maps results, and organic results, then calls until someone answers. Each contractor sets its own after-hours fees | S09, S50 |
| Strengths | Free; instant; the customer is in control; Google Verified badge shows background, license, and insurance checks | S09, S37 |
| Weaknesses | Unanswered calls at night; after-hours service call fees commonly $150 to $250 (C) and surprise weekend upcharges; Google's consumer Money Back Guarantee ended in late 2025 | S09, S50, S51 |
| Who it serves | Everyone | |
| What the customer pays before arrival | Whatever each contractor charges; often a service call fee | S50 (C) |

### D2. Roto-Rooter

| Attribute | Finding | Source |
|---|---|---|
| Website | https://www.rotorooter.com | S41 |
| Tagline | "Away go troubles down the drain" (jingle since 1954); brand line "Plumbing & Water Cleanup" | S67 |
| Sub-tagline | 24/7, 365 days; no extra charge for nights, weekends, or holidays | S41 |
| Description | National plumbing and water cleanup company with local branches and franchises | S41, S67 |
| Strengths | Always open; no after-hours surcharge; brand everyone knows; typically within two hours for true emergencies (C) | S41 |
| Weaknesses | Upselling and high job prices are recurring complaints (C) | S41, S52 |
| Who it serves | Homeowners and businesses with plumbing and water problems, national | S41 |
| What the customer pays before arrival | No after-hours premium; job price varies | S41 |

### D3. Benjamin Franklin Plumbing

| Attribute | Finding | Source |
|---|---|---|
| Website | https://www.benjaminfranklinplumbing.com | S40 |
| Tagline | "The Punctual Plumber"; "If There's Any Delay, It's You We Pay" | S40 |
| Sub-tagline | $5 for every minute late, up to $300 | S40 |
| Description | National plumbing franchise built around a punctuality guarantee on appointments | S40 |
| Strengths | A specific, money-backed arrival promise; national brand | S40 |
| Weaknesses | Upselling and expensive add-ons are recurring complaints (C). The guarantee covers lateness against a scheduled time, which is a different promise from a guaranteed window for an emergency | S40, S52 |
| Who it serves | Homeowners, national franchise | S40 |
| What the customer pays before arrival | Varies by franchise | |

### D4. Angi

| Attribute | Finding | Source |
|---|---|---|
| Website | https://www.angi.com | S66 |
| Tagline | "And done" | S66 |
| Sub-tagline | Book and pay with Angi for the Happiness Guarantee | S44 |
| Description | Quote marketplace and pre-priced bookings (Angi Services) with upfront prices and instant booking for some services | S44, S47 |
| Strengths | Happiness Guarantee up to the purchase price plus limited damage protection when booked and paid through Angi; upfront prices on pre-priced services; brand recognition | S44, S47 |
| Weaknesses | Homeowners report being flooded with calls and texts from many contractors after one request; Trustpilot 2.2 of 5 | S48, S49 |
| Who it serves | All home services, national | S66 |
| What the customer pays before arrival | Free to request; pre-priced services paid through Angi | S47 |

### D5. Thumbtack

| Attribute | Finding | Source |
|---|---|---|
| Website | https://www.thumbtack.com | S65 |
| Tagline | "Hire Service Pros" (app title) | S65 |
| Sub-tagline | Get prices, read reviews, message pros, hire in the app | S65 |
| Description | Quote marketplace. An emergency request can get messages from several nearby pros in under two minutes (Thumbtack's claim). Customers can contact four to five pros early in a request | S05, S46 |
| Strengths | Fast replies; Thumbtack Guarantee if a job is not done as agreed (reported limits vary, $1,000 to $2,500); free to use | S45, S46 |
| Weaknesses | Several pros contact the customer; the customer still chooses and coordinates in the middle of an emergency | S05 |
| Who it serves | All home services, national | S65 |
| What the customer pays before arrival | Free to request | S46 |

### D6. American Home Shield

| Attribute | Finding | Source |
|---|---|---|
| Website | https://www.ahs.com | S68 |
| Tagline | "Home Warranty Plans by American Home Shield" (page title) | S68 |
| Sub-tagline | Service requests 24/7 by phone, app, or online | S68 |
| Description | Home warranty. The plan holder files a claim and pays a service fee; AHS assigns a network contractor | S20, S56 |
| Strengths | Covered repairs cost only the service fee; 24/7 intake | S56, S68 |
| Weaknesses | Contract terms: contractor contacted within 4 hours on business days and 48 hours on weekends and holidays, with no guarantee of timely emergency service. Complaints of multi-day waits (C) | S20, S56 |
| Who it serves | Plan holders, for covered systems and appliances | S20 |
| What the customer pays before arrival | Service fee typically $75 to $125 (C) | S56 |

### Profiled but not in the tables

| Option | What matters for SOS SMS | Source |
|---|---|---|
| InstaService | The closest model: on-demand by app, "in as little as 60 minutes" depending on availability, upfront pricing. Small public review base, limited metros | S53 |
| Mr. Rooter | Appointment window and upfront flat-rate pricing with no overtime charges | S42 |
| SERVPRO | 24/7 water damage response, 1,900 plus franchises; usually billed through insurance | S43 |
| Nextdoor and neighbors | Nextdoor reports itself as the first place neighbors go to hire maintenance help (45 percent, self-published) | S26 |
| DIY or wait | EPA: dry water-damaged areas within 24 to 48 hours to prevent mold. Triple-I: average water damage and freezing claim $13,954 (2018 to 2022) | S57, S58 |
| Frontdoor app | Video chat with an expert, first chat free, $149 a year unlimited | S55 |
| Jiffy | TrustScore 1.4; complaints include customer phone numbers shared with contractors | S54 |

### SOS SMS (ours), as it stood under pay per request

Filled from `GTM-BRIEF.md` Section 1, not a crawl.

| Attribute | Finding |
|---|---|
| Website | None yet: the zone landing page, from Stage 2 |
| Tagline | Text once, and a vetted contractor is on the way (Phase 6 brand promise) |
| Description | Text one number when something breaks at home. The request goes to the licensed, insured contractors on SOS SMS for that trade in the area, all at once; one accepts with an arrival time; trip charge paid up front and credited to the job if the customer goes ahead; 90-minute guarantee |
| Strengths | By design: one text to every matched contractor; an arrival time on acceptance; the trip charge back on a miss. Nothing live to review |
| Weaknesses | No track record yet; open only in zones at density |
| Who it serves | People with an urgent repair problem at home; homeowners by default |
| What the customer pays before arrival | A $99 trip charge, credited to the job if the customer goes ahead, and a $49 SOS SMS fee (decided 2026-10-03; the fee was retired by the membership revision, 2026-10-11) |

---

## Step 1.1. Customer feature demand research

| # | Our item | Who already offers it | How central | Evidence customers want it | Read |
|---|---|---|---|---|---|
| 1 | One text reaches every matched contractor at once | Thumbtack: several pros message within minutes (S46). Angi sends a request to several pros (S48). Neither is one text, and both lead to several pros contacting the customer | Central to quote marketplaces | Strong for speed; negative for being contacted by many (S48) | A few others. The SOS SMS difference is that only the contractor who accepts contacts the customer |
| 2 | 90-minute arrival guarantee with refund | Benjamin Franklin pays $5 a minute late, up to $300, on appointments (S40). Roto-Rooter typically within two hours, no refund promise (S41). InstaService "as little as 60 minutes", no guarantee (S53). AHS contract disclaims timely emergency service (S20) | Central to Benjamin Franklin's brand | Strong. No-shows and late arrivals are the first complaint theme (S51) | A few others. Refund-backed emergency windows are rare in the set |
| 3 | Text-only access, no app | Many plumbing businesses already take texts through two-way texting software (S64). No network reachable through one text number was found | Peripheral for others | Not directly evidenced. A hypothesis that some customers prefer texting to calling in an emergency | A few others. "Only we" fails |
| 4 | Private by design | Calling a contractor directly shares data with one business. Quote marketplaces share it with several, and homeowners complain about floods of calls (S48); Jiffy complaints include shared numbers (S54) | Not claimed by competitors | Moderate: the flood-of-calls complaint is a privacy complaint in practice | A few others |
| 5 | Verified license and insurance | Google Verified (S09), Angi and Thumbtack background checks, network vetting (S18) | Table stakes | Expected | Most vendors |
| 6 | Google reviews up front | Every search result and marketplace shows ratings | Commodity | Expected | Most vendors |
| 7 | Trip charge credited to the job | Common contractor practice (S28); Roto-Rooter charges no after-hours premium (S41) | Common | Strong: surprise after-hours fees are a top complaint (S50, S51) | Most vendors for the credit itself. The upfront disclosure is the part that is rarer |
| 8 | Known ETA when the contractor accepts | Mr. Rooter appointment windows (S42), Benjamin Franklin scheduled times (S40), app ETAs (S53) | Common | Strong (S51) | A few others |
| 9 | Relaunch guarantee (not built) | Angi and Thumbtack guarantees cover jobs not done as agreed (S44, S45) | Central to marketplace guarantees, in a different form | Moderate | A few others |
| 10 | Photos or video with the request (candidate) | Quote platforms accept photos; Frontdoor does video diagnosis (S55) | Peripheral | Not evidenced | Commodity |
| 11 | Price or price range before arrival (candidate) | Mr. Rooter flat-rate (S42), Angi Services upfront prices (S47), InstaService upfront pricing (S53) | Central to several | Strong: surprise fees complaint (S50, S51) | A few others |
| 12 | Safety triage to 911 or the utility (candidate) | Gas utilities publish it (S60). Not offered by marketplaces in the set | Not offered | Not a demand question. Required on safety grounds | n/a, required |

**What the research changed against Bryan's starting ratings:**

- Item 2, the 90-minute guarantee, moves up from "Most vendors" to "A few others". Only Benjamin Franklin has a money-backed arrival promise in the set, and it covers scheduled appointments.
- Items 3 and 4 cannot be "Unique To Us". Texting a contractor is common, and privacy is not claimed but also not proven unique. Both move to "A few others".
- Candidate item 11, a price range before arrival, turns out to be one of the strongest items on the list. It answers the surprise-fee complaint directly, and three competitors already offer it.

---

## Step 2.7. Review analysis, substituted

Same method as the supply file: frequency is the number of independent sources (n) in which the theme appears. Review-level counts are a follow-up once page access exists.

| Competitor | Top positive themes | Top negative themes | Mainly about |
|---|---|---|---|
| D1 Search and call | 1. Free and immediate (inferred). 2. Verification badge (n=2). 3. Choice of many contractors (inferred) | 1. Unanswered calls at night (n=2). 2. Surprise after-hours fees (n=2). 3. No-shows without notice (n=1) | Not answering, surprise fees |
| D2 Roto-Rooter | 1. Available 24/7 (n=2, A). 2. No after-hours surcharge (n=1, A). 3. Fast response (n=1) | 1. Upselling (n=2). 2. High job prices (n=2). 3. Incomplete repairs needing repeat visits (n=1) | Price and upselling |
| D3 Benjamin Franklin | 1. Punctuality guarantee (n=2, A). 2. Professional brand (n=1). 3. Clear appointment times (n=1) | 1. Upselling (n=2). 2. Expensive (n=2). 3. Pressure to buy service contracts (n=1) | Price and upselling |
| D4 Angi | 1. Happiness Guarantee (n=1, A). 2. Upfront pricing on pre-priced services (n=1, A). 3. Brand recognition (n=1) | 1. Flood of calls and texts after one request (n=2). 2. Low trust rating, 2.2 of 5 (n=1, A). 3. Information shared without clear consent (n=1) | Privacy and being contacted by many |
| D5 Thumbtack | 1. Fast replies, under two minutes claimed (n=1, A). 2. Money-back guarantee (n=2). 3. Free to use (n=1) | 1. Several pros contact the customer (n=1). 2. Customer still coordinates the choice (inferred). 3. Guarantee limits unclear across sources (n=2) | Coordination burden |
| D6 American Home Shield | 1. Covered repairs cost only the service fee (n=1). 2. 24/7 intake (n=1, A). 3. Large network (n=1, dated) | 1. Slow dispatch, up to 48 hours on weekends by contract (n=2, B). 2. Minimal repairs and repeat fees (n=1). 3. High complaint volume (n=1) | Speed |

### What to watch for, and what was found

The brief's hypothesis was that the matrix's features answer three complaints: no-shows, unanswered calls at night, and surprise fees. All three are supported by the sources, at grade C, and they line up with SOS SMS's features: the 90-minute guarantee, one text that reaches someone, and the trip charge stated up front and credited to the job.

Two findings the brief did not predict:

1. **Being contacted by many is its own complaint.** Quote marketplaces fail customers by sending their details to several businesses at once (S48, S54). SOS SMS also sends the request to several contractors, but only the one who accepts contacts the customer. That is the precise, defensible version of "private by design", and it is stronger than the broad version.
2. **The national brands' weakness is price trust, not speed.** Roto-Rooter and Benjamin Franklin are available and fast. Their recurring complaint is upselling (S52). SOS SMS does not control the contractor's quote, so it cannot claim to fix upselling. What it offers is the trip charge stated before anyone rolls. A price range (item 11) is not offered at launch (resolution register R49).

Complaints about workmanship belong to a gap SOS SMS does not close. It checks license and insurance, not the quality of the work, and Phase 6 must not imply otherwise.
