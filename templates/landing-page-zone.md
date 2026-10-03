# Template: zone landing page (customers)

The page every emergency ad lands on, and the organic zone page ("Emergency plumbing help by text in [zone]"). One per zone, from this template. Load `reference/channel-engine-paid-search.md` and `reference/value-proposition-customers.md`.

## Fields
- Zone name and the neighborhoods it covers:
- Covered hours:
- The SOS SMS number (registered):
- Trip charge: [amount] (decision 5), or {TBD}
- Guarantee line with scope (decision 3), or the brackets

## Sections, in order
1. **Above the fold, on a phone.** One line naming the need; the text button with "Something broke at home:" prefilled; the safety line directly under it.
2. **How it works in three texts.** You text what broke and where. The licensed, insured contractors on SOS SMS for that trade see it at once; the first who can come accepts and texts you an arrival time. You agree to the trip charge before anyone is sent.
3. **What it costs.** The trip charge, before anyone is sent, credited to the repair if you go ahead. Nothing about the repair price.
4. **The guarantee, in one line.** "If they are not there within 90 minutes of [clock start], [refund] comes back, automatically." Covered areas and hours named. Link to the guarantee in full.
5. **Who SOS SMS is.** SOS SMS dispatches licensed, insured contractors; the contractor does the work. License and insurance checked before they can take a job.
6. **Your information.** Only the contractor who takes your job gets your address (once conflict C is designed). No selling, no ad targeting.
7. **Before it happens.** Text READY to save the number and get a shutoff guide.
8. **Footer.** Covered areas and hours; links to how it works, the guarantee, privacy.

## Technical
Loads fast on a phone; the text button above the fold; no ad pixels or retargeting; no form that collects a phone number for marketing. Outside the zone, the page says plainly that SOS SMS does not cover that area yet.

Guardrails: one side only (customers). The safety line stays still and legible. Check `rules/do-not-say.md`, `rules/feature-status.md`, `rules/glossary.md`; run `ops/QA-checklist.md`.
