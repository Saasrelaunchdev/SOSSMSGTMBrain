# QA checklist, run before shipping any output

Tick every line against the draft. Any no is a fix before shipping. Every item is answerable yes or no by looking at the draft.

## Writing
- [ ] No em dashes and no en dashes, including ranges.
- [ ] None of the banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower, or their variants.
- [ ] The full name SOS SMS every time; the first word never appears alone.
- [ ] Paragraphs of one to three sentences; no exclamation marks.
- [ ] Every number in the draft is in the brain: a decided value or a labelled planning value from `reference/resolution-register.md`, or a sourced figure with its source ID. No placeholder, gap, or "coming soon".

## Channel
- [ ] The channel is in the mix for this side (`rules/writing-rules.md`, channel discipline). If not, stop and redirect.
- [ ] No cold email or text to homeowners; no marketing text without written consent.
- [ ] No ad that sells dispatch to someone in the middle of an emergency; ads sell memberships, in open zones (decision 11).

## Claims
- [ ] Nothing is described as live. Every capability matches its flag in `rules/feature-status.md`.
- [ ] Pre-launch contractor recruiting copy, and the member side's launch list, readiness scorecard, and guides before a zone opens, say what SOS SMS is building, in the future tense, and promise no service.
- [ ] No testimonial, rating, count, logo, or result. Social proof is the drill's method line; proof is its named record (R44, R45).
- [ ] Every per-message detail is a `{{merge field}}` from the register's list, never typed by hand.
- [ ] No "escrow", "exclusive", "pre-qualified", "guaranteed arrival time", or "every contractor in your area".
- [ ] Any guarantee mention carries the scope in the same sentence: 90 minutes from the member's request text, the $99 trip charge back, and the covered areas and hours (`{{zone neighborhoods}}`, `{{covered hours}}`).
- [ ] No relaunch guarantee (held, R17), no guarantee on the repair, no repair coverage or discount (R21, R53), no price range before arrival (R49), no volume or earnings promise, no free trial.
- [ ] Membership prices are `{{monthly price}}` and `{{annual price}}`, never the planning values (R51, R52); cancellation and renewal terms sit next to the price (R56).
- [ ] Every "only", "first", "best", "never", "always" is cleared in `rules/do-not-say.md`.
- [ ] Nothing presents SOS SMS as the plumber, an emergency service, or 911.

## Naming and strategy
- [ ] "Request", not "lead"; "member", not "customer" or "subscriber", for SOS SMS's demand side; the membership and the trip charge named separately, never one total (`rules/glossary.md`).
- [ ] No framing that contradicts a DECIDED entry in `ops/decisions.md`.
- [ ] No contest on volume or exclusivity (contractors), or repair coverage, brand familiarity, and guarantees on the work (members).

## Audience and stage
- [ ] One side only: contractors or members.
- [ ] Nothing promised to one side that the other side's terms do not deliver.
- [ ] Written for the journey stage it targets (`reference/customer-journey.md`).
- [ ] Membership copy only for open zones, at the density number and covered hours; elsewhere, the launch list, which promises no service (R55).

## Text messages
- [ ] Says it is automated and how to reach a person.
- [ ] Names SOS SMS before any link; no link in the first message.
- [ ] The safety line is present wherever the copy invites an urgent text.
- [ ] No emergency text asks a member for a card, a payment, or a confirmation; the acceptance text states the trip charge, what it covers, and the guarantee scope.

## Search ads, social ads, and pages
- [ ] No superlative, no arrival average, no "24/7" beyond the zone's covered hours.
- [ ] The safety line on the membership page and in one ad description.
- [ ] Location targeting only: no pixel, retargeting, or uploaded list.
- [ ] No bid on "SOS plumbing" (decision 10); not a Local Services Ad.

## Email
- [ ] Accurate sender, honest subject line, postal address, one-click opt-out (S73).
- [ ] Contractor email 1 under 120 words; no claims about SOS SMS results.
- [ ] Homeowner email only after an opt-in (the scorecard, the launch list, joining) or in a partner's own send; never cold.

## Affiliates
- [ ] The kit's words only; a code in every link; the disclosure next to the mention (S88).
- [ ] No payment to anyone referring at a home purchase settlement (R61, S86, S94).

## Voice
- [ ] Reads like the matching file in `examples/`: dispatch-room calm, mechanics before adjectives.

## After shipping
- [ ] Asset filed in `pages/` or logged in `ops/asset-index.md`.
- [ ] Anything the work taught you logged in `ops/signal-log.md`.
