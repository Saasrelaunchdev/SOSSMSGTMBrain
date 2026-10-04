# Template: cold email (contractors)

Four plain-text emails over twelve days, zone by zone, to licensed plumbing and water damage businesses. Load `reference/channel-engine-contractors.md` and `reference/value-proposition-contractors.md`. Example: `examples/cold-email-sequence.md`.

## Preconditions
- [ ] Zone set (decision 1); list built from public license lists and the business's own published email.
- [ ] Sending setup: a separate sending domain, warm-up, daily caps, opt-out handling.
- [ ] The Lead Cost Check web version and the contractor page are live.
- [ ] Every bracket the email carries has its decision logged in `ops/decisions.md`.

## Fields, per email
- Email number and day (1: day 0; 2: day 3; 3: day 7; 4: day 12):
- Recipient business and trade:
- Subject (honest, specific, no hype):
- Body:
- One link:
- Signature: sender's real name, SOS SMS, postal address, one-click opt-out (S73)

## Shape
- **Email 1, the Lead Cost hook.** One question about cost per booked job; the check link; "your answers stay yours"; one line on what SOS SMS is; the revenue sentence. Under 120 words.
- **Email 2, how a job works in three texts.** The mechanics, with the shared request said plainly. A labeled mockup image.
- **Email 3, the terms on one page.** What you pay, when you're paid, what you commit to, what happens if you're late. The terms link.
- **Email 4, founding contractors in {{zone}}.** What founding contractors get and commit to; the real deadline only, {{founding close date}} (R07); text JOIN to {{number}}, about 5 minutes; "last email unless you reply".

Pre-launch framing throughout: what SOS SMS is building, "once it opens in {{zone}}", never a working service. The revenue sentence: "SOS SMS will be paid by the customer on each request, and by you only per completed paid job after the founding period."

## Never in a contractor email
Results, volume, earnings, "more jobs", "exclusive", "pre-qualified", "escrow", a fake deadline, a request for a call, a rival named unkindly.

Guardrails: one side only (contractors). Check `rules/do-not-say.md` (email block) and `rules/glossary.md` ("request", never "lead", for SOS SMS); run `ops/QA-checklist.md`.
