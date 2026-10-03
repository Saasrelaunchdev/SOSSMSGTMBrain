# Asset index

Where the sources and surfaces live. An amendment consults this file to find every place carrying an old claim, so keep it current.

## Repositories

| Repository | What it holds | Role |
|---|---|---|
| `Saasrelaunchdev/SOSSMSGTMBrain` (this one) | The brain | Source of truth for GTM work |
| `Fit137/SOSSMSGTMBuild`, folder `gtm/` | Both `gtm-builder` runs, research, marketplace synthesis, the older rendered XLSX and DOCX dashboards, `tools/render.py`, and the Google folder builders | Origin of the strategy. Markdown is the source of truth there; rendered files are generated |
| `Fit137/SOSSMSGTMBuild`, folder `google-folder/` | The Google folder set, rebuilt 2026-10-03: six workbooks (product feature matrix, competitive market analysis, ICP dashboard, customer journey funnel, marketing assets library, pricing model) and five documents (positioning verdict, value proposition frameworks for customers and contractors, the founding contractor survey, the State of After-Hours Plumbing build doc). The pricing model is proposed, not decided; its handoff is `gtm/pricing/pricing-handoff.md` | Generated from this brain by `gtm/tools/build_google_folder.py`. When a claim changes here, rebuild them; never hand-edit |
| `Fit137/SOSSMSGTMBuild`, folder `design-reference/` | Another company's files (Baseout), kept as the layout and design reference for the Google folder | Layout and design only. Never a source of content, facts, or research for SOS SMS |
| `Fit137/SOSSMSGTMBuild`, folder `deck-handoff/` | The deck content spec, design spec, build prompt, QC tools | Origin of the walkthrough deck |
| `Saasrelaunchdev/SOSSMSGTMWalkthrough` | The built deck (`dist/`: 25 slides, 22 dashboards; the pricing for both sides on slide 23 and M3, from `knowledge/gtm/pricing/`), brand v1 (`brand/`), `NOTES.md`, `knowledge/TBD-REGISTER.md` | Internal presentation and brand files. When the pricing model changes, rebuild it in the GTM build repo, copy `gtm/pricing/pricing-model.md` into the deck's `knowledge/gtm/pricing/`, and regenerate slide 23 and M3 |

## Source deliverables, copied into `sources/`

| Artifact | Type | What it settles | Dated | Location here |
|---|---|---|---|---|
| Product Features Matrix, SOSSMS | CSV | The founders' feature list and Bryan's ratings | 2026-10-01 | `sources/raw/`, extract in `sources/extracted/` |
| Run 1 (contractors), nine phases, lead magnet, deck | Markdown | Contractor ICP, positioning, value proposition, journey, channels, pricing | 2026-10-01, product-led revision | `sources/raw/gtm/run-1-supply-contractors/` |
| Run 2 (customers), nine phases, lead magnet, deck | Markdown | Customer ICP, positioning, value proposition, journey, channels, pricing | 2026-10-01, product-led revision | `sources/raw/gtm/run-2-demand-customers/` |
| Research and source register (S01 to S74) | Markdown | Every market figure and its grade | 2026-10-01 | `sources/raw/gtm/research/` |
| Marketplace synthesis | Markdown | Cross-side check, twelve decisions, speed to scale, launch sequence | 2026-10-01 | `sources/raw/gtm/marketplace/` |
| Pricing dashboards | XLSX extract | Calculators, both sides | 2026-10-01 | `sources/extracted/run-*-pricing-dashboard.md` |
| Walkthrough deltas | Markdown, HTML, CSS | Brand book, tokens, palette record, build notes, TBD register | 2026-10-01 | `sources/raw/walkthrough/` |

Manifest with every file and what it feeds: `sources/extracted/INDEX.md`.

## Brand
Logo SVGs: `brand/logo/` (copied from the walkthrough repo). PNG exports, the embedded font, and the build tools stay in the walkthrough repo `brand/`.

## Live surfaces
None. SOS SMS is pre-launch: no website, no ads, no number, no listings. Add each surface here, with its URL and last review date, the day it goes live.

| Surface | URL | Last reviewed |
|---|---|---|
| Walkthrough deck (internal, Vercel) | {TBD}, protect before sharing | 2026-10-01 |
| GTM engine board (internal, Miro): on top, frames 0.1 to 0.6 explain the work done and the four deliverables (the Google folder, this brain, the walkthrough, the board) and which one to open; below, both channel engines, the density gate, guardrails and decisions, with flowcharts A to H | https://miro.com/app/board/uXjVEfcEtLg=/ | 2026-10-03 |

## Related workstreams that own deferred questions
Founders: the twelve decisions, dispute rules, roles. GTM consultant: the brain itself, its reviews, and drafts for approval. Product: build status, dispatch, payments, verification. Counsel: terms, guarantee, privacy policy. Payment provider: hold, capture, payout timing.
