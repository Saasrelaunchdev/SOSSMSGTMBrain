# Prompt library, common SOS SMS tasks

Filled, runnable prompts for recurring jobs. Each assumes the agent has loaded the router (`CLAUDE.md` or `AGENTS.md`) and the four `rules/` files. Copy, fill the brackets marked with `<angle brackets>`, run. Per-message details in SOS SMS copy are `{{merge fields}}`, filled from a named record and never typed by hand; every other value is in `reference/resolution-register.md`.

There is no sales team in this GTM, so there are no call scripts, demo scripts, or meeting prompts. There is no LinkedIn, no cold email or texts to homeowners, no paid search at launch (decision 11), no Local Services Ads, no retargeting, and no ad that sells dispatch to someone in the middle of an emergency, so there are no prompts for them. Asked for one, refuse and name the in-mix channel that does the job.

## Members

Homeowners join before the need (the membership revision, 2026-10-11), on Basic, Plus, or Premier (the pricing revision, 2026-10-21), for plumbing, HVAC, and electrical. Every member prompt sells being ready, never help tonight, and only for zones where memberships are open (R55); elsewhere it points to the launch list.

**Affiliate kit.** "Build the affiliate kit for <partner name, type> in zone <zone> with code <code> following `templates/affiliate-kit.md`, matching `examples/affiliate-kit.md`. First confirm the partner may be paid: never a real estate agent, lender, title or settlement agent, or anyone referring at a home purchase settlement. The disclosure line next to every mention. The three plans' prices as written (Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350), the $99 trip charge on its own line, the guarantee named only with Plus and Premier and its scope. QA, affiliates block."

**Member email.** "Write the <scorecard / launch list / opening / welcome / seasonal / renewal / cancellation> email for SOS SMS in zone <zone> following `templates/member-email.md`, matching `examples/launch-list-email.md`. Only to people who opted in. The full name, `{{postal address}}`, and `{{opt-out link}}` in every email. No urgency the facts do not carry. QA, email block."

**Membership page.** "Draft the membership page for zone <zone> following `templates/membership-page.md`, matching `examples/membership-page.md`. The three plans, prices, and entitlements as written, Plus in the middle on the annual plan, flagged 'Most popular'; the $99 trip charge on its own line; the guarantee with Plus and Premier and its scope; the three trades named; no plan as faster; no plan mix or contribution figure; the zone's details as merge fields; cancel any time next to the price, before the card. QA before returning."

**Sign-up ad set.** "Write a <readiness / plan comparison / seasonal> paid social sign-up ad set for SOS SMS memberships in open zone <zone>, on the zone's map by location only. Follow `templates/search-ad.md` (sign-up ads for paid social; its search ad drafts are held, with no paid search at launch, decision 11) and match `examples/search-ad-zone.md`. Use `reference/channel-engine-members.md` and `reference/value-proposition-members.md`. Count characters. Mark any line with a condition. The guarantee only with Plus and Premier; no plan as faster. Then run `ops/QA-checklist.md`, paid social ads block included."

**Problem or prevention guide.** "Draft a <problem / prevention> guide for '<problem or season>' following `templates/problem-guide.md`. Shutoff and safety steps only (for HVAC and electrical, the safety steps only), general enough to hold in any home; a licensed contractor in the guide's trade reviews them before publishing. Safety line first. The readiness scorecard and how membership works at the end, for next time; never a sign-up before the steps. QA before returning."

**Member texts.** "Write the <welcome texts / first reply for the problem type '<pipe / water heater / toilet / sewer backup / ceiling leak / no heat / no cooling / a dead panel or circuit>' / late-arrival credit text / reply to a non-member> following `templates/first-reply-sms.md` and matching `examples/first-reply-sms.md`. One idea per message; no link, offer, or confirmation request in any emergency text; no plan price in an emergency text; on a late arrival the trip charge stands, and `{{credit amount}}` goes only in a Plus or Premier text. QA, text messages block."

## Contractors

**Cold email sequence for a zone.** "Write emails 1 to 4 for contractors in <zone> following `templates/cold-email.md`, matching `examples/cold-email-sequence.md`. Email 1 under 120 words. 'Request', never 'lead', for SOS SMS. Decided terms as written: $25 per completed paid job from the first job, $74 of each $99, one set of terms in every trade; no founding terms and no deadline. Per-email details as merge fields. QA, email block."

**Partner kit (contractors).** "Build the partner kit for <partner name, type> with code <code> following `templates/partner-kit.md`. Take the FAQ answers from `reference/objection-handling.md`. No endorsement implied. QA before returning."

**The terms on one page.** "Draft the terms on one page following `templates/terms-on-one-page.md` from the decisions logged in `ops/decisions.md` and the values in `reference/resolution-register.md`. Every term is decided; list the merge fields it carries."

## Both sides

**Edit a draft.** "Edit this draft for <side>: <paste>. Check every claim against `rules/do-not-say.md`, every capability against `rules/feature-status.md`, every term against `rules/glossary.md`, and the promise against `reference/marketplace-cross-side.md`. Return the edit and a list of what changed and why."

**Answer an objection.** "Write a written answer to '<objection>' for <side>, from `reference/objection-handling.md`. Use only decided values; if the brain lacks the fact, say which one and stop."

**Compare with a rival.** "Write a comparison of SOS SMS with <rival> for <side>, from `reference/competitor-battlecards.md`. Lead with the vectors SOS SMS leads; concede the ones it does not. No grade C figures in external copy."

## Operating the brain

**Log a signal.** "Log this in `ops/signal-log.md`: <paste the note, reply, review, or competitor move>. Keep the verbatim. Classify the type, assign a disposition by the thresholds in that file, and if it is a PATCH or AMEND, name exactly which files change and in what order."

**A decided value changes.** "Decision <number> changes to: <exact wording>. Follow the amendment order: `rules/` ledger, then the master context, then a dated entry in `ops/decisions.md`, then `ops/copy-bank.md` and every asset that carries the old value, then regenerate `adapters/portable-control-layer.md`. List each file changed."

**Take a snapshot.** "Build this period's snapshot in `snapshots/` from <data>. Diff product status against `rules/feature-status.md`. End with what this changes, or 'No ledger change this period'."

**Audit.** "Run `python3 tools/audit_brain.py .` and `python3 tools/check_sos_sms.py .`, fix every error, then produce one real asset using only the brain and QA it. Report anything the brain could not supply."
