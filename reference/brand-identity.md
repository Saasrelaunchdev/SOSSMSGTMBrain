# Brand identity

Load for: any visual asset, logo use, colour choice, type setting, motion, or a question about what the brand means. Distills the walkthrough repo's brand v1 (`sources/raw/walkthrough/brand-book.html`, `brand-README.md`, `palette-validation.md`, `tokens.css`, 2026-10-01). Logo files: `brand/logo/`. Status: BUILT, internal; the dark palette kept as validated (2026-10-04).

## What it means
**Cover line:** "One text out. One yes back." **The line that carries the business:** "Every promise to a customer is kept by a contractor first."

| Value | Meaning |
|---|---|
| Calm under pressure | The subject is emergencies; the brand is not one. Nothing flashes, alarms, or shouts |
| Kept, not claimed | A promise goes out only where the other side's terms make it true, and only in a zone at density |
| Fair to both sides | Money moves only to whoever it was promised to |
| Exact, never inflated | Every number carries its source, or it does not appear |

## The mark
A sent-message bubble (three round corners, one tight) holding a round dot and a square. **Round is always a customer. Square is always a contractor**, everywhere in the system. Signal green is the yes, the reply when a contractor accepts; it never means alarm. **Never** red or orange, a siren, a cross, a lifebuoy, a bell, a ringing phone, or "911".

## Logo rules
Six lockups: primary (`sos-sms-logo.svg`), reversed, stacked (and stacked reversed), one colour ink, one colour white, plus the wordmark, the mark (three variants), favicon, and app icon. Always the full "SOS SMS"; never separate the words or use the first alone. Clear space: one contractor square on every side (built into the files). Minimum: 96 px wide on screen, 24 mm in print; the mark alone 16 px. Don't stretch, tilt, recolour, outline, glow, shadow, or pulse it.

## Colour

| Colour | Hex | Job |
|---|---|---|
| Signal green | #28A43A | The yes, the accent. Marks and large text only (3.25:1 on white) |
| Night shift green | #034126 | Bars, wordmark. White on it 11.75:1 |
| White | #FFFFFF | The page |
| Paper | #F2F8F5 | Cards, raised surfaces |

Twelve semantic roles, light and dark (`sources/raw/walkthrough/tokens.css`): ink, body, muted, hairline, surface, surface-raised, surface-inverse, accent, positive, caution, supply, demand. Light accent #28A43A, supply #0057B1, demand #A366CD, caution #A05000. Dark (projector) accent #3EEE92. Rules: accent on one object at a time, never small text; caution for planning values and grade C marks, never for alarm or the safety line; supply always with a square, demand always with a circle. Palette checked against colour-vision simulation and contrast floors; light passes every check; dark passes all but the chart lightness band, deliberately, so every role clears 5:1. **Dark kept as validated (2026-10-04).**

## Type
Inter (SIL Open Font License), embedded and subset, weights 420, 540, 660, tabular figures on digits only. One family. Lowercase l carries a tail so l, I, and 1 never blur on a projector.

## Shape, motion, provenance
One easing curve, cubic-bezier(0.2, 0.8, 0.2, 1): arrives and settles, no bounce. Durations 120, 240, 480, 720 ms. One ambient loop per screen at most; reduced motion shows end states. Projections are drawn as outlines, never filled solids. Planning values carry their label, and merge fields render as field chips. **The safety line is set still and fully legible, never animated, never styled as an alarm.**

## Voice
Plain, exact, unhurried. Each claim stated once, with its source beside it. No hype and no urgency theatre: the reader may be standing in water. Full rules: `rules/writing-rules.md`.
