# Snapshot, 2026-10-03, pre-launch baseline

The first capture, taken as the brain was built. Nothing is live, so most sections record an absence. That record is the point: the next snapshot diffs against it, and the first real numbers will be measured against zero, not against a guess.

## 1. Funnel

| Stage | Contractors | Customers | vs last snapshot |
|---|---|---|---|
| Awareness to staying active | No activity: no list sent, no partner signed, no sign-ups | No activity: no ads, no pages, no number | First snapshot |

KPIs to start measuring at Stage 1: Lead Cost Checks completed by channel, JOIN texts, time from JOIN to verified, acceptance by hour band. At Stage 2: cost per first text, reply-to-agreement rate, time to acceptance, share inside the window, refunds caused by SOS SMS, owned share.

## 2. Channels

| Channel | Assigned role | Actual | Verdict |
|---|---|---|---|
| Cold email (contractors) | Fill the founding zone | Not started; zone not set | Waits on decision 1 |
| Partnership program | Reach contractors at the counter | Not started | Waits on a first partner |
| Referral loop | Fill coverage gaps across trades | Not built | Waits on five paid trips |
| Paid search (customers) | Liquidity in a new zone | Not started | Waits on decisions 9 and 11, and density |
| Problem pages | Owned demand | Not written | Waits on plumber review |
| Product loops | Owned demand, repeat | Not built | Waits on launch |

## 3. Segments
Not measurable. ICP hypotheses stand as written in `reference/icp-personas.md`: Level 2 shops first, Level 1 alongside; both customer levels reached at the moment of search.

## 4. Wins and losses
None. No contractor or customer has been asked anything yet.

## 5. Competitive
Research-dated 2026-10-01 (`reference/competitive-analysis.md`). Facts to recheck by the next snapshot: Google Local Services policy (S70), message asset rules (S72), lead platform prices (S03, S06, S08, S10), Benjamin Franklin's punctuality terms (S40). Every figure was read from search summaries and needs page verification before external use.

## 6. Product and delivery status

| Capability | Ledger says | Reality | Action |
|---|---|---|---|
| Every customer and contractor capability | PLANNED, DESIGN OPEN, CANDIDATE, or NOT BUILT | Build status unconfirmed by the product team | Ask product to confirm each line |
| Launch prerequisites (carrier registration, Google eligibility, payments, name check, counsel) | NOT DONE | Not done | Stage 0 |
| GTM walkthrough deck | BUILT, internal | Built; Vercel protection open | Turn on Deployment Protection |
| Brand v1 | BUILT, dark palette pending | Same | Approve or revise the dark palette |

## 7. What this changes

| Change | Type | Files | Owner | Status |
|---|---|---|---|---|
| Pre-launch framing rule for contractor recruiting, found by the live test | AMEND | `rules/writing-rules.md`, master context, QA checklist, decisions, portable layer | Build | Done 2026-10-03 |
| The twelve decisions remain open; decisions 1 to 5 unblock copy on both sides | none | `ops/decisions.md` | Founders | Open |
| Review cadence and thresholds are proposals | none | `ops/review-cadence.md` | Founders | To confirm |

**Ledgers reviewed this snapshot:** all four `rules/` files, the master context, the copy bank, the decision log.

## Baseline audit results
`tools/audit_brain.py` and `tools/check_sos_sms.py` were run at build; results are in the commit that added this snapshot. Live test: `pages/partner-counter-card.md`, two QA failures on the first draft, both fixed, one rule added.
