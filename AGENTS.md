# SOS SMS GTM, agent entry point

Cross-tool entry file for Codex, Cursor, Zed, Jules, opencode, and other tools that read `AGENTS.md`. Identical in intent to `CLAUDE.md`; if the two differ, `CLAUDE.md` wins. Working in a tool that reads neither, or a chat window with no file access? See `adapters/`.

SOS SMS is a pre-launch, two-sided marketplace for emergency home repair, starting with plumbing and water emergencies. Homeowners join a monthly or annual membership before anything breaks; in an emergency, a member texts one number, the licensed, insured contractors on SOS SMS for that trade and area see it at once, and the first who can come accepts with an arrival time.

## Start here, in order
1. `rules/glossary.md`
2. `rules/feature-status.md`
3. `rules/do-not-say.md`
4. `rules/writing-rules.md`
5. For contractor work: `reference/channel-engine-contractors.md`. For member work: `reference/channel-engine-members.md`.
6. Strategy: `context/SOS-SMS_GTM_Master_Context.md`, `ops/decisions.md`.

## Sides, never blended
- **Contractors:** no charge to see a request, and the trip paid before you roll. Cold email, partnership program, referral loop. Self-serve sign-up by text.
- **Members:** join before you need it; then one text, an arrival time on acceptance, and a 90-minute window from the request text with the $99 trip charge back when it is missed, in the zone's covered areas and hours. The card and address are on file from joining. Affiliates and email before the need, search and SEO pages for sign-ups, member loops.

## Channel discipline
Product-led, no sales team. In: the channels above. Out: sales calls, demos, meetings, shop visits, door-to-door, LinkedIn, cold homeowner email or texts, marketing texts without consent, Local Services Ads, ads that sell dispatch during an emergency, retargeting and pixels, payments to anyone referring at a home purchase settlement. Refuse and redirect.

## Non-negotiables
- Pre-launch: nothing is live, nothing in the present tense as if it were.
- No invented numbers, prices, fees, arrival times, counts, testimonials, or results. Every value comes from `reference/resolution-register.md` (decided, planning value, or counted at a named stage); per-message details and the membership prices are `{{merge fields}}`. The twelve decisions are decided (six revised or replaced 2026-10-11).
- Always "SOS SMS", never the first word alone.
- SOS SMS dispatches; never the plumber, a warranty, insurance, an emergency service, or 911. The membership pays for no repair. The safety line on everything that describes the emergency text.
- Cross-side rule: no promise to one side that the other side's terms do not keep.
- "Request", never "lead". Never "escrow", "exclusive", "pre-qualified", "guaranteed arrival time".
- No em or en dashes. Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower.

## Before shipping
Run `ops/QA-checklist.md`. Match `examples/`.

## Compounding
New market input goes to `ops/signal-log.md`. Rule changes follow the amendment order in `ops/review-cadence.md`: ledger, master context, decision log, copy, portable layer.
