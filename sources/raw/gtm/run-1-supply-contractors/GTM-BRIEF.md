# SOS SMS, Run 1 of 2: Supply Side (Contractors), GTM Builder Discovery Brief

The filled discovery input for the `gtm-builder` skill, contractor side. This is what the skill's REQUIRED INPUTS checklist asks for, answered for the people who do the work. The customer side is a separate run with its own brief in `../run-2-demand-customers/`.

Read `SKILL-ADAPTATION.md` before Phase 1. The skill is written for B2B SaaS and SOS SMS is a two-sided marketplace, so this run covers one side only, and seven of the nine phases carry a documented substitution or note.

**Global rule for the whole run,** taken from the skill's own deck prompt and applied everywhere: if a metric is unknown, keep it as `{TBD}` and do not invent numbers. As far as the source shows, SOS SMS is pre-launch, with no contractors signed, no jobs completed, no revenue, and no testimonials, so every proof point, count, and benchmark is `{TBD}` until the founders supply one.

**Source:** `Product Features Matrix _ SOSSMS - Sheet1.csv`, the only file in this repo at commit `bd90d1a`, read 2026-10-01. Plus the instruction given with the request on 2026-10-01: SOS SMS is a two-sided marketplace, with one GTM for the supply side and one for the demand side. A web search on 2026-10-01 found no SOS SMS website. The matrix refers to a founder memo ("a benefit your memo implied") that is not in this repo.

## Classification

The four facts everything downstream reads from. Identical in both briefs.

| | |
|---|---|
| Archetype | Marketplace. Two-sided, local, on-demand home repair |
| Audiences | Two. Supply: licensed, insured trade contractors. Demand: people with an urgent problem at home. Two runs, never blended |
| Evidence state | Pre-launch, as far as the source shows. It carries no customers, contractors, jobs, revenue, or testimonials, and marks one feature as not yet built. Confirm with the founders |
| Motion | Product-led, no sales team. Demand is self-serve: customers find SOS SMS at the moment of need through bottom-of-funnel search ads and problem-solving pages, then text in. Supply is self-serve: contractors arrive through cold email and a partnership program and sign up by text. Growth follows `../marketplace/speed-to-scale-plan.md` |

## Run order

`gtm-builder` builds one GTM per run, so SOS SMS runs twice. The two runs are never blended into one, because a value proposition written for a plumber and a homeowner at once is true of neither. **This run, supply, goes first.** Three reasons:

1. Every headline promise on the customer side depends on contractor density. "One text reaches every qualified contractor in your area" and the 90-minute guarantee are only true where enough contractors have joined. A demand GTM written before supply exists makes promises the network cannot keep, and the 90-minute guarantee turns each broken promise into a refund.
2. The contractor is a small business buying a way to get jobs, which is close to the shape `gtm-builder` was written for. ICP firmographics, a buying committee in larger shops, and ROI anchoring against what contractors pay for jobs today all run close to as written.
3. This run's Step 5.2, the founding contractor cohort, decides the launch metro, the trades, and the coverage area. The demand run then targets the same place.

Run 2 borrows structure from Phases 3, 6, and 7 here. It does not borrow claims: each side's copy is checked against Section 6 of its own brief.

---

# 1. PROJECT INFORMATION

**Shared by both runs**

| Field | Value |
|---|---|
| Project name | SOS SMS |
| Project website | `{TBD}`. No site found in a 2026-10-01 web search, see open decision 7 |
| Category name | Emergency home repair dispatch by text. A local, two-sided services marketplace |
| Business model | A customer texts one number. The request goes to contractors matched by trade and service area. A contractor accepts and commits to an arrival time. The customer pays a trip charge up front, credited to the job if they go ahead. Contractors pay no subscription and no lead fee. How SOS SMS itself earns money is `{TBD}`, open decision 2 |
| Core thesis, as read from the matrix | The customer's alternative is googling and calling down a list while the damage spreads. The contractor's alternative is paying for leads and sometimes not getting paid for showing up. One text, with the trip charge collected before anyone rolls, answers both |
| Target market | `{TBD}`. The source names no country, region, or metro. Its vocabulary (licensed and insured, trip charge, Google reviews) reads as United States. Confirm |

**This run**

| Field | Value |
|---|---|
| Audience | Licensed, insured trade contractors who will take emergency calls |
| Niche focus | Trades `{TBD}` in launch metro `{TBD}`, open decision 1. Proposed default: one metro, plumbing and water emergencies first, because the source's only worked example is "water's on the floor" |
| One-liner | SOS SMS sends contractors emergency jobs matched to their trade and service area, with no subscription and no lead fees, and the customer's trip charge collected before they roll. |

---

# 2. COMPETITORS

The skill wants 5 to 6 named competitors with websites, and its Step 2.1 is an external research step where you source them.

Nothing below names a company. No research has been done yet, and a fabricated competitor would poison Phase 2 and every phase that reads from it. The slate says where each slot comes from. `RESEARCH-PROMPTS.md` Step 0 fills it.

The contractor is the buyer in this run, so these are the ways a contractor gets emergency jobs today, not the ways a homeowner finds a contractor. The customer side has its own slate.

| Slot | Source from | Why it belongs |
|---|---|---|
| 1 | On-demand platforms that dispatch urgent home repair requests to independent contractors | The closest direct substitute: the same promise to the contractor, a job now rather than a quote request for later |
| 2 | Free local presence: the contractor's own free business and maps listing, and free directory profiles | The free option every contractor already has, and where many emergency searches end |
| 3 | Word of mouth, repeat customers, referrals from other trades, and the contractor's own after-hours phone | Where most contractors solve this today without anyone's help. Expect it to be the strongest rival |
| 4 | National home-services marketplaces that charge contractors per lead or per job, and search engine pay-per-lead ad programs for local services | The better-known option a contractor compares "no lead fees" against |
| 5 | Hiring it: an after-hours answering service or dispatcher, or running their own paid search | Not a company. Profile it from answering service price pages and dispatcher job postings: pay band, hours, time to hire |
| 6 | Home warranty companies and insurer contractor networks that route repair jobs at set rates, plus local trade associations | Institutional. Warranty and insurer networks compete for the same contractor hours. Associations are more likely partners than rivals |

**Selection rule:** a competitor earns a slot only if a contractor actually weighs it against SOS SMS. Not who the founders think of as a rival, who the contractor considers instead. For many owner-operators the honest answer is slot 3, "my phone already rings enough", and that is a finding, not a gap. `RESEARCH-PROMPTS.md` Step 0 sources the slate.

---

# 3. CONTRACTOR FEATURES LIST

Phase 1 runs per side, so this run rates the contractor items only. The two-axis matrix fits a platform's features, so Phase 1 runs close to as written. See `SKILL-ADAPTATION.md`.

The source matrix already rates each item on two axes: Market Relevance (Wanted by All, Most, or Some) and Competitive Differentiation (Unique To Us, A few others can do this, Most vendors can do this). Those ratings are Bryan's, and they are recorded below as **starting hypotheses**. They are self-assessment, not research, and Step 1.1 tests them.

Items marked **stated** came from the source, in its wording. **Inferred** means the source itself says the item was implied rather than stated. Items marked **candidate** are additions to rate and then keep or cut during Phase 1, and none is confirmed to exist. Section 5 narrows the wording for copy. Phase 1 rates the items under their source names.

| # | Item | Source | Built? | Bryan's rating: Relevance / Differentiation |
|---|---|---|---|---|
| 1 | Zero cost to join. No subscription or lead fees | stated | `{TBD}` | All / Unique To Us |
| 2 | High-urgency leads. Active emergencies, customers ready to buy now | stated | `{TBD}` | Most / A few others |
| 3 | Pre-qualified leads. Every job is confirmed to be in your service area and your trade | stated | `{TBD}` | All / Most vendors |
| 4 | Guaranteed trip charge. Held in escrow, so you won't get stiffed if you show up | stated | `{TBD}` | All / Most vendors |
| 5 | Photos and video before you roll | inferred. The source says "a benefit your memo implied, not one you stated" | `{TBD}` | Most / A few others |
| 6 | Accept or decline freely. You only take the jobs you want | stated | `{TBD}` | Most / Most vendors |
| 7 | The customer relationship stays with the contractor after the job | candidate | `{TBD}`, policy not stated | not rated |
| 8 | Trip charge payout timing: how soon after arrival the money lands | candidate | `{TBD}` | not rated |
| 9 | Jobs arrive and are accepted by text, no app, matching the customer side | candidate | `{TBD}`. The source says the customer side is text-only and says nothing about the contractor side | not rated |

**What joining asks of a contractor.** The customer-side promises create contractor obligations that the matrix does not list. Phase 1 does not rate these, but Phases 6 and 7 have to state them, because otherwise a contractor first meets them in the terms.

- Commit to an arrival time when accepting. This comes from the customer feature "Known ETA"
- Credit the trip charge toward the work if the customer goes ahead. From "Trip charge credited to the job"
- Arrive inside the 90-minute window, or accept the consequence set by open decision 3
- Submit license and insurance documents, and keep them current. From "Verified license and insurance"

**Matrix rows that cannot be used yet.** Bryan's contractor section has four rated rows with no item text, and the "CONTRACTOR FEATURES" header row itself carries a rating. Ali's section has 18 rated rows and no item text at all. None of these can be attributed to an item. Ask Bryan and Ali which items they belong to, or delete them, before Phase 1. Open decision 6.

**Deliberately not offered, and not to be rated:** a minimum number of jobs, and exclusive jobs. Each request goes to every matched contractor (open decision 4). Naming both plainly is a selling asset. A contractor who has bought shared leads before will assume the worst unless told up front.

---

# 4. BUSINESS CONTEXT

The skill's fourth input block. None of this is in the source. All four lines need filling.

```
Current team structure:      {TBD}. The matrix names two contributors, Bryan and Ali. Roles not stated
Monthly burn rate:           {TBD}
Runway remaining:            {TBD}
Channels tried, and results: {TBD}. Proposed default, to confirm: none tried, pre-launch
```

If nothing has been tried yet, write "none tried, pre-launch" rather than leaving it blank. That is a real answer and it changes what Phase 8 should recommend.

**Pricing status: deferred.** The supply-side mechanics are stated: no subscription and no lead fee. Every number, the trip charge amount, and how SOS SMS earns money are `{TBD}`. Phase 9 still runs, because the take rate structure and the ROI anchors are worth having before the numbers exist.

**Proof set: empty and closed.** A row is added only when all four columns can be filled. A paraphrased proof point is an unapproved proof point.

| Proof point | Exact permitted wording | Source | Recorded permission |
|---|---|---|---|
| none yet | | | |

## Open decisions that change the output

Ordered by what they block. Proposed defaults are proposals, not decisions, and none of them goes into copy until confirmed.

| # | Decision | Blocks | Note |
|---|---|---|---|
| 1 | Launch metro and trades | Step 0, Phases 2, 4, 5.2, 8. Run 2 inherits the answer | Proposed: one metro, plumbing and water emergencies first. The source's only worked example is water on the floor |
| 2 | How SOS SMS earns money, and which side is subsidized | Phase 9 in both runs, and the "zero cost to join" claim | No default. Options for Phase 9 to price: a customer fee on top of the trip charge, a share of the trip charge, or a share of the completed job. The second and third make "zero cost" untrue as written |
| 3 | Late arrival: what happens to the contractor's trip charge when the customer's 90-minute guarantee pays out | Phases 6 and 9, and the "guaranteed trip charge" claim | No default. If the contractor forfeits it, the claim narrows to "paid when you arrive inside the window". If SOS SMS absorbs it, it is a cost line in Phase 9 |
| 4 | Dispatch rule: does each request go to every matched contractor at once, first to accept wins, or to one contractor at a time | Phase 1 ratings of items 2 and 3, Phases 6 and 7 | Proposed reading, from the customer feature "one text reaches every qualified contractor in your area at once": all at once, first to accept wins. Confirm |
| 5 | Build status of each item in Section 3 | Phases 1 and 6 | Proposed: treat every item as planned until confirmed shipped. Nothing unshipped goes into copy in the present tense |
| 6 | The founder memo, and the matrix rows with no item text | Phase 1 | Add the memo the matrix was drawn from to this repo. Attribute or delete Ali's 18 rows and Bryan's 5 rated rows with no item text |
| 7 | Name collision | Phase 8 search channels in both runs | A 2026-10-01 web search for "SOS SMS" returned several unrelated local plumbing companies with "SOS" in their names. Check trademark and search conflicts in the launch metro before spending on the name |

---

# 5. POSITIONING AND CLAIM CONSTRAINTS

Phase 3 writes positioning statements, Phase 6 writes twenty-seven headlines across nine copy drills, and the deck compresses all of it. All three will reach for the claims below, so the narrowed form has to be here rather than remembered.

**Governing sensitivity, a hypothesis for Step 2.7 to test:** contractors will read every platform claim against the lead platforms they already know. State mechanics, who pays what and when, and never volume or income.

| Do not write | Write instead | Counter-example |
|---|---|---|
| Zero cost to join. No subscription or lead fees. Only we can do this | No subscription and no per-lead fees. Then, once open decision 2 is settled, say exactly how SOS SMS is paid, in the same sentence | If SOS SMS takes any share of the trip charge or the job, "zero cost" is false. "Only we" rests on no market scan |
| High-urgency leads: customers ready to buy now | Requests come from people with an active problem who want someone now | Some will be checking prices, some fix it or find someone else before arrival, and some decline the quote after paying the trip charge |
| Pre-qualified leads: every job is confirmed to be in your service area and in your trade | Requests are matched to the trades and service area you set | Customers describe the problem by text and can name the wrong trade. A ceiling leak can be plumbing or roofing. The customer-side relaunch guarantee exists because this happens |
| Guaranteed trip charge. Held in escrow, so you won't get stiffed if you show up | The customer pays the trip charge before you roll, and SOS SMS holds it until you arrive. Release condition `{TBD}` | Open decision 3: a late arrival may trigger the customer's refund. A card dispute can reverse a payment. Use "escrow" only if a licensed escrow arrangement actually holds the funds |
| Photos and video before you roll | When the customer sends photos or video, you see them before you accept | The customer may send nothing. The source marks this item as implied by a memo, not stated |
| Accept or decline freely: you only take the jobs you want | Holds if declining carries no penalty. Then state the rule: declining does not change which jobs you see next | If acceptance rate affects who gets future requests first, "freely" is untrue |
| Exclusive leads, or anything implying a job is the contractor's alone | Every matched contractor sees the request at the same time, and the first to accept gets the job. Only once open decision 4 confirms it | If each request goes to every matched contractor at once, it is shared by design |

Also banned in every phase of this run: any count of contractors, jobs, or customers; any earnings, income, or "more jobs per month" figure for contractors; any testimonial or named contractor; any comparison against a named platform's fees without a dated source from Phase 2; any market statistic without a citation; and any promised job volume.

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
