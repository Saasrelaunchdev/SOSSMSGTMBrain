# Review cadence

Who reviews what, how often, and when a file is stale. **Set 2026-10-02, adopted 2026-10-04.** Owners map to the two founder roles (R25): the GTM owner and the growth lead are the demand lead; product is the supply lead until the product engineer who owns dispatch and payments joins (one of the first hires, speed-to-scale plan Stage A).

## Rituals

| Ritual | Frequency | Owner | Work |
|---|---|---|---|
| Signal triage | Weekly, Monday | GTM owner | Disposition every new signal, move WATCH counters, execute PATCHes |
| Decision check | Weekly | Founders | Log any change to a decided value with its date and basis; trigger the amendment order |
| Ledger sweep | Monthly | GTM owner, product | Read the four `rules/` files against reality; update `last_reviewed` |
| Zone signals | Weekly from Stage 1 | Growth lead | Density per trade and hour band, acceptance by trade, arrival, late arrivals and no-shows, monthly churn, annual renewal, and members against about 410 (R64), against thresholds (R32) |
| Plan mix | Weekly from the first member (Stage 2) | Growth lead | Joins by plan against the planning mix, Basic 10, Plus 80, Premier 10 percent (R70). Mostly Basic means Plus is overpriced or underbuilt; mostly Premier means Plus is underpriced. A price or entitlement change goes to both founders: tested on the first sheet of the pricing workbook (`Fit137/SOSSMSGTMBuild`), then the amendment order below |
| Acquisition ceilings | Weekly from Stage 2 | Growth lead | Cost per new paid member by channel, plan, and zone against the ceiling of the plan joined (R63, planning values: about $47 Basic, $70 Plus, $151 Premier on the monthly plan; about $48, $70, $139 annual). A channel scales while at or under, and stops when it is not. No paid search at launch; search volume for SOS SMS by name counted once a zone has been open 6 months (R68) |
| Snapshot | Monthly before launch; every two weeks per live zone | GTM owner | The capture in `snapshots/`, ending in what it changed |
| Master context version | On any AMEND, or quarterly | GTM owner | Bump version, refresh `status_notes`, check sections against the ledgers |
| Brain audit | Monthly, and before any launch gate | GTM owner | `tools/audit_brain.py`, `tools/check_sos_sms.py`, then one live asset from the brain only |
| Portable layer | Whenever a `rules/` file changes | GTM owner | Regenerate `adapters/portable-control-layer.md` with a new date |

## Ledger ownership and staleness

| File | Owner | Stale after |
|---|---|---|
| `rules/feature-status.md` | Product | 30 days, and immediately at any build change |
| `rules/do-not-say.md` | Founders and counsel | 90 days |
| `rules/glossary.md` | GTM owner | 90 days |
| `rules/writing-rules.md` | GTM owner | 180 days |
| `context/` master context | GTM owner | 90 days |
| `adapters/portable-control-layer.md` | GTM owner | 30 days, or any ledger change |

`feature-status.md` goes stale fastest and does the most damage: it is what stands between "PLANNED" and a promise.

## The amendment order
1. The `rules/` ledger that changed. 2. The master context section. 3. A dated entry in `decisions.md`. 4. `copy-bank.md` (search for the old phrasing) and every asset carrying the old value, found through `asset-index.md`. 5. Regenerate the portable control layer. The cross-side check runs at step 1: a change on one side is checked against the other side's terms.

## Authority
- A PATCH: anyone producing work.
- An AMEND to any `rules/` file: a founder.
- Positioning, ICP, channel mix, pricing, the plans and their entitlements, or the guarantee: both founders, with a dated entry in `decisions.md`.
