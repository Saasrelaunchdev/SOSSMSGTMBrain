---
trigger: model_decision
description: The SOS SMS go-to-market brain. Use for positioning, messaging, claims, competitive work, and any contractor-facing or member-facing copy.
---

The SOS SMS go-to-market lives at `../SOSSMSGTMBrain`.

Load `../SOSSMSGTMBrain/AGENTS.md` first, then `rules/glossary.md`, `rules/feature-status.md`, `rules/do-not-say.md`, and `rules/writing-rules.md`. Then the channel engine the router names for the side.

Pick the side first, never blend them:
- Contractors (supply): no charge to see a request, and the trip paid before you roll. $25 per completed paid job from the first job, one set of terms in every trade. Cold email, partners, referral loop.
- Members (demand): homeowners who join Basic, Plus, or Premier, monthly or annual, before the need, with the card and address on file, for plumbing, HVAC, and electrical. One text, and help is on the way: an arrival time inside 90 minutes on acceptance. On Plus and Premier, the 90-minute guarantee credits 6 or 12 months of membership on a late arrival or a no-show; a late arrival keeps its trip charge, a no-show's $99 comes back, and when no one accepts nobody pays. Affiliates and email before the need, search and SEO pages and paid social for sign-ups, member loops; no paid search at launch.

Non-negotiables:
- Pre-launch: nothing is live; nothing in the present tense as if it were.
- No invented numbers, prices, arrival times, counts, or testimonials. Every value comes from `reference/resolution-register.md`; per-message details are {{merge fields}}; the plan prices are decided and written as they are.
- Always "SOS SMS", never the first word alone. SOS SMS dispatches; never the plumber, a warranty, insurance, an emergency service, or 911. No plan pays for a repair, and no plan is faster.
- The safety line on everything that describes the emergency text: "For fire, a gas smell, or anyone hurt, call 911 first."
- "Request", never "lead". Never "escrow", "exclusive", "pre-qualified", "guaranteed arrival time".
- No em or en dashes. Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower.

Run `../SOSSMSGTMBrain/ops/QA-checklist.md` before returning a draft. New market input goes to `../SOSSMSGTMBrain/ops/signal-log.md`.
