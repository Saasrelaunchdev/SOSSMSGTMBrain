# Phase 5. Buying Committee Dashboard, member side

Per `../SKILL-ADAPTATION.md`, the committee is a household: one or two adults decide, over days, at a kitchen table or in an inbox, before anything breaks. One column, filled honestly, for each ICP level: the person who reads the partner's offer or the email, the person who holds the card, and the household's decision are often the same person. No procurement process is invented. Revised 2026-10-11, the membership revision.

## Step 5.1. Purchasing committee personas

### ICP Level 1: a new homeowner without a go-to contractor

<!-- sheet: ICP1_Personas -->
| Attribute | The household (user, manager, and decision maker; often one person) |
|---|---|
| Possible Job Titles (read as: who they are) | Homeowner, often a recent buyer or new to the area; sometimes an adult child setting it up for a parent |
| Responsibility Area | Setting up the new home's services, and deciding who to trust with the house |
| Purchasing Influence | Total. One or two adults, deciding over days; the person who holds the card often has the final word |
| Core Customer Journey Stages | Awareness through joining over days or weeks; Value Realization only when something breaks, which may be months later; renewal each month or year |
| Potential Reasons to Block | "Another subscription"; "it rarely happens"; "is my home covered at night"; "what does it cost when I use it"; a card on file with a company they do not know yet; "can I cancel" |
| Drivers | Feeling ready in a new home; someone to reach at night; the cost known in advance; vetted contractors; nothing to do in the emergency but one text |
| Assets to Get Buy-In | The readiness scorecard; the membership page: the three plans and their prices, the $99 trip charge on use and credited to the repair, the guarantee with its plans and scope, what is not included, cancel any time; a trusted partner's mention; the privacy line |
| Channels to Find Them | Before the need: utility new-account offers, association welcome packets, the readiness scorecard, prevention guides, and agents and inspectors who share SOS SMS without payment. In open zones, search and social for sign-ups |

### ICP Level 2: an established homeowner whose contractor does not answer at night

<!-- sheet: ICP2_Personas -->
| Attribute | The household (user, manager, and decision maker; often one person) |
|---|---|
| Possible Job Titles (read as: who they are) | Established homeowner, usually in an older home; sometimes a small landlord with one or two rentals |
| Responsibility Area | Same as Level 1, plus keeping their usual contractor relationship |
| Purchasing Influence | Total. Often decided in the days after a bad night, or as the first freeze comes |
| Core Customer Journey Stages | Awareness after an emergency where nobody answered, or at freeze season; joins over days; keeps their usual contractor for daytime work |
| Potential Reasons to Block | Loyalty to their usual contractor; "how is this different from my warranty"; "another subscription"; expects a catch in the trip charge |
| Drivers | Not waiting until morning next time; an arrival window that costs SOS SMS money when missed; the trip charge credited if the work goes ahead; cancel any time |
| Assets to Get Buy-In | The same membership page, plus a plain comparison with warranties, plumbing plans, and HVAC clubs (they pay for repairs or maintenance; SOS SMS gets someone there) and a clear line that they keep their usual contractor for daytime work |
| Channels to Find Them | Email from their association or insurance agent (existing policyholders); prevention guides; search at freeze season; a neighbor's forwarded card |

### The renter exception

A renter's landlord is a second decision maker, usually the payer, and the owner of the plumbing. That is why renters are outside this run (brief decision 1: homeowners). A small landlord who owns a rental may join in their own right, one membership per address (R54).

## Step 5.2. Design partner profile: the launch zone's member area

For the member side this is a geographic boundary, not a design partner in the B2B sense: the neighborhoods inside Run 1's first contractors' coverage, where memberships open once the density number is met (R55). Before then, the same households join the launch list: email, no charge, no service promised. It keeps the 90-minute guarantee honest. Every Phase 8 asset targets inside it and nowhere else.

<!-- sheet: Design_Partners -->
| Attribute | Specification |
|---|---|
| Design Partner Attributes | Homeowners living inside a zone where Run 1's density number is met in all three trades at every hour, so memberships are open there (R55) |
| Job Titles (read as: who) | Owner-occupiers; recent buyers are the easiest to reach, through partners at moving in |
| Demographics | Inside the launch zone, a 10-mile radius in the founders' home metro; older housing stock raises the odds of an emergency (S63) |
| Responsibility Areas | Their own home |
| Current Tools | Phone search; neighborhood apps and groups; their usual contractor's number; sometimes a warranty or a utility-partner plan |
| Key Pain Points | No one answering at night; surprise fees; no-shows; floods of calls from quote sites; slow claims (S20, S48, S50, S51) |
| Critical Triggers | Moving in; the first freeze; a neighbor's story; an emergency where nobody answered |
| Goals and Motivations | Be ready before something breaks, and have it handled tonight when it does, without being overcharged |
| Decision Criteria | The price and what it includes; the trip charge on use; the covered neighborhoods, at any hour; when dispatch starts (30 days on the monthly plan, at once on the annual); vetted contractors; cancel any time; privacy |
| Influence Level | Neighbors trust neighbors' recommendations ahead of online reviews (S26), so one member's story in a street travels |
| Barriers to Purchase | Another subscription; a card on file with a new company; outside an open zone; "it rarely happens" |
| Information Sources | Their utility, association, newsletter, or insurance agent; prevention guides; neighbors' forwarded cards |
| Success Metrics | Launch list sign-ups per 1,000 homes; joins by plan and cost per new paid member by channel, against the plan's ceiling (R63); monthly churn and annual renewal; share of requests accepted inside the window, by trade; share arriving within 90 minutes; late arrivals and no-shows per 100 accepted requests |
| Early Adopter Characteristics | Comfortable doing business by text; has had a bad emergency experience; active in neighborhood groups; already pays for a plan or two |

### Sizing the zone

<!-- sheet: Design_Partners -->
| Input | Value | Note |
|---|---|---|
| Contractors per trade needed for coverage | 9 per trade, 27 across plumbing, HVAC, and electrical (Run 1 Phase 5 density table) | At a planned acceptance rate of 0.30 for 95 percent coverage (R28), measured in Stage 1 |
| Zone radius | 10 miles (R27) | Must allow arrival within 90 minutes from where contractors are |
| Owner-occupied homes in the zone | Counted in Stage 0 (R41) | Census tract data (ACS) inside the radius |
| Requests per member | Planning value 0.25 a year (R58) | 26 percent of homeowners reported a blocked or overflowing toilet emergency in a year (S82); about 20 percent in 2024 (S83). Do not estimate the trigger rate from insurance claim frequency: most emergencies never become claims |
| Members per zone | Planning value about 410 (R64) | About one request a month for each of the 9 contractors in the first cohort: 9 × 12 ÷ 0.25 |
| Expected requests per month | Measured over the zone's first 8 weeks open (R42) | Members × requests per member ÷ 12 until it is measured |

### The member-side permission rule

Proof capture starts with the first member. The member terms carry a plain-language clause asking whether SOS SMS may quote the member's words about their experience, in what form, and whether they may be named. A follow-up text after the job asks two questions: did someone arrive within the window, and would you tell a neighbor. Answers are recorded verbatim with the date. A quote enters the proof table only with permission on record.
