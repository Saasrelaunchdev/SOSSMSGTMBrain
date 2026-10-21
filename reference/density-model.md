# Density model

Load for: deciding where and when memberships open and member copy and sign-up ads may run, sizing the first cohort in each trade and the member base, and any "how many contractors" question. Distills Run 1 Phase 5 (`sources/raw/gtm/run-1-supply-contractors/output/phase-5-buying-committee.md`, revised 2026-10-20 for three trades) and the launch gates.

## The formula
For one trade, one zone, and one hour band:

- n, the contractors who receive a request
- a, the chance any one accepts within the 10-minute response window: planning value 0.30 (R28), measured by trade and hour band with test requests in Stage 1
- c, the target chance that at least one accepts

The chance at least one accepts is 1 - (1 - a)^n, so **n ≥ ln(1 - c) / ln(1 - a)**.

## Illustrative table (0.30 is the planning value)

| Acceptance chance (a) | 90 percent coverage | 95 percent | 99 percent |
|---|---|---|---|
| 0.10 | 22 | 29 | 44 |
| 0.15 | 15 | 19 | 29 |
| 0.20 | 11 | 14 | 21 |
| 0.30 | 7 | 9 | 13 |
| 0.40 | 5 | 6 | 10 |

## How to read it
- Acceptance varies by trade and hour: lower at 2 a.m. than at 2 p.m. Compute each of the three trades separately, per hour band. A zone opens only when each trade meets the number in every hour band, every day; an open zone is then covered every hour, with no covered hours to name (R15, R55). If a band later falls below, requests still go out at once, sign-ups pause (R34), and recruiting for that trade and band comes first.
- Contractors do not decide independently. A freeze night or a heat wave fills every schedule in a trade at once. Treat n as a floor and over-recruit for nights, weekends, freezes, and heat waves.
- Acceptance is not arrival. A contractor must be close enough to arrive inside 90 minutes, which caps the zone radius: 10 miles in the launch zone (R27), since 90 minutes less up to 15 to accept and about 20 to get on the road leaves about 55 to drive.

## What the number gates
- **Stage 1 to Stage 2.** Memberships open only when the density number is met for each of the three trades in the first zone, in every hour band: 27 places (R08, R55, `launch-and-growth.md`). Before then, the launch list.
- **Sign-ups.** Paid social, affiliate links, and the membership page sell only in open zones; acceptance in any trade below 90 percent over 7 days pauses sign-ups automatically: paid social stops and affiliate links show the launch list (R34, conflict G).
- **Copy.** "Reaches the vetted contractors on SOS SMS for your trade" is only written for open zones. Never "every contractor in your area".

## The member side of the same arithmetic
Contractors stay active only if requests arrive, and each trade has its own rate. Planned at 0.50 requests a member a year (R58): plumbing 0.25, HVAC 0.20, electrical 0.05; Premier 1.5 times, for a second home. At the plan mix, about 410 members (R64) keep each of the 9 plumbers in the first cohort at about one request a month; an HVAC contractor then sees about 0.8 a month and an electrician about one every 5 months. Every contractor is told the expected volume for their trade, and contractor activity is judged over 30 days in plumbing and HVAC and over 6 months in electrical (R32). Requests per month by trade are counted over the zone's first 8 weeks open (R42). Grow the launch list during Stage 1 so the zone opens with members waiting.

## What every contractor gets and commits to (decided)

The same terms for every contractor, in every trade and zone, from the first job (R03, R12).

| Get | Commit to |
|---|---|
| Every matched request in their trades and area, at the same moment as every other matched contractor | Responding within 10 minutes when marked available (R12) |
| $0 to join and per request; $25 per completed paid job from the first job, so $74 of the $99 (R03) | Crediting the trip charge when the member goes ahead |
| The trip charge collected before they roll, paid out within 2 business days of arrival (R14); kept on a late arrival (R67) | Keeping the license for each trade they take, and insurance, current (decision 7) |
| Support by text: HELP reaches a person | A three-question text after their first five jobs |
| | A permission clause on citing their outcomes, asked before the first job |

The permission clause is the only route to a cited result. Until one exists, every drill uses its method line and its named record (R44, R45). The first cohort target is 9 contractors per trade, the density number at 0.30 for 95 percent coverage: 27 places across plumbing, HVAC, and electrical; a shop licensed in more than one trade counts in each (R08).
