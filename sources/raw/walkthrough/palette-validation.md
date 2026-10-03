# Palette validation

How the semantic-role mapping in `src/styles/tokens.css` was chosen and checked, 2026-10-01. Colours were searched, not picked by eye: a grid over OKLCH lightness, chroma, and hue for each signal role, scored with the data-visualisation validator (Machado 2009 CVD simulation, OKLab ΔE × 100), with every role kept at or above its contrast floor.

## The five signal roles appear side by side, so they are tested all-pairs

| Role | Light | Dark | Job |
|---|---|---|---|
| accent | `#28a43a` Signal green | `#3eee92` | The one emissive signal: the lit return, the accent phrase, focus, the lead item |
| positive | `#007452` | `#249c74` | Money arriving where promised, kept promises, ✓ |
| supply | `#0057b1` | `#47b5fa` | Contractors. Always with a square mark |
| demand | `#a366cd` | `#a86fcf` | Customers. Always with a round mark |
| caution | `#a05000` | `#e29936` | Brackets, open decisions, "Open" pills. Never alarm styling |

### Light, on `#ffffff`

```
[PASS] Lightness band         all 5 inside L 0.43 to 0.77
[PASS] Chroma floor           all 5 >= 0.1
[PASS] CVD separation         worst all-pairs #a05000 / #007452 ΔE 8.1 (protan) · tritan 4.0
[PASS] Normal-vision floor    worst all-pairs #007452 / #28a43a ΔE 16.2 (normal)
[PASS] Contrast vs surface    all 5 >= 3:1
```

### Dark (the projector theme), on `#0b1511`

```
[FAIL] Lightness band         outside band: #3eee92 0.841, #47b5fa 0.74, #e29936 0.739   (deliberate, see below)
[PASS] Chroma floor           all 5 >= 0.1
[PASS] CVD separation         worst all-pairs #a86fcf / #47b5fa ΔE 9.7 (deutan) · tritan 10.4
[PASS] Normal-vision floor    worst all-pairs #a86fcf / #47b5fa ΔE 19.4 (normal)
[PASS] Contrast vs surface    all 5 >= 3:1 (lowest: demand 5.17, positive 5.38)
```

**The one deliberate override.** The validator's dark lightness band (L 0.48 to 0.67) keeps chart colours from glowing on a dark page. The dark theme here is the projector theme, and `specs/03` makes projector safety a non-negotiable: a washed-out projector loses mid-tones first. A palette that stays inside the band was found (CVD 8.1, normal 16.9), but its positive role sat at 3.35:1 against the surface. Three roles were allowed above the band so that every role clears 5:1. Every other check still passes, with more margin than the in-band palette.

## Neutral roles and text contrast

| Role | Light | vs surface | Dark | vs surface |
|---|---|---|---|---|
| ink | `#0d1f16` | 17.2 | `#eff5f2` | 16.8 |
| body | `#334139` | 10.7 | `#cdd7d1` | 12.6 |
| muted | `#5d6a62` | 5.7 | `#9ba8a1` | 7.5 |
| hairline | `#d3dcd6` | 1.4 (rules only) | `#3f4b44` | 2.0 (rules only) |
| surface | `#ffffff` | | `#0b1511` | |
| surface-raised | `#f2f8f5` | | `#16211b` | |
| surface-inverse | `#034126` Night shift green | white on it 11.8 | `#075030` | ink on it 8.7 |

## Rules that fall out of the numbers

- **Text on an accent fill is ink, never white** (light: ink 5.3:1, white 3.25:1). The token is `--on-accent`.
- **Accent is never used for small text** in the light theme (3.25:1 on white). It carries the large title phrase, focus rings, lines, and marks. Links and labels use ink.
- **Every status and side colour ships with a shape, glyph, or word.** The CVD separation clears the 8 target in both themes, but the deck never relies on it alone (`specs/02` 1.4 and 1.7).
- **Under `prefers-contrast: more`**, hairlines become 2 px and glass becomes opaque.
