# Phase 4. ICP Dashboard, customer side

Per `../SKILL-ADAPTATION.md`, this is the B2C rewrite. The buyer is a household, and what defines them is a trigger event, not a company stage. The skill's row names are kept so the dashboard lines up with Run 1; where a row means something different for a household, the label says so.

- **Level 1, no go-to contractor.** New to the home or the area, or has never needed a plumber.
- **Level 2, a go-to contractor who does not answer at night.** Has someone they use, who is not available after hours or on weekends.

Run 2 starts here only after Run 1's Step 5.2 has set the founding zone. Every row below applies inside that zone.

## Step 4.1. Two-level ICP

<!-- sheet: ICP -->
| Attribute | ICP Level 1: no go-to contractor | ICP Level 2: contractor who does not answer at night |
|---|---|---|
| Segment | Homeowners in the founding zone with no plumber they would call | Homeowners in the founding zone who have a plumber, but not one who answers after hours |
| Sub-industries (read as: trigger categories) | Burst or leaking pipe, overflowing toilet, sewer backup, failed water heater, water coming through a ceiling | Same |
| Location | Founding zone {TBD}, inside the radius where a contractor can arrive within 90 minutes | Same |
| Revenue, $ (read as: household income band) | Dropped unless the research ties income to willingness to pay a trip charge. None does yet. {TBD} | Same |
| Team Size (read as: household type) | Owner-occupier, often a recent buyer | Owner-occupier, established |
| Business Maturity (read as: time in the home) | Under about two years, or new to the area | Several years; knows the house's weak points |
| Business Model (read as: how they have paid for repairs before) | Unknown or never; may have a warranty from the purchase | Directly to their usual contractor; sometimes a warranty or an insurance claim |
| Best Engagement Model | Self-serve, at the moment of need: a search ad or a problem page, then a text; the stop-the-water first reply before any payment | Same, when their usual contractor does not answer; after the first job, a saved number |
| Organization Challenges and Pain Points (read as: what goes wrong) | Does not know who to trust; does not know where the shutoff is; does not know what a fair price is | Their contractor's voicemail at 2 a.m.; after-hours fees they did not expect; no-shows (S50, S51) |
| Why Should They Choose Us (Value Proposition Hypothesis) | One text reaches vetted contractors; an arrival time when one accepts; the trip charge stated before anyone comes | The text to send when their usual contractor does not answer, with an arrival window that is money-backed |
| Strategic Goals (read as: what the household wants) | Stop the damage; avoid being overcharged by a stranger; get it handled tonight | Stop the damage; not wait until morning; keep their usual contractor for daytime work |
| Triggers | The emergency itself; moving into a home (pre-need); a neighbor's flood story; the first freeze of the season | The emergency after hours; their contractor retiring or getting booked up; a bad experience with an emergency call |

### Rows added for this side

<!-- sheet: ICP -->
| Attribute | ICP Level 1 | ICP Level 2 |
|---|---|---|
| Time of day of the trigger | Any; the night and weekend cases are where SOS SMS differs most | Night and weekend by definition |
| Home age and type | Any. Older housing stock raises the odds of plumbing failures; the median owner-occupied home is 42 years old (S63) | Same |
| Card and smartphone at hand | Needed to pay the trip charge by text. 76.4 percent of households had a credit card in 2023 and 4.2 percent were unbanked (S61), so some households cannot pay this way | Same |
| How they found help last time | Search, or a neighbor's recommendation (S26, S27) | Their usual contractor |
| Renter or landlord | Renters call the landlord first; excluded from this run (open decision 1) | Small landlords who own one or two rentals may fit Level 2; confirm in research |
| Fit for the 90-minute guarantee | Good inside the zone; outside it, do not sell | Same |
| Disqualifiers | Life-safety emergencies (gas, fire, injury), which go to 911 and the utility first (S60); outside the zone | Same |

## Market context

Orientation only; the zone's numbers are {TBD}.

<!-- sheet: Market_Context -->
| Measure | Figure | Source |
|---|---|---|
| Owner-occupied housing units | 85.7 million of 131.3 million occupied units (2023) | S62 (A) |
| Homeownership rate | About 65.6 percent (2024) | S62 (A) |
| Median age of owner-occupied homes | 42 years (2024) | S63 (B) |
| Water damage and freezing claims | 27.6 percent of homeowners claims in 2022; about 1 in 60 insured homes a year; average $13,954 (2018 to 2022) | S57 (B) |
| Owner-occupied homes in the founding zone | {TBD} | Census tract data, once the zone is set |

## Which level goes first, and why

Revised 2026-10-01 for the product-led motion. **Both levels are reached at the same moment: when they search for help.** Level 1 searches because they have no one to call; Level 2 searches after their usual plumber does not answer. Bottom-of-funnel search ads and problem pages meet both, and the stop-the-water first reply converts both.

Recommendation: buy the first request from each household through paid search, inside zones at density, and earn every request after it through the product loops: the saved contact card, the post-job share, and Text READY. The owned share of requests is what makes the second household request cheaper than the first (`../../marketplace/speed-to-scale-plan.md`, section 5).
