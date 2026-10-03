# SOS SMS, Run 2 of 2: Demand Side (Customers), GTM Builder Discovery Brief

The filled discovery input for the `gtm-builder` skill, customer side. This is what the skill's REQUIRED INPUTS checklist asks for, answered for the people who text in when something breaks at home. The contractor side is a separate run with its own brief in `../run-1-supply-contractors/`, and it runs first.

Read `SKILL-ADAPTATION.md` before Phase 1. The skill is written for B2B SaaS, and this run sells to a consumer in the middle of an emergency, through a two-sided marketplace. Seven of the nine phases carry a documented substitution or note.

**Global rule for the whole run,** taken from the skill's own deck prompt and applied everywhere: if a metric is unknown, keep it as `{TBD}` and do not invent numbers. As far as the source shows, SOS SMS is pre-launch, with no customers, no completed jobs, no arrival times on record, no revenue, and no testimonials, so every proof point, count, and benchmark is `{TBD}` until the founders supply one.

**Source:** `Product Features Matrix _ SOSSMS - Sheet1.csv`, the only file in this repo at commit `bd90d1a`, read 2026-10-01. Plus the instruction given with the request on 2026-10-01: SOS SMS is a two-sided marketplace, with one GTM for the supply side and one for the demand side. A web search on 2026-10-01 found no SOS SMS website. The matrix refers to a founder memo ("a benefit your memo implied") that is not in this repo.

**Before starting:** Run 1's Step 5.2, the founding contractor cohort, sets the launch metro, the trades, and the coverage area this run sells into. Do not start Phase 4 here until it exists.

## Classification

The four facts everything downstream reads from. Identical in both briefs.

| | |
|---|---|
| Archetype | Marketplace. Two-sided, local, on-demand home repair |
| Audiences | Two. Supply: licensed, insured trade contractors. Demand: people with an urgent problem at home. Two runs, never blended |
| Evidence state | Pre-launch, as far as the source shows. It carries no customers, contractors, jobs, revenue, or testimonials, and marks one feature as not yet built. Confirm with the founders |
| Motion | Product-led, no sales team. Demand is self-serve: customers find SOS SMS at the moment of need through bottom-of-funnel search ads and problem-solving pages, then text in. Supply is self-serve: contractors arrive through cold email and a partnership program and sign up by text. Growth follows `../marketplace/speed-to-scale-plan.md` |

## Run order

`gtm-builder` builds one GTM per run, so SOS SMS runs twice. The two runs are never blended into one, because a value proposition written for a plumber and a homeowner at once is true of neither. **This run, demand, goes second.** Three reasons:

1. Every headline promise on this side depends on contractor density. "One text reaches every qualified contractor in your area" and the 90-minute guarantee are only true where enough contractors have joined. Written before supply exists, this run makes promises the network cannot keep, and the 90-minute guarantee turns each broken promise into a refund.
2. The contractor side is a B2B sale, which is closer to the shape `gtm-builder` was written for, so it is the more tractable first run. This run needs a B2C rewrite of Phase 4 and a collapsed Phase 5.
3. Run 1's Step 5.2 decides where SOS SMS launches. This run targets the same place.

This run borrows structure from Run 1's Phases 3, 6, and 7. It does not borrow claims: copy here is checked against Section 6 below.

---

# 1. PROJECT INFORMATION

**Shared by both runs**

| Field | Value |
|---|---|
| Project name | SOS SMS |
| Project website | `{TBD}`. No site found in a 2026-10-01 web search, see open decision 7 |
| Category name | Emergency home repair dispatch by text. A local, two-sided services marketplace |
| Business model | A customer texts one number. The request goes to contractors matched by trade and service area. A contractor accepts and commits to an arrival time. The customer pays a trip charge up front, credited to the job if they go ahead. Contractors pay no subscription and no lead fee. How SOS SMS itself earns money is `{TBD}`, open decision 3 |
| Core thesis, as read from the matrix | The customer's alternative is googling and calling down a list while the damage spreads. The contractor's alternative is paying for leads and sometimes not getting paid for showing up. One text, with the trip charge collected before anyone rolls, answers both |
| Target market | `{TBD}`. The source names no country, region, or metro. Its vocabulary (licensed and insured, trip charge, Google reviews) reads as United States. Confirm |

**This run**

| Field | Value |
|---|---|
| Audience | People with an urgent repair problem at home who need someone now. Homeowners by default. Whether renters, landlords, and property managers are in scope is open decision 1 |
| Niche focus | The launch metro and trades set by Run 1's Step 5.2. Proposed default there: one metro, plumbing and water emergencies first |
| One-liner | Text one number when something breaks at home, and SOS SMS sends the request to the licensed, insured contractors on its network for that trade, who reply with an arrival time when they accept. |

---

# 2. COMPETITORS

The skill wants 5 to 6 named competitors with websites, and its Step 2.1 is an external research step where you source them.

Nothing below names a company. No research has been done yet, and a fabricated competitor would poison Phase 2 and every phase that reads from it. The slate says where each slot comes from. `RESEARCH-PROMPTS.md` Step 0 fills it.

The customer is the buyer in this run, so these are what a person does when something breaks at home. The contractor side has its own slate.

| Slot | Source from | Why it belongs |
|---|---|---|
| 1 | On-demand home repair services that promise a fast arrival for urgent jobs, by app, web, or text | The closest direct substitute, the same promise |
| 2 | Searching "emergency [trade] near me" and calling down the results | Free, and the source's own description of what customers do today: "no googling, no calling down a list" |
| 3 | Asking neighbors, friends, and local community groups, or calling the contractor used last time | Where people solve it without help. The last contractor is the strongest rival whenever they pick up |
| 4 | National home-services marketplaces where customers request quotes from several pros | The better-known option found first in search |
| 5 | Doing it yourself until morning: shutting off the water or power, a repair video, waiting for business hours. For renters, calling the landlord | Not a company. Waiting is the most common choice, and the cost of waiting is the whole pitch |
| 6 | Home warranty plan claim lines, and homeowner's insurance claim lines that send their own contractors | Institutional. For a covered failure they send someone at little or no extra cost to the customer, which beats any trip charge |

**Selection rule:** a competitor earns a slot only if the customer actually considers it in the moment. Not who the founders think of as a rival, who the customer reaches for instead. For a customer at 2 a.m., the real contest is usually slot 2 against slot 5: search and call, or wait. `RESEARCH-PROMPTS.md` Step 0 sources the slate.

---

# 3. CUSTOMER FEATURES LIST

Phase 1 runs per side, so this run rates the customer items only. See `SKILL-ADAPTATION.md`.

The source matrix already rates each item on two axes: Market Relevance (Wanted by All, Most, or Some) and Competitive Differentiation (Unique To Us, A few others can do this, Most vendors can do this). Those ratings are Bryan's, and they are recorded below as **starting hypotheses**. They are self-assessment, not research, and Step 1.1 tests them.

Items marked **stated** came from the source, in its wording. Items marked **candidate** are additions to rate and then keep or cut during Phase 1, and none is confirmed to exist. Section 5 narrows the wording for copy. Phase 1 rates the items under their source names.

| # | Item | Source | Built? | Bryan's rating: Relevance / Differentiation |
|---|---|---|---|---|
| 1 | Instant network access. One text reaches every qualified contractor in your area at once | stated | `{TBD}` | All / A few others |
| 2 | Strong Guarantee. 90-minute guarantee: if no one arrives within 90 minutes, SOS still sends someone and refunds you for the miss | stated | `{TBD}` | All / Most vendors |
| 3 | Text-only access. No app, no phone trees, even at 2 a.m. | stated | `{TBD}` | Most / Unique To Us |
| 4 | Private by design. No app tracking, information never sold, shared with advertisers, or used for retargeting | stated | `{TBD}` | Most / Unique To Us |
| 5 | Verified license and insurance. Every contractor is checked by SOS | stated | `{TBD}` | Most / Most vendors |
| 6 | Google reviews up front | stated | `{TBD}` | Most / Most vendors |
| 7 | Trip charge credited to the job | stated | `{TBD}` | All / Most vendors |
| 8 | Known ETA. The contractor commits to an arrival time when they accept | stated | `{TBD}` | Most / A few others |
| 9 | Relaunch guarantee. If the first contractor can't handle the job, SOS sends a new one and you pay the trip charge once | stated | **No.** The source says "this still needs to be built" | Most / Most vendors |
| 10 | Send photos or video with the request | candidate. The customer half of contractor item 5 | `{TBD}` | not rated |
| 11 | The price, or a price range, for the work before the contractor arrives | candidate | `{TBD}` | not rated |
| 12 | Safety triage: an automatic reply that sends a gas smell, fire, or injury to 911 or the utility first | candidate | `{TBD}` | not rated |

**Matrix rows that cannot be used yet.** Bryan's customer section ends with one rated row with no item text, and Ali's section has 18 rated rows with no item text at all. None can be attributed to an item. Run 1 open decision 6 covers both.

**Deliberately not offered, and not to be rated:**

- **The repair itself.** SOS SMS dispatches. The contractor does the work. Whether SOS SMS stands behind the workmanship is `{TBD}`, and until it is decided, copy does not imply that it does.
- **Emergency services.** SOS SMS is not 911. A gas smell, a fire, or an injury goes to 911 or the utility first.
- **A home warranty or an insurance claim.** SOS SMS does not pay for the repair or file the claim.

Naming these plainly is a selling asset. It is the clearest signal that the guarantees SOS SMS does make are meant literally.

---

# 4. BUSINESS CONTEXT

The skill's fourth input block. None of this is in the source. All four lines need filling, and they are the same answers as Run 1.

```
Current team structure:      {TBD}. The matrix names two contributors, Bryan and Ali. Roles not stated
Monthly burn rate:           {TBD}
Runway remaining:            {TBD}
Channels tried, and results: {TBD}. Proposed default, to confirm: none tried, pre-launch
```

If nothing has been tried yet, write "none tried, pre-launch" rather than leaving it blank. That is a real answer and it changes what Phase 8 should recommend.

**Pricing status: deferred.** The customer-side mechanics are stated: a trip charge paid up front, credited to the job if the customer goes ahead, and a refund under the 90-minute guarantee. The trip charge amount, who sets it, any SOS SMS fee, and the refund amount are all `{TBD}`. Phase 9 still runs, because the take rate structure and the ROI anchors are worth having before the numbers exist.

**Proof set: empty and closed.** A row is added only when all four columns can be filled. A paraphrased proof point is an unapproved proof point.

| Proof point | Exact permitted wording | Source | Recorded permission |
|---|---|---|---|
| none yet | | | |

## Open decisions that change the output

Ordered by what they block. Proposed defaults are proposals, not decisions, and none of them goes into copy until confirmed.

| # | Decision | Blocks | Note |
|---|---|---|---|
| 1 | Who the demand side is: homeowners only, or also renters, landlords, and property managers | Phases 4 and 5, and the run count | Proposed: homeowners. The source speaks to one person with a problem at home ("water's on the floor", "even at 2 a.m."). Property managers buy repeatedly and often have contracted vendors. If they are in scope, they are a third run, not part of this one |
| 2 | Launch metro and trades | Step 0, Phases 2, 4, 8 | Set by Run 1 open decision 1 and Step 5.2. Must match |
| 3 | The customer price: trip charge amount, who sets it (SOS SMS or each contractor), and any SOS SMS fee | Phase 9, and every price in Phase 6 copy | No default. Tied to Run 1 open decision 2, how SOS SMS earns money |
| 4 | 90-minute guarantee scope: when the clock starts (the text or the acceptance), what is refunded, which areas and hours are covered, and what happens when no contractor accepts at all | Phases 6, 7, and 9 | No default. Copy names the scope in the same sentence as the guarantee, see Section 5 |
| 5 | Build status of each item in Section 3, including the relaunch guarantee the source says is unbuilt | Phases 1 and 6 | Proposed: treat every item as planned until confirmed shipped, and launch without the relaunch guarantee in copy until it ships |
| 6 | What customer data goes to the accepting contractor, and whether SOS SMS will ever send marketing texts | Phases 3, 6, and 8, and the privacy claim | Proposed: name, address, phone, and photos go to the accepting contractor only. No marketing texts without a separate opt-in |
| 7 | Name collision | Phase 8 search channels | A 2026-10-01 web search for "SOS SMS" returned several unrelated local plumbing companies with "SOS" in their names. A customer searching the name may reach one of them. Check trademark and search conflicts in the launch metro before spending on the name |
| 8 | Paid search eligibility for a dispatch service | Phase 8 Channel 1, the primary demand channel | Google Local Services Ads are closed to SOS SMS: leads may not be resold or re-routed to businesses not listed in the ad (S70). Standard search ads for plumbing are not on Google's US restricted list (S71), but confirm with Google that a dispatch service may advertise this way before spending, and complete message asset verification (S72). Proposed: confirm in writing before launch |

---

# 5. POSITIONING AND CLAIM CONSTRAINTS

Phase 3 writes positioning statements, Phase 6 writes twenty-seven headlines across nine copy drills, and the deck compresses all of it. All three will reach for the claims below, so the narrowed form has to be here rather than remembered.

**Governing sensitivity:** the reader is in the middle of a problem, often at night. A guarantee that turns out to be hedged costs more trust than one scoped up front, so every guarantee carries its scope in the same sentence. And the name "SOS" invites a reading SOS SMS cannot honor: it is not an emergency service.

| Do not write | Write instead | Counter-example |
|---|---|---|
| One text reaches every qualified contractor in your area at once | One text reaches the licensed, insured contractors on SOS SMS for that trade in your area, all at once | Only contractors who have joined are reached. At launch that is a handful, not every contractor in the area |
| If no one arrives within 90 minutes, SOS still sends someone as soon as possible and refunds you for the miss | If your contractor is not there within 90 minutes of [your text, or their acceptance], you get [the refunded amount] back, and SOS SMS keeps working to get someone to you. [Covered areas and hours.] Fill each bracket from open decision 4 before this line is used | "Refunds you for the miss" does not say what is refunded. The clock start, the covered areas and hours, and the case where no one accepts are all unstated |
| Text-only access. Only we can do this | Works entirely by text. No app to download, no phone tree | Many local contractors already take texts directly, and quote platforms contact customers by text. "Only we" rests on no market scan |
| Private by design. Your information is never sold, shared with advertisers, or used to retarget you | We do not sell your information or use it to target you with ads. Your address and job details go only to the contractor who takes your job | The accepting contractor has to receive the customer's name, address, phone, and photos, and a payment processor handles the card. "Never shared" is false the moment a job is accepted |
| No app tracking your location or activity, extended to "we don't know where you are" | No app, so nothing tracks your location. You share your address only to get someone to your door | The customer texts their address. The no-app part holds; the broader reading does not |
| Every contractor is checked by SOS, so you know they're qualified | SOS SMS checks every contractor's license and insurance before they can take a job | A license and an insurance certificate show eligibility, not workmanship. Some trades and states do not license the work. Insurance can lapse after the check, and the recheck cadence is `{TBD}` |
| Google reviews up front: you see the company's reputation before they show up | See the contractor's Google rating and reviews, where they have them, before they arrive | New businesses have few reviews or none, and SOS SMS does not verify third-party reviews |
| Trip charge credited to the job: the trip charge isn't an extra fee | If you go ahead with the work, the trip charge counts toward the bill | A customer who declines the quote has paid the trip charge and nothing else. In that case it is a fee |
| Known ETA, extended to "guaranteed arrival time" | The contractor gives you an arrival time when they accept | Holds as stated. A commitment is not a guarantee. The guarantee is the 90-minute window, scoped as above |
| Relaunch guarantee: SOS sends a new contractor and you only pay the trip charge once | Nothing, until it ships. Then the source wording, with the trip charge rule from Section 6 row 2 | The source says it "still needs to be built". An unshipped capability in the present tense is the most common way a pack ships something false |
| Emergency service, "help is on the way", or anything a reader could take for 911 | Home repair emergencies, worded as such. Wherever copy invites an urgent text, add: for fire, a gas smell, or anyone hurt, call 911 first | The name invites the reading. A customer who texts SOS SMS instead of calling 911 or the gas utility is the worst outcome the business can have |

Also banned in every phase of this run: any count of customers, contractors, or jobs; any average or typical arrival time; any testimonial or named contractor; any cost-of-delay or water damage statistic without a citation; any savings figure; fastest, cheapest, or best; "licensed and insured" applied to SOS SMS itself, since contractors hold the licenses and SOS SMS checks them; and any promise about the quality or outcome of the repair.

Mechanics, matching the skill's own deck rule: no em dashes. Also avoid leverage, unlock, seamless, robust, streamline, cutting-edge, and empower.

---

# 6. CROSS-SIDE DEPENDENCIES

The marketplace-specific section. Every customer-side promise depends on something the contractor side has to deliver, and several of those dependencies are not yet decided. This table is identical in both briefs. Change it in both or in neither.

| # | Customer-side promise | What it needs from the contractor side | Status | Blocks |
|---|---|---|---|---|
| 1 | 90-minute guarantee: a refund if no one arrives in time | A rule for who funds the refund when a contractor accepts and arrives late. If the contractor forfeits the trip charge, "guaranteed trip charge" is false as written. If SOS SMS pays, it is a cost line | `{TBD}`, Run 1 open decision 3 | Phases 6 and 9, both runs |
| 2 | Relaunch guarantee: a second contractor, and the customer pays the trip charge only once | Whether the second contractor is paid a trip charge, and by whom. If not, "guaranteed trip charge" is false for relaunched jobs | Not built. Rule `{TBD}` | Phases 1, 6, and 9, both runs |
| 3 | One text reaches every qualified contractor in your area at once | A dispatch rule. If every matched contractor sees each job and the first to accept wins, contractors compete for every request, which changes what "lead" means on the supply side | `{TBD}`, Run 1 open decision 4 | Phases 1, 6, and 7, both runs |
| 4 | Private by design: information never sold or shared | The accepting contractor needs the customer's name, address, phone, and any photos to do the job. The privacy claim has to name that exchange | Narrowed in Run 2 Section 5 | Phases 3 and 6, Run 2 |
| 5 | Trip charge credited to the job | Contractors agree, as a condition of joining, to credit it toward completed work. The matrix does not list this among contractor features | Unlisted contractor obligation | Phases 6 and 7, Run 1 |
| 6 | Known ETA | Contractors commit to an arrival time when they accept. Its consequence is row 1 | Obligation `{TBD}` | Phases 6 and 7, both runs |
| 7 | Verified license and insurance | Contractors submit documents before their first job, rechecked on a cadence `{TBD}`. Free to join is not effort-free to join | Process `{TBD}` | Phase 7 onboarding, Run 1 |
| 8 | Zero cost to join, a contractor-side promise | SOS SMS earns money somewhere. A share of the trip charge or the job changes the contractor claim. A customer fee changes the customer price | `{TBD}`, Run 1 open decision 2 | Phase 9, both runs |

**Rule for both runs:** at the end of Phase 6, check every headline against this table. Neither side's copy may promise something the other side's terms do not deliver.
