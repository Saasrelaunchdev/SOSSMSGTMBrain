# SOS SMS, Run 2 of 2: Demand Side (Members), GTM Builder Discovery Brief

The filled discovery input for the `gtm-builder` skill, demand side. This is what the skill's REQUIRED INPUTS checklist asks for, answered for the homeowners who join SOS SMS before something breaks, so that when it does, the emergency takes one text. The contractor side is a separate run with its own brief in `../run-1-supply-contractors/`, and it runs first.

**Revised 2026-10-11, the membership revision.** The demand side is a monthly or annual membership, joined before the need. A member's card and home address are on file from the day they join, so in an emergency a member sends one text and dispatch starts: no search, no sign-up, no payment entry, no confirming reply. Members are reached before anything breaks, through lower-cost channels led by affiliates and email, with search and SEO pages for sign-ups. The pay per request model this brief described before (a $49 SOS SMS fee per request, agreed by text at the emergency, customers bought through emergency search ads) is retired. The run's folder keeps its name, `run-2-demand-customers`, so every link still resolves.

**Revised 2026-10-20, the tiers revision.** One membership covers plumbing, HVAC, and electrical emergencies, on three plans: Basic ($10 a month or $100 a year), Plus ($15 or $150, with the 90-minute guarantee and up to 5 phones that can text for the home), and Premier ($35 or $350, with a 12-month credit, one trip charge a year paid by SOS SMS, a second home, and up to 10 phones). A late arrival keeps its trip charge; the guarantee credits the membership paid in the 6 months (Plus) or 12 months (Premier) before the request. A no-show returns the trip charge in full. No paid search at launch. Where this file and `../../marketplace/resolution-register.md` differ, the register wins.

Read `SKILL-ADAPTATION.md` before Phase 1. The skill is written for B2B SaaS, and this run sells a household membership through a two-sided marketplace. Seven of the nine phases carry a documented substitution or note.

**Global rule for the whole run,** taken from the skill's own deck prompt and applied everywhere: never invent a number. An unknown metric is resolved to a planning value with its basis, or to the method and stage that will count it (`../marketplace/resolution-register.md`). SOS SMS is pre-launch, with no members, no completed jobs, no arrival times on record, no revenue, and no testimonials, so no proof point, count, or result exists, and none is written.

**Source:** `Product Features Matrix _ SOSSMS - Sheet1.csv`, the only file in this repo at commit `bd90d1a`, read 2026-10-01, plus the instruction given with the request on 2026-10-01: SOS SMS is a two-sided marketplace, with one GTM for the supply side and one for the demand side. Then the membership revision (2026-10-11), which sets the demand-side model: a monthly or annual membership joined before the need, one text in an emergency, and pre-need channels led by affiliates and email. A web search on 2026-10-01 found no SOS SMS website.

**Before starting:** Run 1's Step 5.2, the first contractor cohort, sets the launch metro, the trades, and the coverage area this run sells into. Do not start Phase 4 here until it exists.

## Classification

The four facts everything downstream reads from. Identical in both briefs.

| | |
|---|---|
| Archetype | Marketplace. Two-sided, local home repair network: a membership on the demand side, free sign-up on the supply side |
| Audiences | Two. Supply: licensed, insured trade contractors. Demand: homeowners who join before they need it (members). Two runs, never blended |
| Evidence state | Pre-launch. The source carries no members, contractors, jobs, revenue, or testimonials, and marks one feature as not yet built |
| Motion | Product-led, no sales team. Demand is self-serve: homeowners join before anything breaks, reached through affiliates and email first, then search and SEO pages for sign-ups and the product's own loops; in an emergency a member sends one text. Supply is self-serve: contractors arrive through cold email and a partnership program and sign up by text. Growth follows `../marketplace/speed-to-scale-plan.md` |

## Run order

`gtm-builder` builds one GTM per run, so SOS SMS runs twice. The two runs are never blended into one, because a value proposition written for a plumber and a homeowner at once is true of neither. **This run, demand, goes second.** Three reasons:

1. Every headline promise on this side depends on contractor density. "One text reaches every qualified contractor in your area" and the 90-minute guarantee are only true where enough contractors have joined. A membership sold before supply exists sells a promise the network cannot keep, and the 90-minute guarantee turns each broken promise into a refund.
2. The contractor side is a B2B sale, which is closer to the shape `gtm-builder` was written for, so it is the more tractable first run. This run needs a B2C rewrite of Phase 4 and a household Phase 5.
3. Run 1's Step 5.2 decides where SOS SMS launches. This run sells memberships in the same place.

This run borrows structure from Run 1's Phases 3, 6, and 7. It does not borrow claims: copy here is checked against Section 6 below.

---

# 1. PROJECT INFORMATION

**Shared by both runs**

| Field | Value |
|---|---|
| Project name | SOS SMS |
| Project website | None yet: no site found in a 2026-10-01 web search. Decided: one site, the contractor page from Stage 1, the readiness scorecard and the launch list from Stage 1, then the membership page and guides from Stage 2 (`../marketplace/resolution-register.md`, R23) |
| Category name | Emergency home repair membership, by text. A local, two-sided home repair network |
| Business model | Homeowners join before they need it, on a monthly or annual membership, with their card and home address on file. In an emergency a member texts one number; the request goes at once to contractors matched by trade and service area; the first to accept commits to an arrival time. The $99 trip charge is charged to the card on file when a contractor accepts and is credited to the job if the member goes ahead. Contractors pay no subscription and no lead fee. SOS SMS earns the membership and $25 per completed paid job from the contractor, from the first job (decision 2, revised 2026-10-11) |
| Core thesis | The homeowner's alternative is searching and calling down a list while the damage spreads. A member skips all of it, because joining happened before anything broke: one text, and help is on the way. The contractor's alternative is paying for leads and sometimes not getting paid for showing up. Members fund the network; contractors join free and are paid before they roll |
| Target market | The United States (decision 1). The source names no country, region, or metro; its vocabulary (licensed and insured, trip charge, Google reviews) reads as United States, and every source in the research is US |

**This run**

| Field | Value |
|---|---|
| Audience | Homeowners in an open zone who join before they need it (members). Property managers would be a separate run |
| Niche focus | Plumbing and water emergencies, in the launch zone in the founders' home metro (decision 1), the same as Run 1 |
| One-liner | Join SOS SMS before something breaks. When it does, text one number: the licensed, insured contractors on SOS SMS for that trade see it at once, and the first who can come replies with an arrival time. |

---

# 2. COMPETITORS

The skill wants 5 to 6 named competitors with websites, and its Step 2.1 is an external research step where you source them. The slots below say where each one comes from; `RESEARCH-PROMPTS.md` Step 0 fills them, and `../research/step-0-competitor-slates.md` holds the member slate (2026-10-11).

The member is the buyer in this run, so these are what a household sets up, or relies on, before anything breaks. The contractor side has its own slate.

| Slot | Source from | Why it belongs |
|---|---|---|
| 1 | A plumbing company's own club membership: priority, discounts, a yearly check | The closest product, paid in advance, and the price anchor |
| 2 | Nothing in advance: search "emergency plumber near me" and call down the results when it happens | Free until needed, and the choice every non-member is making. The source's own description of the moment: "no googling, no calling down a list" |
| 3 | Neighbors, friends, local community groups, or the contractor used last time | Where people solve it without help. The last contractor is the strongest rival whenever they pick up |
| 4 | Free on-demand marketplaces where a request goes to several pros | The free alternative a member gives up |
| 5 | Doing it yourself until morning: shutting off the water, a repair video, waiting for business hours | Not a company. The readiness kit answers it |
| 6 | Plans that pay for repairs: home warranties, and repair plans sold through utilities and cities | Paid in advance and often already held. They pay for the repair; they do not promise speed |

**Selection rule:** a competitor earns a slot if a household would pay for it, or choose to rely on it, before anything breaks. Not who the founders think of as a rival: what the household sets up instead, or what it does by not setting anything up.

---

# 3. MEMBER FEATURES LIST

Phase 1 runs per side, so this run rates the member items only. See `SKILL-ADAPTATION.md`.

The source matrix rates each of its items on two axes: Market Relevance (Wanted by All, Most, or Some) and Competitive Differentiation (Unique To Us, A few others can do this, Most vendors can do this). Those ratings are Bryan's, and they are recorded below as **starting hypotheses**. They are self-assessment, not research, and Step 1.1 tests them.

Items marked **stated** came from the source, in its wording. Items marked **model** come from the membership revision (2026-10-11). Items marked **candidate** are additions to rate and then keep or cut during Phase 1. Section 5 narrows the wording for copy.

| # | Item | Source | Built? | Bryan's rating: Relevance / Differentiation |
|---|---|---|---|---|
| 1 | Instant network access. One text reaches every qualified contractor in your area at once | stated | Planned | All / A few others |
| 2 | Strong Guarantee. 90-minute guarantee: if no one arrives within 90 minutes, SOS still sends someone and refunds you for the miss | stated | Planned | All / Most vendors |
| 3 | Text-only access. No app, no phone trees, even at 2 a.m. | stated | Planned | Most / Unique To Us |
| 4 | Private by design. No app tracking, information never sold, shared with advertisers, or used for retargeting | stated | Planned | Most / Unique To Us |
| 5 | Verified license and insurance. Every contractor is checked by SOS | stated | Planned | Most / Most vendors |
| 6 | Google reviews up front | stated | Planned | Most / Most vendors |
| 7 | Trip charge credited to the job | stated | Planned | All / Most vendors |
| 8 | Known ETA. The contractor commits to an arrival time when they accept | stated | Planned | Most / A few others |
| 9 | Relaunch guarantee. If the first contractor can't handle the job, SOS sends a new one and you pay the trip charge once | stated | **No.** The source says "this still needs to be built" | Most / Most vendors |
| 10 | Send photos or video with the request | candidate. The member half of contractor item 5 | Planned (decision 4) | not rated |
| 11 | The price, or a price range, for the work before the contractor arrives | candidate | Not planned at launch: the trip charge is stated at joining; the price for the work is the contractor's, given on site | not rated |
| 12 | Safety triage: an automatic reply that sends a gas smell, fire, or injury to 911 or the utility first | candidate | Planned (decision 8) | not rated |
| 13 | Membership, monthly or annual, joined before the need | model | Planned | not rated |
| 14 | Card and home address on file from joining, so the emergency is one text: no forms, no payment entry, no confirming reply | model | Planned | not rated |
| 15 | Readiness kit at joining: the shutoff guide, the home check (Text READY), the saved contact card | candidate | Planned | not rated |

**Matrix rows not used.** Bryan's customer section ends with one rated row with no item text, and Ali's section has 18 rated rows with no item text at all. None can be attributed to an item, so both are excluded for good (R26).

**Deliberately not offered, and not to be rated:**

- **The repair itself.** SOS SMS dispatches. The contractor does the work. SOS SMS does not stand behind the workmanship (R21): the guarantee covers the arrival window, and copy never implies it covers the repair.
- **Emergency services.** SOS SMS is not 911. A gas smell, a fire, or an injury goes to 911 or the utility first.
- **A home warranty or an insurance claim.** A membership does not pay for the repair or file the claim. It gets someone there.
- **Member discounts on the repair or a reduced trip charge.** Not offered at launch: the $99 trip charge is the same for everyone and credited to the repair.

Naming these plainly is a selling asset. It is the clearest signal that the promises SOS SMS does make are meant literally.

---

# 4. BUSINESS CONTEXT

The skill's fourth input block. None of this is in the source. All four lines are resolved in `../marketplace/resolution-register.md` (R25, R35, R48), and they are the same answers as Run 1.

```
Current team structure:      Two founders, Bryan and Ali, the matrix's two contributors: a supply lead and a demand lead, split at Stage 2
Monthly burn rate:           Kept out of the GTM; the plan sets the requirement instead (runway, below)
Runway remaining:            At least 18 months at Stage A spending, to cover several proving zones at once
Channels tried, and results: None tried, pre-launch
```

If nothing has been tried yet, write "none tried, pre-launch" rather than leaving it blank. That is a real answer and it changes what Phase 8 should recommend.

**Pricing status: revised 2026-10-20.** The demand side is a membership on three plans, monthly or annual. Decided: Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350, two months free on each (R51, R52, R65, R66), Basic at the closest analog's price (a plumber's club at $10 a month, S75; the band runs $8.25 to $19.99 for plumber clubs, S75 to S77, and $16.99 to $22.99 for a utility-partner plumbing plan, S78). Copy states the prices, and the membership page shows Plus on the annual plan first. The $99 trip charge, set by SOS SMS per trade and zone and the same in all three trades, is paid on use and credited to the repair; the guarantee credits 6 months of membership on Plus and 12 on Premier on a late arrival; there is no fee per request (decisions 2, 3, and 5). Phase 9 still runs, because the structure, the unit economics, and the acquisition ceiling are worth having before measured numbers exist. Dispatch starts 30 days after joining on the monthly plan and at once on the annual plan (R54).

**Proof set: empty and closed.** A row is added only when all four columns can be filled. A paraphrased proof point is an unapproved proof point.

| Proof point | Exact permitted wording | Source | Recorded permission |
|---|---|---|---|
| none yet | | | |

## Decisions that change the output, decided

Ordered by what they blocked. Rows 1 to 8 were decided on 2026-10-03 (`../marketplace/cross-side-check.md` Part 3, `../marketplace/resolution-register.md`); rows 3, 4, 6, and 8 were revised and row 9 added by the membership revision on 2026-10-11.

| # | Decision | Blocked | Decided |
|---|---|---|---|
| 1 | Who the demand side is: homeowners only, or also renters, landlords, and property managers | Phases 4 and 5, and the run count | Homeowners. Property managers buy repeatedly and often have contracted vendors; they would be a third run, not part of this one |
| 2 | Launch metro and trades | Step 0, Phases 2, 4, 8 | Plumbing and water emergencies in one launch zone in the founders' home metro (decision 1), the same as Run 1 |
| 3 | The member price: what a member pays, and when | Phase 9, and every price in Phase 6 copy | Three plans, monthly or annual: Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350 (R51, R52, R65, R66), Plus on the annual plan shown first; the $99 trip charge on use, set by SOS SMS per trade and zone and credited to the repair; no fee per request (decisions 2 and 5, revised 2026-10-20) |
| 4 | 90-minute guarantee scope: when the clock starts, what is refunded, which areas and hours are covered, and what happens when no contractor accepts at all | Phases 6, 7, and 9 | Revised 2026-10-20: on Plus and Premier; 90 minutes from the member's request text; a late arrival keeps its trip charge and credits the membership paid in the 6 months (Plus) or 12 months (Premier) before the request (R65); a no-show returns the trip charge in full; covered: the zone's neighborhoods, named on the membership page, at any hour, because a zone opens only when every trade and hour band meets the density number (R15, R55); with no acceptance, the member is told within 15 minutes and is not charged; after a miss, NEXT sends the request to the other contractors (decision 3, R17, revised 2026-10-11). Copy names the scope in the same sentence as the guarantee, see Section 5 |
| 5 | Build status of each item in Section 3, including the relaunch guarantee the source says is unbuilt | Phases 1 and 6 | Every item is planned until shipped. The relaunch is decided as NEXT after a miss (R17) and is described as planned, like every other capability |
| 6 | What member data goes to the accepting contractor, and how SOS SMS markets to members | Phases 3, 6, and 8, and the privacy claim | Name, the address on file, phone, and photos go to the accepting contractor only. No marketing texts without a separate written opt-in (S31). Email to members and homeowners follows CAN-SPAM (S73) |
| 7 | Name collision | Phase 8 search channels | A 2026-10-01 web search for "SOS SMS" returned several unrelated local plumbing companies with "SOS" in their names. Decided: a US trademark search and a search check in the zone in Stage 0, before any spend on the name (decision 10) |
| 8 | Paid search, and what it is for | Phase 8 search channel | No paid search at launch; never Local Services Ads (S70, S71). Search volume for SOS SMS by name is counted once a zone has been open 6 months (R68) (decision 11, revised 2026-10-20) |
| 9 | The demand-side product: pay per request, or a membership | Every phase | Decided 2026-10-11, the membership revision: a monthly or annual membership, joined before the need; in an emergency, one text starts dispatch. Pre-need channels: affiliates and email lead (R61, S73, S86 to S88, S93, S94) |

---

# 5. POSITIONING AND CLAIM CONSTRAINTS

Phase 3 writes positioning statements, Phase 6 writes twenty-seven headlines across nine copy drills, and the deck compresses all of it. All three will reach for the claims below, so the narrowed form has to be here rather than remembered.

**Governing sensitivity:** the reader is deciding before anything has broken, so every promise is read twice: once at joining, and again in the middle of a problem, often at night. A guarantee that turns out to be hedged costs more trust than one scoped up front, so every guarantee carries its scope in the same sentence. And the name "SOS" invites a reading SOS SMS cannot honor: it is not an emergency service.

| Do not write | Write instead | Counter-example |
|---|---|---|
| One text reaches every qualified contractor in your area at once | One text reaches the licensed, insured contractors on SOS SMS for that trade in your area, all at once | Only contractors who have joined are reached. At launch that is a handful, not every contractor in the area |
| If no one arrives within 90 minutes, SOS still sends someone as soon as possible and refunds you for the miss | On Plus and Premier: if your contractor gets there after 90 minutes from your text, we credit the membership before your request: 6 months on Plus, 12 on Premier. If no one is there, text NEXT and your request goes to the other contractors. Anywhere in {{zone neighborhoods}}, at any hour (decision 3, R17, R65) | "Refunds you for the miss" does not say what is refunded. The clock start, the covered areas and hours, and the case where no one accepts are all unstated |
| Covered 24/7, any time, whenever something breaks | Any hour, anywhere in {{zone neighborhoods}}, named on the membership page | A zone opens only when every hour band meets the density number (R15, R55), so "any hour" is true in an open zone and only there. "24/7" stays out of copy: it reads as an emergency service |
| Text-only access. Only we can do this | Works entirely by text. No app to download, no phone tree | Many local contractors already take texts directly, and quote platforms contact homeowners by text. "Only we" rests on no market scan |
| Private by design. Your information is never sold, shared with advertisers, or used to retarget you | We do not sell your information or use it to target you with ads. Your address and job details go only to the contractor who takes your job | The accepting contractor has to receive the member's name, address, phone, and photos, and a payment processor holds the card. "Never shared" is false the moment a job is accepted |
| No app tracking your location or activity, extended to "we don't know where you are" | No app, so nothing tracks your location. Your home address is on file only to get someone to your door | The address is on file from joining. The no-app part holds; the broader reading does not |
| Every contractor is checked by SOS, so you know they're qualified | SOS SMS checks every contractor's license and insurance before they can take a job | A license and an insurance certificate show eligibility, not workmanship. Insurance can lapse after the check, so SOS SMS rechecks every 6 months and on each policy's expiry date |
| Google reviews up front: you see the company's reputation before they show up | See the contractor's Google rating and reviews, where they have them, before they arrive | New businesses have few reviews or none, and SOS SMS does not verify third-party reviews |
| Trip charge credited to the job: the trip charge isn't an extra fee. Or: no charge when you use it | If you go ahead with the work, the $99 trip charge counts toward the bill | The membership does not include the visit. A member who declines the quote has paid the trip charge, and in that case it is a fee |
| Known ETA, extended to "guaranteed arrival time" | The contractor gives you an arrival time when they accept | A commitment is not a guarantee. The guarantee is the 90-minute window, scoped as above |
| Relaunch guarantee: SOS sends a new contractor and you only pay the trip charge once | If no one is there after 90 minutes, text NEXT: the first contractor's $99 comes back and your request goes to the other contractors on SOS SMS; you pay one trip charge for the visit that happens (R17). Launch-day copy, in the future tense until it ships | The relaunch covers a missed window. A contractor who arrives in time keeps the trip charge, as with any call-out, so "pay once" is never promised for that case |
| It's like a home warranty; your repairs are covered | SOS SMS gets someone to your door. It does not pay for the repair | A membership pays for dispatch and the guarantee, not the work. A covered failure under a warranty is usually cheaper through the warranty |
| Save money; pays for itself; never worry again | What membership includes, what it costs, and that you can cancel any time | No savings figure exists. A household with no emergency in a year has paid the membership and used nothing |
| Emergency service, or anything a reader could take for 911 | Home repair emergencies, worded as such. "One text, and help is on the way" is the member promise; wherever copy invites an urgent text, add: for fire, a gas smell, or anyone hurt, call 911 first | The name invites the reading. A member who texts SOS SMS instead of calling 911 or the gas utility is the worst outcome the business can have |

Also banned in every phase of this run: any count of members, contractors, or jobs; any average or typical arrival time; any testimonial or named contractor; any cost-of-delay or water damage statistic without a citation; any savings figure; fastest, cheapest, or best; "licensed and insured" applied to SOS SMS itself, since contractors hold the licenses and SOS SMS checks them; any promise about the quality or outcome of the repair; a free trial or a first month free, which is not offered; and any price other than the decided $10 a month and $100 a year.

Mechanics, matching the skill's own deck rule: no em dashes. Also avoid leverage, unlock, seamless, robust, streamline, cutting-edge, and empower.

---

# 6. CROSS-SIDE DEPENDENCIES

The marketplace-specific section. Every member-side promise depends on something the contractor side has to deliver, and each of those dependencies was decided on 2026-10-03 and carried into the membership revision on 2026-10-11 (`../marketplace/cross-side-check.md` Part 3). This table is identical in both briefs. Change it in both or in neither.

| # | Member-side promise | What it needs from the contractor side | Status | Blocks |
|---|---|---|---|---|
| 1 | 90-minute guarantee: a refund if no one arrives in time | A rule for who funds the refund when a contractor accepts and arrives late. If the contractor forfeits the trip charge, "guaranteed trip charge" is false as written. If SOS SMS pays, it is a cost line | Decided (decision 3): fault-based. A contractor who misses their committed time funds the refund from the trip charge; SOS SMS pays for misses it causes. The clock runs from the member's request text | Phases 6 and 9, both runs |
| 2 | Relaunch guarantee: a second contractor, and the member pays the trip charge only once | Whether the second contractor is paid a trip charge, and by whom. If not, "guaranteed trip charge" is false for relaunched jobs | Decided 2026-10-11 (R17): after a miss, the $99 comes back and the member can text NEXT; the new acceptance is a new request with its own trip charge, so every contractor who arrives is paid and SOS SMS pays no second trip charge | Phases 1, 6, and 9, both runs |
| 3 | One text reaches every qualified contractor in your area at once | A dispatch rule. If every matched contractor sees each job and the first to accept wins, contractors compete for every request, which changes what "lead" means on the supply side | Decided (decision 4): all matched at once, first to accept | Phases 1, 6, and 7, both runs |
| 4 | Private by design: information never sold or shared | The accepting contractor needs the member's name, address on file, phone, and any photos to do the job. The privacy claim has to name that exchange | Narrowed in Run 2 Section 5 | Phases 3 and 6, Run 2 |
| 5 | Trip charge credited to the job | Contractors agree, as a condition of joining, to credit it toward completed work. The matrix does not list this among contractor features | Unlisted contractor obligation | Phases 6 and 7, Run 1 |
| 6 | Known ETA | Contractors commit to an arrival time when they accept. Its consequence is row 1 | Decided: an arrival time inside the remaining window, in the terms on one page | Phases 6 and 7, both runs |
| 7 | Verified license and insurance | Contractors submit documents before their first job, rechecked every 6 months and on each policy's expiry date. Free to join is not effort-free to join | Decided (decision 7): documents by text at sign-up, checked before the first request | Phase 7 onboarding, Run 1 |
| 8 | Zero cost to join, a contractor-side promise | SOS SMS earns money somewhere. A share of the trip charge or the job changes the contractor claim | Decided (decision 2, revised 2026-10-11): members pay a monthly or annual membership; contractors pay $25 per completed paid job from the first job | Phase 9, both runs |

**Rule for both runs:** at the end of Phase 6, check every headline against this table. Neither side's copy may promise something the other side's terms do not deliver.
