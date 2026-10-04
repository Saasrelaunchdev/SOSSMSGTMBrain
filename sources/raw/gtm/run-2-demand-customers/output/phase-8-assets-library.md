# Phase 8. Assets and Collaterals Library Dashboard, customer side

Revised 2026-10-01 for the product-led motion: no sales team and no outreach. SOS SMS meets customers where they are already trying to solve the problem, and the product does the converting.

## The three channels

<!-- sheet: Channel_Choice -->
| Skill default | Used for SOS SMS | Why |
|---|---|---|
| LinkedIn Ads | 1. Paid search, bottom of funnel (Google Ads, then Microsoft Ads) | Emergency demand shows up as a search: "burst pipe", "water leaking through ceiling", "emergency plumber near me". Those searchers are trying to solve the problem now |
| Cold email | 2. Problem-solving pages (organic search and AI answers) | Pages that answer the urgent question first, then offer the text button, earn the same moment without paying per click |
| LinkedIn outreach | 3. Product loops | The product spreads itself: stop-the-water help in the first reply, the saved contact card, the post-job share, Text READY. Owned channels bring the cost per job down over time |

**What was dropped, and why.** Pre-need partnerships (agents, inspectors, hardware stores, homeowner associations) and founder posts in neighborhood groups both need outreach, which the product-led motion rules out.

### Rules for paid search

<!-- sheet: Paid_Search_Rules -->
| Rule | Detail |
|---|---|
| Density first | Ads run only in zones, and only in hours, where Run 1's density target is met. Acceptance below threshold pauses the zone's campaigns automatically |
| Never pose as the plumber | Every ad and page says SOS SMS dispatches licensed, insured contractors; the contractor does the work |
| Local Services Ads are not an option | Google's Local Services policy bars reselling leads and re-routing requests to businesses not listed in the ad (S70), which is SOS SMS's model |
| Standard search ads | Plumbing is not on Google's US list of restricted local services (S71; locksmith and garage door are). Confirm with Google, in writing, that a dispatch service may advertise this way before spending (decision 11, decided: standard search ads only, after written confirmation) |
| Text-from-ad (message assets) | From 2025-10-30 these need verified business details, a stated response time, automated replies that say they are automated, and a defined human handoff (S72). The first reply must say it is an automated message and how to reach a person |
| Claims | No superlatives, no arrival averages, no "24/7" unless the zone's covered hours are 24/7. The guarantee appears in an ad with its scope on the landing page (decision 3) |
| Safety | The 911 line appears on every landing page and in one ad description |
| Brand terms | The name collision (decision 10) means people searching "SOS plumbing" may be looking for someone else. Do not bid on "SOS plumbing" until the trademark and search check is done |

### Measurement

The conversion to optimize for is a **paid request**, not a click or a first text. First texts are imported as a secondary conversion. Cost per paid job by zone is the number that decides whether a zone's spend grows or shrinks (`../../marketplace/speed-to-scale-plan.md`, sections 5 and 8).

## Step 8.1. Full-funnel asset map

<!-- sheet: Assets -->
| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specs and QA | Contributors | Inputs Required | Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **CHANNEL 1. PAID SEARCH** | | | | | | | | | |
| Top of Funnel | Seasonal prevention campaign | Small campaign on prevention searches ("how to prevent frozen pipes") before the first freeze | Search ads to a prevention page | Three prevention steps; where the shutoff is; Text READY | Capped budget; only in zones at density; seasonal only | Growth lead | Prevention page (Channel 2) | 2 days per season | Lowest priority; builds saved numbers before the spike |
| Middle of Funnel | Problem ad groups | Ads on problem searches ("water heater leaking from bottom", "ceiling dripping water", "toilet won't stop overflowing") | Responsive search ads | Headline names the problem; description offers stop-the-water steps by text and a plumber if needed | Ad copy from the drafts below; landing on the matching problem page | Growth lead | Problem pages (Channel 2) | 1 week per zone | Often cheaper clicks than "emergency plumber" |
| Bottom of Funnel | Emergency ad groups | Ads on emergency searches ("emergency plumber near me", "24 hour plumber", "burst pipe repair", "sewer backup help") | Responsive search ads with a message asset (text-from-ad) | Drafts below | Geofenced to the zone; scheduled to covered hours; every claim narrowed | Growth lead | Zone page; message asset verification (S72) | 1 week per zone | The core of the channel |
| Bottom of Funnel | Zone landing page | The page every emergency ad lands on | Web page | Text button with "Something broke at home:" prefilled; how it works in three texts; the trip charge; the guarantee in one line with its scope; the 911 line | Loads fast on a phone; the text button above the fold; says SOS SMS dispatches and is not the plumber | Product | Zone; registered number (S32) | 3 days | One per zone, from a template |
| Bottom of Funnel | Message asset setup | Text-from-ad configuration | Google Ads asset | Business name; the SOS SMS number; a reply within 15 minutes in covered hours; automated-reply disclosure; the human handoff, text HELP (R50) | Meets the 2025-10-30 requirements (S72) | Growth lead, product | Verified business details | 1 week including verification | If it does not pass, ads still run with the landing page |
| Bottom of Funnel | Negative keyword list | Searches to exclude | List | Jobs and careers; schools and licensing; DIY parts and tools; other cities; competitor brand names | Reviewed weekly against search terms | Growth lead | Search term reports | Ongoing | Cuts wasted clicks |
| Bottom of Funnel | Microsoft Ads import | The Google campaigns imported to Microsoft Ads | Search campaigns | Same structure, same rules | Same QA | Growth lead | Google campaigns live | 2 days | Clicks reported 30 to 60 percent cheaper; audience skews older homeowners (S74, C) |
| **CHANNEL 2. PROBLEM-SOLVING PAGES** | | | | | | | | | |
| Top of Funnel | Prevention guides | "How to prevent frozen pipes", "Where is my main water shutoff?" | Web pages | Steps; when to call a plumber; Text READY to save the number | Accurate and general; no product claims | Growth lead, a founding contractor reviewer | Founding contractor review | 1 week for the first five | |
| Top of Funnel | Home Emergency Readiness Scorecard | The lead magnet, as a page | ScoreApp scorecard | See `lead-magnet-spec.md` | Same as the spec | Growth lead | ScoreApp | 1 week | |
| Middle of Funnel | Problem guides | "Water leaking through the ceiling: what to do first", "Sewer backup: what to do now", "Water heater leaking" | Web pages | Stop-the-water steps first; safety; when it needs a plumber tonight; the text button | Steps limited to shutoff and safety, not repairs; the 911 line; reviewed by a licensed plumber | Growth lead, founding contractor reviewer | Founding contractor review | 1 week for the first five | Paid search problem ad groups land here too |
| Middle of Funnel | How it works, the guarantee in full, privacy in plain words | The pages every other page links to | Web pages | Three texts; the trip charge and crediting; the guarantee scope; who sees what | Written to the decided terms; counsel-reviewed | Founders, counsel | Decisions 2, 3, 4, and 6 | 1 week | |
| Bottom of Funnel | Zone pages | "Emergency plumbing help by text in {{zone}}" | Web pages | Same as the paid landing page, written for search | Same QA | Product | Zone | 2 days per zone | Shared template with Channel 1 |
| **CHANNEL 3. PRODUCT LOOPS** | | | | | | | | | |
| Top of Funnel | Forwardable contact card | Sent after a completed job: "save this, and share it with a neighbor if you like" | Text with a contact file | One line; the contact card | Sent once; no follow-ups without opt-in (S31) | Product | Completed jobs | 2 days | Forwards per job is the loop's KPI |
| Top of Funnel | Text READY | The pre-need keyword printed on the contact card and every page | Text sequence | Five-question check; shutoff guide; contact card | Informational only | Product | Message design | 1 week | |
| Middle of Funnel | Saved contact card | The card every customer gets, so the next emergency starts with a saved number, not a search | Contact file | Name, number, "text us when something breaks at home", the 911 line | Full name "SOS SMS", never "SOS" alone (name collision) | Product | None | 1 day | Repeat requests from saved contacts are owned demand |
| Bottom of Funnel | Stop-the-water first reply | The product's first answer to any first text: steps to stop the water for the problem described, then the offer of a plumber with the trip charge | Text | Automated-reply disclosure; safety check; shutoff steps; trip charge; guarantee scope; then the payment link | Value before payment; no link in the first message (Phase 7 stage 3); steps limited to shutoff and safety | Product, founding contractor reviewer | Decisions 2, 3, and 5 | 2 weeks, tested with 20 people | The demand driver (Phase 1) and the conversion moment for every channel |
| Bottom of Funnel | Automatic refund text | When the window is missed, the refund and an explanation arrive without the customer asking | Text | What happened; the refund; what happens next | Sent automatically; plain words | Product | Guarantee rule | 3 days | Trust that turns into the next request |
| Bottom of Funnel | Permission request | After the job, a separate request to quote the customer's words | Text | One question; how the quote would be used | Explicit and separate from the review question | Product | Terms of service clause | 1 day | Feeds the proof table only with permission |

## Search ad drafts, zone template

Lengths checked: headlines at most 30 characters, descriptions at most 90. Merge fields are filled per zone from the zone record. The guarantee headline runs only where the zone's covered hours are on the landing page.

<!-- sheet: Ad_Copy -->
| Type | Text | Length | Note |
|---|---|---|---|
| Headline | Text Us When a Pipe Bursts | 26 | |
| Headline | Emergency Plumbing by Text | 26 | |
| Headline | Dispatch to Licensed Plumbers | 29 | Says SOS SMS dispatches |
| Headline | One Text Reaches Local Pros | 27 | Holds only in zones at density |
| Headline | Trip Charge Shown Upfront | 25 | |
| Headline | Arrival Time When They Accept | 29 | |
| Headline | No App. No Phone Tree. | 22 | |
| Headline | Water Leaking? Text Us Now | 26 | Problem ad groups |
| Headline | Sewer Backup? Text for Help | 27 | Problem ad groups |
| Headline | Ceiling Dripping? Text Us | 25 | Problem ad groups |
| Headline | Steps to Stop the Water Now | 27 | The first reply delivers this |
| Headline | Only One Pro Gets Your Info | 27 | Only once the broadcast hides identity (Phase 6 drill 5) |
| Headline | Plumbers Near {{zone name}} | 14 plus the zone name | Per zone; at most 30 once filled |
| Headline | 90 Minutes or Trip Charge Back | 30 | The guarantee (decision 3); scope on the landing page |
| Description | Text what broke. Vetted local plumbers on SOS SMS see it at once. Trip charge shown first. | 90 | |
| Description | Get steps to stop the water right away, then a licensed plumber with an arrival time. | 85 | |
| Description | We dispatch local licensed, insured plumbers. Only the one who accepts gets your address. | 89 | Second sentence only once the broadcast hides identity |
| Description | Fire, gas smell, or anyone hurt? Call 911 first. For leaks and backups, text SOS SMS. | 85 | The safety line |

## Production order

1. Confirm paid search eligibility with Google in writing (decision 11) and register the number for A2P 10DLC (decision 9, S32). Without both, Channel 1 cannot start.
2. The stop-the-water first reply, the guarantee in full, and how it works. Nothing else is honest without them; they carry decisions 2, 3, and 5.
3. The zone landing page template, message asset verification, and the emergency ad groups for the first zone.
4. The first five problem guides, reviewed by a founding contractor; then the problem ad groups pointed at them.
5. Product loops: contact card, forwardable card, refund text, READY.
6. Microsoft Ads import; the prevention campaign before the first freeze.

## Name collision note

A web search for "SOS SMS" returns several unrelated local plumbing companies with "SOS" in their names (decision 10: a US trademark search and a search check in the zone, in Stage 0). In paid search this has a direct cost: brand searches for "SOS" may belong to someone else, and an ad that reads like theirs invites confusion. Use the full name in every ad and on every page, and make the saved contact card, not the name, the main way customers come back.
