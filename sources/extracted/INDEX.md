# Source manifest

Every artifact the brain distills, what it settles, and where it went in the brain. Markdown files are the source of truth for both runs; the rendered XLSX and DOCX files in the build repo are generated from them. All artifacts are dated 2026-10-01 unless noted.

## Extracts (converted for reading)

| Artifact | Type | Extract | What it settles | Dated |
|---|---|---|---|---|
| Product Features Matrix, SOSSMS | csv | [product-features-matrix-sossms-sheet1.md](product-features-matrix-sossms-sheet1.md) | The founders' feature list, both sides, and Bryan's starting ratings | 2026-10-01 |
| Run 1 pricing dashboard | xlsx | [run-1-pricing-dashboard.md](run-1-pricing-dashboard.md) | Contractor take rate, late-arrival options, fee ceiling, Lead Cost Check calculator | 2026-10-01, re-extracted 2026-10-11 |
| Run 2 pricing dashboard | xlsx | [run-2-pricing-dashboard.md](run-2-pricing-dashboard.md) | Member price structure (the membership, the trip charge on use), member economics, guarantee economics, the acquisition calculator per new paid member | 2026-10-01, re-extracted 2026-10-11 after the membership revision |

## Markdown sources (`sources/raw/`)

| Artifact | What it settles | Feeds |
|---|---|---|
| `gtm/run-1-supply-contractors/GTM-BRIEF.md`, `SKILL-ADAPTATION.md`, `RESEARCH-PROMPTS.md` | Contractor inputs, claim constraints, the brief's decisions | `rules/do-not-say.md`, `ops/decisions.md` |
| `gtm/run-1-supply-contractors/output/phase-1` to `phase-9`, lead magnet, deck, run log | The contractor GTM | `reference/` contractor files, `context/` sections 6 to 15 |
| `gtm/run-2-demand-customers/` (same set) | The member GTM, revised by the membership revision on 2026-10-11 | `reference/` member files, `context/` sections 6 to 15 |
| `gtm/research/` | Competitor slates, research, 92 graded sources (S75 to S94 added 2026-10-11) | `reference/research-and-sources.md`, `reference/competitive-analysis.md` |
| `gtm/marketplace/cross-side-check.md` | The eight rows, conflicts A to H, the twelve decisions | `reference/marketplace-cross-side.md`, `ops/decisions.md` |
| `gtm/marketplace/speed-to-scale-plan.md`, `launch-sequence.md` | Growth gates, unit economics, stages | `reference/launch-and-growth.md`, `reference/pricing-and-economics.md` |
| `gtm/marketplace/marketplace_walkthrough.md` | The ten-slide marketplace summary | `context/` |
| `walkthrough/brand-book.html`, `tokens.css`, `palette-validation.md`, `brand-README.md` | Brand v1 | `reference/brand-identity.md`, `brand/logo/` |
| `walkthrough/NOTES.md`, `walkthrough-README.md`, `vercel.json` | Deck build state, the dated decision log, deploy | `reference/gtm-walkthrough-deck.md` |
| `gtm/marketplace/resolution-register.md` (2026-10-03; R50 added 2026-10-04; R51 to R64 added and R02, R30 retired 2026-10-11) | Every former unknown and founder decision, resolved: decided, planning value, counted at, merge fields | `reference/resolution-register.md`, `ops/decisions.md`, every `rules/` file |
| `gtm/pricing/pricing-model.md`, `pricing-handoff.md` (2026-10-03, rebuilt for the membership 2026-10-11) | The pricing model as tables, and its handoff | `reference/pricing-and-economics.md` |

## What the walkthrough repo added that the build repo did not have
Brand identity v1 (logo files, mark meaning, palette in twelve roles, type, motion, voice, the cover line); the built deck and its QC results; the deploy configuration; three minor spec discrepancies, all settled 2026-10-04. Everything else in the walkthrough `knowledge/` is a copy of the build repo's `gtm/`.

## Conflicts found, and how they were resolved

| Conflict | Sources | Resolution |
|---|---|---|
| Contractor lead magnet "call bookings by tier" and "an audit call" | Run 1 lead magnet spec; marketplace walkthrough slide 8 | Decision: product-led, no calls. Measure JOIN texts by tier |
| Contractor scorecard name | Run 1 Phase 1 ("After-Hours Readiness Scorecard") vs the spec ("Job Leak Scorecard") | The spec name is canonical |
| Per-brief decision numbers | Run 1 and Run 2 briefs vs the merged twelve | The merged twelve are used; crosswalk in `ops/decisions.md` |
| "Only option that pays for the visit" | Run 1 Phase 2 advantage vs warranty networks paying for dispatched visits (S20) | Scoped to lead platforms in `rules/do-not-say.md` |
| Homeowner email | Channel rule "no outbound email to homeowners" vs the readiness scorecard's opt-in sequence | Opt-in sequence allowed; cold email to homeowners refused |
| Source "SOS-caused" shorthand | Marketplace files | Written "caused by SOS SMS" in the brain |
| The demand-side model | Decision 2 as decided 2026-10-03 (a $49 SOS SMS fee per request) vs the membership revision (2026-10-11) | The membership revision governs; the per-request model stays in `ops/decisions.md` as dated history |
