---
trigger: model_decision
description: The SOS SMS go-to-market brain. Use for positioning, messaging, claims, competitive work, and any contractor-facing or customer-facing copy.
---

The SOS SMS go-to-market lives at `../SOSSMSGTMBrain`.

Load `../SOSSMSGTMBrain/AGENTS.md` first, then `rules/glossary.md`, `rules/feature-status.md`, `rules/do-not-say.md`, and `rules/writing-rules.md`. Then the channel engine the router names for the side.

Pick the side first, never blend them:
- Contractors (supply): no charge to see a request, and the trip paid before you roll. Cold email, partners, referral loop.
- Customers (demand): one text, an arrival time on acceptance, and a 90-minute window from the request with the $99 trip charge back when missed, in the zone's covered areas and hours. Search ads, problem pages, product loops.

Non-negotiables:
- Pre-launch: nothing is live; nothing in the present tense as if it were.
- No invented numbers, prices, arrival times, counts, or testimonials. Every value comes from `reference/resolution-register.md`; per-message details are {{merge fields}}.
- Always "SOS SMS", never the first word alone. SOS SMS dispatches; never the plumber, an emergency service, or 911.
- The safety line on every urgent call to text: "For fire, a gas smell, or anyone hurt, call 911 first."
- "Request", never "lead". Never "escrow", "exclusive", "pre-qualified", "guaranteed arrival time".
- No em or en dashes. Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower.

Run `../SOSSMSGTMBrain/ops/QA-checklist.md` before returning a draft. New market input goes to `../SOSSMSGTMBrain/ops/signal-log.md`.
