# GTM walkthrough deck

Load for: presenting the GTM internally, pointing someone at a dashboard, or checking what the deck shows. Distills the walkthrough repo (`Saasrelaunchdev/SOSSMSGTMWalkthrough`: README, NOTES, the build from `deck-handoff/` in the GTM build repo). Status: BUILT, internal only. It carries grade C figures and open decisions; it is not a customer or contractor surface.

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
| 23 | M3 | Pricing, both sides, once: contractors join free, SOS SMS earns on transactions (proposed amounts, decisions 2 and 5 open) |
| 24 | M4 | Decisions: the twelve (the ask) |
| 25 | | Close |

## Pricing added (2026-10-03)
Slide 23 and dashboard M3 show the pricing model once, for both sides, from `knowledge/gtm/pricing/` (generated in the GTM build repo from the Google folder pricing model). The decisions moved to M4 on slide 24 and the close to slide 25. Checks: check_deck 0 errors, navigation 91 of 91, 60 fps; the new hero has 85 elements. On branch `claude/quirky-tesla-29ad5a` of the walkthrough repo until merged; the deployed deck updates on merge. The proposed amounts appear only there, labelled proposed; `rules/do-not-say.md` keeps them out of copy.

## Verified at build (2026-10-01)
check_deck 0 errors (13 warnings, each the first word of the name quoted alone inside the name-collision notes themselves); navigation tests 91 of 91; hub interactive in about 0.23 s; every hero under 350 elements.

## Open items from the build
- Vercel: `vercel.json` serves `dist/` only with noindex. Confirm the config on first deploy and **turn on Deployment Protection** before sharing a URL.
- Dark palette awaiting approval.
- The request to fill every {TBD} was declined: `TBD-REGISTER.md` lists 244 occurrences on 227 lines in 29 files, none filled.
- S08 band count: the spec register says 7, the content spec writes 6; 6 built. Confirm.
- Minor: three hero labels compressed rather than verbatim; slide 20's assumed 50 percent rate shown as illustrative with "(assumed)".

## Rules when using it
Present it as the plan, not as results: every metric is {TBD} and current scores are 0. Never screenshot a dashboard into external material. When a decision lands, the deck changes after `ops/decisions.md`, not before.
