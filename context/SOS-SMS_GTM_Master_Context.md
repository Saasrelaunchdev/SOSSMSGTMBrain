---
title: SOS SMS Go-To-Market Master Context
project: SOS SMS
type: gtm_context_file
purpose: Single source of truth for any AI agent executing SOS SMS go-to-market work.
version: 1.1
last_updated: 2026-10-03
status_notes: Pre-launch. Nothing is live, so there are no contractors, customers, jobs, revenue, arrival times, or testimonials, and the closed set of proof points is empty. Every product capability is PLANNED, never shipped. Twelve founder decisions are open, including the revenue model, the late-arrival rule and guarantee scope, the dispatch rule, who sets the trip charge, and the launch zone. Google paid search eligibility is unconfirmed and carrier registration is not done. Brand v1 exists; its dark palette awaits approval. Every unknown number stays {TBD} and every copy line waiting on a decision keeps its [bracket].
canonical_vocabulary: SOS SMS, contractor, customer, request, trip charge, SOS SMS fee, arrival time, 90-minute window, guarantee, dispatch, matched contractors, accept, zone, hour band, density number, founding contractor, founding period, owned share, covered hours, first reply, Text READY, contact card, terms on one page, Lead Cost Check, safety line
---

# SOS SMS Go-To-Market Master Context

This file is the complete, distilled go-to-market for SOS SMS, both sides of the marketplace. It exists so that any AI agent can absorb the strategy, ICPs, positioning, messaging, competitive frame, funnels, channels, economics, and launch plan in one read, then execute go-to-market work precisely without re-deriving anything.

If you are an AI agent, read the next section first.

---

## 0. Agent operating instructions

**What this file is.** The distilled output of two complete `gtm-builder` runs (Run 1 contractors, Run 2 customers), their research and source register, the marketplace synthesis (cross-side check, speed-to-scale plan, launch sequence), and the deltas from the walkthrough build (brand identity, the TBD register, the built deck). Sources are listed in `ops/asset-index.md` and kept in `sources/`.

**How to use it.**

1. Before any customer-facing or contractor-facing copy, load the four `rules/` files. They govern naming, status, claims, and mechanics, and they override any instinct or older phrasing.
2. **Pick one side.** Contractors (supply) or customers (demand). Never blend them in one asset. A line written for a plumber and a homeowner at once is true of neither.
3. Respect the funnel stage (Section 13). Write to the stage, not past it.
4. Obey the verdicts in Section 9. They are decided. Do not contradict them, and do not present a recommendation as a decision.
5. Before shipping, run `ops/QA-checklist.md`.

**Hard guardrails, never violate:**

- SOS SMS is pre-launch. Never write a capability in the present tense as if it were live. Customer copy is written for launch day and held until the zone opens. Contractor recruiting copy goes out before launch and describes what SOS SMS is building, in the future tense.
- Never invent a number, count, arrival time, price, fee, testimonial, or result. Unknowns stay `{TBD}`. The proof-point set is empty.
- Never fill a `[bracket]`. It waits on a named founder decision (Section 9 and `ops/decisions.md`).
- Neither side's copy may promise what the other side's terms do not deliver (Section 5.3).
- Never present SOS SMS as the plumber, an emergency service, or anything that reads as 911. Carry the safety line wherever copy invites an urgent text.
- Always write the full name, SOS SMS. Never the first word alone.
- Only produce for the channels in Section 14. Refuse the excluded ones and say so.

---

## 1. House writing rules

No em dashes and no en dashes, including in ranges: write "$25 to $60". Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower. Short paragraphs, one to three sentences. Specific mechanics over adjectives: who pays what, and when.

Register: dispatch-room calm. Plain, exact, unhurried, each claim stated once with its source beside it. The subject is emergencies; the copy is not one. The customer may be standing in water, and the contractor has heard every platform pitch before. Full rules: `rules/writing-rules.md`.

---

## 2. Canonical vocabulary

| Term | Rule |
|---|---|
| SOS SMS | Always the full name. Unrelated plumbing companies use the first word alone |
| request | What a contractor receives. Never "lead" for an SOS SMS request: contractors associate leads with paying to look |
| trip charge | What the customer pays for the visit, agreed by text before dispatch, credited to the repair if they go ahead. Not a "service fee" or "call-out fee" |
| SOS SMS fee | The customer-side per-request fee, recommended home of SOS SMS revenue. Amount {TBD} |
| arrival time vs 90-minute window | The arrival time is the contractor's commitment on accepting. The window is the guarantee. Never "guaranteed arrival time" |
| dispatch | What SOS SMS does. The contractor does the work |
| matched contractors | Contractors on SOS SMS matched by trade and area. Never "every contractor in your area" |
| zone, hour band | The unit of launch and of density |
| founding contractor, founding period | The launch cohort and the period in which contractors pay $0 (recommended) |
| first reply | The automated reply to a customer's first text |

Full table, including banned near-synonyms: `rules/glossary.md`.

---

## 3. Status ledger

Nothing is shipped. Legend and the full list: `rules/feature-status.md`. In short:

- **PLANNED** (in the product design, build status unconfirmed): one number by text; broadcast to matched contractors; arrival time on acceptance; 90-minute guarantee with automatic refund (scope open); trip charge stated and collected before dispatch and credited to the repair; license and insurance checks; Google rating sent with acceptance; stop-the-water first reply; safety triage; contact card, Text READY, forwardable card; contractor sign-up by text; accept or decline freely; zero cost to join (depends on the revenue model); add-a-technician flow; fifth-trip referral prompt; Lead Cost Check.
- **DESIGN OPEN**: hiding the customer's identity until acceptance (conflict C); payout timing; pay-on-arrival for customers without a card.
- **CANDIDATE** (proposed by research, not in the product): price range before arrival; photos before accepting; requests accepted by text on the contractor side; customer relationship policy.
- **NOT BUILT, out of copy**: relaunch guarantee. **FLAG ONLY**: paid priority for contractors, household membership.
- **Launch prerequisites NOT DONE**: carrier registration, Google eligibility and message asset verification, payment provider, name and trademark check, counsel review.
- **Internal assets BUILT**: the GTM walkthrough deck; brand identity v1.

---

## 4. Claim hygiene ledger

The spine of `rules/do-not-say.md`. The claims the source matrix made, and what survived research:

| Source claim | Verdict |
|---|---|
| "Zero cost to join. Only we can do this" | Not unique: free sign-up is common and warranty networks charge no join fee (S33). Say "no subscription and no per-lead fees" and state how SOS SMS is paid in the same sentence, once decided |
| "Guaranteed trip charge, held in escrow" | Say "the customer pays the trip charge before you roll, and SOS SMS holds it until you arrive" plus the release rule. "Escrow" only if a licensed escrow arrangement holds the funds |
| "Pre-qualified leads, confirmed in your area and trade" | Say "matched to the trades and service area you set". The FTC found a platform's quality claims unsubstantiated (S01) |
| "High-urgency leads, customers ready to buy now" | Say "requests come from people with an active problem who want someone now". Some decline the quote |
| "One text reaches every qualified contractor in your area" | Say "reaches the vetted contractors on SOS SMS for your trade", only in zones at density |
| "Text-only access, only we can do this" | Plumbers already take texts (S64). A mechanic, never "only we" |
| "Private by design, never shared" | The accepting contractor gets the address. Say "only the contractor who takes your job gets your address and details" once the design is made |
| "Verified license and insurance, so you know they're qualified" | Say "we check license and insurance before they can take a job". Licenses, not workmanship |
| "90-minute guarantee" | Only with clock start, refund, and covered areas and hours in the same sentence (decision 3) |
| "Relaunch guarantee" | Not built. Out of every piece of copy |

Never: exclusive requests, more jobs, earnings, any volume, any average arrival time, damage prevented, a guarantee on the repair, any price or fee as a number.

---

## 5. What SOS SMS is

### 5.1 The product

A pre-launch, two-sided marketplace for emergency home repair, starting with plumbing and water emergencies. A person with a problem at home texts one number. The request goes to licensed, insured contractors matched by trade and area, all at once, and the first who can come accepts and commits to an arrival time. The customer agrees to a trip charge by text before anyone is dispatched; it is credited to the repair if they go ahead. Contractors join free, with no subscription and no lead fees. A 90-minute guarantee pays the customer back when the window is missed.

The core thesis: the customer's alternative is searching and calling down a list while the damage spreads; the contractor's alternative is paying for leads and sometimes not getting paid for showing up. One text, with the trip charge collected before anyone rolls, answers both.

### 5.2 Two audiences, never blended

| | Contractors (supply, Run 1) | Customers (demand, Run 2) |
|---|---|---|
| Who | Licensed, insured plumbing and water-emergency contractors who take emergency calls | Homeowners in the founding zone with an urgent plumbing or water problem |
| Promise | No charge to see a request, and the trip paid before you roll | One text, an arrival time when someone accepts, and a missed 90-minute window costs SOS SMS money |
| How they arrive | Cold email and a partnership program, then a referral loop; they sign up by text | Bottom-of-funnel search and problem-solving pages at the moment of need; product loops bring them back |

### 5.3 The cross-side dependency

Every customer promise is kept by a contractor first. The eight shared rows (identical in both briefs, Section 6): the 90-minute refund needs a late-arrival rule; relaunch needs a second trip-charge rule (parked); "one text reaches" needs the dispatch rule; privacy needs approximate distance before acceptance; crediting the trip charge is a contractor obligation; known arrival time is a contractor commitment; verification needs a recheck cadence; zero cost to join needs the revenue model. Six rows are consistent or parked, two are open and compatible. Eight further conflicts (A to H) each have a recommended resolution. Detail: `reference/marketplace-cross-side.md`.

### 5.4 Why supply leads

The customer promises are only true where enough contractors say yes. The density model: the contractors needed per trade, zone, and hour band are n ≥ ln(1 - c) / ln(1 - a), where a is the acceptance chance (unknown until measured) and c the coverage target. At 90 percent coverage, a of 0.10 needs 22 contractors, 0.30 needs 7, 0.40 needs 5 (illustrative). Treat it as a floor. Detail: `reference/density-model.md`.

---

## 6. Feature matrix: what leads

Scored for demand and competitiveness, -20 to +20, from Bryan's ratings in the source matrix, moved by research (pre-launch scoring).

**Contractors.** Lead with the trip charge collected before rolling (10.6 / 11.8, the strongest competitive score: no lead platform in the researched set collects it for the contractor). Zero cost to join (17.6 / 6.3) opens the door but is not unique. High-urgency requests (11.2 / 7.9) support. Fast payout is a provisional hero (6.8 / 3.1, unbuilt). Table stakes: matching by trade and area (16.4 / -8.7), decline freely, the customer stays the contractor's.

**Customers.** Lead with the 90-minute guarantee (17.9 / 9.6, highest on both axes) and instant network access (15.2 / 7.4). Privacy in its narrow form (9.7 / 6.1) and the known arrival time (11.6 / 4.2) support. The strongest new finding is a price range before arrival (16.1 / 8.3): wanted by all, offered by few, not in the product. Text-only access (-2.6 / 4.8) is a mechanic. Safety triage is required whatever its score.

**Demand drivers.** Contractors: the Lead Cost Check, a two-minute calculator of true cost per booked job. Customers: stop-the-water help in the first reply, value before payment. Detail: `reference/feature-matrix.md`.

---

## 7. Competitive market analysis

**Contractor side** weighs: C1 Angi Leads, C2 Thumbtack, C3 Google Local Services Ads, C4 Service Direct, C5 home warranty networks (American Home Shield, Frontdoor), C6 the status quo (word of mouth and their own listing). Praised for volume and exclusive calls; criticized for paying for leads that never reply, shared requests, and unpaid trips. Plumbing cost per lead: Angi $25 to $60 (S03, C), Thumbtack $25 to $45 (S06, C), Google LSA about $57 to $69 (S08, C), Service Direct $60 to $255 exclusive (S10, A).

| Vector, contractors | SOS SMS current / projected | Leader |
|---|---|---|
| V1 Lead volume and reach (they lead) | 0.4 / 4.2 | Google LSA 9.1 |
| V2 Exclusive calls (they lead) | 0.0 / 2.8 | Status quo 9.5 |
| V3 No charge for requests that never become work | 0.0 / 9.4 | SOS SMS projected, with the status quo |
| V4 Paid to show up | 0.0 / 9.1 | SOS SMS projected |

**Customer side** weighs: D1 search and call down the list, D2 Roto-Rooter, D3 Benjamin Franklin Plumbing, D4 Angi, D5 Thumbtack, D6 American Home Shield. Praised for availability, punctuality guarantees, and guarantees on the work; criticized for no-shows, unanswered nights, surprise fees, and floods of calls.

| Vector, customers | SOS SMS current / projected | Leader |
|---|---|---|
| V1 Always-open, trusted brand (they lead) | 0.0 / 3.1 | Roto-Rooter 9.3 |
| V2 Guarantee on the work (they lead) | 0.0 / 2.4 | Angi 8.4 |
| V3 Guaranteed arrival window | 0.0 / 8.8 | SOS SMS projected; Benjamin Franklin 7.9 for booked appointments |
| V4 Many contractors reached, one reply | 0.0 / 9.0 | SOS SMS projected |

**The wedge.** Every lead platform earns when a request arrives, so none can stop charging to look without changing its model; a single plumbing company cannot broadcast to rivals, and a quote site earns from everyone calling back. Defensibility is local density, not technology. Battlecards: `reference/competitor-battlecards.md`.

---

## 8. Ideal customer profile and buying committee

**Contractors.** Level 2 goes first: small plumbing and water damage shops with at least one paid lead source and an on-call technician. They have a savings anchor, night capacity, and have already accepted platforms. Level 1, owner-operators living on referrals, is recruited alongside to fill hours and refer other trades. Disqualifiers: unlicensed or uninsured, won't credit the trip charge, won't commit to an arrival time. Triggers: a lead platform renewal or price rise, a month of unreplied leads, a new technician, freeze season.

In a shop the committee is technician, dispatcher, owner. **The dispatcher is the likely blocker**, because a job accepted on a technician's phone goes around the dispatch board. Settle who receives requests before the first one arrives. Owners block on platform distrust and on the obligations. The founding cohort, sized by the density model, is the most valuable output of Run 1.

**Customers.** Level 1 has no go-to contractor; Level 2 has one who doesn't answer at night. Both are reached at the moment they search for help. The committee collapses to the person at home deciding in minutes. **The blocker is the payment link from an unknown number**, the pattern of text scams that cost consumers $470 million in 2024 (S59, A). Others: no card at hand (76.4 percent of households had a credit card; 4.2 percent were unbanked, S61, A), fear of being overcharged, wanting a voice. The founding customer area is the neighborhoods inside the founding contractor zone, nowhere else. Renters and property managers are out of scope.

Detail: `reference/icp-personas.md`.

---

## 9. Strategic verdicts

**Decided** (dated in `ops/decisions.md`):

1. Two runs, never blended: one value proposition per side.
2. Supply leads, demand follows, zone by zone. Demand opens only at the density number, for covered hours.
3. Product-led, no sales team. No calls, demos, meetings, or shop visits on either side.
4. Contractor channels: cold email, a partnership program, an in-product referral loop.
5. Customer channels: bottom-of-funnel paid search (Google, then Microsoft), problem-solving pages, product loops. No outreach.
6. Do not contest volume or exclusivity (contractors), or brand familiarity and guarantees on the work (customers).
7. Claims follow the narrowed forms. Nothing invented, ever.
8. Speed only inside proven zones; slow down at thresholds set before launch.

**Recommended, not decided** (the twelve decisions, `cross-side-check.md` Part 3). The first five unblock the copy on both sides: (1) launch zone, one zone in one metro, plumbing and water; (2) revenue model, customer fee plus $0 to contractors in the founding period, then a per-completed-job contractor fee; (3) late-arrival rule and guarantee scope together, fault-based, clock from the text, refund equals the trip charge; (4) dispatch rule, all matched at once, first to accept, approximate distance not address; (5) one trip charge per trade and zone, set by SOS SMS. Then (6) payments, capture at acceptance and release on arrival; (7) verification recheck cadence {TBD}; (8) safety handling; (9) carrier registration; (10) name and trademark check; (11) Google paid search eligibility in writing; (12) the paid search ceiling per zone {TBD}.

---

## 10. Value proposition: contractors

**Brand promise:** Emergency jobs you choose, with the trip paid before you roll.

**Positioning:** The emergency dispatch line where seeing a request costs nothing. Built on two things lead platforms do not do: no charge to receive a request, and the trip charge collected before the contractor drives out.

| Pillar | Reasons to believe |
|---|---|
| VP1 No lead fees | No subscription and no per-lead fee; a request you do not win costs you nothing; decline freely without it changing which requests reach you |
| VP2 Paid to show up | The trip charge is collected before you leave; release and payout timing stated before your first job; the customer has already agreed to the trip charge, and it counts toward the work |
| VP3 Know the job before you go | Requests from people with an active problem; matched to the trades and area you set; photos or video before you accept, when the customer sends them |

Every social-proof headline and proof point is {TBD}. Drills and their conditions: `reference/value-proposition-contractors.md`.

---

## 11. Value proposition: customers

**Brand promise:** Text once, and a vetted contractor is on the way, with the trip charge stated before anyone comes.

**Positioning:** The emergency repair line you text instead of calling down a list. Built on one message that reaches the vetted contractors for the trade at once, and an arrival window that costs SOS SMS money when it is missed.

| Pillar | Reasons to believe |
|---|---|
| VP1 On the way, inside a guaranteed window | One text reaches the licensed, insured contractors on SOS SMS for that trade nearby, at once; an arrival time when they accept; if they are not there within 90 minutes of [scope], [refund] comes back |
| VP2 One text, one reply | Works entirely by text; only the contractor who takes your job gets your address and details; no selling your information, no ad targeting |
| VP3 Know the cost and the contractor first | The trip charge before anyone is sent, credited if you go ahead; license and insurance checked; the contractor's Google rating, where they have one |

Every drill inviting a text carries the safety line. Drills and conditions: `reference/value-proposition-customers.md`.

---

## 12. Positioning statements

**Category:** emergency home repair dispatch by text, a local two-sided marketplace. **Niche:** plumbing and water emergencies, one zone at a time.

**Contractors:** "For licensed plumbing and water-emergency contractors who are tired of paying for requests that never become work, SOS SMS is the emergency dispatch line where seeing a job costs nothing and the trip is paid before you roll."

**Customers:** "For homeowners with a plumbing or water emergency and no one answering, SOS SMS is the one text that reaches the vetted contractors nearby, with an arrival time when one accepts and money back if they miss the window."

**Differentiation and defensibility.** Lead platforms cannot stop charging per request without changing their model, and no one else holds the visit payment before the contractor rolls. On the customer side, a competitor needs the same contractor density in a zone before it can make the same window promise, so density is both the constraint and the moat.

**The two objections that matter most:**
- Contractors, "Every request is shared, like the platforms I quit": it is shared, openly, and losing one costs nothing because nobody pays to look.
- Customers, "Is this text a scam?": the first reply says who SOS SMS is, the trip charge, and the guarantee scope before any link.

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

Critical: terms in writing before sign-up; a fast first paid trip; payouts on time, every time. Blocker to watch: first-job silence, so recruit by zone.

**Customer journey, minutes not days.**

| Stage | Mindset | Touchpoint | KPI |
|---|---|---|---|
| 1 Awareness | "Water is coming through the ceiling at 1 a.m." | Problem ad groups and guides | Text-button taps |
| 2 Discovery | "Who can I get at this hour?" | Emergency ads with text-from-ad; zone page; saved card | First texts by source |
| 3 Evaluation | "Is this legit? What will it cost?" | **The first reply**, before any link | Reply-to-agreement rate |
| 4 Purchase | "Send someone" | Payment link after agreement; contractor name and arrival time | Time to acceptance |
| 5 Value | "They're here, inside the window" | Arrival text; automatic refund if late | Share inside the window; refund rate |
| 6 Advocacy | "My neighbor had this last winter" | Two-question follow-up; forwardable card | Forwards per job |
| 7 Loyalty | "I know who to text" | Contact card kept | Saved-number rate; repeat requests |

**The hand-off.** Acceptance is the moment both journeys meet: the contractor's commitment becomes the customer's arrival time. Measured together: time to acceptance, share arriving within the window, share of refunds caused by SOS SMS. Detail: `reference/customer-journey.md`.

---

## 14. Channel and asset plan

**In the mix, contractors:** (1) cold email, zone by zone, four emails over twelve days; (2) partnership program: supply house counter cards, association newsletters, trade school job boards, a partner kit, a ten-minute explainer video; (3) in-product referral loop. The Lead Cost Check is the top of the funnel in all three. Lead magnet: the Job Leak Scorecard.

**In the mix, customers:** (1) paid search, Google then Microsoft, emergency and problem ad groups, geofenced to zones at density and scheduled to covered hours; (2) problem-solving pages and zone pages; (3) product loops: stop-the-water first reply, contact card, forwardable card, Text READY, automatic refund text. Lead magnet: "How Ready Is Your Home for a 2 a.m. Leak?"

**Out of the mix, refuse:** sales calls, demos, meetings, shop visits, LinkedIn ads and outreach, outbound email or texts to homeowners, marketing texts without written consent, Local Services Ads (closed to a dispatch model, S70), partnerships with agents, inspectors, hardware stores, or homeowner associations, posts in neighborhood groups, ad retargeting and pixels. Organic social and newsletters are not in the mix; treat as out until a decision adds them.

**Production order.** Contractors: the terms on one page and the contractor page, then the Lead Cost Check and sign-up by text, then the list and emails, then the partner kit, then the referral prompt. Customers: Google eligibility and carrier registration, then the first reply and guarantee page, then the zone page and first ad groups, then five problem guides, then the loops, then Microsoft. Engines: `reference/channel-engine-contractors.md`, `reference/channel-engine-paid-search.md`.

---

## 15. Pricing and unit economics

**Structure, recommended.** Customers pay per request: a trip charge credited to the repair plus an SOS SMS fee, both shown before dispatch, both {TBD}. Contractors pay $0 during the founding period, then a per-completed-job fee, never per request, below about $125 per booked job: what the cheapest per-lead options cost at a 20 percent close rate (S03, S06, grade C). Late-arrival rule, recommended option C, fault-based: the contractor's own missed commitment funds the refund from their trip charge; SOS SMS pays for the misses it causes.

**Paid search economics, illustrative.** $10.49 a click with 7.63 percent of clicks becoming leads (S15, B) is about $137 per first text; at an assumed 50 percent first-text-to-paid rate, about $275 per paid job. The emergency dataset (S69, C) gives about $216 and $431. Trip charges run $75 to $100 when charged (S28, C). **A customer fee alone will not pay back paid search on the first job.** Four levers close it: owned share (at 50 percent owned, about $137), jobs per customer (at 1.5, about $183), cheaper clicks (Microsoft 30 to 60 percent cheaper, S74, C), and revenue from both sides after the founding period. Detail: `reference/pricing-and-economics.md`.

---

## 16. Launch sequence and growth

Stage 0, decisions and plumbing: all twelve decisions written down; Google eligibility; carrier registration; payment hold and payout tested; both self-serve paths tested end to end; terms and guarantee counsel-reviewed; zone thresholds set before launch. Stage 1, supply fills the founding zone; gate: the density number met for the first trade, zone, and covered hours. Stage 2, demand opens through search. Stage 3, prove the zone, then accelerate: zone proven, zone full, metro proven, trade added. Slow down when refunds, acceptance, contractor activity, or cost per paid job cross their thresholds.

Paid search is the liquidity engine of a new zone; owned channels are the profit engine of a mature one. Never traded for speed: claim accuracy, safety triage, paying contractors on time, automatic refunds, privacy as promised, messaging and ad law. Detail: `reference/launch-and-growth.md`.

---

## 17. Brand identity

Green and white. The mark is a sent-message bubble holding a round dot (the customer) and a square (the contractor): round is always a customer, square always a contractor. Signal green is the yes; it never means alarm. Never red, sirens, crosses, bells, or "911" in the identity. One typeface, Inter, three weights, tabular figures. Voice: plain, exact, unhurried. Brand values: calm under pressure; kept, not claimed; fair to both sides; exact, never inflated. Detail and files: `reference/brand-identity.md`, `brand/logo/`.

---

## 18. Quick-reference cheatsheet

- **One-line positioning, contractors:** the emergency dispatch line where seeing a job costs nothing and the trip is paid before you roll.
- **One-line positioning, customers:** the one text that reaches the vetted contractors nearby, with an arrival time when one accepts and money back if they miss the window.
- **Flagship differentiators:** paid to show up (contractors); the guaranteed window and one reply (customers).
- **Table stakes:** matching by trade and area; license and insurance checks.
- **Top-of-funnel hooks:** the Lead Cost Check; stop-the-water help in the first reply.
- **Audiences:** contractors and customers, never blended.
- **ICP first:** Level 2 shops; homeowners in the founding zone, reached while searching.
- **Proof points on file:** none. The set is empty until the founding period produces permissioned results.
- **Signature line:** "Every promise to a customer is kept by a contractor first."
- **Primary rivals:** lead platforms (contractors); search and call, Benjamin Franklin on punctuality (customers).
- **Channels:** cold email, partners, referral loop; paid search, problem pages, product loops.
- **Do not say:** escrow, exclusive, pre-qualified, guaranteed arrival time, every contractor in your area, any number not in the brain.
- **Always:** the full name SOS SMS; the safety line on urgent copy; brackets and {TBD} kept visible.

---

*End of the SOS SMS GTM master context. When status changes, update the ledger in `rules/` first, then this file, then `ops/decisions.md`, then the copy.*
