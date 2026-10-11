# Run 2 log: SOS SMS demand side (members)

The `gtm-builder` run for the demand side, executed 2026-10-01 against `../GTM-BRIEF.md` and `../SKILL-ADAPTATION.md`, after Run 1, and revised by the membership revision on 2026-10-11 (below). This file records what the run assumed. The folder keeps its name, `run-2-demand-customers`, so every link resolves.

## Inputs used

| Input | Value used | Status |
|---|---|---|
| Project | SOS SMS, an emergency home repair membership by text | From the brief; the membership revision, 2026-10-11 |
| Website | None yet | Decided: the readiness scorecard and the launch list from Stage 1; the membership page (with a ZIP check), the guarantee page, and five problem and prevention guides from Stage 2 (R23) |
| Category | Emergency home repair membership, by text; a local two-sided network | From the brief |
| Audience | Homeowners who want to be ready before something breaks, in open zones | Decided (brief decisions 1 and 9) |
| Niche | Plumbing and water emergencies, inside Run 1's founding contractor zone | Decided (decision 1) |
| Launch metro and zone | One founding zone, a 10-mile radius around the founding contractors' shops, in the founders' home metro | Decided (decision 1); drawn in Stage 0 |
| Competitors | D1 Search and call when it happens, D2 plumber club memberships, D3 home warranties, D4 utility-partner plumbing plans, D5 Frontdoor, D6 on-demand marketplaces | Step 0, member slate (2026-10-11), filled in `../../research/` |
| Features | The nine demand-side items from the matrix, three candidates, and three membership items | From the brief, Section 3 |
| Business context | Two founders, Bryan and Ali, as supply lead and demand lead; at least 18 months of runway required; no channels tried, pre-launch | Resolved 2026-10-03 (R25, R35, R48) |

## Assumptions the run applied

| Brief decision | Assumption used, and the decision of 2026-10-03 | Where it matters |
|---|---|---|
| 1. Who the demand side is | Homeowners. Renters and landlords noted where they differ; property managers excluded (a possible third run) | Phases 4, 5 |
| 2. Launch metro and trades | Plumbing and water emergencies. Decided: one founding zone in the founders' home metro | Phases 2, 4, 8 |
| 3. Member price | Revised 2026-10-11: a monthly or annual membership, planning values $10 a month or $100 a year (R51, R52), shown as `{{monthly price}}` and `{{annual price}}`; the $99 trip charge on use, set by SOS SMS, credited to the repair; no fee per request | Phases 6, 9 |
| 4. 90-minute guarantee scope | Revised 2026-10-11: 90 minutes from the member's request text; the $99 trip charge back, automatically; covered areas and hours from the zone record; no charge when no one accepts. Fault-based late-arrival rule | Phases 3, 6, 7, 9 |
| 5. Build status | Every item treated as planned. The relaunch guarantee is excluded from copy | Phases 1, 6 |
| 6. Member data, marketing texts, and email | The address on file and job details go to the accepting contractor only; no marketing texts without separate written opt-in; email follows CAN-SPAM (decided) | Phases 3, 6, 8 |
| 7. Name collision | Decided: a US trademark search and a search check in the zone in Stage 0; no bids on "SOS plumbing" (decision 10) | Phase 8 |
| 8. Paid search | Revised 2026-10-11: sells memberships before the need, never dispatch during an emergency; standard search ads after Google's written confirmation; never Local Services Ads (decision 11) | Phase 8 |
| 9. The demand-side product | Decided 2026-10-11, the membership revision: a monthly or annual membership, joined before the need; one text starts dispatch; affiliates and email lead | Every phase |

## Rules carried through every phase

- Pre-launch: no proof point, count, arrival time, or result exists, and none is invented; each unknown carries a planning value with its basis, or the method that will count it (`../../marketplace/resolution-register.md`). No average arrival time and no count of members or homes helped, anywhere.
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

## Revision: the membership model (2026-10-11)

The membership revision, 2026-10-11. The demand side is a monthly or annual membership, joined before anything breaks, with the card and home address on file. In an emergency a member sends one text and help is on the way: no search, no sign-up, no payment entry, nothing to confirm. Speed is the point, and membership is what makes it possible. It also opens lower-cost channels that only work before the need: affiliates and email lead, and search and social sell sign-ups in open zones. A homeowner searching mid-emergency is not the target: at that moment, calling a contractor from the results is the faster route. The contractor side is unchanged.

| File | What changed |
|---|---|
| `../GTM-BRIEF.md`, `../SKILL-ADAPTATION.md`, `../RESEARCH-PROMPTS.md`, `../README.md` | Rewritten for members: the membership, the member slate, the member features, decisions 3, 4, 8, and 9, the pre-need channels, the member research prompts first |
| `../../research/` | Sources S75 to S94; the member slate in Step 0; member research in `demand-research.md`, with the pay per request research kept below it |
| `phase-1-product-feature-matrix.md` | Three membership items (13 to 15); one text starts dispatch is the lead; the readiness check is the demand driver |
| `phase-2-competitive-analysis.md`, `phase-2-positioning-summary.md` | Member slate D1 to D6, vectors V1 to V4, features F1 to F16, the summary rewritten |
| `phase-3-positioning-statements.md` | Statements against doing nothing, plumber clubs, and warranties and plans; the one line; what not to claim |
| `phase-4-icp.md`, `phase-5-buying-committee.md` | New homeowners and established homeowners, reached before the need; a household deciding over days; the founding member area and zone sizing |
| `phase-6-value-proposition.md` | Brand promise "One text, and help is on the way."; VP1 one text, VP2 ready before it happens, VP3 know the cost and who is coming; nine member drills |
| `phase-7-customer-journey.md` | Two clocks, weeks before and minutes during; renewal as Stage 7; new blockers and accelerators |
| `phase-8-assets-library.md` | Affiliates, email, and search and SEO pages for sign-ups, plus member loops; rules for each channel; sign-up ad drafts |
| `phase-9-pricing.md` | The membership as the value metric; packaging; guarantee economics per member; acquisition economics per member and the ceiling; anchors; decisions |
| `lead-magnet-spec.md`, `gtm_walkthrough.md` | The scorecard ends at the ZIP check (join, launch list, or the plan alone); the deck rewritten for members |

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
