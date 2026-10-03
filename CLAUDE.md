# SOS SMS GTM, agent entry point

This repository is the SOS SMS go-to-market: a pre-launch, two-sided marketplace for emergency home repair. A customer texts one number; licensed, insured contractors matched by trade and area see the request at once; the first who can come accepts with an arrival time. You are an AI agent working inside it. Read this file, then follow its pointers. Do not improvise strategy that is already decided here.

## Read before any contractor-facing or customer-facing output
1. `rules/glossary.md`, the words SOS SMS uses, and the ones it never uses.
2. `rules/feature-status.md`, what is shipped (nothing) and what is planned, open, or not built.
3. `rules/do-not-say.md`, the claims you must never make, and what to write instead.
4. `rules/writing-rules.md`, how every word is written, per side and per medium.
5. The `reference/` file for the job. For strategy questions: `context/SOS-SMS_GTM_Master_Context.md` and `ops/decisions.md`.

## Pick the side first, never blend them
- **Contractors (supply).** Promise: no charge to see a request, and the trip paid before you roll. Channels: cold email, a partnership program, an in-product referral loop. Engine: `reference/channel-engine-contractors.md`.
- **Customers (demand).** Promise: one text, an arrival time when someone accepts, and a missed 90-minute window costs SOS SMS money. Channels: Google then Microsoft search ads, problem-solving pages, product loops. Engine: `reference/channel-engine-paid-search.md`.

Supply leads, demand follows, zone by zone. Customer copy is only for zones at the density number, in covered hours.

## This GTM is product-led, with no sales team
Refuse sales call or demo scripts, meetings, shop visits, LinkedIn, outbound email or texts to homeowners, marketing texts without written consent, Local Services Ads, outreach partnerships (agents, inspectors, hardware stores, homeowner associations), neighborhood group posts, and retargeting. Say it is out of the mix and name the in-mix channel that does the job.

## Non-negotiables
- SOS SMS is pre-launch. Nothing is live: never write a capability in the present tense as if it were.
- Never invent a number, count, price, fee, arrival time, testimonial, or result. Unknowns stay `{TBD}`. The proof-point set is empty.
- Never fill a `[bracket]`. It waits on a founder decision in `ops/decisions.md`.
- Always the full name, SOS SMS. Never the first word alone.
- SOS SMS dispatches; the contractor does the work. Never the plumber, an emergency service, or 911. The safety line goes on every urgent call to text: "For fire, a gas smell, or anyone hurt, call 911 first."
- Neither side's copy promises what the other side's terms do not deliver (`reference/marketplace-cross-side.md`).
- "Request", never "lead", for SOS SMS. Never "escrow", "exclusive", "pre-qualified", or "guaranteed arrival time".
- No em dashes or en dashes. Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower.
- Grade C figures stay internal. Recommendations are never written as decisions.

## Before you ship
Run `ops/QA-checklist.md` against the draft. Match the voice in `examples/`. Templates: `templates/`. Prompts: `prompts/common-tasks.md`.

## When something changes
New input from a contractor, customer, partner, rival, or platform goes in `ops/signal-log.md` first. A rule change follows the amendment order in `ops/review-cadence.md`: the `rules/` ledger, then the master context, then `ops/decisions.md`, then the copy bank and assets, then `adapters/portable-control-layer.md`. Never the other way around.

Index of every file: `llms.txt`. For people: `README.md`.
