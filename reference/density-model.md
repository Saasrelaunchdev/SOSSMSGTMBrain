# Density model

Load for: deciding where and when customer copy and paid search may run, sizing the founding cohort, and any "how many contractors" question. Distills Run 1 Phase 5 (`sources/raw/gtm/run-1-supply-contractors/output/phase-5-buying-committee.md`) and the launch gates.

## The formula
For one trade, one zone, and one hour band:

- n, the contractors who receive a request
- a, the chance any one accepts within the acceptance window ({TBD}, measured in the founding period)
- c, the target chance that at least one accepts

The chance at least one accepts is 1 - (1 - a)^n, so **n ≥ ln(1 - c) / ln(1 - a)**.

## Illustrative table (a is unknown)

| Acceptance chance (a) | 90 percent coverage | 95 percent | 99 percent |
|---|---|---|---|
| 0.10 | 22 | 29 | 44 |
| 0.15 | 15 | 19 | 29 |
| 0.20 | 11 | 14 | 21 |
| 0.30 | 7 | 9 | 13 |
| 0.40 | 5 | 6 | 10 |

## How to read it
- Acceptance varies by hour: lower at 2 a.m. than at 2 p.m. Compute per hour band. The guarantee may be offered only in the hours and zones where coverage is met: those are the covered hours.
- Contractors do not decide independently. A freeze night fills every schedule at once. Treat n as a floor and over-recruit for nights, weekends, and freezes.
- Acceptance is not arrival. A contractor must be close enough to arrive inside 90 minutes, which caps the zone radius ({TBD} per metro).

## What the number gates
- **Stage 1 to Stage 2.** Demand opens only when the density number is met for the first trade, zone, and covered hours (`launch-and-growth.md`).
- **Paid search.** Campaigns are geofenced to zones at density and scheduled to covered hours; acceptance below threshold pauses them (conflict G).
- **Copy.** "Reaches the vetted contractors on SOS SMS for your trade" is only written for zones at density. Never "every contractor in your area".

## What founding contractors get and commit to (proposals, none decided)

| Get | Commit to |
|---|---|
| The first requests in their zone | Responding within {TBD} minutes when marked available |
| A say in dispatch, payouts, and disputes | Crediting the trip charge when the customer goes ahead |
| Founding terms held for {TBD} if a fee is introduced | Keeping license and insurance current |
| Support by text from the founders | A three-question text after their first five jobs |
| | A permission clause on citing their outcomes, asked before the first job |

The permission clause is the only route to a proof point. Without it the proof-point set stays empty.
