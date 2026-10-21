# Snapshot, 2026-10-21, the tiers and pricing revisions

The fourth capture, taken when the founder's feedback (`ops/signal-log.md`, 2026-10-20) and the user's pricing instruction (2026-10-21) reached the brain: three trades in one membership, the two ways a 90-minute window is missed, no paid search at launch, no founding period, and three plans with sliding-scale entitlements (`ops/decisions.md`, 2026-10-20 and 2026-10-21). It diffs against `2026-10-11-membership-revision.md`. Nothing is live, so there is still no activity and nothing measured; what changed is the member offer, the miss rules, the channel mix, the economics, and the rules that govern the copy.

## 1. Funnel
Nothing measured yet. What will be counted, and when (R43):
- Contractors, from Stage 1: sign-ups and acceptance **by trade**, plumbing, HVAC, and electrical, weekly, against the zone thresholds (R32). Each trade fills toward its own 9 places (R08).
- Members, from Stage 1: readiness scorecard completions, launch list joins, and ZIP checks, by channel and affiliate code.
- Members, from the day memberships open in the launch zone: new paid members **by plan** and channel, the plan mix against its planning value (R70), monthly churn, annual renewals, requests per member by trade (R42, R58 to R60), and late arrivals and no-shows per 100 accepted requests (R29, R32).

## 2. Channels

| Channel | Assigned role | Actual | Verdict |
|---|---|---|---|
| Cold email, partnership program, referral loop (contractors) | Fill the launch zone in all three trades | Not started | Lists by trade from the state license lists (R40); no founding list and no deadline (R07, retired) |
| Affiliates (members) | Lead, before the need | Not started | $20 per new paid member on any plan, decided, paid once the second monthly or first annual payment clears (R61) |
| Email (members) | Lead, before the need | Not started | Unchanged: the readiness scorecard and the launch list from Stage 1, the opening email the day memberships open |
| SEO pages (members) | Support, sign-ups | Not written | The five problem and prevention guides now cover no heat, no cooling, and a dead circuit as well as water |
| Paid social (members) | Support, sign-ups | Not started | In open zones only, on the zone's map, paused with sign-ups (R34), at or under the ceiling of the plan joined (R63) |
| Paid search (members) | Out at launch, 2026-10-20 | Never started | No Google search ads, no Microsoft Ads, never Local Services Ads (decision 11). Search volume for SOS SMS by name is counted once a zone has been open 6 months (R68); a brand campaign may then run under the ceiling |
| Member loops | Retention and referral | Not built | Launch day: the welcome texts with the plan, the contact card, Text READY, the phones on file, the renewal |

## 3. Economics, planning values (internal)
From the pricing model in `Fit137/SOSSMSGTMBuild` (`google-folder/SOS_SMS_Pricing_Model.xlsx`, every input on its first sheet; tables in `sources/raw/gtm/pricing/pricing-model.md`), illustrative until the zone runs: the three plans at $10, $15, and $35 a month (decided); contribution about $9.29, $13.77, and $29.62 a member a month, about $14.91 at the plan mix; every request nets about $13.03; the acquisition ceiling, the first 6 months of contribution at 6.5 percent monthly churn (R59), about $47 Basic, $70 Plus, $151 Premier (R63); the Plus credit about $0.17 a member a month at the 5 percent late share (R29). Paid search at the plumbing benchmark costs about $137 per new paid member (S15, B), about 3 times Basic's ceiling, which is why it does not run at launch. The plan mix and every figure here stay off member pages.

## 4. Positioning and the offer
Unchanged: the two promises, the sides never blended, the safety line, the dispatch rule. Changed: the member offer is three plans, Plus shown first and flagged most popular; the 90-minute guarantee is the Plus and Premier credit (6 and 12 months of membership), never written for Basic; no plan is faster; three trades named on every member page.

## 5. Claims and copy
New bans (`rules/do-not-say.md`): the guarantee on Basic or without its plans; "your $99 back if they're late"; priority or faster dispatch by plan; `{{monthly price}}` and `{{annual price}}` (retired, the prices are decided); the plan mix or contribution on a page; "plumbing only"; search ads as a running channel; founding wording and recruiting deadlines; contractor terms that change with the member's plan. New merge fields: `{{plan}}`, `{{credit amount}}`.

## 6. Product and delivery status

| Capability | Ledger says | Reality | Action |
|---|---|---|---|
| Three plans, upgrades and downgrades, the late-arrival credit to the next bills | PLANNED (decision 2, R54, R65, R66) | Not built | Loaded into membership billing and tested in Stage 0 |
| Phones on file; Premier's second home and trip charge a year | PLANNED (R66, R69) | Not built | Built before memberships open |
| NEXT after the 90 minutes | PLANNED (R17), no longer held | Not built | Built before memberships open |
| Contractor standing on late arrivals and no-shows | PLANNED (R67) | Not built | Built with dispatch |
| Paid search, priority dispatch | NOT AT LAUNCH | Never built | None |
| Founding terms, first refusal, covered hours | Retired (R05 to R07, R13, R15) | Never built | None |
| The pricing workbook | BUILT 2026-10-21, internal | Built | The founder tests prices on its first sheet |

## 7. What this changes

| Change | Type | Files | Owner | Status |
|---|---|---|---|---|
| Three trades, the miss cases, no paid search, no founding period; decisions 1, 2, 3, 5, 7, 8, 10, 11, 12 revised; R65 to R68 added, R05 to R07 and R13 retired | AMEND | `ops/decisions.md`, `reference/resolution-register.md`, every `rules/` file, the master context (version 1.5) | GTM consultant | Done 2026-10-21 |
| Three plans with sliding-scale entitlements; decisions 2, 3, 12 revised; R69 and R70 added | AMEND | The same, and `reference/pricing-and-economics.md` | GTM consultant | Done 2026-10-21 |
| Every reference file, template, example, and page brought to the three trades and the three plans | AMEND | `reference/`, `templates/`, `examples/`, `pages/`, `prompts/common-tasks.md`, `ops/copy-bank.md`, `ops/QA-checklist.md`, `ops/review-cadence.md` | GTM consultant | Done 2026-10-21 |
| Routers, adapters, and the portable control layer regenerated | AMEND | `CLAUDE.md`, `AGENTS.md`, `README.md`, `llms.txt`, `adapters/` | GTM consultant | Done 2026-10-21 |
| Sources synced; new research S95 to S100 | AMEND | `sources/raw/gtm/`, `sources/extracted/INDEX.md` | GTM consultant | Done 2026-10-21 |
| The walkthrough deck (first), the GTM build repo, the Google folder, the deck handoff | AMEND, downstream | `Saasrelaunchdev/SOSSMSGTMWalkthrough`, `Fit137/SOSSMSGTMBuild` | GTM consultant | In the same revision |
| The Miro board | AMEND, downstream | The handover prompt, extended for these revisions (no access from here) | GTM consultant | Handed over |

**Ledgers reviewed this snapshot:** all four `rules/` files, the master context, the resolution register, the copy bank, the decision log, the signal log, the review cadence, the QA checklist, the asset index.

**Items for later, recorded and not acted on here:** whether the plan mix lands near 80 percent on Plus once real members choose (R70 says what each skew means); Premier's worst case, a heavy two-home member, which the workbook's Checks sheet flags WATCH; the contractor volume in electrical, about one request every 5 months at the zone's member base (R64), and whether the 9 electricians stay active (R32 measures activity in plumbing and HVAC only); the credit's real cost once the late share is measured.

## Audit results
`tools/audit_brain.py`: 0 errors, 1 warning (`reference/resolution-register.md` over its line budget: 70 rows and the merge fields). `tools/check_sos_sms.py`: 0 errors.
