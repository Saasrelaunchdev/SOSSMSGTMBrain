# Example: sign-up ads for paid social, zone template (members)

Status: **voice reference, rewritten 2026-10-11 for the membership revision; revised 2026-10-21 as sign-up ads for paid social at launch, for three trades and three plans.** It replaces the emergency ad group of 2026-10-04: ads sell the membership before the need, never dispatch during an emergency. There is no paid search at launch (decision 11, revised 2026-10-20), so the search ad group of 2026-10-11 is held, below. Assembled from Run 2 Phase 8 (the paid social drafts) against the brain, with every value decided or a merge field. Runs once the membership page is up (R23) and memberships are open in the zone (R55). Template: `templates/search-ad.md`.

Zone: {{zone name}}. Limited to the open zone's map, by location only; no pixels, no retargeting, no uploaded lists. Paused automatically with sign-ups when acceptance in any trade falls under 90 percent over 7 days (R34).

Ad sets: readiness and plan comparison, promoted to homeowners in the zone; a seasonal set before the first freeze, and one before the first heat wave. No ad offers dispatch during an emergency, and no ad uses the first word of the name alone (decision 10).

## Headlines (max 30 characters)

| Headline | Characters | Condition |
|---|---|---|
| Join Before Something Breaks | 28 | |
| One Text When Something Breaks | 30 | |
| Plumbing, HVAC, Electrical | 26 | The three trades |
| Dispatch to Licensed Pros | 25 | Says SOS SMS dispatches |
| One Text Reaches Local Pros | 27 | Open zones only |
| Trip Charge Only When Used | 26 | |
| Arrival Time When They Accept | 29 | |
| No App. No Phone Tree. | 22 | |
| No Forms at 2 a.m. | 18 | The card and address are on file |
| Cancel Any Time | 15 | |
| Plans From $10 a Month | 22 | |
| Ready Before the First Freeze | 29 | Seasonal set |
| Ready Before the Heat Wave | 26 | Seasonal set |
| Membership in {{zone name}} | 14 plus the zone name | Per zone; at most 30 once filled |
| Late? 6 Months Credited | 23 | The guarantee on Plus and Premier (decision 3); plans and scope on the membership page |

## Ad text (max 90 characters)

| Ad text | Characters |
|---|---|
| Join before you need it. In an emergency, one text reaches vetted local pros at once. | 85 |
| Your card and address are on file, so the emergency is one text. Cancel any time. | 81 |
| The $99 trip charge applies only when you use it, and counts toward the repair. | 79 |
| Not a warranty. We get a vetted contractor to your door; they price the repair on site. | 87 |
| Plumbing, HVAC, and electrical in one plan. Basic from $10 a month; Plus adds a guarantee. | 90 |
| Fire, gas smell, sparks, or anyone hurt? Call 911 first. Otherwise, members text us. | 84 |

Final URL: the membership page for the zone, which opens on the ZIP check. Conversion: a new paid member, by plan (primary); the ZIP check and a launch list join (secondary). Cost per new paid member, by ad set, is read weekly against the ceiling of the plan joined (R63); an ad set over it stops.

## Held back, and why
- "Only One Pro Gets Your Info" (27 characters), and the ad text "We dispatch licensed, insured pros. Only the one who accepts gets your address." (79): the second sentence only once the broadcast that hides identity ships (decision 4).
- Any "24 hour" or "24/7" line: never. An open zone is covered at any hour, said as "any hour, in {{zone neighborhoods}}".
- The search ad group (Google responsive search ads on readiness and plan searches, and the Microsoft import): held, not run at launch (decision 11). From Stage 3, once search volume for SOS SMS by name is counted (R68), a brand campaign on the full name may run, with Google's written confirmation (S71), at or under the plan's ceiling (R63), and with emergency dispatch searches on its negative list. Never Local Services Ads (S70).

## Why this works
Homeowners scrolling at home in an open zone are not in the middle of an emergency: they have time to read, compare plans, and join, which is when a membership makes sense. Someone mid-emergency needs a contractor now, not a membership, which is part of why there is no paid search at launch. Each headline is one fact a reader can check: one text, three trades, a trip charge only when used, plans from $10, cancel any time. "Not a warranty" in the ad text sets the category before the click, so the membership page never has to undo a wrong expectation. The guarantee line names its plans, the safety line is part of the ad set, and every conditional line carries its condition, so a hurried operator cannot run it early.
