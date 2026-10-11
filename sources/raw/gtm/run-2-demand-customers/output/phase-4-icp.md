# Phase 4. ICP Dashboard, member side

Per `../SKILL-ADAPTATION.md`, this is the B2C rewrite. The buyer is a household joining a membership before anything breaks, and what defines them is a readiness trigger, not a company stage. The skill's row names are kept so the dashboard lines up with Run 1; where a row means something different for a household, the label says so. Revised 2026-10-11, the membership revision.

- **Level 1, a new homeowner without a go-to plumber.** Recently bought or moved, and has no one they would call.
- **Level 2, an established homeowner whose plumber does not answer at night.** Usually an older home; has someone they use, who is not available after hours or on weekends.

Memberships open in a zone only once Run 1's density number is met there (R55). Every row below applies inside an open zone; before it opens, the same households join the launch list.

## Step 4.1. Two-level ICP

<!-- sheet: ICP -->
| Attribute | ICP Level 1: new homeowner without a go-to plumber | ICP Level 2: established homeowner whose plumber does not answer at night |
|---|---|---|
| Segment | Homeowners in an open zone who recently bought or moved, with no plumber they would call | Homeowners in an open zone, usually in an older home, who have a plumber but not one who answers after hours |
| Sub-industries (read as: the emergencies the membership is for) | Burst or leaking pipe, overflowing toilet, sewer backup, failed water heater, water coming through a ceiling | Same |
| Location | An open zone: a 10-mile radius in the founders' home metro where memberships are open at the density number (R27, R55) | Same |
| Revenue, $ (read as: household income band) | Not a targeting criterion (decided, R39): no research ties income to joining a home repair membership. Members are targeted by zone and by readiness triggers | Same |
| Team Size (read as: household type) | Owner-occupier, often a recent buyer; first-time buyers were 24 percent of buyers in the 2024 profile (S91) | Owner-occupier, established; sometimes a small landlord with one or two rentals, one membership per address (R54) |
| Business Maturity (read as: time in the home) | Under about two years, or new to the area | Several years; knows the house's weak points |
| Business Model (read as: how they pay for home repairs today) | Unknown or never; may hold a home warranty from the purchase | Directly to their usual contractor; sometimes a warranty, a utility-partner plan, or an insurance claim |
| Best Engagement Model | Self-serve, before the need: a partner's mention at moving in, the readiness scorecard, or a prevention guide, then the membership page; about 3 minutes to join (R54) | Self-serve, before the next one: an email from their association or insurance agent, a prevention guide, or a search at freeze season, then the membership page |
| Organization Challenges and Pain Points (read as: what goes wrong) | Does not know who to trust or who would come at night; does not know where the shutoff is; does not know what a fair call-out costs | Their plumber's voicemail at 2 a.m.; after-hours fees they did not expect; no-shows (S50, S51); a warranty claim that took days (S20) |
| Why Should They Choose Us (Value Proposition Hypothesis) | Ready before anything breaks: one number saved, the card and address on file, so the emergency is one text to vetted contractors, with an arrival time when one accepts and the 90-minute guarantee | The text to send when their plumber does not answer: many vetted contractors at once, a money-backed window, and their own plumber kept for daytime work |
| Strategic Goals (read as: what the household wants) | Feel ready in a new home; avoid being overcharged by a stranger; have someone to reach at night | Not wait until morning next time; stop the damage; keep their usual contractor for daytime work |
| Triggers | Moving in and setting up services; the first freeze; a neighbor's flood story; a home inspection that flagged old plumbing | An emergency where nobody answered; a warranty claim denied or slow; their plumber retiring or booked up; freeze season |

### Rows added for this side

<!-- sheet: ICP -->
| Attribute | ICP Level 1 | ICP Level 2 |
|---|---|---|
| Time of day of the emergency | Any; the night and weekend cases are where membership differs most | Night and weekend by definition |
| Home age and type | Any. Older housing stock raises the odds of plumbing failures; the median owner-occupied home is 42 years old (S63) | Same |
| Card and smartphone at hand | Needed to join: the card goes on file at joining, and the request is a text. 76.4 percent of households had a credit card in 2023 and 4.2 percent were unbanked (S61), so some households cannot join this way; a text from a non-member gets the free help by text (R57) | Same |
| How they found help last time | Search, or a neighbor's recommendation (S26, S27) | Their usual contractor |
| What they already pay for | Often nothing; sometimes a home warranty from the purchase | Sometimes a warranty or a utility-partner plan. Those pay for repairs; SOS SMS gets someone there. Many will hold both |
| Renter or landlord | Renters call the landlord first; members are homeowners (brief decision 1) | Small landlords who own one or two rentals may fit Level 2: one membership per address (R54) |
| Fit for the 90-minute guarantee | Good inside an open zone; outside it, the launch list, never a membership | Same |
| Disqualifiers | Homes outside an open zone; renters. Life-safety emergencies (gas, fire, injury) go to 911 and the utility first, member or not (S60) | Same |

## Market context

Orientation only; the zone's own numbers are counted from Census tract data when the zone is drawn in Stage 0.

<!-- sheet: Market_Context -->
| Measure | Figure | Source |
|---|---|---|
| Owner-occupied housing units | 85.7 million of 131.3 million occupied units (2023) | S62 (A) |
| Homeownership rate | About 65.6 percent (2024) | S62 (A) |
| Median age of owner-occupied homes | 42 years (2024) | S63 (B) |
| Home repair emergencies | Almost 81 percent of homeowners reported one in the past year; a blocked or overflowing toilet, 26 percent; pipe breaks the top worry, 49 percent (2025 survey) | S82 (B) |
| Existing-home sales | 4.06 million in 2024; first-time buyers 24 percent (2024 profile), 21 percent (2025) | S91 (A, B) |
| Households already on a partner-sold repair plan | HomeServe: more than 1,300 utility, municipal, and association partners; over 4.6 million customers | S93 (A) |
| Water damage and freezing claims | 27.6 percent of homeowners claims in 2022; about 1 in 60 insured homes a year; average $13,954 (2018 to 2022) | S57 (B) |
| Owner-occupied homes in the founding zone | Counted in Stage 0 | Census tract data (ACS) inside the 10-mile radius, when the zone is drawn (R41) |
| Member base per zone | Planning value about 430 members: about one request a month for each of 9 founding contractors | R64 (R08, R58) |

## Which level goes first, and why

Revised 2026-10-11, the membership revision. **Both levels join before the need, through the partners and lists that already reach them, never through an ad at the moment of the emergency.** Level 1 is reached at moving in: utility new-account offers, association welcome packets, the readiness scorecard, and agents and inspectors who share SOS SMS without payment (R61). Level 2 is reached through email from its association or insurance agent, prevention guides, and search at freeze season.

The plan: grow each zone's launch list during Stage 1 with the readiness scorecard, prevention guides, and affiliates signed with codes ready; email the launch list first when memberships open; then let affiliates and email carry sign-ups, with search and social for sign-ups in support. Every member also brings the next one through the product loops: the forwardable contact card, the two questions after a job, and Text READY. Cost per new paid member is measured by channel against the ceiling (R63; `../../marketplace/speed-to-scale-plan.md`, section 5).
