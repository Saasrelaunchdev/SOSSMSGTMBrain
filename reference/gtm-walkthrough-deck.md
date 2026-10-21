# GTM walkthrough deck

Load for: presenting the GTM internally, pointing someone at a dashboard, or checking what the deck shows. Distills the walkthrough repo (`Saasrelaunchdev/SOSSMSGTMWalkthrough`: README, NOTES, the build from `deck-handoff/` in the GTM build repo). Status: BUILT, internal only. It carries grade C figures; it is not a member or contractor surface.

## What it is
One self-contained HTML file (`dist/index.html`, identical to `dist/sos-sms-gtm.html`, about 1.8 MB, zero network requests): a 27-slide hub and 22 linked dashboards, light and dark themes, reduced motion, and print paths. Every word comes from the deck content spec; every dashboard table comes from the knowledge files, through a plain-language layer that changes wording, never numbers.

## The map

| Slides | Dashboards | Covers |
|---|---|---|
| 01 | | Cover, with a gate of three doors: Supply side · Contractors, Demand side · Members, Where the sides meet · Marketplace |
| 02 | S05 density | Density model: supply leads, 9 contractors per trade in three trades |
| 03, 13 | | The two side hubs, each listing its nine dashboards |
| 04 to 12 | S01 to S09 | Contractors: product, market, positioning, who first, committee, value, journey, channels, pricing (slide 12: $25 per completed paid job from the first job) |
| 14 to 22 | D01 to D09 | Members: the same nine. Slide 14 shows five problems across plumbing, HVAC, and electrical; slide 19's miss is a credit on Plus and Premier. Slide 22 is the still slide: a new Plus member's first 6 months, about $70, against what each channel costs to win one |
| 23 | M1 | Where the sides meet, the cross-side check (the peak) |
| 24 | M2 | Speed to scale. Hero, "The levers": a plan control (Basic, Plus, Premier), a channel control (Affiliate; "Paid search, not run"), price change and churn sliders, and a ceiling band per plan |
| 25 | M3 | Pricing, both sides. Hero, "Who pays, and when": a contractor receipt that never changes with the plan, a member receipt per plan, and the $25 take per completed job as a wireframe column |
| 26 | M4 | The twelve decisions, made and revised (the answer); Stage 0 is decisions and setup |
| 27 | | Close |

## The tiers and pricing revisions (2026-10-21)
Repository `Saasrelaunchdev/SOSSMSGTMWalkthrough`, branch `claude/busy-babbage-6lapos`: `21c4430` ("The tiers and pricing revisions in the walkthrough: three trades, three plans, the late-arrival credit, no paid search") and `cd7d6e4` ("wording fixes from the screenshot read-through"). The deck now draws the three plans: Basic $10 or $100, Plus $15 or $150 (built for most members, a planning value), Premier $35 or $350, with the credit (none, 6, 12 months) and the phones (1, 5, 10) on a sliding scale. Slide 24's hero reads each plan's levers; slide 25's receipts switch by plan with the contractor receipt fixed. The late-arrival credit replaces the trip charge refund on the demand slides; a late arrival keeps its trip charge. No paid search runs anywhere: paid search is drawn only as the benchmark, and Microsoft Ads are gone. One set of terms for every contractor: $25 per completed paid job from the first job (slides 12 and 25; S05, S09, M3). Dashboards: D09 adds a credit calculator and the plan calculator, shared with M2; S09 shows the late-arrival rule as decided (the trip charge stands) and the plans to join; M3 adds the entitlements, plan mix, zone economics, and miss cases tables. Calculators at their defaults: Plus $15, $13.77 a month, about $70 ceiling, about $212 over the membership, the $20 affiliate paid back in month 2; the credit about $0.17 a member a month on Plus, $1.18 on Premier; one job, $74 to the contractor, $25 kept, $13.03 net (planning values). Still 27 slides and 22 dashboards. Checks: check_deck 0 errors (11 warnings, the name-collision quotes), specs 0 errors, resolved_check 0, navigation 110 of 110, time to interactive 167 ms.

## The membership revision (2026-10-11), superseded where the revisions above changed it
The member side follows the revision (`ops/decisions.md`): the side is named Members on screen, and the cover line reads "Every promise to a member is kept by a contractor first." The member mockups were redrawn for one-text dispatch, with no confirming reply, no payment link, and no card entry at the emergency; slide 24's hero is redrawn around the acquisition ceiling, and slide 25's member receipt showed the membership as merge field chips. The D09 and M2 calculators then reproduced that revision's planning values (one plan, one ceiling), now replaced by the plan values above. Register IDs on the dashboards render as chips with the value and its basis. Walkthrough `main` at `a503b8f`. Checks then: check_deck 0 errors (12 warnings), specs 0 errors, resolved_check 0, navigation 110 of 110.

## Pricing added (2026-10-03)
The pricing model shows once, for both sides, from `knowledge/gtm/pricing/` (generated in the GTM build repo from the Google folder pricing model). Since 2026-10-04 the decided amounts are shown as decided; since 2026-10-21 the three plans' prices are decided and shown as decided, and the economics as planning values.

## Every value resolved (2026-10-04)
The deck carries no placeholder and no decision left for the founders: every value comes from the resolution register (`knowledge/gtm/marketplace/resolution-register.md` in the deck repo; `reference/resolution-register.md` here), and the deck's own value table is generated from it, with the same IDs. Planning values are labelled; per-message details render as merge field chips. `tools/resolved_check.py` fails on any unresolved placeholder, and `check_deck.py` treats one as an error.

## Settled from the build
- Vercel: `vercel.json` serves `dist/` only with noindex. The config is checked on the first deploy, and Deployment Protection is on before any URL is shared.
- Dark palette: kept as validated.
- Three hero labels are compressed rather than verbatim, as the content spec allows. The still slide's old 50 percent rate (R30, first text to paid) is retired; the slide shows a new Plus member's arithmetic instead.

## Rules when using it
Present it as the plan, not as results: no result exists before launch, planning values are labelled, and current scores are 0. Never screenshot a dashboard into external material. When a decided value changes, the deck changes after `ops/decisions.md`, not before.
