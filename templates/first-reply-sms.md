# Template: member texts (welcome, first reply, and transactional texts)

The texts a member gets on joining, the product's answer to a member's request text, and the texts that follow, plus the reply to a text from a non-member. The member's card and address are on file from joining, so in an emergency there is nothing to ask for: no offer, no link, nothing to confirm (the membership revision, 2026-10-11). Texts to one member name the plan as `{{plan}}`, and the 90-minute guarantee appears only for Plus and Premier (the pricing revision, 2026-10-21). Load `reference/channel-engine-members.md`, `reference/customer-journey.md`, and `rules/writing-rules.md` (writing for a text message). Example: `examples/first-reply-sms.md`.

## Preconditions
- [ ] Carrier registration done (S32); the number is the registered SOS SMS number.
- [ ] Memberships are open in the zone (R55); the member record holds the plan, the card (and any backup card, R16), the home address (two on Premier), the phones on file (R69), and consent to the member terms (R54).
- [ ] Safety handling (decision 8): texts that mention gas, smoke, fire, sparks, a burning smell, a shock, or anyone hurt get the safety reply first and are not broadcast until the member confirms they are safe and 911 or the utility has been called.
- [ ] First steps reviewed by a licensed contractor in each trade; tested with 20 people before launch.

## On joining, the welcome texts

| # | Content |
|---|---|
| W1 | The `{{plan}}` membership is active, for `{{zone name}}`; when dispatch starts (annual: at once; monthly: 30 days after joining, R54); automated, from SOS SMS; text HELP for a person (R50) |
| W2 | The contact card: save this number |
| W3 | How it works in one text: when something breaks (plumbing, HVAC, or electrical), text what happened from any phone on the membership; the request goes to the licensed, insured contractors on SOS SMS for that trade at once; an arrival time when one accepts; the card and address are already on file |
| W4 | On use: the $99 trip charge on the card when a contractor accepts, credited to the repair. If no one is there after 90 minutes, text NEXT |
| W5 | Plus and Premier only: the 90-minute guarantee with its scope, the credit named in months (6 on Plus, 12 on Premier). Never on Basic |
| W6 | The safety line |

## In an emergency, one idea per message

| # | When | Content |
|---|---|---|
| 1 | On the member's request text, at once | Automated, from SOS SMS, to `{{first name}}`: the request is going to the licensed, insured contractors on SOS SMS near their home now. Text HELP for a person (R50). The safety line |
| 2 | Same moment | The first steps for the problem described: stop the water for plumbing; for HVAC and electrical, the safety steps only. Shutoff and safety, never repairs |
| 3 | On acceptance | `{{contractor name}}`, `{{arrival time}}`, `{{rating}}` where they have one; the $99 trip charge goes on the card on file now and counts toward the repair; on Plus and Premier, the guarantee in one line with its scope; on every plan, NEXT after 90 minutes |
| 4 | No acceptance in time | Told within 15 minutes that no contractor could come; the card is never charged, and no contractor is paid (decision 3, R11) |
| 5 | Card declines | The backup card is tried at once; if both decline, told at once, with how to update the card (the membership page, or HELP); the request goes out when a card authorizes, the 90 minutes running from then (R16) |
| 6 | On arrival | Arrival confirmed |
| 7 | Late arrival | The trip charge stands, because it pays for the work. Plus and Premier: `{{credit amount}}` credited to the next bills or the renewal, automatically, never cash; no claim needed (R65, R66). Basic: no credit |
| 8 | No-show, or NEXT after 90 minutes | The $99 back in full; the request goes to the other matched contractors at once, and a new acceptance is a new request with its own $99 and its own 90 minutes (R17). Plus and Premier: `{{credit amount}}` credited |
| 9 | After the job | Two questions: arrived within the window? would you tell a neighbor? Then the forwardable card |
| 10 | Separately | Permission to quote their words, and how |

## A text from a non-member, or from a phone not on file (R57, R69)

| # | Content |
|---|---|
| N1 | Automated, from SOS SMS. The safety line |
| N2 | The first steps for the problem described |
| N3 | Dispatch is for members; how to join for next time, and whether their ZIP is open. Nothing charged |

## Rules
No link, offer, or confirmation request in any emergency text. No marketing in any transactional text. No follow-ups without opt-in (S31). Full name SOS SMS every time. The membership prices never appear in emergency texts.

Guardrails: one side only (members). Check `rules/do-not-say.md` (text block), `rules/feature-status.md`; run `ops/QA-checklist.md` (text messages block).
