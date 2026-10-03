# Phase 5. Buying Committee Dashboard, customer side

Per `../SKILL-ADAPTATION.md`, the committee collapses. Whoever is at home with the problem decides, at that moment. One column, filled honestly, for each ICP level, rather than an invented Manager and Decision Maker.

## Step 5.1. Purchasing committee personas

### ICP Level 1: no go-to contractor (committee collapses)

<!-- sheet: ICP1_Personas -->
| Attribute | The person at home with the problem (all three roles) |
|---|---|
| Possible Job Titles (read as: who they are) | Homeowner, often a recent buyer; sometimes an adult child helping a parent |
| Responsibility Area | Stopping the damage now and deciding who to let into the house |
| Purchasing Influence | Total, in the moment |
| Core Customer Journey Stages | Problem Awareness through Purchase in minutes; Value Realization within the hour |
| Potential Reasons to Block | A text with a payment link from an unknown number looks like a scam (S59); no card at hand; fear of being overcharged by a stranger; would rather call a voice |
| Drivers | Someone coming, with a time; knowing the cost before anyone comes; a vetted contractor; not being flooded with calls |
| Assets to Get Buy-In | The first reply text that says who SOS SMS is, what happens next, and the trip charge before any link; the contractor's name, rating, and arrival time |
| Channels to Find Them | In the moment: Google and Microsoft search ads and problem pages. After the first job: the saved contact card |

### ICP Level 2: a contractor who does not answer at night (committee collapses)

<!-- sheet: ICP2_Personas -->
| Attribute | The person at home with the problem (all three roles) |
|---|---|
| Possible Job Titles (read as: who they are) | Established homeowner; sometimes a small landlord with one or two rentals |
| Responsibility Area | Same as Level 1, plus keeping their usual contractor relationship |
| Purchasing Influence | Total, in the moment |
| Core Customer Journey Stages | Tries their usual contractor first; reaches SOS SMS at Solution Discovery |
| Potential Reasons to Block | Loyalty to their usual contractor; the same payment-link trust problem; expects the after-hours price to be a trap |
| Drivers | Not waiting until morning; an arrival window that costs SOS SMS money if missed; the trip charge credited if the work goes ahead |
| Assets to Get Buy-In | The same first reply; a clear line that they can keep their usual contractor for daytime work |
| Channels to Find Them | In the moment, after their usual contractor does not answer: search ads and problem pages. After the first job: the saved contact card and neighbors' shares |

### The renter exception

A renter's landlord is a second decision maker and usually the payer. That is why renters are outside this run (open decision 1). A small landlord who owns a rental may be a Level 2 customer in their own right, paying for a repair at a property they do not live in.

## Step 5.2. Design partner profile: the founding customer area

For the customer side this is a geographic boundary, not a design partner in the B2B sense: the neighborhoods inside Run 1's founding contractor coverage. It keeps the 90-minute guarantee honest. Every Phase 8 asset targets inside it and nowhere else.

<!-- sheet: Design_Partners -->
| Attribute | Specification |
|---|---|
| Design Partner Attributes | Homeowners living inside a zone where Run 1's density target is met for the hours the guarantee covers |
| Job Titles (read as: who) | Owner-occupiers; recent buyers are the easiest to reach before an emergency |
| Demographics | Inside the founding zone {TBD}; older housing stock raises trigger frequency (S63) |
| Responsibility Areas | Their own home |
| Current Tools | Phone search; neighborhood apps and groups; their usual contractor's number |
| Key Pain Points | No one answering at night; surprise fees; no-shows; floods of calls from quote sites (S48, S50, S51) |
| Critical Triggers | The emergency; moving in; the first freeze; a neighbor's story |
| Goals and Motivations | Get it stopped and fixed tonight without being overcharged |
| Decision Criteria | Someone coming, with a time; cost known first; vetted; not a scam |
| Influence Level | Neighbors trust neighbors' recommendations ahead of online reviews (S26), so one good experience in a street travels |
| Barriers to Purchase | Payment-link trust; no card; outside the zone; preference for a voice call |
| Information Sources | Search results at the moment of need; neighbors' shared contact cards; problem guides |
| Success Metrics | Requests per 1,000 homes in the zone; share accepted within the window; share arriving within 90 minutes; refund rate; saved-number rate from READY |
| Early Adopter Characteristics | Comfortable doing business by text; has had a bad emergency experience; active in neighborhood groups |

### Sizing the zone

<!-- sheet: Design_Partners -->
| Input | Value | Note |
|---|---|---|
| Contractors per trade needed for coverage | From Run 1 Phase 5 density table | Depends on acceptance rate, {TBD} |
| Zone radius | {TBD} | Must allow arrival within 90 minutes from where contractors are |
| Owner-occupied homes in the zone | {TBD} | Census tract data |
| Expected requests per month | Homes × trigger rate × share who text SOS SMS, all {TBD} | Do not estimate the trigger rate from insurance claim frequency: most emergencies never become claims |

### The customer-side permission rule

Proof capture starts with the first customer. The terms of service carry a plain-language clause asking whether SOS SMS may quote the customer's words about their experience, in what form, and whether they may be named. A follow-up text after the job asks two questions: did someone arrive within the window, and would you tell a neighbor. Answers are recorded verbatim with the date. A quote enters the proof table only with permission on record.
