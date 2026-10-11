# Snapshot, 2026-10-11, the membership revision

The third capture, taken when the demand side became a monthly or annual membership, joined before the need (`ops/decisions.md`, 2026-10-11). It diffs against `2026-10-04-everything-resolved.md`. Nothing is live, so there is still no activity and nothing measured; what changed is the plan for the member side, its channels, its economics, and the rules that govern its copy.

## 1. Funnel
Nothing measured yet. What will be counted, and when (R43):
- Contractors, unchanged: from Stage 1, weekly, against the zone thresholds (R32).
- Members, from Stage 1: readiness scorecard completions, launch list joins, and ZIP checks, by channel and partner code.
- Members, from the day memberships open in the founding zone: new paid members by channel, monthly churn, annual renewals, and requests per member (R42, R58 to R60).

## 2. Channels

| Channel | Assigned role | Actual | Verdict |
|---|---|---|---|
| Cold email, partnership program, referral loop (contractors) | Fill the founding zone | Not started | Unchanged from 2026-10-04 |
| Affiliates (members) | Lead, before the need | Not started | Partners signed for the founding zone in Stage 1, codes ready before it opens; commission $20 per new paid member after the first paid month (planning value, R61); never a payment at a home purchase settlement |
| Email (members) | Lead, before the need | Not started | The readiness scorecard and the launch list from Stage 1; the opening email the day memberships open; member email after |
| Search and SEO pages (members) | Support | Not written | Prevention and problem guides from Stage 1, reviewed by a licensed plumber; the membership page from Stage 2 |
| Paid search and paid social (members) | Support, sign-ups only | Not started | In open zones only, after Google's written confirmation; emergency dispatch searches excluded; spend held to the ceiling of about $43 per new paid member (decision 12, R63) |
| Member loops | Retention and referral | Not built | Launch day: the welcome texts, the contact card, Text READY, the forwardable card, the renewal |
| Paid search for dispatch (the paid request funnel) | Retired 2026-10-11 | Never started | Replaced by sign-ups before the need; the first-text-to-paid rate and the owned share are retired (R30) |

## 3. Economics, planning values (internal)
From the pricing model in `Fit137/SOSSMSGTMBuild` (`gtm/pricing/pricing-model.md`), all planning values until the zone runs: the membership at $10 a month or $100 a year (R51, R52); costs about $1.49 a member a month; contribution about $8.51 a member a month in the founding period and $9.03 after it; the acquisition ceiling about $43 per new paid member, the first 6 months of contribution at 6.5 percent monthly churn (R63); about 430 members per zone for about one request a month per founding contractor (R64). Paid search for dispatch would have cost about $137 per paid job, about three times the ceiling, which is why search now sells sign-ups. None of these figures goes into copy; the prices reach copy only as `{{monthly price}}` and `{{annual price}}`.

## 6. Product and delivery status

| Capability | Ledger says | Reality | Action |
|---|---|---|---|
| Membership, joining with the card and address on file, cancel any time, renewal reminders | PLANNED (decision 2, R54 to R56) | Not built | Membership billing tested in Stage 0 |
| One request text starts dispatch; welcome texts; the reply to a non-member | PLANNED (R57) | Not built | Built before memberships open |
| Affiliate program, a code per partner | PLANNED (R61) | Not built | Affiliate terms written in Stage 0 |
| The SOS SMS fee, the confirming text, the payment link for dispatch | Retired (R02, R30) | Never built | None |
| Every contractor capability | Unchanged | Not built | Unchanged |
| Stage 0 work | Decided, not yet done; now also the launch price, membership billing, the affiliate terms, email sending, and counsel review of the member terms with the automatic renewal disclosures (S87) | Not done | Stage 0 |

## 7. What this changes

| Change | Type | Files | Owner | Status |
|---|---|---|---|---|
| The demand side is a membership joined before the need; decisions 2, 3, 6, 8, and 11 revised, decision 12 replaced; R51 to R64 added, R02 and R30 retired | AMEND | `ops/decisions.md`, `reference/resolution-register.md`, every `rules/` file, the master context (version 1.4) | GTM consultant | Done 2026-10-11 |
| The member value proposition, channel engine, journey, ICP, positioning, pricing, objections, battlecards, and the density arithmetic rewritten; two reference files renamed | AMEND | `reference/` | GTM consultant | Done 2026-10-11 |
| Member templates and examples rewritten or added (the membership page, the member texts, sign-up ads, guides, the affiliate kit, member email) | AMEND | `templates/`, `examples/`, `prompts/common-tasks.md`, `ops/copy-bank.md` | GTM consultant | Done 2026-10-11 |
| Routers, adapters, and the portable control layer regenerated | AMEND | `CLAUDE.md`, `AGENTS.md`, `README.md`, `llms.txt`, `adapters/` | GTM consultant | Done 2026-10-11 |
| Sources synced; new research S75 to S94 | AMEND | `sources/raw/gtm/`, `sources/extracted/` | GTM consultant | Done 2026-10-11 |
| The GTM build repo, the Google folder, the walkthrough deck, the deck handoff | AMEND, downstream | `Fit137/SOSSMSGTMBuild`, `Saasrelaunchdev/SOSSMSGTMWalkthrough` | GTM consultant | In the same revision |
| The Miro board | AMEND, downstream | A prompt for another agent, handed to the consultant (no access from here) | GTM consultant | Handed over |

**Ledgers reviewed this snapshot:** all four `rules/` files, the master context, the resolution register, the copy bank, the decision log, the review cadence, the QA checklist.

**Items for later, recorded and not acted on here:** the contractor fee after the founding period now rests on a smaller per-job role in the economics; covered hours shorter than 24 hours meet a membership many will expect to cover any hour; the member base a zone needs before contractors see steady requests; a declined card at billing; the home purchase payment rule's edge cases for insurance agents. Each is a question to work through with the founders after the GTM is in place.

## Audit results
`tools/audit_brain.py`: 0 errors, 0 warnings. `tools/check_sos_sms.py`: 0 errors.
