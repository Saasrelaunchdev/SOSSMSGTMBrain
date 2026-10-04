# SOS SMS · GTM walkthrough

An interactive deck suite for the SOS SMS go-to-market: a 25-slide hub and 22 linked dashboards, built as one self-contained HTML file. Pricing appears once for both sides: slide 23 and dashboard M3, from `knowledge/gtm/pricing/`. Internal: it carries grade C figures. Every former unknown and the twelve launch decisions are resolved (`knowledge/gtm/marketplace/resolution-register.md`, 2026-10-03).

Start with `CLAUDE.md` (the operating manual), then `specs/03_build_prompt.md`.

| Path | What it is |
|---|---|
| `specs/` | What to build: content, design, build prompt. Read-only |
| `knowledge/` | What is true: both GTM runs, the marketplace synthesis, the research. Read-only. Start at `knowledge/README.md` |
| `reference/` | Where the structure came from. Read-only |
| `brand/` | The brand: logo files, the embedded typeface, the palette record, and `brand-book.html` |
| `src/` | The deck source: `index.html` (hub), `dashboards/`, `styles/`, `scripts/`, `data/notes.json` |
| `tools/` | Build, QC, and helpers |
| `dist/` | The built deck. `dist/index.html` is what Vercel serves; `dist/sos-sms-gtm.html` is the same file |
| `qa/` | Screenshots used to check the work (`qa/final/`: contact sheets of every slide, the print paths, dashboard pages) |
| `NOTES.md` | The dated log: decisions, discrepancies, and questions, each with its status |

## Build and check

```bash
python3 tools/gen_content.py                        # specs/01 -> src/index.html: every slide's text, verbatim
python3 tools/gen_dash.py                           # specs/01 + knowledge/ -> src/dashboards/*.html (recipes in tools/dash_*.py)
python3 tools/build.py                              # src/ -> dist/index.html (one file, no network requests)
python3 tools/check_deck.py dist/index.html         # QC: 0 errors before every push
NODE_PATH=$(npm root -g) node tools/qa/nav_test.mjs # every route, key, gesture, and history rule, in Chromium
NODE_PATH=$(npm root -g) node tools/qa/slides.mjs "$PWD/dist/index.html" qa/hub light r   # every slide, reduced motion
NODE_PATH=$(npm root -g) node tools/qa/dashboards.mjs "$PWD/dist/index.html" qa/dash S01,M1   # whole dashboards, in chunks
NODE_PATH=$(npm root -g) node tools/qa/print.mjs "$PWD/dist/index.html" qa/hub.pdf "#/deck/3"  # the print path
NODE_PATH=$(npm root -g) node tools/qa/perf.mjs "$PWD/dist/index.html"                    # time to interactive, frame rate
python3 tools/extract_notes.py                      # presenter notes from specs/01, verbatim
python3 tools/resolved_check.py                     # fails on any unresolved placeholder in knowledge, specs, src, dist
python3 brand/tools/build_book.py                   # brand/brand-book.html
```

## Deploy on Vercel

`vercel.json` serves `dist/` only, so the specs and knowledge files are never published. Import the repository in Vercel with no framework preset; the build step is a no-op because `dist/index.html` is committed. The deck is internal: turn on Vercel Deployment Protection before sharing the URL.
