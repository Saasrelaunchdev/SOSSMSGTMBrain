# Channel engine: contractors

Load for: anything in cold email, the partnership program, or the referral loop, and every contractor template. Distills Run 1 Phase 8 (`phase-8-assets-library.md`, product-led revision 2026-10-01; the tiers revision, 2026-10-20). Templates: `templates/cold-email.md`, `templates/partner-kit.md`, `templates/terms-on-one-page.md`.

## Thesis
Contractors are recruited zone by zone, in all three trades at once, plumbing, HVAC, and electrical, without a salesperson. Every channel opens with something useful (the Lead Cost Check), states the terms before asking for anything, and ends in self-serve sign-up by text. No asset asks for a meeting. Supply density in every trade and hour band, not sign-up count, is the goal: 9 contractors per trade in the launch zone, 27 places; a shop licensed in more than one trade counts in each (R08).

## The three channels

| Channel | Replaces | What it does |
|---|---|---|
| 1 Cold email | (kept) | Four plain-text emails over twelve days, to every licensed plumbing, HVAC, and electrical business in the zone, from the state license lists (R40). Level 2 lead-platform advertisers first; each trade's list fills toward its own 9 places |
| 2 Partnership program | LinkedIn outreach | A supply house for each trade (counter cards), the trade associations (PHCC for plumbing, ACCA for HVAC, NECA and IEC for electrical), trade school job boards, the partner kit, a ten-minute explainer video. Counter staff are the channel |
| 3 In-product referral loop | LinkedIn Ads | After the fifth paid trip, one text: which other trade do you trust? Plus the forwardable Lead Cost Check and add-a-technician |

## Rules
- **Self-serve.** Every CTA ends in JOIN by text or the contractor page.
- **Email law (S73).** Accurate sender, honest subject, postal address, one-click opt-out within 10 business days, a separate sending domain, warm-up, daily caps.
- **Texting (S31).** A contractor receives texts only after starting sign-up themselves.
- **Partners.** No endorsement implied unless given in writing. No partner referral fee and no referral reward at launch (R18); partners are thanked by text. A contractor may join the member affiliate program on the same terms as any partner (R61).
- **One set of terms, no deadline.** Every contractor in every trade pays $0 to join and per request and $25 per completed paid job from the first job, $74 of the $99 reaching them (R03), whatever the member's plan. Contractors join any time on the same terms; no copy carries a deadline or urgency (R07, retired).
- **Each trade's facts.** The state license for each trade taken, and insurance, checked at sign-up and rechecked every 6 months and at each policy's expiry (decision 7). Every contractor is told the expected volume for their trade (R64): about one request a month in plumbing, about 0.8 in HVAC, about one every 5 months in electrical.
- **Name.** Always SOS SMS, the sending domain, and the zone.
- **Mockups** labeled as mockups until the product exists.

## The sequence

| Email | Day | Subject | Job |
|---|---|---|---|
| 1 | 0 | What did each job from your leads cost? | One question, the Lead Cost Check link, one line on SOS SMS, the revenue sentence. Under 120 words |
| 2 | 3 | How a job works in three texts | The mechanics, the shared request stated openly |
| 3 | 7 | The terms, on one page | What you pay ($25 per completed paid job, $74 of the $99 to you), when you're paid, what you commit to, what happens if you're late (the trip charge stands; two late arrivals or no-shows in 90 days pause requests, R67) |
| 4 | 12 | When SOS SMS opens in {{zone}} | Memberships open once enough plumbing, HVAC, and electrical contractors cover every hour; every contractor joins on the same terms; JOIN by text. No deadline and no urgency. "Last email unless you reply" |

Measure clicks to the check, not opens. Full drafts: `examples/cold-email-sequence.md`.

## Method: plan, write, edit
1. **Plan.** Zone set; list built by trade from public license lists and the business's own site; Level 2 first. List the merge fields the asset carries and the record each fills from.
2. **Write.** Lead with the contractor's own numbers, then mechanics, then terms. One idea per email. Rational headline before emotional. Use the drills in `value-proposition-contractors.md`.
3. **Edit.** Run `ops/QA-checklist.md`. Cut any adjective a term could replace. Every number is a register value; every per-message detail is a merge field.

## Production order
1. The terms on one page, then the contractor page (they carry decisions 2, 3, 4, and 6).
2. The Lead Cost Check web version and sign-up by text.
3. The zone list and emails 1 to 4 with the sending setup.
4. The partner kit, counter cards, and video, once one partner says yes.
5. The referral prompt and add-a-technician, once contractors reach five paid trips.

## Signals to log
Replies by objection type and trade, drop-off step in sign-up, Lead Cost Check results by tier, partner-code sign-ups by trade. Each goes to `ops/signal-log.md`.

## Not in the mix
Sales calls, demos, shop visits, LinkedIn. Contractor-facing search ads ("plumbing leads", "HVAC leads", "electrician jobs") are an optional later test, not a channel: SOS SMS runs no paid search at launch on either side (decision 11), revisited only if email and partners miss the density target in a trade.
