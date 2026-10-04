# Snapshot, 2026-10-04, every value resolved

The second capture, taken when every former unknown and founder decision was resolved (`ops/decisions.md`, 2026-10-04). It diffs against `2026-10-03-pre-launch-baseline.md`. Nothing is live, so the funnel, segments, and wins sections are unchanged: no activity, nothing measured, nothing asked yet.

## 1. Funnel
Unchanged from the baseline: no list sent, no partner signed, no ads, no pages, no number. The first numbers are counted from Stage 1 (contractors) and the first request in the founding zone (customers), weekly, against the zone thresholds (R32, R43).

## 2. Channels

| Channel | Assigned role | Actual | Verdict |
|---|---|---|---|
| Cold email (contractors) | Fill the founding zone | Not started | Ready once the zone is drawn and the terms on one page are published (Stage 1) |
| Partnership program | Reach contractors at the counter | Not started | Ready once a first partner signs; no referral fee at launch (R18) |
| Referral loop | Fill coverage gaps across trades | Not built | Runs after five paid trips |
| Paid search (customers) | Liquidity in a new zone | Not started | Runs once decisions 9 and 11 are done in Stage 0 and the zone is at density; ceiling $275 per paid job while proving (decision 12) |
| Problem pages | Owned demand | Not written | Written in Stage 2; shutoff steps reviewed by a licensed plumber before publishing |
| Product loops | Owned demand, repeat | Not built | Launch day |

## 6. Product and delivery status

| Capability | Ledger says | Reality | Action |
|---|---|---|---|
| Every customer and contractor capability | PLANNED with every rule decided, HELD, or NOT AT LAUNCH | Not built; pre-launch | Build in Stage 0 or at the stage named (`rules/feature-status.md`) |
| Stage 0 work (carrier registration, Google eligibility, Stripe Connect, trademark check, counsel) | Decided, not yet done | Not done | Stage 0 |
| GTM walkthrough deck | BUILT, internal, every value resolved | Built | Deployment Protection on at the first deploy |
| Brand v1 | BUILT, dark palette kept as validated | Same | None |

## 7. What this changes

| Change | Type | Files | Owner | Status |
|---|---|---|---|---|
| The twelve decisions made (2026-10-03) and every other value resolved in the register (R01 to R50) | AMEND | every `rules/` file, the master context, `reference/`, `templates/`, `examples/`, `adapters/`, `tools/check_sos_sms.py` | GTM consultant | Done 2026-10-04 |
| Review cadence and corroboration thresholds adopted | AMEND | `ops/review-cadence.md`, `ops/signal-log.md` | GTM consultant | Done 2026-10-04 |
| The house checker fails on any placeholder, open-decision wording, bracket slot, or unregistered merge field | AMEND | `tools/check_sos_sms.py`, `tools/audit_brain.py` (merge fields only) | GTM consultant | Done 2026-10-04 |

**Ledgers reviewed this snapshot:** all four `rules/` files, the master context, the copy bank, the decision log, the review cadence.

## Audit results
`tools/audit_brain.py`: 0 errors, 0 warnings. `tools/check_sos_sms.py`: 0 errors.
