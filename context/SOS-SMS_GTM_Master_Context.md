---
title: SOS SMS Go-To-Market Master Context
project: SOS SMS
type: gtm_context_file
purpose: Single source of truth for any AI agent executing SOS SMS go-to-market work.
version: 1.4
last_updated: 2026-10-11
status_notes: Pre-launch. Nothing is live, so there are no contractors, members, jobs, revenue, arrival times, or testimonials, and no result exists to cite. Every product capability is PLANNED, never shipped. The membership revision (2026-10-11) made the demand side a monthly or annual membership, joined before the need, with the card and home address on file, so an emergency is one text; members are reached before the need through affiliates and email first, and search and social sell sign-ups in open zones. The twelve founder decisions are decided (2026-10-03; decisions 2, 3, 6, 8, 11 revised and 12 replaced on 2026-10-11): the founding zone, the revenue model (members' membership at planning values $10 a month or $100 a year, copy {{monthly price}} and {{annual price}}; contractors $0 in the founding period, then $25 a completed paid job), the guarantee from the member's request text, the dispatch rule, the $99 trip charge on use set by SOS SMS, and the rest. Every other value is resolved in `reference/resolution-register.md`: decided, a labelled planning value, or counted at a named stage; per-message details are {{merge fields}}. Stage 0 work (carrier registration, Google's written confirmation, Stripe Connect, membership billing, the affiliate terms, the trademark check, the launch price) is decided and not yet done. Brand v1 exists, dark palette included.
canonical_vocabulary: SOS SMS, contractor, member, membership, request text, request, trip charge, card on file, arrival time, 90-minute window, guarantee, dispatch, matched contractors, accept, zone, open zone, launch list, hour band, density number, founding contractor, founding period, affiliate, covered hours, first reply, welcome texts, Text READY, readiness kit, contact card, membership page, terms on one page, Lead Cost Check, safety line
---

# SOS SMS Go-To-Market Master Context

This file is the complete, distilled go-to-market for SOS SMS, both sides of the marketplace. It exists so that any AI agent can absorb the strategy, ICPs, positioning, messaging, competitive frame, funnels, channels, economics, and launch plan in one read, then execute go-to-market work precisely without re-deriving anything.

If you are an AI agent, read the next section first.

---

## 0. Agent operating instructions

**What this file is.** The distilled output of two complete `gtm-builder` runs (Run 1 contractors, Run 2 members), their research and source register, the marketplace synthesis (cross-side check, speed-to-scale plan, launch sequence), and the deltas from the walkthrough build (brand identity, the built deck), all resolved through the resolution register and revised by the membership revision (2026-10-11). Sources are listed in `ops/asset-index.md` and kept in `sources/`.

**How to use it.**

1. Before any member-facing or contractor-facing copy, load the four `rules/` files. They govern naming, status, claims, and mechanics, and they override any instinct or older phrasing.
2. **Pick one side.** Contractors (supply) or members (demand). Never blend them in one asset. A line written for a plumber and a homeowner at once is true of neither.
3. Respect the funnel stage (Section 13). Write to the stage, not past it.
4. Obey the verdicts in Section 9. They are decided. Do not contradict them, and do not present a planning value as a result.
5. Before shipping, run `ops/QA-checklist.md`.

**Hard guardrails, never violate:**

- SOS SMS is pre-launch. Never write a capability in the present tense as if it were live. Membership copy is written for launch day and held until memberships open in the zone; the readiness scorecard, prevention guides, and the launch list go out from Stage 1 and promise no service. Contractor recruiting copy goes out before launch and describes what SOS SMS is building, in the future tense.
- Never invent a number, count, arrival time, price, fee, testimonial, or result. Every value is in `reference/resolution-register.md`; a fact that cannot exist before launch is stated as how and when it is counted. Social proof is the method line; proof is the named record (R44, R45). The membership prices are planning values: copy writes `{{monthly price}}` and `{{annual price}}`.
- Per-message details are `{{merge fields}}`, filled from a named record and never typed by hand. The twelve decisions are decided (Section 9 and `ops/decisions.md`): write their decided words.
- Neither side's copy may promise what the other side's terms do not deliver (Section 5.3).
- Never present SOS SMS as the plumber, an emergency service, a warranty, insurance, or anything that reads as 911. Carry the safety line wherever copy invites an urgent text.
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
| request text | The member's one text that starts dispatch; the 90-minute window starts here |
| request | What a contractor receives. Never "lead" for an SOS SMS request: contractors associate leads with paying to look |
| trip charge | What the member pays for the visit, on use: $99, charged to the card on file when a contractor accepts, credited to the repair if they go ahead. Not a "service fee" or "call-out fee" |
| arrival time vs 90-minute window | The arrival time is the contractor's commitment on accepting. The window is the guarantee. Never "guaranteed arrival time" |
| dispatch | What SOS SMS does. The contractor does the work |
| matched contractors | Contractors on SOS SMS matched by trade and area. Never "every contractor in your area" |
| zone, open zone, launch list, hour band | The unit of launch and of density; a zone where memberships are open; the email list for a zone not yet open, which promises no service |
| founding contractor, founding period | The launch cohort (the founding list, closed 60 days after the first email) and the founding zone's first 6 months open to members, when contractors pay $0 a job; founding contractors keep $0 a job for 12 months after it |
| first reply | The automated reply to a member's request text: going out now, the safety line, how to reach a person, then the stop-the-water steps |

Retired with the membership revision: the SOS SMS fee, the confirming text, the payment link for dispatch, the owned share. Full table, including banned near-synonyms: `rules/glossary.md`.

---

## 3. Status ledger

Nothing is shipped. Legend and the full list: `rules/feature-status.md`. In short:

- **PLANNED** (in the product design, every rule decided, built in Stage 0 or at its named stage): the membership, monthly or annual, billed to the card on file (decision 2); joining with the card, the home address, and consent on file (R54); memberships opening per zone at the density number, the launch list before then (R55); cancel any time and renewal reminders (R56); the welcome texts; one number by text; one request text starts dispatch; broadcast to matched contractors; arrival time on acceptance; 90-minute guarantee with automatic refund from the request text (decision 3); the $99 trip charge on use, credited to the repair; license and insurance checks; Google rating sent with acceptance; stop-the-water first reply; safety triage; the reply to a non-member (R57); the readiness kit, Text READY, forwardable card; the affiliate program (R61); contractor sign-up by text; accept or decline freely; zero cost to join (decision 2); member identity hidden until acceptance (decision 4); payout within 2 business days of arrival (decision 6); photos before accepting; requests accepted by text; add-a-technician flow; fifth-trip referral prompt; Lead Cost Check.
- **HELD** (decided, out of copy until dispatch supports it): the relaunch after a miss (R17); first refusal on a contractor's own customers (R13).
- **NOT AT LAUNCH**: price range before arrival (R49); repair coverage or discounts (R21, R53); a member referral reward (R62); a guarantee on the repair (R21); paid priority for contractors.
- **Launch prerequisites NOT DONE**: carrier registration, Google's written confirmation, the payment provider and membership billing, the affiliate terms, the launch price, the name and trademark check, counsel review of the terms and the automatic renewal disclosures.
- **Internal assets BUILT**: the GTM walkthrough deck; brand identity v1.

---

## 4. Claim hygiene ledger

The spine of `rules/do-not-say.md`. The claims the source matrix made, and what survived research:

| Source claim | Verdict |
|---|---|
| "Zero cost to join. Only we can do this" | Not unique: free sign-up is common and warranty networks charge no join fee (S33). Say "no subscription and no per-lead fees" and state how SOS SMS is paid in the same sentence: members' monthly or annual fees, and $25 per completed paid job after the founding period (decision 2) |
| "Guaranteed trip charge, held in escrow" | Say "the trip charge goes on the member's card when you accept, before you roll, and SOS SMS holds it until you arrive" plus the release rule. "Escrow" only if a licensed escrow arrangement holds the funds |
| "Pre-qualified leads, confirmed in your area and trade" | Say "matched to the trades and service area you set". The FTC found a platform's quality claims unsubstantiated (S01) |
| "High-urgency leads, customers ready to buy now" | Say "requests come from SOS SMS members with an active problem who want someone now". Some decline the quote |
| "One text reaches every qualified contractor in your area" | Say "reaches the vetted contractors on SOS SMS for your trade", only in open zones |
| "Text-only access, only we can do this" | Plumbers already take texts (S64). A mechanic, never "only we" |
| "Private by design, never shared" | The accepting contractor gets the address on file. Say "only the contractor who takes your job gets your address and details" |
| "Verified license and insurance, so you know they're qualified" | Say "we check license and insurance before they can take a job". Licenses, not workmanship |
| "90-minute guarantee" | Only with clock start (the member's request text), refund, and covered areas and hours in the same sentence (decision 3) |
| "Relaunch guarantee" | Not built. Out of every piece of copy |

Never: exclusive requests, more jobs, earnings, any volume, any average arrival time, damage prevented, "pays for itself", a guarantee on the repair, repair coverage, "warranty" or "insurance" for the membership, a free trial, any price or fee as a number unless it is decided (the planning prices are merge fields).

---

## 5. What SOS SMS is

### 5.1 The product

A pre-launch, two-sided network for emergency home repair, starting with plumbing and water emergencies. Homeowners join before anything breaks, on a monthly or annual membership, with their card and home address on file. In an emergency a member sends one text, and help is on the way: the request goes to licensed, insured contractors matched by trade and area, all at once, and the first who can come accepts and commits to an arrival time. The $99 trip charge goes on the card on file when a contractor accepts and is credited to the repair if the member goes ahead; there is no fee per request. Contractors join free, with no subscription and no lead fees. A 90-minute guarantee from the request text pays the member back when the window is missed.

The core thesis: be ready before it breaks. The homeowner's alternative is searching and calling down a list while the damage spreads, and in the middle of an emergency, calling a contractor from the search results beats joining anything; so SOS SMS is joined before the need, and the emergency itself takes one text. The contractor's alternative is paying for leads and sometimes not getting paid for showing up. Members fund the network; contractors join free and are paid before they roll.

### 5.2 Two audiences, never blended

| | Contractors (supply, Run 1) | Members (demand, Run 2) |
|---|---|---|
| Who | Licensed, insured plumbing and water-emergency contractors who take emergency calls | Homeowners in an open zone who join before anything breaks |
| Promise | No charge to see a request, and the trip paid before you roll | One text, and help is on the way: an arrival time when someone accepts, and a missed 90-minute window costs SOS SMS money |
| How they arrive | Cold email and a partnership program, then a referral loop; they sign up by text | Before the need: affiliates and email first, then search and SEO pages and paid sign-ups in open zones; member loops bring the next one |

### 5.3 The cross-side dependency

Every member promise is kept by a contractor first. The eight shared rows (identical in both briefs, Section 6): the 90-minute refund needs a late-arrival rule; relaunch needs a second trip-charge rule (decided: SOS SMS pays it from membership revenue, held out of copy, R17); "one text reaches" needs the dispatch rule; privacy needs approximate distance before acceptance; crediting the trip charge is a contractor obligation; known arrival time is a contractor commitment; verification needs a recheck cadence; zero cost to join needs the revenue model. Every row is closed or consistent. Eight further conflicts (A to H) are each resolved by a decision. Detail: `reference/marketplace-cross-side.md`.

### 5.4 Why supply leads

The member promises are only true where enough contractors say yes, so memberships open per zone only at the density number (R55). The density model: the contractors needed per trade, zone, and hour band are n ≥ ln(1 - c) / ln(1 - a), where a is the acceptance chance (planned at 0.30, R28) and c the coverage target. At 90 percent coverage, a of 0.10 needs 22 contractors, 0.30 needs 7, 0.40 needs 5 (illustrative); 9 for 95 percent at 0.30. Treat it as a floor. The other side of the same arithmetic: about 430 members per zone keep each of 9 founding contractors at about one request a month (R64). Detail: `reference/density-model.md`.

---

## 6. Feature matrix: what leads

Scored for demand and competitiveness, -20 to +20, from Bryan's ratings in the source matrix, moved by research (pre-launch scoring).

**Contractors.** Lead with the trip charge collected before rolling (10.6 / 11.8, the strongest competitive score: no lead platform in the researched set collects it for the contractor). Zero cost to join (17.6 / 6.3) opens the door but is not unique. High-urgency requests (11.2 / 7.9) support. Fast payout is a hero (6.8 / 3.1), set at within 2 business days of arrival (decision 6). Table stakes: matching by trade and area (16.4 / -8.7), decline freely, the customer stays the contractor's.

**Members.** Lead with one text starting dispatch, because the card and address are on file from joining (18.4 / 11.6, the highest on both axes). The 90-minute guarantee (17.9 / 9.6) and instant network access (15.2 / 7.4) stand with it; the known arrival time (11.6 / 4.2), privacy in its narrow form (9.7 / 6.1), and the readiness kit (6.4 / 3.4) support. The membership itself is table stakes (10.8 / -6.2): households know the format from clubs, warranties, and utility plans, so it opens the door and never leads. A price range before arrival (16.1 / 8.3) is wanted by all and not at launch (R49). Text-only access (-2.6 / 4.8) is a mechanic. Safety triage is required whatever its score.

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
| V3 One text, money-backed arrival window | 0.0 / 9.0 | SOS SMS projected; plumber clubs 6.0 for priority with one company |
| V4 Many contractors reached, one reply | 0.0 / 9.0 | SOS SMS projected |

**The wedge.** Every lead platform earns when a request arrives, so none can stop charging to look without changing its model. Every plan a household can buy today leaves the emergency itself alone: warranties and utility plans pay after a claim and a wait, and a plumber's club gives priority with one company. One text that reaches many contractors, with a money-backed window, needs local density no single company has. Defensibility is local density, not technology. Battlecards: `reference/competitor-battlecards.md`.

---

## 8. Ideal customer profile and buying committee

**Contractors.** Level 2 goes first: small plumbing and water damage shops with at least one paid lead source and an on-call technician. They have a savings anchor, night capacity, and have already accepted platforms. Level 1, owner-operators living on referrals, is recruited alongside to fill hours and refer other trades. Disqualifiers: unlicensed or uninsured, won't credit the trip charge, won't commit to an arrival time. Triggers: a lead platform renewal or price rise, a month of unreplied leads, a new technician, freeze season.

In a shop the committee is technician, dispatcher, owner. **The dispatcher is the likely blocker**, because a job accepted on a technician's phone goes around the dispatch board. Settle who receives requests before the first one arrives. Owners block on platform distrust and on the obligations. The founding cohort, sized by the density model, is the most valuable output of Run 1.

**Members.** Level 1 is a new homeowner without a go-to plumber (first-time buyers were 24 percent of buyers in the 2024 profile, S91); Level 2 is an established homeowner, usually in an older home, whose plumber does not answer at night. Both join before the need, through the partners and lists that already reach them: utility new-account offers, association welcome packets, newsletters, insurance agents for existing policyholders, prevention guides, and search at freeze season. The committee is a household of one or two adults deciding over days. **The blocker is "another subscription"**: a fee every month or year before anything breaks (R46). Others: "it rarely happens", "is my home covered at night", "how is this different from my warranty", a card on file with a new company, "can I cancel". It wins with the price and the trip charge stated plainly, the guarantee with its scope, cancel any time, the readiness scorecard, a trusted partner's mention, and privacy. The founding member area is the neighborhoods inside the founding contractor zone, nowhere else. Renters and property managers are out of scope.

Detail: `reference/icp-personas.md`.

---

## 9. Strategic verdicts

**Decided** (dated in `ops/decisions.md`):

1. Two runs, never blended: one value proposition per side.
2. Supply leads, memberships follow, zone by zone. Memberships open only at the density number, for covered hours; before then, the launch list.
3. Product-led, no sales team. No calls, demos, meetings, shop visits, or door-to-door on either side.
4. Contractor channels: cold email, a partnership program, an in-product referral loop.
5. Member channels (the membership revision, 2026-10-11): affiliates and email lead, before the need; search and SEO pages, paid search, and paid social support sign-ups in open zones; organic social and community posts by SOS SMS itself; member loops. Never an ad that sells dispatch in the middle of an emergency.
6. Do not contest volume or exclusivity (contractors), or repair coverage, brand familiarity, and guarantees on the work (members).
7. Claims follow the narrowed forms. Nothing invented, ever.
8. Speed only inside proven zones; slow down at thresholds set before launch.

**Decided 2026-10-03, revised 2026-10-11** (the twelve decisions, `ops/decisions.md`; every other value in `reference/resolution-register.md`): (1) the founding zone, a 10-mile radius in the founders' home metro, plumbing and water emergencies; (2) the revenue model: members pay a monthly or annual membership, planning values $10 a month or $100 a year (copy `{{monthly price}}`, `{{annual price}}`), no fee per request; contractors $0 in the founding period (the zone's first 6 months open to members), then $25 per completed paid job, founding contractors $0 a job for 12 months after it; (3) the late-arrival rule and guarantee scope together, fault-based, 90 minutes from the member's request text, the $99 trip charge back, covered areas and hours on the membership page, no acceptance told within 15 minutes; (4) dispatch to all matched at once, first to accept, approximate distance and cross-street area before acceptance, the address after; (5) one $99 trip charge per trade and zone, set by SOS SMS, on use. Then (6) Stripe Connect: the card saved at joining and billed monthly or annually; the trip charge authorized when the request text arrives, captured at acceptance, released on arrival, payout within 2 business days; (7) verification at sign-up, every 6 months, and at each policy's expiry; (8) safety reply first, no broadcast until the member is safe; (9) one registered local number; (10) the trademark and search check in Stage 0; (11) paid search sells memberships before the need, standard search ads after Google's written confirmation, never Local Services Ads; (12) the acquisition ceiling, about $43 per new paid member by channel (R63), replacing the per paid job ceiling.

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

**Positioning:** The emergency home repair membership you join before anything breaks, so the emergency itself is one text. Built on one message that reaches the vetted contractors for the trade at once, and an arrival window that costs SOS SMS money when it is missed.

| Pillar | Reasons to believe |
|---|---|
| VP1 One text, help on the way | One text reaches the licensed, insured contractors on SOS SMS for that trade nearby, at once; an arrival time when they accept, with their name and Google rating; if they are not there within 90 minutes of the text, the $99 trip charge comes back, in the zone's covered areas and hours |
| VP2 Ready before it happens | The card and home address are on file from joining, so there is nothing to fill in at 2 a.m.; no app and no phone tree, one number saved on joining; monthly or annual, cancel any time, a person by text |
| VP3 Know the cost and who is coming | The $99 trip charge only when a contractor accepts, credited to the repair; license and insurance checked; only the contractor who takes the job gets the address, and no selling or ad targeting |

Every drill describing the emergency text carries the safety line. Drills and conditions: `reference/value-proposition-members.md`.

---

## 12. Positioning statements

**Category:** an emergency home repair membership, by text; a local two-sided network. **Niche:** plumbing and water emergencies, one zone at a time.

**Contractors:** "For licensed plumbing and water-emergency contractors who are tired of paying for requests that never become work, SOS SMS is the emergency dispatch line where seeing a job costs nothing and the trip is paid before you roll."

**Members:** "For homeowners who want to be ready before something breaks, SOS SMS is the membership that makes a home emergency one text: the vetted contractors nearby see it at once, the first who can come commits to an arrival time, and if they miss the 90-minute window the trip charge comes back."

**Differentiation and defensibility.** Lead platforms cannot stop charging per request without changing their model, and no one else holds the visit payment before the contractor rolls. On the member side, a competitor needs the same contractor density in a zone before it can make the same one-text, money-backed promise, so density is both the constraint and the moat. A number saved in a phone before the pipe bursts is worth more than an ad seen during the flood.

**The two objections that matter most:**
- Contractors, "Every request is shared, like the platforms I quit": it is shared, openly, and losing one costs nothing because nobody pays to look.
- Members, "Another subscription, for something that rarely happens": say it first, then what the membership includes, the trip charge only on use, and cancel any time.

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
| 6 Advocacy | "The water damage guy should be on this" | Fifth-trip referral prompt; add a technician | Referrals per contractor |
| 7 Staying active | "Still worth it?" | Monthly summary; 30-day check-in | Active contractors vs density target |

Critical: terms in writing before sign-up; a fast first paid trip; payouts on time, every time. Blocker to watch: first-job silence, so recruit by zone and grow the zone's launch list in parallel.

**Member journey, two clocks: weeks before the need, minutes during it.**

| Stage | Mindset | Touchpoint | KPI |
|---|---|---|---|
| 1 Awareness | "Who would I even call at 2 a.m.?" | An affiliate's mention; a partner's email; the readiness scorecard; prevention guides | Scorecards and email sign-ups by channel |
| 2 Discovery | "What is it, and is my home covered?" | The membership page with the ZIP check; the launch list | ZIP checks; launch list joins |
| 3 Evaluation | "Worth it? What does it cost when I use it?" | **The membership page**: the price, the trip charge on use, the guarantee, what is not included, cancel any time | Page to join rate |
| 4 Join | "Sign me up" | Card, address, consent; the welcome texts; the contact card | Cost per new paid member by channel |
| 5 Value | "Something broke. One text." | The first reply; stop-the-water steps; acceptance with name and arrival time; automatic refund if late | Time to acceptance; share inside the window; refund rate |
| 6 Advocacy | "My neighbor should have this" | Two-question follow-up; forwardable card | Referrals per member |
| 7 Renewal | "Still worth keeping?" | Seasonal notes (opt-in); the renewal reminder; cancel any time | Monthly churn; annual renewal |

**The hand-off.** Acceptance is the moment both journeys meet: the contractor's commitment becomes the member's arrival time. Measured together: time from the request text to acceptance, share arriving within the window, share of refunds caused by SOS SMS. Detail: `reference/customer-journey.md`.

---

## 14. Channel and asset plan

**In the mix, contractors:** (1) cold email, zone by zone, four emails over twelve days; (2) partnership program: supply house counter cards, association newsletters, trade school job boards, a partner kit, a ten-minute explainer video; (3) in-product referral loop. The Lead Cost Check is the top of the funnel in all three. Lead magnet: the Job Leak Scorecard.

**In the mix, members:** (1) affiliates, before the need: utilities and cities, homeowner and neighborhood associations, local publications and newsletters, home content creators, home improvement retailers, insurance agents for existing policyholders, employers' benefit platforms, each with a code, the kit, and a disclosed commission (R61); (2) email, before the need: SOS SMS's own list from the readiness scorecard and the launch list, partner sends, and member email (welcome, seasonal notes, renewal); (3) search and SEO pages for sign-ups: prevention and problem guides, the membership page, zone pages, paid search (Google, then Microsoft) and paid social geofenced to open zones; plus member loops: the contact card, Text READY, the forwardable card, the two questions after a job, renewal. Lead magnet: "How Ready Is Your Home for a 2 a.m. Leak?"

**Out of the mix, refuse:** sales calls, demos, meetings, shop visits, door-to-door, LinkedIn ads and outreach, cold email or texts to homeowners, marketing texts without written consent, Local Services Ads (S70), ads that sell dispatch in the middle of an emergency, ad retargeting and pixels, and any payment to someone referring at a home purchase settlement (real estate agents, lenders, title and settlement agents; agents and inspectors may share SOS SMS without payment, S86, S94).

**Production order.** Contractors: the terms on one page and the contractor page, then the Lead Cost Check and sign-up by text, then the list and emails, then the partner kit, then the referral prompt. Members: Stage 0 terms (counsel-reviewed member terms and renewal disclosures, the affiliate terms, email setup, carrier registration), then the membership page and the guarantee page, then in Stage 1 the readiness scorecard, guides, and the launch list sequence, then the affiliate kit and the first partners with codes ready, then the member loops, then when the zone opens the opening email, affiliates live, and sign-up ads after Google's written confirmation. Engines: `reference/channel-engine-contractors.md`, `reference/channel-engine-members.md`.

---

## 15. Pricing and unit economics

**Structure, decided (decisions 2 and 5; decision 2 revised 2026-10-11).** Members pay a membership, monthly or annual, billed to the card on file: planning values $10 a month or $100 a year (two months free) until the launch price is set in Stage 0; copy writes `{{monthly price}}` and `{{annual price}}`. On use, the $99 trip charge goes on the card on file when a contractor accepts, is paid to the contractor, and is credited to the repair; there is no fee per request. Contractors pay $0 during the founding period, then $25 per completed paid job, never per request: a fifth of the about $125 the cheapest per-lead options cost per booked job at a 20 percent close rate (S03, S06, grade C, internal). Late-arrival rule, option C, fault-based: the contractor's own missed commitment funds the refund from their trip charge; SOS SMS pays for the misses it causes, from membership revenue.

**Member economics, illustrative (pricing model).** At $10 a month, a member costs about $1.49 a month to serve (card processing, messages, support and platform, and their share of request costs on both sides at 0.25 requests a year, refund reserve included), leaving about $8.51 a month of contribution in the founding period and $9.03 after it. The planning price sits at the closest analog's price, a plumber's club at $10 a month (S75), inside a band of $4.83 to $22.99 a month (S75 to S78, S80), far above the cost floor of about $3.75. The first 6 months of contribution at 6.5 percent monthly churn (R59) is the acquisition ceiling: about $43 per new paid member (R63). About 430 members per zone keep 9 founding contractors at about one request a month (R64).

**Acquisition, illustrative.** An affiliate's $20 commission (R61) sits under the ceiling and is paid back in the third month. Paid search at the plumbing benchmark ($10.49 a click, 7.63 percent converting, S15, B) costs about $137 per new paid member, about 3 times the ceiling, which is why affiliates and email lead and paid sign-ups only support. Levers: partner-led acquisition, retention, annual plans and more trades, and the contractor fee after the founding period. Detail: `reference/pricing-and-economics.md`.

---

## 16. Launch sequence and growth

Stage 0, decisions and plumbing: the twelve decisions written into the member terms, the guarantee, the terms on one page, and the founding agreement; the launch price; membership billing tested; counsel review of the member terms and automatic renewal disclosures (S87); the affiliate terms (S86, S88, S94); email sending; Google's written confirmation; carrier registration; payment hold and payout tested; the self-serve paths tested end to end; zone thresholds (R32) in the weekly review before launch. Stage 1, supply fills the founding zone while the launch list grows (the readiness scorecard, guides, affiliates signed with codes ready); gate: the density number met for the first trade, zone, and covered hours. Stage 2, memberships open: the opening email to the launch list, affiliates live, the membership page, then sign-up ads. Stage 3, prove the zone, then accelerate: zone proven, zone full (members growing toward about 430), metro proven, trade added. Slow down when refunds, acceptance, monthly churn, cost per new paid member, or contractor activity cross their thresholds (R32; ceiling, decision 12).

Affiliates and the launch list open each zone; paid sign-ups support only under the ceiling. Never traded for speed: claim accuracy, safety triage, paying contractors on time, automatic refunds, easy cancellation, privacy as promised, messaging, email, subscription, affiliate, and ad law. Detail: `reference/launch-and-growth.md`.

---

## 17. Brand identity

Green and white. The mark is a sent-message bubble holding a round dot (the member) and a square (the contractor): round is always a member, square always a contractor. Signal green is the yes; it never means alarm. Never red, sirens, crosses, bells, or "911" in the identity. One typeface, Inter, three weights, tabular figures. Voice: plain, exact, unhurried. Brand values: calm under pressure; kept, not claimed; fair to both sides; exact, never inflated. Detail and files: `reference/brand-identity.md`, `brand/logo/`.

---

## 18. Quick-reference cheatsheet

- **One-line positioning, contractors:** the emergency dispatch line where seeing a job costs nothing and the trip is paid before you roll.
- **One-line positioning, members:** the membership that makes a home emergency one text, with an arrival time when a contractor accepts and money back if they miss the window.
- **Flagship differentiators:** paid to show up (contractors); one text with the card on file, the guaranteed window, and one reply (members).
- **Table stakes:** matching by trade and area; license and insurance checks; the membership format itself.
- **Top-of-funnel hooks:** the Lead Cost Check; the readiness check before anything breaks.
- **Audiences:** contractors and members, never blended.
- **ICP first:** Level 2 shops; homeowners in the founding zone, reached before the need through partners and email.
- **Proof points on file:** the named records per drill (R45), which show each claim from the first job. No result is cited until the founding period produces real, permissioned ones.
- **Signature line:** "Every promise to a member is kept by a contractor first."
- **Primary rivals:** lead platforms (contractors); doing nothing in advance, plumber clubs, warranties, and utility plans (members).
- **Channels:** cold email, partners, referral loop; affiliates, email, search and SEO pages for sign-ups, member loops.
- **Do not say:** escrow, exclusive, pre-qualified, guaranteed arrival time, every contractor in your area, warranty, covers repairs, subscriber, any number not in the brain.
- **Always:** the full name SOS SMS; the safety line on urgent copy; register values as written, planning values labelled, `{{merge fields}}` for per-message details and the membership prices.

---

*End of the SOS SMS GTM master context. When status changes, update the ledger in `rules/` first, then this file, then `ops/decisions.md`, then the copy.*
