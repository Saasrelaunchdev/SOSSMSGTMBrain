# Example: sign-up ad group, zone template (members)

Status: **voice reference, rewritten 2026-10-11 for the membership revision.** It replaces the emergency ad group of 2026-10-04: ads now sell the membership before the need, never dispatch during an emergency (decision 11, revised 2026-10-11). Assembled from Run 2 Phase 8 against the brain, with every value decided or a merge field. Runs once Google confirms in writing that SOS SMS may advertise its membership with standard search ads (decision 11), the membership page is up (R23), and memberships are open in the zone (R55). Template: `templates/search-ad.md`.

Zone: {{zone name}}. Geofenced to the zone, by location only; no pixels, no retargeting. Paused automatically when acceptance falls under 90 percent over 7 days (R34).

Ad group: readiness and plan searches, such as "plumbing protection plan", "home warranty alternatives", "plumber membership"; a seasonal group before the first freeze, such as "how to prevent frozen pipes". Negative list: emergency dispatch searches ("emergency plumber near me", "24 hour plumber", "burst pipe repair"), jobs and careers, DIY parts and tools, other cities, and competitor brand names. No bids on "SOS plumbing" (decision 10).

## Headlines (max 30 characters)

| Headline | Characters | Condition |
|---|---|---|
| Join Before Your Pipes Burst | 28 | |
| One Text When Something Breaks | 30 | |
| Plumbing Emergency Membership | 29 | |
| Dispatch to Licensed Plumbers | 29 | |
| One Text Reaches Local Pros | 27 | Open zones only |
| Trip Charge Only When Used | 26 | |
| Arrival Time When They Accept | 29 | |
| No App. No Phone Tree. | 22 | |
| No Forms at 2 a.m. | 18 | |
| Cancel Any Time | 15 | |
| Ready Before the First Freeze | 29 | Seasonal group |
| Membership in {{zone name}} | 14 plus the zone name | Per zone; at most 30 once filled |
| 90 Minutes or Trip Charge Back | 30 | The guarantee (decision 3); scope on the membership page |

## Descriptions (max 90 characters)

| Description | Characters |
|---|---|
| Join before you need it. In an emergency, one text reaches vetted local plumbers at once. | 89 |
| Your card and address are on file, so the emergency is one text. Cancel any time. | 81 |
| The $99 trip charge applies only when you use it, and counts toward the repair. | 79 |
| Not a warranty. We get a vetted plumber to your door; they price the repair on site. | 84 |
| Fire, gas smell, or anyone hurt? Call 911 first. For leaks and backups, members text us. | 88 |

Final URL: the membership page for the zone, which opens on the ZIP check. Conversion: a new paid member (primary); the ZIP check and a launch list join (secondary). Cost per new paid member, by ad group, is read against the ceiling of about $43 (R63).

## Held back, and why
- "Only One Pro Gets Your Info" (27 characters), and the description "We dispatch local licensed, insured plumbers. Only the one who accepts gets your address." (89): only once the broadcast that hides identity ships (decision 4).
- Any "24 hour" line: only where the zone's covered hours are 24 hours.
- The guarantee headline: only where the zone's covered hours are on the membership page.

## Why this works
People searching "plumbing protection plan" or "how to prevent frozen pipes" have time to read, compare, and join, which is when a membership makes sense; someone searching "emergency plumber near me" is better served by a plumber from the results, so those searches are excluded. Each headline is one fact a reader can check: one text, a trip charge only when used, cancel any time. "Not a warranty" in a description sets the category before the click, so the membership page never has to undo a wrong expectation. The safety description is part of the ad, not an afterthought, and every conditional line carries its condition, so a hurried operator cannot run it early.
