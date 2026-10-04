# External research prompts, pre-filled. Run 2: Demand (Customers)

Three steps in the skill need a person rather than the model: Step 1.1, Step 2.1, and Step 2.7. Each one below is filled with SOS SMS's customer-side details and ready to paste into a research tool or a browser.

There is also a Step 0 below that the skill does not have. You need it, because the skill assumes you already know your five or six competitors by name.

Run Step 0 first. Everything after it depends on the slate it produces.

These prompts are for the customer run only. The contractor run has its own set in `../run-1-supply-contractors/RESEARCH-PROMPTS.md`. Expect almost no overlap between the two slates: a contractor compares SOS SMS with ways to get jobs, a homeowner compares it with ways to get someone to the door.

Before pasting any prompt, replace `{{launch metro}}` and `{{trades}}` with the answers from Run 1's Step 5.2.

---

## Step 0. Source the competitor slate

Not in the skill. Do this before Phase 1.

```
I am researching the competitive set for SOS SMS, from the customer side.

SOS SMS is a pre-launch, two-sided marketplace for emergency home repair. A
person with an urgent problem at home texts one number, with no app, and the
request goes to the licensed, insured contractors on the network for that
trade and area. A contractor accepts and gives an arrival time. The customer
pays a trip charge up front, credited to the job if they go ahead, and there
is a 90-minute arrival guarantee. I am looking at it from the customer's side:
what people do today when something breaks at home and they need someone now.

Launch area: {{launch metro}}
Trades: {{trades}}

Find me real, currently operating examples in each of these categories.
For each, give the name, the website URL, what the customer pays before
anyone arrives (trip charge, service fee, after-hours premium) if public, and
who and where they serve.

1. On-demand home repair services that promise a fast arrival for urgent
   jobs, by app, web, or text
2. The top local search and maps results for "emergency {{trade}} near me" in
   the launch area: the contractors a customer would call down a list
3. Not a company: where people in the launch area ask for help finding
   someone now, in neighborhood apps and local community groups. Find real
   threads
4. National home-services marketplaces where customers request quotes from
   several pros
5. Not a company: doing it yourself until morning. The most viewed shutoff
   and temporary-fix guides for these trades
6. Home warranty plans, and homeowner's insurance claim lines that send their
   own contractors for covered repairs

Tell me whether each one is active in the launch area specifically or is
national, and prioritise ones active in the launch area.

Do not include anything you cannot verify with a working URL.
```

**Selection rule when the results come back.** Keep the five or six a customer would actually reach for in the moment, not the five or six that look most like SOS SMS. Expect that to reorder the table: the top search results (slot 2) and waiting until morning (slot 5) move to the top, and an app-based service that needs an account before it will dispatch drops down, because nobody downloads an app with water on the floor.

**Record what you find** in a table with these columns: name, URL, category slot, what the customer pays before arrival, who it serves. Phase 2 reads from it.

---

## Step 1.1. Customer feature demand research

The skill's version researches software features from feature and pricing pages. This version asks what each alternative gives and costs a customer in an emergency.

```
I need feature demand research for SOS SMS, from the customer side, in the
emergency home repair category.

RESEARCH SCOPE

For each competitor below, gather:
- How the customer asks for help: call, app, web form, or text, and whether
  an account is needed first
- How fast they promise arrival, and whether that promise carries a refund
- What the customer pays before anyone arrives (trip charge, service fee,
  after-hours premium), and whether it is credited to the job
- How contractors are vetted, and what the customer sees about them before
  arrival
- What customer data is shared or sold, from the privacy policy
- What customers praise most
- What customers complain about, or say they wish had been included
- What they promise explicitly, and what they explicitly refuse to promise
- Refund policy and any guarantee, and how it is hedged

COMPETITORS TO RESEARCH:
1. {{name}} - {{url}}
2. {{name}} - {{url}}
3. {{name}} - {{url}}
4. {{name}} - {{url}}
5. {{name}} - {{url}}
6. {{name}} - {{url}}

OUR FEATURES TO VALIDATE:
1. One text reaches every matched contractor in the area at once
2. 90-minute arrival guarantee with a refund on a miss
3. Text-only access: no app, no phone tree, any hour
4. Private by design: no app tracking, data never sold or used for ad
   targeting
5. Contractor license and insurance verified before they take jobs
6. The contractor's Google reviews shown before they arrive
7. Trip charge credited to the job
8. Arrival time given when the contractor accepts
9. Relaunch: a second contractor if the first cannot do the job, one trip
   charge only
10. Photos or video sent with the request
11. A price or price range for the work before arrival
12. Safety triage that sends gas, fire, or injury to 911 first

For each of ours, tell me: does anyone in the competitor set already offer
this, how central is it to their offer, and is there public evidence that
customers want it.

SOURCES TO CHECK:
- Maps and search reviews of emergency contractors in the launch area
- Customer-side app store reviews, iOS and Google Play
- Trustpilot and BBB complaints from customers
- Reddit homeowner and home repair communities, for example r/HomeImprovement
  and r/homeowners, plus trade communities where customers ask questions
- Each competitor's privacy policy and guarantee terms

Return findings in a structured format.
```

---

## Step 2.1. Competitor deep research

```
I need competitive research for the emergency home repair category, with
focus on homeowners in {{launch metro}} who need a {{trades}} contractor now.

RESEARCH SCOPE

For each competitor below, gather:
- Website URL
- Tagline from the homepage
- Sub-tagline or secondary headline
- Full description from the homepage and about page
- Strengths, from customer reviews, testimonials, and public discussion
- Weaknesses, from customer complaints and negative feedback
- Who they say they serve, in their own words
- What the customer pays before anyone arrives, if public

COMPETITORS TO RESEARCH:
1. {{name}} - {{url}}
2. {{name}} - {{url}}
3. {{name}} - {{url}}
4. {{name}} - {{url}}
5. {{name}} - {{url}}
6. SOS SMS (ours) - no website yet

SOURCES TO CHECK:
- Each competitor's homepage, pricing or fees page, and guarantee terms
- Maps and search reviews
- Customer-side app store reviews
- Trustpilot, BBB, and Reddit homeowner communities

This category is not reviewed on G2 or Capterra. Those are software review
sites. Do not substitute a software company that happens to match a name,
and note that several unrelated local plumbing companies use "SOS" in their
names: do not confuse any of them with SOS SMS.

Return findings in a structured format matching the attributes above.
```

**Note on our own row.** The skill asks you to research your own product alongside the competitors. SOS SMS has no website and no reviews, so fill that row from `GTM-BRIEF.md` Section 1 rather than from a crawl, and state strengths and weaknesses by design, with the weaknesses written plainly, rather than writing aspirational ones. A self-assessment written as evidence is the fastest way to get a wrong Phase 2.

---

## Step 2.7. Review analysis, substituted

The skill sends you to G2. This category is not on G2. Same question, customer sources.

```
I need review analysis to define positioning vectors for the emergency home
repair category, from the customer's point of view.

RESEARCH SCOPE

For each competitor below, find published feedback from customers who used
it for an urgent or after-hours repair, and analyse it.

WHAT CUSTOMERS LOVE:
- Extract repeated positive themes
- Identify what each one is seen as leading in
- Count how often each theme appears
- These are what competitors currently lead in

WHAT CUSTOMERS DISLIKE OR WISH FOR:
- Extract repeated complaints
- Identify gaps and unmet wishes
- Count how often each theme appears
- These are the openings

COMPETITORS TO ANALYSE:
1. {{name}} - {{url}}
2. {{name}} - {{url}}
3. {{name}} - {{url}}
4. {{name}} - {{url}}
5. {{name}} - {{url}}

WHERE TO LOOK:
- Maps and search reviews, filtered to reviews that mention emergency,
  after hours, night, weekend, or no-show
- Customer-side app store reviews
- Trustpilot and BBB complaints
- Reddit homeowner communities, searching each competitor's name

OUTPUT NEEDED:
For each competitor:
- Top 3 positive themes, with frequency
- Top 3 negative themes, with frequency
- Whether the complaints are mainly about not showing up, not answering,
  surprise fees, or the quality of the work itself

Return findings in a structured format.
```

**What to watch for.** The matrix's features read as answers to three complaints: no-shows, unanswered calls at night, and surprise fees. Treat that as a hypothesis. Where Step 2.7 confirms no-shows, the finding lands in Phase 6 as the 90-minute guarantee pillar and in Phase 7 at the dispatch stage. Where it confirms surprise fees, it lands on "trip charge credited to the job" and in Phase 9 as Anchor 2. Where the complaints are about the quality of the work itself, record it as a gap SOS SMS does not close. It checks license and insurance, not workmanship, and Phase 6 must not imply otherwise.

---

## Before you start Phase 1

The skill runs 5 to 6 hours across multiple sessions. These research steps sit outside that estimate and gate Phases 1 and 2. Doing them properly first is what makes the rest of the run worth anything, and Step 0 is what makes the other three possible.
