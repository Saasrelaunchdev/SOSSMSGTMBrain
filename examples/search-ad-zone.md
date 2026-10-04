# Example: emergency ad group, zone template (customers)

Status: **voice reference, approved 2026-10-04.** Assembled from Run 2 Phase 8 against the brain, with every value decided. Runs once Google confirms eligibility in writing (decision 11), the number is registered (decision 9), message assets are verified (S72), and the zone meets the density number (Stage 2). Template: `templates/search-ad.md`.

Zone: {{zone name}}. Covered hours: {{covered hours}}. Geofenced to the zone; scheduled to covered hours; paused automatically when acceptance falls.

## Headlines (max 30 characters)

| Headline | Characters | Condition |
|---|---|---|
| Text Us When a Pipe Bursts | 26 | |
| Dispatch to Licensed Plumbers | 29 | |
| One Text Reaches Local Pros | 27 | Zone at density |
| Trip Charge Shown Upfront | 25 | |
| Arrival Time When They Accept | 29 | |
| No App. No Phone Tree. | 22 | |
| Steps to Stop the Water Now | 27 | |
| Plumbers Near {{zone name}} | 14 plus the zone name | Per zone; at most 30 once filled |
| 90 Minutes or Trip Charge Back | 30 | The guarantee (decision 3); scope on the landing page |

## Descriptions (max 90 characters)

| Description | Characters |
|---|---|
| Text what broke. Vetted local plumbers on SOS SMS see it at once. Trip charge shown first. | 90 |
| Get steps to stop the water right away, then a licensed plumber with an arrival time. | 85 |
| Fire, gas smell, or anyone hurt? Call 911 first. For leaks and backups, text SOS SMS. | 85 |

Message asset: SOS SMS, the registered number, a reply within 15 minutes in covered hours, automated-reply disclosure, and the human handoff: text HELP (R50). Final URL: the zone landing page. Conversion: paid request.

## Held back, and why
- "Only One Pro Gets Your Info": runs once the broadcast that hides identity ships (decision 4).
- "24 Hour Plumber" style lines: only if the zone's covered hours are 24 hours.

## Why this works
Each headline is one fact the customer can check: who sends, what they see first, when they learn the time. "Dispatch to Licensed Plumbers" keeps SOS SMS from posing as the plumber, which the channel rules require. The safety description is part of the ad, not an afterthought. Every conditional line carries its condition, so a hurried operator cannot run it early.
