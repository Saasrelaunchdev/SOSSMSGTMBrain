# Template: zone landing page (customers)

The page every emergency ad lands on, and the organic zone page ("Emergency plumbing help by text in {{zone name}}"). One per zone, from this template. Load `reference/channel-engine-paid-search.md` and `reference/value-proposition-customers.md`.

## Fields
Merge fields from the zone record: `{{zone name}}`, `{{zone neighborhoods}}`, `{{covered hours}}`, `{{SOS SMS number}}` (registered, decision 9). Decided values, written as is: the $99 trip charge (decision 5), the $49 SOS SMS fee (decision 2), and the guarantee scope (decision 3).

## Sections, in order
1. **Above the fold, on a phone.** One line naming the need; the text button with "Something broke at home:" prefilled; the safety line directly under it.
2. **How it works in three texts.** You text what broke and where. The licensed, insured contractors on SOS SMS for that trade see it at once; the first who can come accepts and texts you an arrival time. You agree to the trip charge before anyone is sent.
3. **What it costs.** The $99 trip charge, before anyone is sent, credited to the repair if you go ahead; the $49 SOS SMS fee, charged only when a plumber accepts. Nothing about the repair price.
4. **The guarantee, in one line.** "If they are not there within 90 minutes of your request, the $99 trip charge comes back to you, automatically." Covered in `{{zone neighborhoods}}`, `{{covered hours}}`; with no acceptance, told within 15 minutes and nothing charged. Link to the guarantee in full.
5. **Who SOS SMS is.** SOS SMS dispatches licensed, insured contractors; the contractor does the work. License and insurance checked before they can take a job.
6. **Your information.** Only the contractor who takes your job gets your address (decision 4). No selling, no ad targeting.
7. **Before it happens.** Text READY to save the number and get a shutoff guide.
8. **Footer.** Covered areas and hours; links to how it works, the guarantee, privacy.

## Technical
Loads fast on a phone; the text button above the fold; no ad pixels or retargeting; no form that collects a phone number for marketing. Outside the zone, the page says plainly that SOS SMS does not cover that area yet.

Guardrails: one side only (customers). The safety line stays still and legible. Check `rules/do-not-say.md`, `rules/feature-status.md`, `rules/glossary.md`; run `ops/QA-checklist.md`.
