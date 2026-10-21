# Run 1 log: SOS SMS supply side (contractors)

The `gtm-builder` run for the contractor side, executed 2026-10-01 against `../GTM-BRIEF.md` and `../SKILL-ADAPTATION.md`. This file records what the run assumed, so every output can be traced and every assumption can be overturned. The member-side wording was revised on 2026-10-11 (below).

## Inputs used

| Input | Value used | Status |
|---|---|---|
| Project | SOS SMS, emergency home repair dispatch by text | From the brief |
| Website | None yet | Decided: one site, the contractor page from Stage 1, then the membership page and the guides from Stage 2 (R23) |
| Category | Emergency home repair dispatch by text, two-sided marketplace | From the brief |
| Niche | Licensed, insured plumbing, HVAC, and electrical contractors who take emergency calls | Decided (decision 1, revised 2026-10-20) |
| Launch metro | The founders' home metro, one launch zone | Decided (decision 1). Research is national; local items are counted in Stage 0 (`../../research/step-0-competitor-slates.md`) |
| Competitors | C1 Angi Leads, C2 Thumbtack, C3 Google Local Services Ads, C4 Service Direct, C5 home warranty network (American Home Shield), C6 status quo (word of mouth and own free listing) | Step 0, filled in `../../research/` |
| Features | The six contractor items from the matrix plus three candidates | From the brief, Section 3 |
| Business context | Two founders, Bryan and Ali, as supply lead and demand lead; at least 18 months of runway required; no channels tried, pre-launch | Resolved 2026-10-03 (R25, R35, R48) |

## Assumptions the run applied, with the decision each one stands in for

| Brief decision | Assumption used in this run, and the decision of 2026-10-03 | Where it matters |
|---|---|---|
| 1. Launch metro and trades | Plumbing, HVAC, and electrical emergencies (revised 2026-10-20). Decided: one launch zone in the founders' home metro | Phases 2, 4, 5.2, 8 |
| 2. How SOS SMS earns money | Decided, revised 2026-10-11: members' monthly or annual membership; $25 per completed paid job from each contractor's first job | Phase 9, every "no lead fees" line |
| 3. Late arrival and the contractor's trip charge | Revised 2026-10-20 (option D): a late arrival keeps the trip charge; a no-show is paid nothing; two in 90 days pause requests (R67). The copy that depended on it carries the decided words | Phases 6, 9 |
| 4. Dispatch rule | Every matched contractor sees the request at once; the first to accept gets it (decision 4) | Phases 1, 3, 6, 7 |
| 5. Build status | Every item treated as planned, not shipped. Copy is written for launch day and must not run before the item ships | Phases 1, 6 |
| 6. Founder memo, unattributed rows | Not available. Ali's 18 rows and Bryan's 5 rated rows with no item text are excluded for good | Phase 1 |
| 7. Name collision | Decided: a US trademark search and a search check in the zone in Stage 0 (decision 10) | Phase 8 |

## Rules carried through every phase

- SOS SMS is pre-launch. No proof point, count, rate, or result exists, and none is invented: each unknown carries a planning value with its basis, or the method that will count it (`../../marketplace/resolution-register.md`). The eighteen Phase 6 proof fields are method lines and named records, by design.
- Market figures carry a source ID and grade from `../../research/SOURCES.md`. Grade C figures are for internal direction only.
- Claims follow `../GTM-BRIEF.md` Section 5 (the narrowed forms) and Section 6 (cross-side dependencies).
- No em dashes. None of the banned words.

## Revision: product-led motion (2026-10-01)

The founders changed the motion after the first run: product-led growth, no sales team. On the contractor side that means cold email and a partnership program, with every contractor signing themselves up by text. No calls, shop visits, or audits.

| File | What changed |
|---|---|
| `../GTM-BRIEF.md`, `../SKILL-ADAPTATION.md` | Motion row and Phase 8 adaptation |
| `phase-1-product-feature-matrix.md` | The white-glove audit variant replaced by an automated lead spend report; top-of-funnel uses now email and partners |
| `phase-4-icp.md` | Best engagement model is self-serve for both levels |
| `phase-5-buying-committee.md` | Channels to find each persona: cold email, partners, referrals |
| `phase-6-value-proposition.md` | Proof capture by automated text |
| `phase-7-customer-journey.md` | Every touchpoint self-serve |
| `phase-8-assets-library.md` | Rewritten: cold email, partnership program, in-product referral loop, with draft email copy |
| `phase-9-pricing.md` | A per-completed-job contractor fee is planned from the start, because paid search on the customer side is unlikely to be paid back by a customer fee alone (since 2026-10-11 it applies from each contractor's first job) |
| `lead-magnet-spec.md`, `gtm_walkthrough.md` | Self-serve calls to action; channel slide |

Growth across zones follows `../../marketplace/speed-to-scale-plan.md`.

## Revision: the membership model (2026-10-11)

The membership revision, 2026-10-11, changed the demand side: homeowners join SOS SMS as members, monthly or annually, before anything breaks, and in an emergency a member sends one text. On the contractor side, free to join, $0 per request, the trip charge collected before you roll, the density gate, and the channels did not change. Two contractor terms did: the founding terms are retired, so the $25 contractor fee applies from every contractor's first completed paid job, on the same terms for everyone, and the founding list and its deadline are gone. What else changed here is every line that describes the other side, and the opening gate: a zone opens to members only when every hour band meets the density number.

| File | What changed |
|---|---|
| `../GTM-BRIEF.md` | Classification and Section 6 copied from Run 2, identical; the shared project information; the revenue sentence; the guarantee clock from the member's request text; "member" for the homeowner, "your customers" for a contractor's own clients |
| `../README.md`, `../SKILL-ADAPTATION.md`, `../RESEARCH-PROMPTS.md` | The model description names the membership |
| `phase-2-positioning-summary.md`, `phase-3-positioning-statements.md`, `phase-5-buying-committee.md`, `phase-7-customer-journey.md` | Member-side wording; memberships open only at the density number, with the launch list growing in parallel |
| `phase-6-value-proposition.md` | VP1's revenue sentence; VP2 and drills 4, 6, and 7: the trip charge goes on the member's card when you accept, agreed when they joined; drill 9 and the cross-side check |
| `phase-8-assets-library.md` | Cold emails 1 to 4: the revenue sentence, how a job works, the terms, and the zone opening to members |
| `phase-9-pricing.md` | The take rate: the membership replaces the per-request SOS SMS fee; the late-arrival options and the guarantee wording; decision 1 |
| `gtm_walkthrough.md` | Memberships open only at density; the member guarantee |

## Revision: three trades and the late-arrival rule (2026-10-20)

The tiers revision, 2026-10-20. Contractors are recruited in three trades from the launch zone, 9 per trade, 27 in all; a shop licensed in more than one trade counts in each. The $99 trip charge and the $25 contractor fee are the same in each trade. A late arrival keeps the trip charge; a no-show is paid nothing; two in 90 days pause requests until a person reviews them. Members choose Basic, Plus, or Premier, and SOS SMS pays the guarantee's credit on Plus and Premier. No paid search at launch.

| File | What changed |
|---|---|
| `phase-2-competitive-analysis.md`, `phase-2-positioning-summary.md`, `phase-3-positioning-statements.md` | SOS SMS's description, who it is for, and the positioning line name the three trades |
| `phase-4-icp.md`, `phase-5-buying-committee.md` | Three trades in the segment, sub-industries, and licenses; 27 places in the first cohort; the trade associations as channels |
| `phase-6-value-proposition.md` | Drill 4 releases the trip charge on arrival; the late-arrival rule in the terms |
| `phase-7-customer-journey.md`, `phase-8-assets-library.md` | Cross-trade referral; the zone list and cold email 3 and 4 for three trades and the new rule |
| `phase-9-pricing.md` | Option D decided; the take rate with the plans; HVAC and electrical lead costs in Anchors 2 and 3 |
| `gtm_walkthrough.md` | Three trades, 27 contractors, and the new rule |

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

The Markdown files are the source of truth. The XLSX and DOCX files are generated from them by `gtm/tools/render.py` and should not be edited by hand.

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
