# SOS SMS GTM, agent entry point

This repository is the SOS SMS go-to-market: a pre-launch, two-sided marketplace for emergency home repair in plumbing, HVAC, and electrical. Homeowners join one of three membership plans, monthly or annual, before anything breaks; in an emergency, a member texts one number, licensed, insured contractors matched by trade and area see the request at once, and the first who can come accepts with an arrival time. You are an AI agent working inside it. Read this file, then follow its pointers. Do not improvise strategy that is already decided here.

## Read before any contractor-facing or member-facing output
1. `rules/glossary.md`, the words SOS SMS uses, and the ones it never uses.
2. `rules/feature-status.md`, what is shipped (nothing), what is planned with its decided rules, what is held, and what is not at launch.
3. `rules/do-not-say.md`, the claims you must never make, and what to write instead.
4. `rules/writing-rules.md`, how every word is written, per side and per medium.
5. The `reference/` file for the job. For strategy questions: `context/SOS-SMS_GTM_Master_Context.md` and `ops/decisions.md`.

## Pick the side first, never blend them
- **Contractors (supply).** Promise: no charge to see a request, and the trip paid before you roll. One set of terms in every trade: $25 per completed paid job from the first job, no founding period. Channels: cold email, a partnership program, an in-product referral loop. Engine: `reference/channel-engine-contractors.md`.
- **Members (demand).** Promise: one text, and help is on the way; join before you need it. The card and address are on file from joining, and an arrival time inside 90 minutes comes when someone accepts. Three plans: Basic, Plus (shown first, most popular), and Premier; on Plus and Premier the 90-minute guarantee credits 6 or 12 months of membership on a late arrival or a no-show. A late arrival keeps its trip charge; when no one accepts, nobody pays. Channels: affiliates and email before the need, search and SEO pages and paid social for sign-ups, member loops; no paid search at launch. Engine: `reference/channel-engine-members.md`.

Supply leads, demand follows, zone by zone. Memberships open only in zones where each of the three trades meets the density number in every hour band; elsewhere, member copy offers the launch list (R55).

## This GTM is product-led, with no sales team
Refuse sales call or demo scripts, meetings, shop visits, door-to-door, LinkedIn, cold email or texts to homeowners, marketing texts without written consent, paid search at launch, Local Services Ads, ads that sell dispatch to someone in the middle of an emergency, retargeting and pixels, and any payment to someone referring at a home purchase settlement. Say it is out of the mix and name the in-mix channel that does the job.

## Non-negotiables
- SOS SMS is pre-launch. Nothing is live: never write a capability in the present tense as if it were.
- Never invent a number, count, price, fee, arrival time, testimonial, or result. Every value is in `reference/resolution-register.md`: decided, a labelled planning value, or counted at a named stage. Per-message details are `{{merge fields}}`. No result exists before launch.
- The twelve decisions are decided (2026-10-03; revised by the membership revision, 2026-10-11, the tiers revision, 2026-10-20, and the pricing revision, 2026-10-21, `ops/decisions.md`). Write their decided words; never reopen one in copy. The plan prices are decided and go into member copy as written: Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350. The plan mix and the economics are internal.
- Always the full name, SOS SMS. Never the first word alone.
- SOS SMS dispatches; the contractor does the work. Never the plumber, a warranty, insurance, an emergency service, or 911. No plan pays for a repair, and no plan is faster than another. The safety line goes on everything that describes the emergency text: "For fire, a gas smell, or anyone hurt, call 911 first."
- Neither side's copy promises what the other side's terms do not deliver (`reference/marketplace-cross-side.md`).
- "Request", never "lead", for SOS SMS. Never "escrow", "exclusive", "pre-qualified", or "guaranteed arrival time".
- No em dashes or en dashes. Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower.
- Grade C figures stay internal. Planning values are never written as results.

## Before you ship
Run `ops/QA-checklist.md` against the draft. Match the voice in `examples/`. Templates: `templates/`. Prompts: `prompts/common-tasks.md`.

## When something changes
New input from a contractor, member, homeowner, partner, rival, or platform goes in `ops/signal-log.md` first. A rule change follows the amendment order in `ops/review-cadence.md`: the `rules/` ledger, then the master context, then `ops/decisions.md`, then the copy bank and assets, then `adapters/portable-control-layer.md`. Never the other way around.

Index of every file: `llms.txt`. For people: `README.md`.
