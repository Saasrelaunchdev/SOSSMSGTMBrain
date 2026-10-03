# QA checklist, run before shipping any output

Tick every line against the draft. Any no is a fix before shipping. Every item is answerable yes or no by looking at the draft.

## Writing
- [ ] No em dashes and no en dashes, including ranges.
- [ ] None of the banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower, or their variants.
- [ ] The full name SOS SMS every time; the first word never appears alone.
- [ ] Paragraphs of one to three sentences; no exclamation marks.
- [ ] Every number in the draft is in the brain with its source ID, or shows as {TBD}.

## Channel
- [ ] The channel is in the mix for this side (`rules/writing-rules.md`, channel discipline). If not, stop and redirect.
- [ ] No outbound email or text to homeowners; no marketing text without written consent.

## Claims
- [ ] Nothing is described as live. Every capability matches its flag in `rules/feature-status.md`.
- [ ] No testimonial, rating, count, logo, or result. The proof-point set is empty.
- [ ] Every [bracket] and {TBD} is still visible and unfilled.
- [ ] No "escrow", "exclusive", "pre-qualified", "guaranteed arrival time", or "every contractor in your area".
- [ ] Any guarantee mention carries clock start, refund, and covered areas and hours in the same sentence, or the brackets for them.
- [ ] No relaunch guarantee, no guarantee on the repair, no volume or earnings promise.
- [ ] Every "only", "first", "best", "never", "always" is cleared in `rules/do-not-say.md`.
- [ ] Nothing presents SOS SMS as the plumber, an emergency service, or 911.

## Naming and strategy
- [ ] "Request", not "lead"; "trip charge" and "SOS SMS fee" named separately (`rules/glossary.md`).
- [ ] No framing that contradicts a DECIDED entry in `ops/decisions.md`; no recommendation presented as decided.
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
- [ ] No bid on "SOS plumbing" while decision 10 is open; not a Local Services Ad.

## Email
- [ ] Accurate sender, honest subject line, postal address, one-click opt-out (S73).
- [ ] Contractor email 1 under 120 words; no claims about SOS SMS results.
- [ ] Homeowner email only after a scorecard opt-in; never cold.

## Voice
- [ ] Reads like the matching file in `examples/`: dispatch-room calm, mechanics before adjectives.

## After shipping
- [ ] Asset filed in `pages/` or logged in `ops/asset-index.md`.
- [ ] Anything the work taught you logged in `ops/signal-log.md`.
