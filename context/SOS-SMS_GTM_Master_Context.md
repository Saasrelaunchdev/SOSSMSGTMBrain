---
title: SOS SMS Go-To-Market Master Context
project: SOS SMS
type: gtm_context_file
purpose: Single source of truth for any AI agent executing SOS SMS go-to-market work.
version: 1.5
last_updated: 2026-10-21
status_notes: Pre-launch. Nothing is live, so there are no contractors, members, jobs, revenue, arrival times, or testimonials, and no result exists to cite. Every product capability is PLANNED, never shipped. The membership revision (2026-10-11) made the demand side a membership joined before the need, with the card and home address on file, so an emergency is one text, and retired the fee-free launch period (R05 to R07). The tiers revision (2026-10-20) put plumbing, HVAC, and electrical in one membership, kept the trip charge on a late arrival, and took paid search out of the launch. The pricing revision (2026-10-21) decided three plans, Basic $10 a month or $100 a year, Plus $15 or $150 (most popular, the 90-minute guarantee as a 6-month credit, up to 5 phones), Premier $35 or $350 (a 12-month credit, a trip charge a year paid by SOS SMS, a second home, up to 10 phones), and one acquisition ceiling per plan. The twelve founder decisions are decided (2026-10-03; revised 2026-10-11, 2026-10-20, and 2026-10-21). Every other value is resolved in `reference/resolution-register.md`: decided, a labelled planning value, or counted at a named stage; per-message details are {{merge fields}}. Stage 0 work (carrier registration, Stripe Connect, membership billing for the three plans, the affiliate terms, the trademark check) is decided and not yet done. Brand v1 exists, dark palette included.
canonical_vocabulary: SOS SMS, contractor, member, membership, plan, Basic, Plus, Premier, request text, request, trip charge, contractor fee, card on file, phones on file, arrival time, 90-minute window, guarantee, late-arrival credit, NEXT, dispatch, matched contractors, accept, zone, launch zone, open zone, launch list, hour band, density number, first cohort, affiliate, first reply, welcome texts, Text READY, readiness kit, contact card, membership page, terms on one page, Lead Cost Check, safety line
---

# SOS SMS Go-To-Market Master Context

This file is the complete, distilled go-to-market for SOS SMS, both sides of the marketplace. It exists so that any AI agent can absorb the strategy, ICPs, positioning, messaging, competitive frame, funnels, channels, economics, and launch plan in one read, then execute go-to-market work precisely without re-deriving anything.

If you are an AI agent, read the next section first.

---

## 0. Agent operating instructions

**What this file is.** The distilled output of two complete `gtm-builder` runs (Run 1 contractors, Run 2 members), their research and source register, the marketplace synthesis (cross-side check, speed-to-scale plan, launch sequence), and the deltas from the walkthrough build (brand identity, the built deck), all resolved through the resolution register and revised by the membership revision (2026-10-11), the tiers revision (2026-10-20), and the pricing revision (2026-10-21), whose model is `sources/raw/gtm/pricing/`. Sources are listed in `ops/asset-index.md` and kept in `sources/`.

**How to use it.**

1. Before any member-facing or contractor-facing copy, load the four `rules/` files. They govern naming, status, claims, and mechanics, and they override any instinct or older phrasing.
2. **Pick one side.** Contractors (supply) or members (demand). Never blend them in one asset. A line written for a contractor and a homeowner at once is true of neither.
3. Respect the funnel stage (Section 13). Write to the stage, not past it.
4. Obey the verdicts in Section 9. They are decided. Do not contradict them, and do not present a planning value as a result.
5. Before shipping, run `ops/QA-checklist.md`.

**Hard guardrails, never violate:**

- SOS SMS is pre-launch. Never write a capability in the present tense as if it were live. Membership copy is written for launch day and held until memberships open in the zone; the readiness scorecard, prevention guides, and the launch list go out from Stage 1 and promise no service. Contractor recruiting copy goes out before launch and describes what SOS SMS is building, in the future tense.
- Never invent a number, count, arrival time, price, fee, testimonial, or result. Every value is in `reference/resolution-register.md`; a fact that cannot exist before launch is stated as how and when it is counted. Social proof is the method line; proof is the named record (R44, R45). The plan prices are decided and go into member copy as written (Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350); the plan mix and every contribution figure stay internal, never on a page.
- Per-message details are `{{merge fields}}`, filled from a named record and never typed by hand. The twelve decisions are decided (Section 9 and `ops/decisions.md`): write their decided words.
- Neither side's copy may promise what the other side's terms do not deliver (Section 5.3).
- Never present SOS SMS as the plumber, the HVAC company, the electrician, an emergency service, a warranty, insurance, or anything that reads as 911. Carry the safety line wherever copy invites an urgent text.
- Always write the full name, SOS SMS. Never the first word alone.
- Only produce for the channels in Section 14. Refuse the excluded ones and say so.

---

## 1. House writing rules

No em dashes and no en dashes, including in ranges: write "$25 to $60". Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower. Short paragraphs, one to three sentences. Specific mechanics over adjectives: who pays what, and when.

Register: dispatch-room calm. Plain, exact, unhurried, each claim stated once with its source beside it. The subject is emergencies; the copy is not one. A homeowner deciding whether to join is calm and wants the price, the scope, and how to cancel; a member who texts may be standing in water; the contractor has heard every platform pitch before. Full rules: `rules/writing-rules.md`.

---

## 2. Canonical vocabulary

| Term | Rule |
|---|---|
| SOS SMS | Always the full name. Unrelated plumbing companies use the first word alone |
| member, membership | A homeowner who has joined, monthly or annually, before the need; "homeowner" before joining. Never "customer" or "subscriber" for SOS SMS's demand side. In contractor copy, "an SOS SMS member", then "the member" |
| plan: Basic, Plus, Premier | Basic $10 a month or $100 a year, the entry plan, the member's phone, no credit; Plus $15 or $150, most popular, the 90-minute guarantee and up to 5 phones; Premier $35 or $350, a 12-month credit, a trip charge a year paid by SOS SMS, a second home, up to 10 phones (R51, R52, R65, R66). Every plan gets the same dispatch; no plan is faster (R53) |
| request text | The member's one text, from any phone on file (R69), that starts dispatch; the 90-minute window starts here |
| request | What a contractor receives. Never "lead" for an SOS SMS request: contractors associate leads with paying to look |
| trip charge | What the member pays for the visit, on use: $99, one per trade and zone, the same in plumbing, HVAC, and electrical, day or night; charged to the card on file when a contractor accepts, credited to the repair if they go ahead. It stands on a late arrival and comes back in full on a no-show. Not a "service fee" or "call-out fee" |
| contractor fee | $25 per completed paid job, from the first job, for every contractor in every trade, deducted from the trip charge payout: the contractor receives $74 of the $99 (R03) |
| arrival time vs 90-minute window | The arrival time is the contractor's commitment on accepting, inside the window. On Plus and Premier, SOS SMS backs the window with the 90-minute guarantee. Never "guaranteed arrival time" |
| late-arrival credit | What the guarantee pays on Plus and Premier on a late arrival, a no-show, or NEXT after the 90 minutes: the membership paid in the 6 months (Plus) or 12 months (Premier) before the request, credited to the next bills, never cash; `{{credit amount}}` |
| dispatch | What SOS SMS does. The contractor does the work |
| matched contractors | Contractors on SOS SMS matched by trade (plumbing, HVAC, or electrical) and area. Never "every contractor in your area" |
| zone, launch zone, open zone, launch list, hour band | The unit of launch and of density; the first zone; a zone where memberships are open, covered every hour (R15); the email list for a zone not yet open, which promises no service |
| first cohort | The launch zone's first contractors: 9 per trade, 27 places (R08, planning value). Contractors join any time, on the same terms |
| first reply | The automated reply to a member's request text: going out now, the safety line, how to reach a person, then the first steps for the problem |

Retired with the membership revision: the SOS SMS fee, the confirming text, the payment link for dispatch, the owned share, the fee-free launch period with its terms and list (R05 to R07), first refusal (R13), covered hours (R15). Retired 2026-10-20: a refund on a late arrival, the price merge fields. Full table, including banned near-synonyms: `rules/glossary.md`.

---

## 3. Status ledger

Nothing is shipped. Legend and the full list: `rules/feature-status.md`. In short:

- **PLANNED** (in the product design, every rule decided, built in Stage 0 or at its named stage): the three plans, Basic, Plus, and Premier, monthly or annual, billed to the card on file, with an optional backup card (decision 2, R16); joining, upgrades, and downgrades (R54); the phones on file (R69); Premier's second home and trip charge a year (R66); memberships opening per zone when each of the three trades meets the density number, the launch list before then (R55); cancel any time, renewal reminders, failed payments retried (R56); the welcome texts; one number by text; one request text starts dispatch in plumbing, HVAC, and electrical; broadcast to matched contractors; arrival time on acceptance, inside 90 minutes of the request text; never charged when no one accepts, told within 15 minutes (R11); the 90-minute guarantee on Plus and Premier, the late-arrival credit applied automatically (decision 3, R65, R66); the $99 back in full on a no-show, and NEXT after a miss (R17); the $99 trip charge on use, credited to the repair; license for each trade and insurance checks (decision 7); contractor standing on late arrivals and no-shows (R67); Google rating sent with acceptance; the first reply with the first steps for the problem; safety triage (decision 8); a person by text, HELP (R50); the reply to a non-member (R57); the readiness kit, Text READY, forwardable card; the affiliate program (R61); contractor sign-up by text; accept or decline freely; zero cost to join (decision 2); member identity hidden until acceptance (decision 4); payout within 2 business days of arrival (decision 6); photos before accepting; requests accepted by text; add-a-technician flow; fifth-trip referral prompt; Lead Cost Check.
- **HELD** (decided, out of copy until its condition is met): a brand search campaign, from Stage 3 once search volume for SOS SMS by name is counted (R68), at or under the plan's ceiling.
- **NOT AT LAUNCH**: paid search (decision 11); price range before arrival (R49); repair coverage or discounts (R21, R53); faster dispatch on any plan (R53); a member referral reward (R62); a guarantee on the repair (R21); paid priority for contractors.
- **Launch prerequisites NOT DONE**: carrier registration, the payment provider and membership billing for the three plans, the affiliate terms, the name and trademark check, counsel review of the terms and the automatic renewal disclosures.
- **Internal assets BUILT**: the GTM walkthrough deck; brand identity v1; the pricing model, every input on its first sheet (`sources/raw/gtm/pricing/pricing-model.md`).

---

## 4. Claim hygiene ledger

The spine of `rules/do-not-say.md`. The claims the source matrix made, what survived research, and the two claims the 2026-10-20 and 2026-10-21 revisions ruled out:

| Source claim | Verdict |
|---|---|
| "Zero cost to join. Only we can do this" | Not unique: free sign-up is common and warranty networks charge no join fee (S33). Say "no subscription and no per-lead fees" and state how SOS SMS is paid in the same sentence: members' plans, and the $25 contractor fee per completed paid job, from the first job (decision 2) |
| "Guaranteed trip charge, held in escrow" | Say "the trip charge goes on the member's card when you accept, before you roll, and SOS SMS holds it until you arrive" plus the release rule. "Escrow" only if a licensed escrow arrangement holds the funds |
| "Pre-qualified leads, confirmed in your area and trade" | Say "matched to the trades and service area you set". The FTC found a platform's quality claims unsubstantiated (S01) |
| "High-urgency leads, customers ready to buy now" | Say "requests come from SOS SMS members with an active problem who want someone now". Some decline the quote |
| "One text reaches every qualified contractor in your area" | Say "reaches the vetted contractors on SOS SMS for your trade", only in open zones |
| "Text-only access, only we can do this" | Plumbers already take texts (S64). A mechanic, never "only we" |
| "Private by design, never shared" | The accepting contractor gets the address on file. Say "only the contractor who takes your job gets your address and details" |
| "Verified license and insurance, so you know they're qualified" | Say "we check license and insurance before they can take a job". Licenses, not workmanship |
| "90-minute guarantee" | Only named with Plus and Premier, with the clock start (the member's request text), what it pays (the membership paid in the 6 or 12 months before the request, credited, never cash), and the covered area in the same sentence (decision 3). Never for Basic |
| "Your $99 back if they're late" | A late arrival keeps the trip charge, because it pays for the work; Plus and Premier get the credit. The $99 comes back in full only on a no-show or NEXT (decision 3, R17) |
| "Relaunch guarantee" | Write NEXT as decided: the first trip charge back in full, and the request to the other matched contractors as a new request with its own $99 and its own 90 minutes (R17) |
| "Priority dispatch", "faster on Premier" | No plan is faster. Plans differ by the credit, the phones, and Premier's second home and trip charge a year (R53) |

Never: exclusive requests, more jobs, earnings, any volume, any average arrival time, damage prevented, "pays for itself", a guarantee on the repair, repair coverage, "warranty" or "insurance" for the membership, a free trial, a guarantee on Basic, any price or fee as a number unless it is decided (the three plans, the $99 trip charge, and the $25 contractor fee are), and the plan mix or any contribution figure on a page.

---

## 5. What SOS SMS is

### 5.1 The product

A pre-launch, two-sided network for emergency home repair: plumbing, HVAC, and electrical in one membership, from opening day (burst pipes, leaks, backups, and water heaters; no heat and no cooling; a dead panel or circuit). Homeowners join before anything breaks, on Basic, Plus, or Premier, monthly or annual, with their card and home address on file. In an emergency a member sends one text, and help is on the way: the request goes to licensed, insured contractors matched by trade and area, all at once, and the first who can come accepts and commits to an arrival time inside 90 minutes. The $99 trip charge goes on the card on file when a contractor accepts and is credited to the repair if the member goes ahead; there is no fee per request. If no one accepts, the member is told within 15 minutes and nobody pays or is paid. On Plus and Premier, the 90-minute guarantee credits the membership when the contractor is late or does not come. Contractors join free, with no subscription and no lead fees, and pay $25 per completed paid job from the first job.

The core thesis: be ready before it breaks. The homeowner's alternative is searching and calling down a list while the damage spreads, and in the middle of an emergency, calling a contractor from the search results beats joining anything; so SOS SMS is joined before the need, and the emergency itself takes one text. The contractor's alternative is paying for leads and sometimes not getting paid for showing up. Members fund the network; contractors join free and are paid before they roll.

### 5.2 Two audiences, never blended

| | Contractors (supply, Run 1) | Members (demand, Run 2) |
|---|---|---|
| Who | Licensed, insured plumbing, HVAC, and electrical contractors who take emergency calls | Homeowners in an open zone who join before anything breaks |
| Promise | No charge to see a request, and the trip paid before you roll | One text, and help is on the way: an arrival time inside 90 minutes when someone accepts, and on Plus and Premier a late arrival or a no-show credits the membership |
| How they arrive | Cold email and a partnership program, then a referral loop; they sign up by text | Before the need: affiliates and email first, then search and SEO pages and paid social for sign-ups in open zones, no paid search at launch; member loops bring the next one |

### 5.3 The cross-side dependency

Every member promise is kept by a contractor first. The eight shared rows (identical in both briefs, Section 6): the 90-minute guarantee needs a late-arrival rule (decided: the trip charge stands on a late arrival on both sides, and the credit on Plus and Premier is SOS SMS's to pay, decision 3); relaunch needs a second trip-charge rule (decided: NEXT treats the first contractor as a no-show, so SOS SMS pays no second trip charge, R17); "one text reaches" needs the dispatch rule; privacy needs approximate distance before acceptance; crediting the trip charge is a contractor obligation; known arrival time is a contractor commitment; verification needs a recheck cadence; zero cost to join needs the revenue model. Every row is closed or consistent. Eight further conflicts (A to H) are each resolved by a decision. Detail: `reference/marketplace-cross-side.md`.

### 5.4 Why supply leads

The member promises are only true where enough contractors say yes in every trade a member may need, so memberships open per zone only when each of plumbing, HVAC, and electrical meets the density number in every hour band (R55). The density model: the contractors needed per trade, zone, and hour band are n ≥ ln(1 - c) / ln(1 - a), where a is the acceptance chance (planned at 0.30, R28) and c the coverage target. At 90 percent coverage, a of 0.10 needs 22 contractors, 0.30 needs 7, 0.40 needs 5 (illustrative); 9 for 95 percent at 0.30, so the first cohort is 9 per trade, 27 places; a shop licensed in more than one trade counts in each (R08). Treat it as a floor. The other side of the same arithmetic, at 0.50 requests a member a year (plumbing 0.25, HVAC 0.20, electrical 0.05, R58): about 410 members per zone give each first-cohort plumber about one request a month, an HVAC contractor about 0.8, and an electrician about one every 5 months; every contractor is told the expected volume for their trade (R64). Detail: `reference/density-model.md`.

---

## 6. Feature matrix: what leads

Scored for demand and competitiveness, -20 to +20, from Bryan's ratings in the source matrix, moved by research (pre-launch scoring).

**Contractors.** Lead with the trip charge collected before rolling (10.6 / 11.8, the strongest competitive score: no lead platform in the researched set collects it for the contractor). Zero cost to join (17.6 / 6.3) opens the door but is not unique. High-urgency requests (11.2 / 7.9) support. Fast payout is a hero (6.8 / 3.1), set at within 2 business days of arrival (decision 6). Table stakes: matching by trade and area (16.4 / -8.7), decline freely, the customer stays the contractor's.

**Members.** Lead with one text starting dispatch, because the card and address are on file from joining (18.4 / 11.6, the highest on both axes). The 90-minute guarantee (17.9 / 9.6, on Plus and Premier) and instant network access (15.2 / 7.4) stand with it; the known arrival time (11.6 / 4.2), privacy in its narrow form (9.7 / 6.1), and the readiness kit (6.4 / 3.4) support. The membership itself is table stakes (10.8 / -6.2): households know the format from clubs, warranties, and utility plans, so it opens the door and never leads. A price range before arrival (16.1 / 8.3) is wanted by all and not at launch (R49). Text-only access (-2.6 / 4.8) is a mechanic. Safety triage is required whatever its score.

**Demand drivers.** Contractors: the Lead Cost Check, a two-minute calculator of true cost per booked job. Members: the readiness check before anything breaks ("How Ready Is Your Home for a 2 a.m. Leak?", on the web or Text READY), carried by affiliates and email, ending at the ZIP check. Detail: `reference/feature-matrix.md`.

---

## 7. Competitive market analysis

**Contractor side** weighs: C1 Angi Leads, C2 Thumbtack, C3 Google Local Services Ads, C4 Service Direct, C5 home warranty networks (American Home Shield, Frontdoor), C6 the status quo (word of mouth and their own listing). Praised for volume and exclusive calls; criticized for paying for leads that never reply, shared requests, and unpaid trips. Plumbing cost per lead: Angi $25 to $60 (S03, C), Thumbtack $25 to $45 (S06, C), Google LSA about $57 to $69 (S08, C), Service Direct $60 to $255 exclusive (S10, A).

| Vector, contractors | SOS SMS current / projected | Leader |
|---|---|---|
| V1 Lead volume and reach (they lead) | 0.4 / 4.2 | Google LSA 9.1 |
| V2 Exclusive calls (they lead) | 0.0 / 2.8 | Status quo 9.5 |
| V3 No charge for requests that never become work | 0.0 / 9.4 | SOS SMS projected, with the status quo |
| V4 Paid to show up | 0.0 / 9.1 | SOS SMS projected |

**Member side** weighs what a household sets up, or relies on, before anything breaks: D1 nothing in advance (search and call when it happens), D2 plumber club memberships (Benjamin Franklin Plumbing $10 a month or $120 a year, S75; Roto-Rooter $19.99, S77, C), D3 home warranties ($47 to $82 a month plus $75 to $125 a visit, S79), D4 utility-partner plumbing plans (HomeServe, $16.99 to $22.99 a month, S78; more than 1,300 partners and 4.6 million customers, S93), D5 Frontdoor (video help, S81), D6 on-demand marketplaces (Angi, Thumbtack). Praised for priority, covered repairs, and plans that arrive through a trusted utility; criticized for unanswered nights, slow claims, waiting periods, upselling, and floods of calls.

| Vector, members | SOS SMS current / projected | Leader |
|---|---|---|
| V1 Pays for repairs (they lead) | 0.0 / 1.0 | Home warranties 9.0, utility-partner plans 8.2 |
| V2 A known brand at the door (they lead) | 0.0 / 3.1 | Plumber clubs 9.0 |
| V3 One text, an arrival window with a guarantee on Plus and Premier | 0.0 / 9.0 | SOS SMS projected; plumber clubs 6.0 for priority with one company |
| V4 Many contractors reached, one reply | 0.0 / 9.0 | SOS SMS projected |

**The wedge.** Every lead platform earns when a request arrives, so none can stop charging to look without changing its model. Every plan a household can buy today leaves the emergency itself alone: warranties and utility plans pay after a claim and a wait, and a plumber's club gives priority with one company. One text that reaches many contractors in three trades, with a window backed by a credit on Plus and Premier, needs local density no single company has. Defensibility is local density, not technology. Battlecards: `reference/competitor-battlecards.md`.

---

## 8. Ideal customer profile and buying committee

**Contractors.** Level 2 goes first: small plumbing, HVAC, and electrical shops with at least one paid lead source and an on-call technician. They have a savings anchor, night capacity, and have already accepted platforms. Level 1, owner-operators living on referrals, is recruited alongside to fill hours and refer other trades. Disqualifiers: no current license for each trade they take, uninsured, won't credit the trip charge, won't commit to an arrival time. Triggers: a lead platform renewal or price rise, a month of unreplied leads, a new technician, freeze and heat-wave seasons.

In a shop the committee is technician, dispatcher, owner. **The dispatcher is the likely blocker**, because a job accepted on a technician's phone goes around the dispatch board. Settle who receives requests before the first one arrives. Owners block on platform distrust and on the obligations. The first cohort, 9 per trade sized by the density model, is the most valuable output of Run 1.

**Members.** Level 1 is a new homeowner without a go-to contractor (first-time buyers were 24 percent of buyers in the 2024 profile, S91); Level 2 is an established homeowner, usually in an older home, whose plumber, HVAC company, or electrician does not answer at night. Both join before the need, through the partners and lists that already reach them: utility new-account offers, association welcome packets, newsletters, insurance agents for existing policyholders, prevention guides, and search pages found at freeze and heat-wave seasons. The committee is a household of one or two adults deciding over days. **The blocker is "another subscription"**: a fee every month or year before anything breaks (R46). Others: "it rarely happens", "is my home covered at night" (yes: an open zone is covered every hour, R15), "how is this different from my warranty", a card on file with a new company, "can I cancel". It wins with the plan prices and the trip charge stated on separate lines, the guarantee named with Plus and Premier and its scope, cancel any time, the readiness scorecard, a trusted partner's mention, and privacy. The member area is the neighborhoods inside the launch zone, nowhere else. Renters and property managers are out of scope.

Detail: `reference/icp-personas.md`.

---

## 9. Strategic verdicts

**Decided** (dated in `ops/decisions.md`):

1. Two runs, never blended: one value proposition per side.
2. Supply leads, memberships follow, zone by zone. Memberships open only when each of the three trades meets the density number in every hour band; before then, the launch list.
3. Product-led, no sales team. No calls, demos, meetings, shop visits, or door-to-door on either side.
4. Contractor channels: cold email, a partnership program, an in-product referral loop.
5. Member channels (the membership revision, 2026-10-11, and the tiers revision, 2026-10-20): affiliates and email lead, before the need; search and SEO pages and paid social support sign-ups in open zones, each at or under its plan's ceiling; organic social and community posts by SOS SMS itself; member loops. No paid search at launch. Never an ad that sells dispatch in the middle of an emergency.
6. Do not contest volume or exclusivity (contractors), or repair coverage, brand familiarity, and guarantees on the work (members).
7. Claims follow the narrowed forms. Nothing invented, ever.
8. Speed only inside proven zones; slow down at thresholds set before launch.

**Decided 2026-10-03, revised 2026-10-11, 2026-10-20, and 2026-10-21** (the twelve decisions, `ops/decisions.md`; every other value in `reference/resolution-register.md`): (1) the launch zone, a 10-mile radius around the first contractors' shops in the founders' home metro, with plumbing, HVAC, and electrical in one membership from opening day; (2) the revenue model: members choose Basic ($10 a month or $100 a year), Plus ($15 or $150, the 90-minute guarantee with a 6-month credit, up to 5 phones), or Premier ($35 or $350, a 12-month credit, a trip charge a year paid by SOS SMS, a second home, up to 10 phones), two months free on every annual plan, no fee per request; contractors in all three trades pay $0 to join and per request, and $25 per completed paid job from the first job, deducted from the trip charge payout; no share of the repair; (3) the late-arrival rule and guarantee scope together: an arrival time inside the remaining window, 90 minutes from the member's request text; no acceptance, told within 15 minutes, never charged, no contractor paid; a late arrival keeps the trip charge, with the credit on Plus and Premier; a no-show or NEXT returns the $99 in full, the contractor paid nothing, with the credit on Plus and Premier; two late arrivals or no-shows in 90 days pause a contractor's requests until a person reviews them; anywhere in the zone's neighborhoods, at any hour; (4) dispatch to all matched at once, first to accept, approximate distance and cross-street area before acceptance, the address after, no first refusal; (5) one $99 trip charge per trade and zone, the same in all three trades, day or night, set by SOS SMS, on use. Then (6) Stripe Connect: the card saved at joining, with an optional backup card, billed monthly or annually; the trip charge authorized when the request text arrives, captured at acceptance, released on arrival, payout within 2 business days less the $25 contractor fee; (7) the state license for each trade and insurance, checked at sign-up, every 6 months, and at each policy's expiry; (8) the safety reply first for gas, smoke, fire, sparks, a burning smell, a shock, or injury, no broadcast until the member is safe; (9) one registered local number; (10) the trademark and search check in Stage 0; (11) no paid search at launch and never Local Services Ads; a brand campaign only once a zone has been open 6 months and search volume for SOS SMS by name is counted (R68); (12) one acquisition ceiling per plan, the first 6 months of contribution: about $47 Basic, $70 Plus, $151 Premier on the monthly plan (R63), replacing the per paid job ceiling.

---

## 10. Value proposition: contractors

**Brand promise:** Emergency jobs you choose, with the trip paid before you roll.

**Positioning:** The emergency dispatch line where seeing a request costs nothing. Built on two things lead platforms do not do: no charge to receive a request, and the trip charge collected before the contractor drives out.

| Pillar | Reasons to believe |
|---|---|
| VP1 No lead fees | No subscription and no per-lead fee; a request you do not win costs you nothing; decline freely without it changing which requests reach you |
| VP2 Paid to show up | The trip charge is collected before you leave; release and payout timing stated before your first job; SOS SMS members agree to the trip charge when they join, and it counts toward the work |
| VP3 Know the job before you go | Requests from SOS SMS members with an active problem; matched to the trades and area you set; photos or video before you accept, when the member sends them |

Every social-proof headline is a method line, and every proof point a named record (R44, R45); no result exists before launch. Drills and their conditions: `reference/value-proposition-contractors.md`.

---

## 11. Value proposition: members

**Brand promise:** One text, and help is on the way. **Sub tag:** Join before you need it.

**Positioning:** The emergency home repair membership you join before anything breaks, so the emergency itself is one text. Built on one message that reaches the vetted contractors for the trade (plumbing, HVAC, or electrical) at once, and, on Plus and Premier, an arrival window SOS SMS backs with a membership credit.

| Pillar | Reasons to believe |
|---|---|
| VP1 One text, help on the way | One text reaches the licensed, insured contractors on SOS SMS for that trade nearby, at once; an arrival time inside 90 minutes of the text when they accept, with their name and Google rating; on Plus and Premier, a late arrival or a no-show credits the membership paid in the 6 or 12 months before the request; anywhere in the zone's neighborhoods, at any hour |
| VP2 Ready before it happens | The card and home address are on file from joining, so there is nothing to fill in at 2 a.m.; no app and no phone tree, one number saved on joining; up to 5 phones in the home on Plus, 10 on Premier; monthly or annual, cancel any time, a person by text |
| VP3 Know the cost and who is coming | The plan price and the $99 trip charge on separate lines; the trip charge only when a contractor accepts, credited to the repair, never if no one accepts; license and insurance checked; only the contractor who takes the job gets the address, and no selling or ad targeting |

Every drill describing the emergency text carries the safety line. Drills and conditions: `reference/value-proposition-members.md`.

---

## 12. Positioning statements

**Category:** an emergency home repair membership, by text; a local two-sided network. **Niche:** plumbing, HVAC, and electrical emergencies, one zone at a time.

**Contractors:** "For licensed plumbing, HVAC, and electrical contractors who are tired of paying for requests that never become work, SOS SMS is the emergency dispatch line where seeing a job costs nothing and the trip is paid before you roll."

**Members:** "For homeowners who want to be ready before something breaks, SOS SMS is the membership that makes a plumbing, HVAC, or electrical emergency one text: the vetted contractors nearby see it at once, the first who can come commits to an arrival time inside 90 minutes, and on Plus and Premier a late arrival or a no-show credits the membership."

**Differentiation and defensibility.** Lead platforms cannot stop charging per request without changing their model, and no one else holds the visit payment before the contractor rolls. On the member side, a competitor needs the same contractor density in three trades in a zone before it can make the same one-text promise with a guarantee behind it, so density is both the constraint and the moat. A number saved in a phone before the pipe bursts is worth more than an ad seen during the flood.

**The two objections that matter most:**
- Contractors, "Every request is shared, like the platforms I quit": it is shared, openly, and losing one costs nothing because nobody pays to look.
- Members, "Another subscription, for something that rarely happens": say it first, then what the plan includes across three trades, the trip charge only on use, and cancel any time.

Statements with their conditions: `reference/positioning.md`.

---

## 13. Customer journey funnels

**Contractor journey, self-serve throughout.**

| Stage | Mindset | Touchpoint | KPI |
|---|---|---|---|
| 1 Awareness | "Leads that never called back, trips I never got paid for" | Cold email 1 with the Lead Cost Check; counter card; partner listing | Checks completed by channel |
| 2 Discovery | "What's the catch?" | Email 2, how a job works in three texts; contractor page | Page visits, objection replies |
| 3 Evaluation | "Show me the terms, not the pitch" | Email 3, the terms on one page; lead spend report | Terms views to JOIN |
| 4 Trial | "Sign me up" | JOIN by text; documents; payout setup; agreement | Time to verified; drop-off step |
| 5 Value | "Did the trip charge show up?" | Payout confirmation | Days to first paid trip |
| 6 Advocacy | "The HVAC company I work with should be on this" | Fifth-trip referral prompt; add a technician | Referrals per contractor |
| 7 Staying active | "Still worth it?" | Monthly summary; 30-day check-in | Active contractors vs density target |

Critical: terms in writing before sign-up; a fast first paid trip; payouts on time, every time. Blocker to watch: first-job silence, so recruit by zone and grow the zone's launch list in parallel.

**Member journey, two clocks: weeks before the need, minutes during it.**

| Stage | Mindset | Touchpoint | KPI |
|---|---|---|---|
| 1 Awareness | "Who would I even call at 2 a.m.?" | An affiliate's mention; a partner's email; the readiness scorecard; prevention guides | Scorecards and email sign-ups by channel |
| 2 Discovery | "What is it, and is my home covered?" | The membership page with the ZIP check; the launch list | ZIP checks; launch list joins |
| 3 Evaluation | "Worth it? Which plan? What does it cost when I use it?" | **The membership page**: the three plans, Plus first on the annual plan; the trip charge on use, on its own line; the guarantee on Plus and Premier; what is not included; cancel any time | Page to join rate, by plan |
| 4 Join | "Sign me up" | Plan, card, address, phones, consent; the welcome texts; the contact card | Cost per new paid member by channel and plan, against the plan's ceiling |
| 5 Value | "Something broke. One text." | The first reply; the first steps for the problem; acceptance with name and arrival time; on Plus and Premier, the credit applied automatically if late; on a no-show, the $99 back and NEXT | Time to acceptance, by trade; share inside the window; late arrivals and no-shows, and credits applied |
| 6 Advocacy | "My neighbor should have this" | Two-question follow-up; forwardable card | Referrals per member |
| 7 Renewal | "Still worth keeping?" | Seasonal notes (opt-in); the upgrade note; the renewal reminder; cancel any time | Monthly churn; annual renewal; upgrades |

**The hand-off.** Acceptance is the moment both journeys meet: the contractor's commitment becomes the member's arrival time. Measured together: time from the request text to acceptance, by trade; share arriving within the window; late arrivals and no-shows per 100 accepted requests. Detail: `reference/customer-journey.md`.

---

## 14. Channel and asset plan

**In the mix, contractors:** (1) cold email, zone by zone, in all three trades, four emails over twelve days; (2) partnership program: one supply house per trade with counter cards, association chapter newsletters, trade school job boards, a partner kit, a ten-minute explainer video; (3) in-product referral loop. The Lead Cost Check is the top of the funnel in all three. Lead magnet: the Job Leak Scorecard.

**In the mix, members:** (1) affiliates, before the need: utilities and cities, homeowner and neighborhood associations, local publications and newsletters, home content creators, home improvement retailers, insurance agents for existing policyholders, employers' benefit platforms, each with a code, the kit, and a disclosed commission, $20 per new paid member on any plan, paid once the second monthly or first annual payment clears; contractors may join on the same terms (R61); (2) email, before the need: SOS SMS's own list from the readiness scorecard and the launch list, partner sends, and member email (welcome, seasonal notes, upgrades, renewal); (3) search and SEO pages and paid social for sign-ups: the five problem and prevention guides for plumbing, HVAC, and electrical, found in organic search, the membership page, zone pages, and paid social limited to open zones' maps, paused with sign-ups (R34), each at or under the plan's ceiling; plus member loops: the contact card, Text READY, the forwardable card, the two questions after a job, renewal; no member referral reward (R62). Lead magnet: "How Ready Is Your Home for a 2 a.m. Leak?", whose plan covers all three trades.

**Held:** a brand search campaign from Stage 3, once search volume for SOS SMS by name is counted (R68), at or under the ceiling.

**Out of the mix, refuse:** sales calls, demos, meetings, shop visits, door-to-door, LinkedIn ads and outreach, cold email or texts to homeowners, marketing texts without written consent, paid search at launch (Google search ads, Microsoft Ads; decision 11), Local Services Ads (S70), ads that sell dispatch in the middle of an emergency, ad retargeting and pixels, and any payment to someone referring at a home purchase settlement (real estate agents, lenders, title and settlement agents; agents and inspectors may share SOS SMS without payment, S86, S94).

**Production order.** Contractors: the terms on one page and the contractor page, then the Lead Cost Check and sign-up by text, then the list and emails, then the partner kit, then the referral prompt. Members: Stage 0 terms (counsel-reviewed member terms and renewal disclosures, membership billing for the three plans with upgrades and the late-arrival credit, the affiliate terms, email setup, carrier registration), then the membership page with the three plans and the guarantee page, then in Stage 1 the readiness scorecard, the first five guides, and the launch list sequence, then the affiliate kit and the first partners with codes ready, then the member loops, then when the zone opens the opening email, affiliates live, and paid social for sign-ups. No paid search at launch. Engines: `reference/channel-engine-contractors.md`, `reference/channel-engine-members.md`.

---

## 15. Pricing and unit economics

**Structure, decided (decisions 2 and 5; decision 2 revised 2026-10-11, 2026-10-20, and 2026-10-21).** Members choose one of three plans, billed to the card on file, two months free on every annual plan. Basic, $10 a month or $100 a year: the entry plan, the member's phone, no credit. Plus, $15 or $150, most popular, shown first on the annual plan: the 90-minute guarantee (on a late arrival, a no-show, or NEXT after the 90 minutes, the membership paid in the 6 months before the request, up to $90 monthly or $75 annual, credited to the next bills, never cash) and up to 5 phones. Premier, $35 or $350: the credit at 12 months (up to $420 monthly, $350 annual), one trip charge a membership year paid by SOS SMS (annual from joining, monthly after 6 paid months), a second home in an open zone, and up to 10 phones. The plans never differ by dispatch speed (R53). Monthly dispatch starts 30 days after joining, annual at once (R54). On use, the $99 trip charge goes on the card on file when a contractor accepts, is paid to the contractor less the fee ($74 of the $99), and is credited to the repair; no fee per request. Contractors pay $0 to join and per request, and $25 per completed paid job from the first job: a third of the about $75 the cheapest per-lead option costs per booked job in any of the three trades at a 20 percent close rate (S98, grade C, internal; about $125 in plumbing, S03, S06, C). Late-arrival rule (decision 3): a late arrival keeps the trip charge, because it pays for the work; a no-show is paid nothing and the $99 comes back; when no one accepts, nobody pays and nobody is paid.

**Member economics, illustrative (pricing model; planning values, never results, never on a page).** Contribution about $9.29 Basic, $13.77 Plus, $29.62 Premier a member a month, after card processing, messages ($0.05 for each phone on file) and support and platform (R31), each member's share of request costs on both sides at 0.50 requests a year (R58), the late-arrival credit, and Premier's covered trip charge, with the contractor fee (about $0.89 a member a month); about $14.91 at the plan mix (Basic 10, Plus 80, Premier 10 percent, R70). Every request nets about $13.03. The Plus credit costs about $0.17 a member a month at the 5 percent late share (R29). Plus sits just under the market median of $16.99 (band $4.83 to $36.95 a month) and above its cost floor of about $9.48 at an 80 percent margin; Basic sits at the closest analog's price, a plumber's club at $10 a month (S75), above its floor of about $7.69; Premier, at 2.33 times Plus, anchors the ladder. An annual Plus member is worth about $559 over the membership, against about $212 on the monthly plan. About 410 members per zone (R64).

**Acquisition, illustrative.** One ceiling per plan, the first 6 months of contribution at 6.5 percent monthly churn (R59): about $47 Basic, $70 Plus, $151 Premier on the monthly plan; about $48, $70, $139 on the annual plan (R63, decision 12). Every channel scales while its measured cost per new paid member is at or under the ceiling of the plan joined, and stops when it is not; reviewed weekly by channel, plan, and zone. An affiliate's $20 commission (R61) sits under every ceiling. Paid search at the plumbing benchmark ($10.49 a click, 7.63 percent converting, S15, B) costs about $137 per new paid member, about 3 times Basic's ceiling, so there is no paid search at launch (decision 11): affiliates and email lead, and paid social supports. Levers: partner-led acquisition, retention, annual plans and three trades, the plan ladder (Plus built for 80 percent of members), and the contractor fee from the first job. Detail: `reference/pricing-and-economics.md`.

---

## 16. Launch sequence and growth

Stage 0, decisions and setup: the twelve decisions written into the member terms, the guarantee on Plus and Premier, the terms on one page, and the contractor agreement; the six plan prices loaded and membership billing tested on each plan (upgrades, the late-arrival credit, Premier's covered trip charge, failed payments, cancelling); counsel review of the member terms and automatic renewal disclosures (S87); the affiliate terms (S86, S88, S94), with affiliates signed from Stage 0, fastest categories first; email sending; paid social audiences built, nothing run before the zone opens; carrier registration; payment hold and payout tested; the self-serve paths tested end to end, NEXT and the safety reply included; zone thresholds (R32) in the weekly review before launch; the launch zone drawn, with licensed plumbing, HVAC, and electrical businesses counted by trade (R40). Stage 1, supply fills the launch zone in all three trades while the launch list grows (the readiness scorecard, guides, affiliates signed with codes ready); gate: the density number met for each of the three trades in every hour band, every day, 27 places (R08, R55). Stage 2, memberships open: the opening email to the launch list, affiliates live, the membership page with the three plans, then paid social for sign-ups. Stage 3, prove the zone, then accelerate: zone proven, zone full (members growing toward about 410), metro proven, trade added (a fourth trade behind the same membership); search volume for SOS SMS by name counted once the zone has been open 6 months (R68). Slow down when late arrivals and no-shows, acceptance in any trade, monthly churn, cost per new paid member against the plan's ceiling, or contractor activity cross their thresholds (R32; ceiling, decision 12).

Affiliates and the launch list open each zone; paid social supports only under the ceiling. Never traded for speed: claim accuracy, safety triage, paying contractors on time, automatic credits and no-show refunds, easy cancellation, privacy as promised, messaging, email, subscription, affiliate, and ad law. Detail: `reference/launch-and-growth.md`.

---

## 17. Brand identity

Green and white. The mark is a sent-message bubble holding a round dot (the member) and a square (the contractor): round is always a member, square always a contractor. Signal green is the yes; it never means alarm. Never red, sirens, crosses, bells, or "911" in the identity. One typeface, Inter, three weights, tabular figures. Voice: plain, exact, unhurried. Brand values: calm under pressure; kept, not claimed; fair to both sides; exact, never inflated. Detail and files: `reference/brand-identity.md`, `brand/logo/`.

---

## 18. Quick-reference cheatsheet

- **One-line positioning, contractors:** the emergency dispatch line where seeing a job costs nothing and the trip is paid before you roll.
- **One-line positioning, members:** the membership that makes a plumbing, HVAC, or electrical emergency one text, with an arrival time inside 90 minutes when a contractor accepts and, on Plus and Premier, a membership credit if they are late or do not come.
- **Plans:** Basic $10 a month or $100 a year; Plus $15 or $150, most popular; Premier $35 or $350. The trip charge, $99, on its own line. No plan is faster.
- **Flagship differentiators:** paid to show up (contractors); one text with the card on file, three trades, the guarantee on Plus and Premier, and one reply (members).
- **Table stakes:** matching by trade and area; license and insurance checks; the membership format itself.
- **Top-of-funnel hooks:** the Lead Cost Check; the readiness check before anything breaks.
- **Audiences:** contractors and members, never blended.
- **ICP first:** Level 2 shops in all three trades; homeowners in the launch zone, reached before the need through partners and email.
- **Proof points on file:** the named records per drill (R45), which show each claim from the first job. No result is cited until the launch zone produces real, permissioned ones.
- **Signature line:** "Every promise to a member is kept by a contractor first."
- **Primary rivals:** lead platforms (contractors); doing nothing in advance, plumber clubs, warranties, and utility plans (members).
- **Channels:** cold email, partners, referral loop; affiliates, email, search and SEO pages and paid social for sign-ups, member loops. No paid search at launch.
- **Do not say:** escrow, exclusive, pre-qualified, guaranteed arrival time, every contractor in your area, warranty, covers repairs, subscriber, priority or faster dispatch, a guarantee on Basic, the $99 back on a late arrival, any number not in the brain.
- **Always:** the full name SOS SMS; the safety line on urgent copy; register values as written, planning values labelled, `{{merge fields}}` for per-message details such as `{{plan}}` and `{{credit amount}}`.

---

*End of the SOS SMS GTM master context. When status changes, update the ledger in `rules/` first, then this file, then `ops/decisions.md`, then the copy.*
