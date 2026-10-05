# GTM walkthrough deck

Load for: presenting the GTM internally, pointing someone at a dashboard, or checking what the deck shows. Distills the walkthrough repo (`Saasrelaunchdev/SOSSMSGTMWalkthrough`: README, NOTES, the build from `deck-handoff/` in the GTM build repo). Status: BUILT, internal only. It carries grade C figures; it is not a customer or contractor surface.

## What it is
One self-contained HTML file (`dist/index.html`, identical to `dist/sos-sms-gtm.html`, about 1.2 MB, zero network requests): a 25-slide hub and 22 linked dashboards, light and dark themes, reduced motion, and print paths. Every word comes from the deck content spec; every dashboard table is verbatim from the knowledge files.

## The map

| Slides | Dashboards | Covers |
|---|---|---|
| 01 | | Cover and launcher |
| 02 | S05 density | Marketplace: supply leads |
| 03 to 11 | S01 to S09 | Contractors: product, market, positioning, who first, committee, value, journey, channels, pricing |
| 12 to 20 | D01 to D09 | Customers: the same nine. Slide 20 is the still slide |
| 21 | M1 | Where the sides meet, the cross-side check (the peak) |
| 22 | M2 | Speed to scale, with the calculators |
| 23 | M3 | Pricing, both sides, once: contractors join free, SOS SMS earns on transactions (decisions 2 and 5) |
| 24 | M4 | The twelve decisions, made (the answer) |
| 25 | | Close |

## Pricing added (2026-10-03)
Slide 23 and dashboard M3 show the pricing model once, for both sides, from `knowledge/gtm/pricing/` (generated in the GTM build repo from the Google folder pricing model). The decisions moved to M4 on slide 24 and the close to slide 25. Checks: check_deck 0 errors, navigation 91 of 91, 60 fps; the new hero has 85 elements. Merged into the walkthrough repo's `main` on 2026-10-05, so the deployed deck carries it. Since 2026-10-04 the amounts are decided and shown as decided.

## Verified at build (2026-10-01)
check_deck 0 errors (13 warnings, each the first word of the name quoted alone inside the name-collision notes themselves); navigation tests 91 of 91; hub interactive in about 0.23 s; every hero under 350 elements.

## Every value resolved (2026-10-04)
The deck carries no placeholder and no decision left for the founders: every value comes from the resolution register (`knowledge/gtm/marketplace/resolution-register.md` in the deck repo; `reference/resolution-register.md` here). Planning values are labelled; per-message details render as merge field chips. `tools/resolved_check.py` fails on any unresolved placeholder, and `check_deck.py` treats one as an error. Checks: 0 unresolved, check_deck 0 errors, navigation 91 of 91.

## Settled from the build
- Vercel: `vercel.json` serves `dist/` only with noindex. The config is checked on the first deploy, and Deployment Protection is on before any URL is shared.
- Dark palette: kept as validated.
- S08 has 6 bands; the spec register now says so.
- Three hero labels are compressed rather than verbatim, as the content spec allows; slide 20's 50 percent rate is the labelled planning value (R30).

## Rules when using it
Present it as the plan, not as results: no result exists before launch, planning values are labelled, and current scores are 0. Never screenshot a dashboard into external material. When a decided value changes, the deck changes after `ops/decisions.md`, not before.
