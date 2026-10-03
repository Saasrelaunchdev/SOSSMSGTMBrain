# brand/

The SOS SMS brand: green and white. Open `brand-book.html` for the full guide (meaning, mark, logo use, colour, type, shape, motion, voice).

| Path | What it is |
|---|---|
| `brand-book.html` | The brand book, one self-contained file. Built from `src/brand-book.html` |
| `logo/*.svg` | Every lockup, the mark, the favicon, the app icon. The SVGs are the source of truth |
| `logo/png/` | PNG exports for places that cannot take SVG |
| `fonts/Inter-SOS-subset.woff2` | Inter (SIL Open Font License, `fonts/OFL.txt`), subset to the characters the suite uses, weights 400 to 700, tabular figures limited to digits |
| `palette-validation.md` | How the colour roles were searched and checked, in both themes |
| `tools/` | Regenerate everything from source |

```bash
python3 brand/tools/make_logo.py                         # logo/*.svg (needs fonttools, uharfbuzz)
NODE_PATH=$(npm root -g) node brand/tools/export_png.mjs # logo/png/
python3 brand/tools/make_font.py <InterVariable.woff2>   # fonts/Inter-SOS-subset.woff2 (see the script's header)
python3 brand/tools/build_book.py                        # brand-book.html
```

The colour roles themselves live in `src/styles/tokens.css`; the brand book reads them from there, so the book and the deck cannot disagree.
