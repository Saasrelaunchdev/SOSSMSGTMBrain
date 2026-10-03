# Rendering tools

`render.py` regenerates every XLSX and DOCX in both runs' `output/` folders from the Markdown sources. Run it from the repository root after editing any output Markdown file.

```bash
python3 gtm/tools/render.py
```

Requirements: Python with `openpyxl`, and Node with the `docx` package (docx-js) for `build_docx.js`. If `docx` is installed globally, set `NODE_PATH` to the global `node_modules` folder.

How tables map to sheets: a `<!-- sheet: Name -->` comment directly before a Markdown table sends it to that sheet. Unmarked tables go to a sheet named after the nearest heading. Some sheets are built with live formulas instead of copied values: the Phase 1 scatter chart, the Phase 5 density model (contractor side), and the Phase 9 calculators (both sides).

After rendering, recalculate the formula workbooks in LibreOffice so cached values exist for viewers that do not compute formulas.
