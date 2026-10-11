# Template: member email (launch list, opening, welcome, seasonal, renewal)

SOS SMS's own email to homeowners who opted in (the readiness scorecard, the launch list, joining). Never cold. Load `reference/channel-engine-members.md`, `reference/lead-magnets.md`, and `rules/writing-rules.md`. Example: `examples/launch-list-email.md`.

## Preconditions
- [ ] Consent on record: the scorecard, the launch list, or the member terms.
- [ ] Every email carries the full name SOS SMS, `{{postal address}}`, and `{{opt-out link}}`, honored within 10 business days (S73).
- [ ] Seasonal notes to members only with opt-in.

## The sequences

| Sequence | Email | Content | Call to action |
|---|---|---|---|
| Scorecard | Days 0, 2, 5, 8 | `lead-magnets.md`: the score and the plan; the first ten minutes of a leak (S58); how membership works in one text, the prices as merge fields, the trip charge on use, the guarantee with its scope; seasonal only when true | Check your ZIP |
| Launch list | Join, then before opening | What SOS SMS is; the shutoff guide; no charge and no service promised until the zone opens | Keep the steps |
| Opening | The day memberships open in the zone (R55) | The zone is open; the prices; how it works in one text; the guarantee with its scope; what is not included; cancel any time | Join before you need it |
| Welcome | On joining | The membership is active; save the contact card; how it works; the safety line; text HELP for a person; how to cancel | Save the number |
| Seasonal | Before the first freeze, before summer storms (opt-in) | One problem, the steps, one line on membership | Text READY for the home check |
| Renewal | Before `{{renewal date}}` (annual members) | What renews, the price, the date, how to cancel, in plain words (S87) | Nothing to do to stay; cancel any time |
| Cancellation | On cancelling | Confirmed, with the end date; the number stops dispatching after it | None |

## Fields
- Sequence and email:
- Zone, and whether memberships are open there:
- Merge fields used (all from the register):
- Subject line (honest, no urgency the facts do not carry):

## Never in an email
A count of members, an arrival average, a savings figure, "covers repairs", a planning price as the price, false urgency, or an emergency offer to someone who is not a member.

Guardrails: one side only (members). Check `rules/do-not-say.md` (email block) and `rules/writing-rules.md`; run `ops/QA-checklist.md` (email block).
