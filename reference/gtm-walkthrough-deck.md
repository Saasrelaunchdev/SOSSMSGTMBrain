# GTM walkthrough deck

Load for: presenting the GTM internally, pointing someone at a dashboard, or checking what the deck shows. Distills the walkthrough repo (`Saasrelaunchdev/SOSSMSGTMWalkthrough`: README, NOTES, the build from `deck-handoff/` in the GTM build repo). Status: BUILT, internal only. It carries grade C figures; it is not a member or contractor surface.

## What it is
One self-contained HTML file (`dist/index.html`, identical to `dist/sos-sms-gtm.html`, about 1.5 MB, zero network requests): a 27-slide hub and 22 linked dashboards, light and dark themes, reduced motion, and print paths. Every word comes from the deck content spec; every dashboard table comes from the knowledge files, through a plain-language layer that changes wording, never numbers.

## The map

| Slides | Dashboards | Covers |
|---|---|---|
| 01 | | Cover, with a gate of three doors: Supply side · Contractors, Demand side · Members, Where the sides meet · Marketplace |
| 02 | S05 density | Density model: supply leads |
| 03, 13 | | The two side hubs, each listing its nine dashboards |
| 04 to 12 | S01 to S09 | Contractors: product, market, positioning, who first, committee, value, journey, channels, pricing |
| 14 to 22 | D01 to D09 | Members: the same nine. Slide 22 is the still slide: a new member's first 6 months against what each channel costs to win one |
| 23 | M1 | Where the sides meet, the cross-side check (the peak) |
| 24 | M2 | Speed to scale: a new member against the acquisition ceiling, with the calculators |
| 25 | M3 | Pricing, both sides, once: members pay a membership and the $99 trip charge on use; contractors join free, then $25 per completed job |
| 26 | M4 | The twelve decisions, made (the answer) |
| 27 | | Close |

## The membership revision (2026-10-11)
The member side follows the revision (`ops/decisions.md`): the side is named Members on screen, and the cover line reads "Every promise to a member is kept by a contractor first." The member mockups were redrawn for one-text dispatch, with no confirming reply, no payment link, and no card entry at the emergency; slide 24's hero is redrawn around the acquisition ceiling, and slide 25's member receipt shows the membership as merge field chips. The D09 and M2 calculators reproduce the planning values at their defaults ($8.51 a month, about $43, about $131, an affiliate paid back in month 3). Register IDs on the dashboards render as chips with the value and its basis. Walkthrough `main` at `a503b8f`. Checks: check_deck 0 errors (12 warnings, the name-collision quotes), specs 0 errors, resolved_check 0, navigation 110 of 110.

## Pricing added (2026-10-03)
The pricing model shows once, for both sides, from `knowledge/gtm/pricing/` (generated in the GTM build repo from the Google folder pricing model). Since 2026-10-04 the decided amounts are shown as decided; since 2026-10-11 the membership price shows as a planning value.

## Every value resolved (2026-10-04)
The deck carries no placeholder and no decision left for the founders: every value comes from the resolution register (`knowledge/gtm/marketplace/resolution-register.md` in the deck repo; `reference/resolution-register.md` here), and the deck's own value table is generated from it, with the same IDs. Planning values are labelled; per-message details render as merge field chips. `tools/resolved_check.py` fails on any unresolved placeholder, and `check_deck.py` treats one as an error.

## Settled from the build
- Vercel: `vercel.json` serves `dist/` only with noindex. The config is checked on the first deploy, and Deployment Protection is on before any URL is shared.
- Dark palette: kept as validated.
- Three hero labels are compressed rather than verbatim, as the content spec allows. The still slide's old 50 percent rate (R30, first text to paid) is retired; the slide shows the member arithmetic instead.

## Rules when using it
Present it as the plan, not as results: no result exists before launch, planning values are labelled, and current scores are 0. Never screenshot a dashboard into external material. When a decided value changes, the deck changes after `ops/decisions.md`, not before.
