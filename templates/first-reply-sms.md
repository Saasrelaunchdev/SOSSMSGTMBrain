# Template: member texts (welcome, first reply, and transactional texts)

The texts a member gets on joining, the product's answer to a member's request text, and the texts that follow, plus the reply to a text from a non-member. The member's card and address are on file from joining, so in an emergency there is nothing to ask for: no offer, no link, nothing to confirm (the membership revision, 2026-10-11). Load `reference/channel-engine-members.md`, `reference/customer-journey.md`, and `rules/writing-rules.md` (writing for a text message). Example: `examples/first-reply-sms.md`.

## Preconditions
- [ ] Carrier registration done (S32); the number is the registered SOS SMS number.
- [ ] Memberships are open in the zone (R55); the member record holds the card, the home address, and consent to the member terms (R54).
- [ ] Safety handling (decision 8): gas, smoke, fire, or injury get the safety reply and are not broadcast until the member confirms it is safe and 911 or the utility has been called.
- [ ] Tested with 20 people before launch.

## On joining, the welcome texts

| # | Content |
|---|---|
| W1 | The membership is active, for `{{zone name}}`; automated, from SOS SMS; text HELP for a person (R50) |
| W2 | The contact card: save this number |
| W3 | How it works in one text: when something breaks, text what happened; the request goes to the licensed, insured contractors on SOS SMS for that trade at once; an arrival time when one accepts; the card and address are already on file |
| W4 | On use: the $99 trip charge on the card when a contractor accepts, credited to the repair; the 90-minute guarantee with its scope |
| W5 | The safety line |

## In an emergency, one idea per message

| # | When | Content |
|---|---|---|
| 1 | On the member's request text, at once | Automated, from SOS SMS, to `{{first name}}`: the request is going to the licensed, insured contractors on SOS SMS near their home now. Text HELP for a person (R50). The safety line |
| 2 | Same moment | Stop-the-water steps for the problem described (shutoff and safety only) |
| 3 | On acceptance | `{{contractor name}}`, `{{arrival time}}`, `{{rating}}` where they have one; the $99 trip charge goes on the card on file now and counts toward the repair; the guarantee in one line with its scope |
| 4 | No acceptance in time | Told within 15 minutes that no contractor could come; the card is never charged (decision 3) |
| 5 | On arrival | Arrival confirmed |
| 6 | Window missed | The refund, applied automatically, and what happens next. No claim needed |
| 7 | After the job | Two questions: arrived within the window? would you tell a neighbor? Then the forwardable card |
| 8 | Separately | Permission to quote their words, and how |

## A text from a non-member (R57)

| # | Content |
|---|---|
| N1 | Automated, from SOS SMS. The safety line |
| N2 | Stop-the-water steps for the problem described |
| N3 | Dispatch is for members; how to join for next time, and whether their ZIP is open. Nothing charged |

## Rules
No link, offer, or confirmation request in any emergency text. No marketing in any transactional text. No follow-ups without opt-in (S31). Full name SOS SMS every time. The membership prices never appear in emergency texts.

Guardrails: one side only (members). Check `rules/do-not-say.md` (text block), `rules/feature-status.md`; run `ops/QA-checklist.md` (text messages block).
