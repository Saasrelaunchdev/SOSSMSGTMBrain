# Run 2 log: SOS SMS demand side (customers)

The `gtm-builder` run for the customer side, executed 2026-10-01 against `../GTM-BRIEF.md` and `../SKILL-ADAPTATION.md`, after Run 1. This file records what the run assumed.

## Inputs used

| Input | Value used | Status |
|---|---|---|
| Project | SOS SMS, emergency home repair dispatch by text | From the brief |
| Website | None yet | Decided: the zone landing page, the guarantee page, and the first five problem guides from Stage 2 (R23) |
| Category | Emergency home repair dispatch by text, two-sided marketplace | From the brief |
| Audience | Homeowners with an urgent repair problem at home | Decided (brief decision 1) |
| Niche | Plumbing and water emergencies, inside Run 1's founding contractor zone | Decided (decision 1) |
| Launch metro and zone | One founding zone, a 10-mile radius around the founding contractors' shops, in the founders' home metro | Decided (decision 1); drawn in Stage 0 |
| Competitors | D1 Google search and call down the list, D2 Roto-Rooter, D3 Benjamin Franklin Plumbing, D4 Angi, D5 Thumbtack, D6 American Home Shield | Step 0, filled in `../../research/` |
| Features | The nine customer items from the matrix plus three candidates | From the brief, Section 3 |
| Business context | Two founders, Bryan and Ali, as supply lead and demand lead; at least 18 months of runway required; no channels tried, pre-launch | Resolved 2026-10-03 (R25, R35, R48) |

## Assumptions the run applied

| Brief decision | Assumption used, and the decision of 2026-10-03 | Where it matters |
|---|---|---|
| 1. Who the demand side is | Homeowners. Renters and landlords noted where they differ; property managers excluded (a possible third run) | Phases 4, 5 |
| 2. Launch metro and trades | Plumbing and water emergencies. Decided: one founding zone in the founders' home metro | Phases 2, 4, 8 |
| 3. Customer price | Decided: a $99 trip charge set by SOS SMS, credited to the repair, and a $49 SOS SMS fee per dispatched request | Phases 6, 9 |
| 4. 90-minute guarantee scope | Decided: 90 minutes from the confirming text; the $99 trip charge back, automatically; covered areas and hours from the zone record; no charge when no one accepts. Fault-based late-arrival rule | Phases 3, 6, 7, 9 |
| 5. Build status | Every item treated as planned. The relaunch guarantee is excluded from copy | Phases 1, 6 |
| 6. Customer data and marketing texts | Address and job details go to the accepting contractor only; no marketing texts without separate opt-in (decided) | Phases 3, 6, 8 |
| 7. Name collision | Decided: a US trademark search and a search check in the zone in Stage 0; no bids on "SOS plumbing" (decision 10) | Phase 8 |

## Rules carried through every phase

- Pre-launch: no proof point, count, arrival time, or result exists, and none is invented; each unknown carries a planning value with its basis, or the method that will count it (`../../marketplace/resolution-register.md`). No average arrival time and no count of homes helped, anywhere.
- Any line that invites an urgent text carries the safety line: for fire, a gas smell, or anyone hurt, call 911 first. Gas utilities say to leave the building and call from a safe distance, without using phones near a leak (S60).
- Market figures carry a source ID and grade from `../../research/SOURCES.md`.
- Claims follow `../GTM-BRIEF.md` Sections 5 and 6. No em dashes, none of the banned words.

## Revision: product-led motion (2026-10-01)

The founders changed the motion after the first run: product-led growth, no sales team, no outreach. Customers are met where they are already trying to solve the problem: bottom-of-funnel search ads (Google, then Microsoft) and problem-solving pages. The product converts them, starting with stop-the-water help in the first reply, and the product loops bring them back.

| File | What changed |
|---|---|
| `../GTM-BRIEF.md`, `../SKILL-ADAPTATION.md` | Motion row; Phase 8 adaptation; new decision 8, paid search eligibility (decided: decision 11 in the merged list) |
| `phase-1-product-feature-matrix.md` | Demand driver is now the stop-the-water first reply; partner-distributed variants dropped |
| `phase-4-icp.md`, `phase-5-buying-committee.md` | Engagement model and channels: search at the moment of need, then the saved number |
| `phase-6-value-proposition.md` | Drill 1 call to action for in-the-moment traffic |
| `phase-7-customer-journey.md` | Stages 1 and 2 rebuilt around paid search and problem pages; new accelerators |
| `phase-8-assets-library.md` | Rewritten: paid search, problem-solving pages, product loops, with search ad drafts and policy rules |
| `phase-9-pricing.md` | New paid acquisition economics, with a live calculator; decisions updated |
| `lead-magnet-spec.md`, `gtm_walkthrough.md` | Lead magnet placed in Channel 2; channel and pricing slides |

Growth across zones follows `../../marketplace/speed-to-scale-plan.md`.

## Output files

| Phase | Source file (Markdown) | Rendered file |
|---|---|---|
| 1. Product Feature Matrix | `phase-1-product-feature-matrix.md` | `product_feature_matrix.xlsx` |
| 2. Competitive Market Analysis | `phase-2-competitive-analysis.md`, `phase-2-positioning-summary.md` | `competitive_analysis.xlsx`, `positioning_summary.docx` |
| 3. Positioning | `phase-3-positioning-statements.md` | `positioning_statements.docx` |
| 4. ICP | `phase-4-icp.md` | `icp_dashboard.xlsx` |
| 5. Buying Committee | `phase-5-buying-committee.md` | `buying_committee.xlsx` |
| 6. Value Proposition | `phase-6-value-proposition.md` | `value_proposition.docx` |
| 7. Customer Journey | `phase-7-customer-journey.md` | `customer_journey.xlsx` |
| 8. Assets and Collaterals | `phase-8-assets-library.md` | `assets_library.xlsx` |
| 9. Pricing and Packaging | `phase-9-pricing.md` | `pricing_dashboard.xlsx` |
| Lead Magnet | `lead-magnet-spec.md` | `lead_magnet_spec.xlsx`, `scorecard_spec.docx` |
| Deck | `gtm_walkthrough.md` | Markdown for Gamma |

The Markdown files are the source of truth; `gtm/tools/render.py` generates the XLSX and DOCX files.

## Progress tracker

- [x] Step 0, competitor slate (research folder)
- [x] Phase 1, Steps 1.1 to 1.7
- [x] Phase 2, Steps 2.1 to 2.16
- [x] Phase 3, Step 3.1
- [x] Phase 4, Step 4.1
- [x] Phase 5, Steps 5.1 and 5.2
- [x] Phase 6, Steps 6.1 to 6.3
- [x] Phase 7, Steps 7.1 and 7.2
- [x] Phase 8, Step 8.1
- [x] Phase 9, Steps 9.1 to 9.3
- [x] Lead Magnet Specification
- [x] 10-slide GTM Walkthrough Deck
- [x] Cross-side check against Section 6 (in `../../marketplace/`)
