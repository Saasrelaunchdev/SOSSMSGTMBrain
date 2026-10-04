# Channel engine: contractors

Load for: anything in cold email, the partnership program, or the referral loop, and every contractor template. Distills Run 1 Phase 8 (`phase-8-assets-library.md`, product-led revision 2026-10-01). Templates: `templates/cold-email.md`, `templates/partner-kit.md`, `templates/terms-on-one-page.md`.

## Thesis
Contractors are recruited zone by zone, without a salesperson. Every channel opens with something useful (the Lead Cost Check), states the terms before asking for anything, and ends in self-serve sign-up by text. No asset asks for a meeting. Supply density, not sign-up count, is the goal.

## The three channels

| Channel | Replaces | What it does |
|---|---|---|
| 1 Cold email | (kept) | Four plain-text emails over twelve days, to every licensed plumbing and water damage business in the zone. Level 2 lead-platform advertisers first |
| 2 Partnership program | LinkedIn outreach | Supply house counter cards, association newsletters, trade school job boards, the partner kit, a ten-minute explainer video. Counter staff are the channel |
| 3 In-product referral loop | LinkedIn Ads | After the fifth paid trip, one text: which other trade do you trust? Plus the forwardable Lead Cost Check and add-a-technician |

## Rules
- **Self-serve.** Every CTA ends in JOIN by text or the contractor page.
- **Email law (S73).** Accurate sender, honest subject, postal address, one-click opt-out within 10 business days, a separate sending domain, warm-up, daily caps.
- **Texting (S31).** A contractor receives texts only after starting sign-up themselves.
- **Partners.** No endorsement implied unless given in writing. No partner referral fee and no referral reward at launch (R18); partners are thanked by text.
- **Name.** Always SOS SMS, the sending domain, and the zone.
- **Mockups** labeled as mockups until the product exists.

## The sequence

| Email | Day | Subject | Job |
|---|---|---|---|
| 1 | 0 | What did each job from your leads cost? | One question, the Lead Cost Check link, one line on SOS SMS, the revenue sentence. Under 120 words |
| 2 | 3 | How a job works in three texts | The mechanics, the shared request stated openly |
| 3 | 7 | The terms, on one page | What you pay, when you're paid, what you commit to, what happens if you're late |
| 4 | 12 | Founding contractors in {{zone}} | The founding offer and its real deadline, {{founding close date}} (R07). "Last email unless you reply" |

Measure clicks to the check, not opens. Full drafts: `examples/cold-email-sequence.md`.

## Method: plan, write, edit
1. **Plan.** Zone set; list built from public license lists and the business's own site; Level 2 first. List the merge fields the asset carries and the record each fills from.
2. **Write.** Lead with the contractor's own numbers, then mechanics, then terms. One idea per email. Rational headline before emotional. Use the drills in `value-proposition-contractors.md`.
3. **Edit.** Run `ops/QA-checklist.md`. Cut any adjective a term could replace. Every number is a register value; every per-message detail is a merge field.

## Production order
1. The terms on one page, then the contractor page (wait on decisions 2, 3, 4).
2. The Lead Cost Check web version and sign-up by text.
3. The zone list and emails 1 to 4 with the sending setup.
4. The partner kit, counter cards, and video, once one partner says yes.
5. The referral prompt and add-a-technician, once contractors reach five paid trips.

## Signals to log
Replies by objection type, drop-off step in sign-up, Lead Cost Check results by tier, partner-code sign-ups. Each goes to `ops/signal-log.md`.

## Not in the mix
Sales calls, demos, shop visits, LinkedIn. Contractor-facing search ads ("plumbing leads") are an optional later test, not a channel, revisited only if email and partners miss the density target.
