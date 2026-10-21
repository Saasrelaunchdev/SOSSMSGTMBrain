# Asset index

Where the sources and surfaces live. An amendment consults this file to find every place carrying an old claim, so keep it current.

## Repositories

| Repository | What it holds | Role |
|---|---|---|
| `Saasrelaunchdev/SOSSMSGTMBrain` (this one) | The brain | Source of truth for GTM work |
| `Fit137/SOSSMSGTMBuild`, folder `gtm/` | Both `gtm-builder` runs, research, marketplace synthesis, the older rendered XLSX and DOCX dashboards, `tools/render.py`, and the Google folder builders | Origin of the strategy. Markdown is the source of truth there; rendered files are generated |
| `Fit137/SOSSMSGTMBuild`, folder `google-folder/` | The Google folder set, rebuilt 2026-10-03, for the membership revision on 2026-10-11, and for the tiers and pricing revisions on 2026-10-21: six workbooks (product feature matrix, competitive market analysis, ICP dashboard, customer journey funnel, marketing assets library, pricing model) and five documents (positioning verdict, value proposition frameworks for members and contractors, the early adopters survey, the State of After-Hours Plumbing build doc). The pricing model (`SOS_SMS_Pricing_Model.xlsx`) carries decisions 2, 3, 5, and 12: every input on its first sheet, "Founder Inputs" (the plan prices, credit months, phones, plan mix, costs, churn, the trade table), and every other sheet follows it by formula, colour-coded, with a Checks sheet; its handoff is `gtm/pricing/pricing-handoff.md`. Every file resolved 2026-10-04 | Generated from this brain by `gtm/tools/build_google_folder.py`. When a claim changes here, rebuild them; never hand-edit |
| `Fit137/SOSSMSGTMBuild`, folder `design-reference/` | Another company's files (Baseout), kept as the layout and design reference for the Google folder | Layout and design only. Never a source of content, facts, or research for SOS SMS |
| `Fit137/SOSSMSGTMBuild`, folder `deck-handoff/` | The deck content spec, design spec, build prompt, QC tools | Origin of the walkthrough deck |
| `Saasrelaunchdev/SOSSMSGTMWalkthrough` | The built deck (`dist/`: a 27-slide hub, the 25 specified slides plus two side hubs, and 22 dashboards; the pricing for both sides on hub slide 25 and M3, from `knowledge/gtm/pricing/`; redrawn for the membership revision on 2026-10-11, and for three trades, three plans, the late-arrival credit, and no paid search on 2026-10-21), brand v1 (`brand/`), `NOTES.md`, the register copy `knowledge/gtm/marketplace/resolution-register.md` | Internal presentation and brand files. When the pricing model changes, rebuild it in the GTM build repo, copy `gtm/pricing/pricing-model.md` into the deck's `knowledge/gtm/pricing/`, and regenerate the pricing slide and M3 |

## Source deliverables, copied into `sources/`

| Artifact | Type | What it settles | Dated | Location here |
|---|---|---|---|---|
| Product Features Matrix, SOSSMS | CSV | The founders' feature list and Bryan's ratings | 2026-10-01 | `sources/raw/`, extract in `sources/extracted/` |
| Run 1 (contractors), nine phases, lead magnet, deck | Markdown | Contractor ICP, positioning, value proposition, journey, channels, pricing | 2026-10-01, product-led revision; member wording 2026-10-11; three trades and no founding period 2026-10-20 | `sources/raw/gtm/run-1-supply-contractors/` |
| Run 2 (members), nine phases, lead magnet, deck | Markdown | Member ICP, positioning, value proposition, journey, channels, pricing | 2026-10-01; the membership revision 2026-10-11; the tiers and pricing revisions 2026-10-20 and 2026-10-21 | `sources/raw/gtm/run-2-demand-customers/` |
| Research and source register (S01 to S100) | Markdown | Every market figure and its grade | 2026-10-01; the member slate and S75 to S94 added 2026-10-11; HVAC and electrical, S95 to S100, added 2026-10-20 | `sources/raw/gtm/research/` |
| Marketplace synthesis | Markdown | Cross-side check, twelve decisions, the resolution register, speed to scale, launch sequence | 2026-10-01; revised 2026-10-11, 2026-10-20, and 2026-10-21 | `sources/raw/gtm/marketplace/` |
| Pricing model as tables, and its handoff | Markdown | The three plans and the contractor pricing, member economics by plan, the miss cases, acquisition | 2026-10-03; revised 2026-10-11 and 2026-10-21 | `sources/raw/gtm/pricing/` |
| Pricing dashboards | XLSX extract | Calculators, both sides | 2026-10-01; the run 2 extract regenerated 2026-10-11 | `sources/extracted/run-*-pricing-dashboard.md` |
| Walkthrough deltas | Markdown, HTML, CSS | Brand book, tokens, palette record, build notes | 2026-10-04 | `sources/raw/walkthrough/` |

Manifest with every file and what it feeds: `sources/extracted/INDEX.md`.

## Brand
Logo SVGs: `brand/logo/` (copied from the walkthrough repo). PNG exports, the embedded font, and the build tools stay in the walkthrough repo `brand/`.

## Live surfaces
None. SOS SMS is pre-launch: no website, no ads, no number, no listings. Add each surface here, with its URL and last review date, the day it goes live.

| Surface | URL | Last reviewed |
|---|---|---|
| Walkthrough deck (internal, Vercel) | Assigned by Vercel on the first deploy and recorded here then, with Deployment Protection on | 2026-10-04 |
| GTM engine board (internal, Miro): on top, frames 0.1 to 0.6 explain the work done and the four deliverables (the Google folder, this brain, the walkthrough, the board) and which one to open; below, both channel engines, the density gate, guardrails and decisions, with flowcharts A to H. Stale since 2026-10-04, and again since the membership revision (2026-10-11) and the tiers and pricing revisions (2026-10-20, 2026-10-21): its decision frames and every member-side frame predate them. A frame-by-frame update prompt (`Fit137/SOSSMSGTMBuild`, `handover/miro-board-membership-revision.md`, extended 2026-10-21 for the three trades and the three plans) is with the GTM consultant, to apply with board access | https://miro.com/app/board/uXjVEfcEtLg=/ | 2026-10-03 |

## Related workstreams that own deferred questions
Founders: the twelve decisions, the plan prices and the pricing workbook's inputs, dispute rules, roles. GTM consultant: the brain itself, its reviews, and drafts for approval. Product: build status, dispatch, payments, membership billing, verification. Counsel: the terms on one page, the member terms and automatic renewal disclosures, the affiliate terms, the guarantee, the privacy policy. Payment provider: saved cards and recurring billing, hold, capture, payout timing.
