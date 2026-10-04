# Channel engine: customers (paid search, problem pages, product loops)

Load for: any search ad, landing or zone page, problem guide, first reply, or loop text, and every customer template. Distills Run 2 Phase 8 (`phase-8-assets-library.md`, product-led revision 2026-10-01) and the paid search rules. Templates: `templates/search-ad.md`, `templates/landing-page-zone.md`, `templates/problem-guide.md`, `templates/first-reply-sms.md`.

## Thesis
Emergency demand shows up as a search. Meet it there, answer the urgent question first, and let the product convert: the first reply helps before it asks for anything. Paid search is the liquidity engine of a new zone; problem pages and loops are the profit engine of a mature one. No outreach to homeowners, ever.

## The three channels
1. **Paid search, Google then Microsoft.** Emergency ad groups with text-from-ad; problem ad groups landing on problem guides; a capped seasonal prevention campaign before the first freeze; a negative keyword list (jobs, schools, DIY parts, other cities, competitor brands) reviewed weekly.
2. **Problem-solving pages.** Problem guides (ceiling leak, sewer backup, water heater), prevention guides, the readiness scorecard, zone pages, and the pages everything links to: how it works, the guarantee in full, privacy in plain words.
3. **Product loops.** Stop-the-water first reply, saved contact card, forwardable card, Text READY, automatic refund text, permission request.

## Paid search rules (hard)
- **Density first.** Ads run only in zones and hours at the density number. Acceptance below threshold pauses the zone automatically (conflict G).
- **Never pose as the plumber.** Every ad and page says SOS SMS dispatches licensed, insured contractors.
- **No Local Services Ads.** Reselling or re-routing leads is barred (S70). Standard search ads: plumbing is not on Google's US restricted list (S71), but confirm in writing first (decision 11).
- **Message assets (S72).** Verified business details, a stated response time, automated replies that say so, a defined human handoff.
- **Claims.** No superlatives, no arrival averages, no "24/7" unless the zone's covered hours are. The guarantee appears with its scope on the landing page (decision 3).
- **Safety.** The safety line on every landing page and in one ad description.
- **Brand terms.** No bids on "SOS plumbing" (decision 10).
- **Optimize for a paid request**, not a click or a first text. Cost per paid job by zone decides spend.

## Ad drafts, zone template (headlines max 30 characters, descriptions max 90)

| Text | Condition |
|---|---|
| Text Us When a Pipe Bursts | |
| Dispatch to Licensed Plumbers | |
| One Text Reaches Local Pros | Zones at density only |
| Trip Charge Shown Upfront | |
| Arrival Time When They Accept | |
| No App. No Phone Tree. | |
| Water Leaking? Text Us Now / Sewer Backup? Text for Help / Ceiling Dripping? Text Us | Problem ad groups |
| Steps to Stop the Water Now | |
| Only One Pro Gets Your Info | Only once the broadcast that hides identity ships (decision 4) |
| Plumbers Near {{zone name}} | Per zone; at most 30 characters once filled |
| 90 Minutes or Trip Charge Back | The guarantee (decision 3); scope on the landing page |
| Text what broke. Vetted local plumbers on SOS SMS see it at once. Trip charge shown first. | |
| Get steps to stop the water right away, then a licensed plumber with an arrival time. | |
| Fire, gas smell, or anyone hurt? Call 911 first. For leaks and backups, text SOS SMS. | The safety description |

## Method: plan, write, edit
1. **Plan.** Confirm the zone is at density and the covered hours. Pick the ad group (emergency, problem, prevention) and its landing page. List the merge fields the asset carries.
2. **Write.** Name the problem, then the next step, then the mechanic. Value before payment. Use `value-proposition-customers.md` drills.
3. **Edit.** Count characters. Run `ops/QA-checklist.md`, the search ads block included.

## Production order
1. Google eligibility in writing and carrier registration (S32). Without both, nothing starts.
2. The first reply, the guarantee in full, how it works (wait on decisions 3, 4, 5).
3. The zone landing page template, message asset verification, emergency ad groups.
4. The first five problem guides, reviewed by a founding contractor, then problem ad groups.
5. Loops: contact card, forwardable card, refund text, READY.
6. Microsoft import; the prevention campaign before the first freeze.

## Dropped, and why
Partnerships with agents, inspectors, hardware stores, and homeowner associations, and posts in neighborhood groups: both need outreach, which the product-led motion rules out.
