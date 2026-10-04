# Prompt library, common SOS SMS tasks

Filled, runnable prompts for recurring jobs. Each assumes the agent has loaded the router (`CLAUDE.md` or `AGENTS.md`) and the four `rules/` files. Copy, fill the brackets marked with `<angle brackets>`, run. Per-message details in SOS SMS copy are `{{merge fields}}`, filled from a named record and never typed by hand; every other value is in `reference/resolution-register.md`.

There is no sales team in this GTM, so there are no call scripts, demo scripts, or meeting prompts. There is no LinkedIn, no social, no outbound homeowner email or text, and no Local Services Ads, so there are no prompts for them. Asked for one, refuse and name the in-mix channel that does the job.

## Customers

**Search ad group.** "Write an <emergency / problem / prevention> ad group for SOS SMS customers in zone <zone>, covered hours <hours>. Follow `templates/search-ad.md` and match `examples/search-ad-zone.md`. Use `reference/channel-engine-paid-search.md` and `reference/value-proposition-customers.md`. Count characters. Mark any line with a condition. Then run `ops/QA-checklist.md`, search ads block included."

**Problem guide.** "Draft a problem guide for '<problem>' following `templates/problem-guide.md`. Shutoff and safety steps only, general enough to hold in any home; a licensed plumber reviews them before publishing. Safety line first. The text button and one line on SOS SMS at the end, only for zones at density. QA before returning."

**Zone landing page.** "Draft the zone landing page for <zone> following `templates/landing-page-zone.md`, matching `examples/zone-landing-page.md`. Decided values as written; the zone's details as merge fields. QA before returning."

**First reply variant.** "Write the first reply for the problem type '<pipe / water heater / toilet / sewer backup / ceiling leak>' following `templates/first-reply-sms.md` and matching `examples/first-reply-sms.md`. One idea per message; no link before agreement. QA, text messages block."

## Contractors

**Cold email sequence for a zone.** "Write emails 1 to 4 for contractors in <zone> following `templates/cold-email.md`, matching `examples/cold-email-sequence.md`. Email 1 under 120 words. 'Request', never 'lead', for SOS SMS. Decided terms as written; per-email details as merge fields. QA, email block."

**Partner kit.** "Build the partner kit for <partner name, type> with code <code> following `templates/partner-kit.md`. Take the FAQ answers from `reference/objection-handling.md`. No endorsement implied. QA before returning."

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
