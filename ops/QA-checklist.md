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
- [ ] No outbound email or text to homeowners; no marketing text without written consent.

## Claims
- [ ] Nothing is described as live. Every capability matches its flag in `rules/feature-status.md`.
- [ ] Pre-launch contractor recruiting copy says what SOS SMS is building, in the future tense.
- [ ] No testimonial, rating, count, logo, or result. Social proof is the drill's method line; proof is its named record (R44, R45).
- [ ] Every per-message detail is a `{{merge field}}` from the register's list, never typed by hand.
- [ ] No "escrow", "exclusive", "pre-qualified", "guaranteed arrival time", or "every contractor in your area".
- [ ] Any guarantee mention carries the scope in the same sentence: 90 minutes from the request, the $99 trip charge back, and the covered areas and hours (`{{zone neighborhoods}}`, `{{covered hours}}`).
- [ ] No relaunch guarantee (held, R17), no guarantee on the repair, no price range before arrival (R49), no volume or earnings promise.
- [ ] Every "only", "first", "best", "never", "always" is cleared in `rules/do-not-say.md`.
- [ ] Nothing presents SOS SMS as the plumber, an emergency service, or 911.

## Naming and strategy
- [ ] "Request", not "lead"; "trip charge" and "SOS SMS fee" named separately (`rules/glossary.md`).
- [ ] No framing that contradicts a DECIDED entry in `ops/decisions.md`.
- [ ] No contest on volume or exclusivity (contractors), or brand familiarity and guarantees on the work (customers).

## Audience and stage
- [ ] One side only: contractors or customers.
- [ ] Nothing promised to one side that the other side's terms do not deliver.
- [ ] Written for the journey stage it targets (`reference/customer-journey.md`).
- [ ] Customer copy only for zones at the density number and covered hours.

## Text messages
- [ ] Says it is automated and how to reach a person.
- [ ] Names SOS SMS before any link; no link in the first message.
- [ ] The safety line is present wherever the copy invites an urgent text.
- [ ] A payment request states the trip charge, what it covers, and the guarantee scope.

## Search ads and pages
- [ ] No superlative, no arrival average, no "24/7" beyond the zone's covered hours.
- [ ] The safety line on the landing page and in one ad description.
- [ ] No bid on "SOS plumbing" (decision 10); not a Local Services Ad.

## Email
- [ ] Accurate sender, honest subject line, postal address, one-click opt-out (S73).
- [ ] Contractor email 1 under 120 words; no claims about SOS SMS results.
- [ ] Homeowner email only after a scorecard opt-in; never cold.

## Voice
- [ ] Reads like the matching file in `examples/`: dispatch-room calm, mechanics before adjectives.

## After shipping
- [ ] Asset filed in `pages/` or logged in `ops/asset-index.md`.
- [ ] Anything the work taught you logged in `ops/signal-log.md`.
