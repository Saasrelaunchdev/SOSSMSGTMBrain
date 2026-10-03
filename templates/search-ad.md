# Template: search ad (customers)

For Google responsive search ads, then the Microsoft import. Load `reference/channel-engine-paid-search.md` and `reference/value-proposition-customers.md` first. Example: `examples/search-ad-zone.md`.

## Preconditions (all yes, or the ad does not run)
- [ ] Google has confirmed in writing that a dispatch service may run standard search ads for plumbing (decision 11).
- [ ] The SOS SMS number is registered with carriers (S32).
- [ ] The zone meets the density number; the campaign is geofenced to it and scheduled to its covered hours.
- [ ] The landing page exists and carries the safety line.

## Fields
- Zone and covered hours:
- Ad group type: emergency / problem / prevention
- Keywords (and the negative list in use):
- Headlines (max 30 characters each, up to 15):
- Descriptions (max 90 characters each, up to 4; one is the safety description):
- Message asset: business name, number, stated response time, automated-reply disclosure, human handoff (S72):
- Final URL: the zone landing page, or the matching problem guide for problem groups
- Conversion tracked: paid request (primary), first text (secondary)

## Shape
1. Name the problem or the need ("Water Leaking? Text Us Now").
2. Give the next step ("Steps to Stop the Water Now").
3. State one mechanic ("Trip Charge Shown Upfront", "Arrival Time When They Accept").
4. Say who SOS SMS is ("Dispatch to Licensed Plumbers").

## Angles to rotate
The problem and the first step; one text instead of a list; the trip charge first; an arrival time on acceptance; no app. The guarantee angle waits on decision 3. "Only One Pro Gets Your Info" waits on conflict C.

## Never in an ad
Superlatives, arrival averages, "24/7" beyond covered hours, "emergency service", any number not in the brain, competitor brand names, "SOS" alone, bids on "SOS plumbing" while decision 10 is open.

Guardrails: one side only (customers). Check `rules/do-not-say.md` (search ads block), `rules/feature-status.md`, and `rules/glossary.md`. Run `ops/QA-checklist.md` before launch.
