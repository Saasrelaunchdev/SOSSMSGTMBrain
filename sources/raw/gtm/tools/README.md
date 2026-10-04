# Rendering tools

## The Google folder

`build_google_folder.py` builds the eleven files in `google-folder/` and runs a writing-rule audit over all of them: no dashes, no banned words, and the full name every time. It builds the six workbooks with openpyxl, from `google_folder/*.py`, then calls `build_google_docs.js` for the five documents (docx-js, from `google_folder/docs/*.js`). It also writes the pricing handoff, `gtm/pricing/pricing-handoff.md`, and the model as tables, `gtm/pricing/pricing-model.md` (copied into the walkthrough deck's `knowledge/gtm/pricing/`), from the same inputs as the pricing model (`google_folder/pricing.py`, the `A` table at the top). The pricing workbook uses live formulas and is set to recalculate on open.

```bash
python3 gtm/tools/build_google_folder.py
```

Layout and design follow `design-reference/` (layout only). Content comes from the GTM brain and the runs. Edit the builders and rebuild; never hand-edit the outputs.

## The run renders

`render.py` regenerates every XLSX and DOCX in both runs' `output/` folders from the Markdown sources. Run it from the repository root after editing any output Markdown file.

```bash
python3 gtm/tools/render.py
```

Requirements: Python with `openpyxl`, and Node with the `docx` package (docx-js) for `build_docx.js`. If `docx` is installed globally, set `NODE_PATH` to the global `node_modules` folder.

How tables map to sheets: a `<!-- sheet: Name -->` comment directly before a Markdown table sends it to that sheet. Unmarked tables go to a sheet named after the nearest heading. Some sheets are built with live formulas instead of copied values: the Phase 1 scatter chart, the Phase 5 density model (contractor side), and the Phase 9 calculators (both sides).

After rendering, recalculate the formula workbooks in LibreOffice so cached values exist for viewers that do not compute formulas.
