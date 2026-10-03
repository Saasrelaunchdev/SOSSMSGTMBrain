# External research prompts, pre-filled. Run 1: Supply (Contractors)

Three steps in the skill need a person rather than the model: Step 1.1, Step 2.1, and Step 2.7. Each one below is filled with SOS SMS's contractor-side details and ready to paste into a research tool or a browser.

There is also a Step 0 below that the skill does not have. You need it, because the skill assumes you already know your five or six competitors by name.

Run Step 0 first. Everything after it depends on the slate it produces.

These prompts are for the contractor run only. The customer run has its own set in `../run-2-demand-customers/RESEARCH-PROMPTS.md`, with a different slate and different sources, because a contractor and a homeowner compare SOS SMS against entirely different things.

Before pasting any prompt, replace `[launch metro]` and `[trades]` with the answers to `GTM-BRIEF.md` open decision 1.

---

## Step 0. Source the competitor slate

Not in the skill. Do this before Phase 1.

```
I am researching the competitive set for SOS SMS, from the contractor side.

SOS SMS is a pre-launch, two-sided marketplace for emergency home repair. A
homeowner texts one number, the request goes to licensed, insured contractors
matched by trade and service area, and a contractor accepts and commits to an
arrival time. Contractors pay no subscription and no lead fee. The customer
pays a trip charge up front, credited to the job if they go ahead. I am
looking at it from the contractor's side: how trade contractors get emergency
and after-hours jobs today.

Launch area: [launch metro]
Trades: [trades]

Find me real, currently operating examples in each of these categories.
For each, give the name, the website URL, what it charges contractors if
public (per lead, per job, subscription, or commission), and which trades and
areas it serves.

1. On-demand platforms that dispatch urgent home repair requests to
   independent contractors
2. Free business and directory listings contractors use to be found for
   emergency work
3. Not a company: how contractors in these trades say they get emergency jobs
   today, through word of mouth, repeat customers, and referrals between
   trades. Find real forum and community threads where they discuss it
4. National home-services marketplaces that charge contractors per lead or
   per job, and search engine pay-per-lead ad programs for local services
5. After-hours answering and dispatch services for trade contractors, with
   their price pages, and job postings for after-hours dispatchers in the
   launch area
6. Home warranty companies and insurer contractor networks that route repair
   jobs to contractors, and the trade associations for these trades in the
   launch area

Tell me whether each one is active in the launch area specifically or is
national, and prioritise ones active in the launch area.

Do not include anything you cannot verify with a working URL.
```

**Selection rule when the results come back.** Keep the five or six a contractor would actually weigh against SOS SMS, not the five or six that look most like it. For many owner-operators that reorders the table: word of mouth and repeat customers (slot 3) move to the top, and an on-demand platform that is not active in the launch metro drops out entirely, however close its offer is.

**Record what you find** in a table with these columns: name, URL, category slot, what it charges contractors, who it serves. Phase 2 reads from it.

---

## Step 1.1. Contractor feature demand research

The skill's version researches software features from feature and pricing pages. This version asks what each alternative gives and costs a contractor.

```
I need feature demand research for SOS SMS, from the contractor side, in the
emergency home repair dispatch category.

RESEARCH SCOPE

For each competitor below, gather:
- What the contractor gets: how jobs arrive, how they accept, how and when
  they are paid, and what customer details they see before accepting
- What the contractor pays: per lead, per job, subscription, commission, and
  any minimums or contract terms
- What contractors praise most
- What contractors complain about, or say they wish were included
- What the platform promises contractors explicitly, and what it refuses to
  promise (job volume, lead quality, exclusivity)
- Its refund or credit policy for bad leads, and how that policy is hedged

COMPETITORS TO RESEARCH:
1. [name] - [url]
2. [name] - [url]
3. [name] - [url]
4. [name] - [url]
5. [name] - [url]
6. [name] - [url]

OUR FEATURES TO VALIDATE:
1. Zero cost to join: no subscription and no lead fees
2. High-urgency requests: active emergencies only
3. Requests matched to the contractor's service area and trade
4. Trip charge collected from the customer before the contractor rolls
5. Photos and video of the problem before accepting
6. Accept or decline any job, with no penalty for declining
7. The customer relationship stays with the contractor after the job
8. Fast payout of the trip charge after arrival
9. Jobs received and accepted by text, no app

For each of ours, tell me: does anyone in the competitor set already offer
this, how central is it to their offer, and is there public evidence that
contractors want it.

SOURCES TO CHECK:
- Pro-side app store reviews, iOS and Google Play, for each platform
- Reddit trade communities, for example r/Plumbing, r/HVAC, r/electricians,
  and general contractor and small trade business communities
- Trade Facebook groups and trade forums
- BBB and Trustpilot complaints filed by contractors, not homeowners
- YouTube reviews of the platforms by contractors

Return findings in a structured format.
```

---

## Step 2.1. Competitor deep research

```
I need competitive research for the emergency home repair dispatch category,
with focus on how [trades] contractors in [launch metro] get emergency jobs.

RESEARCH SCOPE

For each competitor below, gather:
- Website URL
- Tagline from the homepage, or from the contractor sign-up page if separate
- Sub-tagline or secondary headline
- Full description from the homepage and about page
- Strengths, from contractor reviews, testimonials, and public discussion
- Weaknesses, from contractor complaints and negative feedback
- Who they say they serve, in their own words
- What they charge contractors, if public

COMPETITORS TO RESEARCH:
1. [name] - [url]
2. [name] - [url]
3. [name] - [url]
4. [name] - [url]
5. [name] - [url]
6. SOS SMS (ours) - no website yet

SOURCES TO CHECK:
- Each competitor's contractor sign-up and pricing pages
- Pro-side app store reviews
- Reddit trade communities and trade Facebook groups
- BBB and Trustpilot, filtered to complaints from contractors

This category is not reviewed on G2 or Capterra. Those are software review
sites. Field service management software will match some searches; it is a
tool contractors use, not a source of jobs, so do not include it, and do not
substitute any software company that happens to match a name.

Return findings in a structured format matching the attributes above.
```

**Note on our own row.** The skill asks you to research your own product alongside the competitors. SOS SMS has no website and no reviews, so fill that row from `GTM-BRIEF.md` Section 1 rather than from a crawl, and mark strengths and weaknesses `{TBD}` rather than writing aspirational ones. A self-assessment written as evidence is the fastest way to get a wrong Phase 2.

---

## Step 2.7. Review analysis, substituted

The skill sends you to G2. This category is not on G2. Same question, contractor sources.

```
I need review analysis to define positioning vectors for the emergency home
repair dispatch category, from the contractor's point of view.

RESEARCH SCOPE

For each competitor below, find published feedback from contractors who have
used it, and analyse it.

WHAT CONTRACTORS LOVE:
- Extract repeated positive themes
- Identify what each one is seen as leading in
- Count how often each theme appears
- These are what competitors currently lead in

WHAT CONTRACTORS DISLIKE OR WISH FOR:
- Extract repeated complaints
- Identify gaps and unmet wishes
- Count how often each theme appears
- These are the openings

COMPETITORS TO ANALYSE:
1. [name] - [url]
2. [name] - [url]
3. [name] - [url]
4. [name] - [url]
5. [name] - [url]

WHERE TO LOOK:
- Pro-side app store reviews, iOS and Google Play
- Reddit trade communities, searching each competitor's name with "leads",
  "worth it", and "charged"
- Trade Facebook groups and trade forums
- BBB and Trustpilot complaints from contractors
- Contractor YouTube reviews and their comment sections

OUTPUT NEEDED:
For each competitor:
- Top 3 positive themes, with frequency
- Top 3 negative themes, with frequency
- Whether the complaints are mainly about lead cost, lead quality (fake,
  unreachable, or shared with many contractors), or getting paid

Return findings in a structured format.
```

**What to watch for.** The matrix's working hypothesis is that contractors resent paying for leads that do not become jobs, and resent showing up without getting paid. If Step 2.7 confirms it, the finding lands in Phase 6 as the lead pillar and in Phase 9 as Anchor 2. If the complaints center on leads shared with many contractors instead, treat that as a warning rather than an opening: SOS SMS also sends each request to every matched contractor at once (open decision 4), so the dispatch rule becomes a weakness Phase 3 has to answer, not a strength it can claim.

---

## Before you start Phase 1

The skill runs 5 to 6 hours across multiple sessions. These research steps sit outside that estimate and gate Phases 1 and 2. Doing them properly first is what makes the rest of the run worth anything, and Step 0 is what makes the other three possible.
