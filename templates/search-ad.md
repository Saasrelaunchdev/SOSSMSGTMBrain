# Template: sign-up ad, paid social at launch (members)

For paid social sign-up ads at launch: short readiness ads promoted to homeowners on the open zone's map, by location only, paused with sign-ups (R34). Ads sell the membership before the need, never dispatch during an emergency. There is no paid search at launch (decision 11, revised 2026-10-20): the Google and Microsoft search ad drafts are held, below. The file keeps its name because links point at it. Load `reference/channel-engine-members.md` and `reference/value-proposition-members.md` first. Example: `examples/search-ad-zone.md`.

## Preconditions (all yes, or the ad does not run)
- [ ] Memberships are open in the zone (R55); the ads are limited to the zone's map, by location only: no pixels, retargeting, or uploaded lists.
- [ ] The membership page exists, with the ZIP check, the three plans as written, the renewal terms, and the safety line.
- [ ] Sign-ups pause automatically when acceptance in any trade falls below 90 percent over 7 days: paid social stops (R34).
- [ ] Cost per new paid member is read weekly against the ceiling of the plan joined (R63); the ad set stops when it is over.

## Fields
- Zone:
- Ad set: readiness / plan comparison / seasonal (the first freeze, the first heat wave)
- Targeting: the open zone's map, by location only
- Headlines (max 30 characters each):
- Ad text (max 90 characters each; one is the safety line):
- Final URL: the membership page, or the matching prevention guide
- Conversion tracked: new paid member, by plan (primary); ZIP check and launch list join (secondary)

## Shape
1. Name the readiness gap ("Join Before Something Breaks").
2. Give the mechanic ("One Text When Something Breaks").
3. State one term ("Trip Charge Only When Used", "Plans From $10 a Month", "Cancel Any Time").
4. Say who SOS SMS is ("Dispatch to Licensed Pros", "Not a warranty").

## Angles to rotate
One text instead of a list; plumbing, HVAC, and electrical in one plan; the card and address already on file; an arrival time on acceptance; no app; cancel any time; the first freeze and the first heat wave (seasonal). The guarantee angle names its plans: "Late? 6 Months Credited", only with Plus and Premier, and the scope on the membership page (decision 3). "Only One Pro Gets Your Info" runs once the broadcast that hides identity ships (decision 4).

## Held: search ads
Google responsive search ads and the Microsoft import do not run at launch (decision 11), and Local Services Ads never run (S70). Once a zone has been open 6 months, search volume for SOS SMS by name is counted with free tools (R68, Stage 3); a brand campaign on the full name may then run, with Google's written confirmation (S71), at or under the plan's ceiling (R63). Emergency dispatch searches always sit on its negative list.

## Never in an ad
An offer of dispatch during an emergency; superlatives; arrival averages; "24/7" (an open zone is covered at any hour, said as "any hour, in {{zone neighborhoods}}"); "emergency service", "warranty", "insurance", "covers repairs"; a price other than the plans as written; the guarantee without its plans, or on Basic; any plan as faster; any number not in the brain; competitor brand names; "SOS" alone; bids on "SOS plumbing" (decision 10).

Guardrails: one side only (members). Check `rules/do-not-say.md` (search and social ads block), `rules/feature-status.md`, and `rules/glossary.md`. Run `ops/QA-checklist.md` before launch.
