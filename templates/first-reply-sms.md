# Template: first reply and transactional texts (customers)

The product's first answer to any first text, and the texts that follow. The first reply decides everything: trust is earned here, before any link. Load `reference/channel-engine-paid-search.md`, `reference/customer-journey.md`, and `rules/writing-rules.md` (writing for a text message). Example: `examples/first-reply-sms.md`.

## Preconditions
- [ ] Carrier registration done (S32); the number is the registered SOS SMS number.
- [ ] Safety handling decided (decision 8): gas, smoke, fire, or injury get the safety reply and are not broadcast until the customer confirms it is safe and 911 or the utility has been called.
- [ ] Trip charge (decision 5) and guarantee scope (decision 3) logged, or the texts keep their brackets and do not ship.
- [ ] Tested with 20 people before launch.

## The sequence, one idea per message

| # | When | Content |
|---|---|---|
| 1 | On the first text | Automated, from SOS SMS, how to reach a person. The safety line. |
| 2 | Same moment | Stop-the-water steps for the problem described (shutoff and safety only) |
| 3 | Same moment | The offer: a licensed, insured plumber; the trip charge, credited if they go ahead; the guarantee in one line with its scope. Reply YES to agree |
| 4 | After YES | The payment link, naming SOS SMS and the trip charge again |
| 5 | On acceptance | Contractor's name, arrival time, Google rating where they have one |
| 6 | No acceptance in time | [What the customer is told, and when]. Nothing charged |
| 7 | On arrival | Arrival confirmed |
| 8 | Window missed | The refund, applied automatically, and what happens next. No claim needed |
| 9 | After the job | Two questions: arrived within the window? would you tell a neighbor? Then the contact card |
| 10 | Separately | Permission to quote their words, and how |

## Rules
Never a link in message 1. Never a link before message 3 has been read and agreed. No marketing in any transactional text. No follow-ups without opt-in (S31). Full name SOS SMS every time.

Guardrails: one side only (customers). Check `rules/do-not-say.md` (text block), `rules/feature-status.md`; run `ops/QA-checklist.md` (text messages block).
