# Asset index

Where the sources and surfaces live. An amendment consults this file to find every place carrying an old claim, so keep it current.

## Repositories

| Repository | What it holds | Role |
|---|---|---|
| `Saasrelaunchdev/SOSSMSGTMBrain` (this one) | The brain | Source of truth for GTM work |
| `Fit137/SOSSMSGTMBuild`, folder `gtm/` | Both `gtm-builder` runs, research, marketplace synthesis, rendered XLSX and DOCX dashboards, `tools/render.py` | Origin of the strategy. Markdown is the source of truth there; rendered files are generated |
| `Fit137/SOSSMSGTMBuild`, folder `deck-handoff/` | The deck content spec, design spec, build prompt, QC tools | Origin of the walkthrough deck |
| `Saasrelaunchdev/SOSSMSGTMWalkthrough` | The built deck (`dist/`), brand v1 (`brand/`), `NOTES.md`, `knowledge/TBD-REGISTER.md` | Internal presentation and brand files |

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

## Related workstreams that own deferred questions
Founders: the twelve decisions, dispute rules, roles. GTM consultant: the brain itself, its reviews, and drafts for approval. Product: build status, dispatch, payments, verification. Counsel: terms, guarantee, privacy policy. Payment provider: hold, capture, payout timing.
