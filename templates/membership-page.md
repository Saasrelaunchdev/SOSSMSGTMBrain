# Template: the membership page (members)

The page every member channel lands on: affiliate links (with the partner's code), the opening email, guides, and sign-up ads; and the organic zone page ("Plumbing emergency membership in {{zone name}}"). One template, one per zone. Load `reference/channel-engine-members.md` and `reference/value-proposition-members.md`. Example: `examples/membership-page.md`.

## Fields
Merge fields from the zone and price records: `{{zone name}}`, `{{zone neighborhoods}}`, `{{covered hours}}`, `{{monthly price}}`, `{{annual price}}` (R51, R52), `{{SOS SMS number}}` (registered, decision 9); from the affiliate agreement: `{{partner}}`, `{{code}}`. Decided values, written as is: the $99 trip charge on use (decision 5), no fee per request (decision 2), the guarantee scope (decision 3), cancel any time (R56).

## Sections, in order
1. **Above the fold, on a phone.** "One text, and help is on the way." The ZIP check (open zone: join; zone not yet open: the launch list, no charge, no service promised; outside: the readiness steps alone). The safety line directly under it. On a partner's page, the partner's welcome line and the disclosure.
2. **How it works in one text.** You join once, with your card and home address. When something breaks, you text what happened. The licensed, insured contractors on SOS SMS for that trade see it at once; the first who can come accepts and texts you an arrival time.
3. **What it costs.** `{{monthly price}}` a month or `{{annual price}}` a year; "two months free" only while the annual price is ten times the monthly (R52). When you use it, the $99 trip charge goes on your card when a contractor accepts, and counts toward the repair. No fee per request. Nothing about the repair price.
4. **The guarantee, in one line.** "If they are not there within 90 minutes of your text, the $99 trip charge comes back to you, automatically." Covered in `{{zone neighborhoods}}`, `{{covered hours}}`; with no acceptance, told within 15 minutes and nothing charged. Link to the guarantee in full.
5. **What is included, and what is not.** Included: one-text dispatch, an arrival time on acceptance, the 90-minute guarantee, a person by text, the readiness kit. Not included: the repair, parts, or a guarantee on the work (R53). A warranty pays for covered repairs; SOS SMS gets someone there.
6. **Cancel any time.** On this page, or by texting HELP to reach a person. Annual members get a reminder before `{{renewal date}}` (R56). Stated next to the price, before the card (S87).
7. **Who SOS SMS is.** SOS SMS dispatches licensed, insured contractors; the contractor does the work. License and insurance checked before they can take a job.
8. **Your information.** Only the contractor who takes your job gets your address (decision 4). No selling, no ad targeting.
9. **Join.** Card, home address, consent to the member terms; one address per membership (R54). Then the welcome texts.
10. **Footer.** Covered areas and hours; links to how it works, the guarantee, the member terms, privacy.

## Technical
Loads fast on a phone; the ZIP check and join above the fold; no ad pixels or retargeting; no form that collects a phone number for marketing. Outside an open zone, the page says plainly that SOS SMS does not cover that area yet.

Guardrails: one side only (members). The safety line stays still and legible. Check `rules/do-not-say.md`, `rules/feature-status.md`, `rules/glossary.md`; run `ops/QA-checklist.md`.
