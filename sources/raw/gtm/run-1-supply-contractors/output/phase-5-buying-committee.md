# Phase 5. Buying Committee Dashboard, contractor side

Per `../SKILL-ADAPTATION.md`: the three-person committee holds for shops with technicians (ICP Level 2) and collapses for owner-operators (ICP Level 1). Step 5.2 is the deliverable of this run, because it defines the founding contractor cohort and the launch area Run 2 sells into.

## Step 5.1. Purchasing committee personas

### ICP Level 1: owner-operator (committee collapses)

The owner-operator is the User, the Manager, and the Decision Maker. One column, filled once, rather than three invented personas.

<!-- sheet: ICP1_Personas -->
| Attribute | Owner-operator (all three roles) |
|---|---|
| Possible Job Titles | Owner, Master Plumber, Licensed Plumber, Owner-operator |
| Responsibility Area | Everything: answering the phone, quoting, doing the work, collecting payment, the books |
| Purchasing Influence | Total |
| Core Customer Journey Stages | All seven, with the most weight on Trial (first request) and Value Realization (first paid trip) |
| Potential Reasons to Block | Has been burned by a lead platform; does not want night calls they cannot take; suspects a catch in "no fees"; does not want to commit to an arrival time at 2 a.m.; does not want another app |
| Drivers | Trip paid before rolling; costs nothing when quiet; decline freely; keeps the customer for repeat work |
| Assets to Get Buy-In | The terms on one page (what you pay, when you get paid, what you commit to); "how a job works in three texts"; the Lead Cost Check if they buy any leads |
| Channels to Find Them | Cold email to their published business address; supply house counters and partner newsletters; referrals from other contractors in the product |

Possible second person, checked in the founding contractor survey: some owner-operators have a family member who handles the books or the phone. Where the survey shows it, that person is an influencer on onboarding and payout setup, not a buyer.

### ICP Level 2: small shop (committee holds)

<!-- sheet: ICP2_Personas -->
| Attribute | User | Manager | Decision Maker |
|---|---|---|---|
| Possible Job Titles | Service Technician, Journeyman Plumber, On-call Technician, Water Mitigation Technician | Dispatcher, Office Manager, Service Manager, Customer Service Lead | Owner, President, General Manager, Master Plumber |
| Responsibility Area | Rolls on jobs, diagnoses, quotes on site, collects payment for the work | The schedule, the dispatch board, answering the phone, billing | Profit and loss, marketing spend, hiring, the company's reputation |
| Purchasing Influence | Low formally, real in practice: technicians refuse jobs they think are bad | High. The gatekeeper who decides which jobs get accepted | Final say |
| Core Customer Journey Stages | Value Realization, Expansion and Advocacy | Vendor Evaluation, Trial, Value Realization | Problem Awareness through Purchase Decision, then Renewal (staying active) |
| Potential Reasons to Block | More night calls; jobs outside their skill; customers who dispute; text overload on their personal phone | Jobs that go around the dispatch board; double booking; reconciling payouts; unclear dispute handling; one more thing to watch | Distrust of platforms after shared leads and the FTC order (S01); fear of a race to the bottom on price; liability if an arrival commitment is missed; the obligations (arrival time, crediting the trip charge) |
| Drivers | Trip paid before they arrive, so no awkward collection; photos before rolling; on-call hours that pay | Fewer after-hours calls to field; payment already secured; clean records | Lower cost per booked job; no fixed fee; emergency revenue; control over hours and jobs |
| Assets to Get Buy-In | "How a job works in three texts"; a sample request with photos | A diagram of where an SOS SMS job enters their dispatch flow; a sample payout record; the dispute FAQ | The Lead Cost Check; the terms on one page; the founding contractor offer |
| Channels to Find Them | Through the owner; supply house counters; trade schools | Through the owner; partner tools they already use | Cold email; the partnership program (supply houses, PHCC chapter, S24); contractor referrals |

**The Manager is the most likely blocker.** A request accepted by text on a technician's phone goes around the dispatch board, which is the dispatcher's whole job. Onboarding for Level 2 shops has to decide who receives requests (the dispatcher, the owner, or on-call technicians) before the first one arrives.

## Step 5.2. Design partner profile: the founding contractor cohort

For a pre-launch marketplace this is the most valuable step in the run. The cohort decides where SOS SMS launches, and Run 2 cannot start Phase 4 without it.

<!-- sheet: Design_Partners -->
| Attribute | Specification |
|---|---|
| Design Partner Attributes | Licensed and insured; takes emergency calls; has spare after-hours capacity at least some nights; willing to credit the trip charge and commit to an arrival time; willing to give feedback after early jobs |
| Job Titles | Owner of a small plumbing or water damage shop (Level 2); owner-operator (Level 1) |
| Demographics | Established local business inside the founding zone, in the founders' home metro; plumbing and water emergencies first |
| Responsibility Areas | Decides which jobs the business takes and who answers after hours |
| Current Tools | Phone and text; often a free business listing; Level 2 also uses lead platforms and field service software |
| Key Pain Points | Paying for requests that never become work; unpaid trips; night calls; unpredictable slow weeks |
| Critical Triggers | A lead platform renewal or price rise; a bad month of unreplied leads; a new technician to keep busy; freeze season |
| Goals and Motivations | Emergency revenue without marketing spend; getting paid for every trip; a say in how the platform works |
| Decision Criteria | What they pay and when; when the trip charge reaches them; what they commit to; whether they can decline freely; whether the customer stays theirs |
| Influence Level | Locally high: owners know the other trades and supply counter staff, so one founding contractor can recruit others |
| Barriers to Purchase | Platform distrust; fear the guarantee will cost them; payout onboarding (identity and bank checks); "no fee" sounding too good to be true |
| Information Sources | Supply house staff; other contractors; trade associations; trade groups online |
| Success Metrics | First paid trip within 30 days of the zone opening, or of joining if later; share of trips paid before rolling; requests they chose to accept |
| Early Adopter Characteristics | Already experimenting with lead sources; vocal about lead platform frustrations; comfortable doing business by text; respected by peers |

### The density number

The member-side promises depend on enough active contractors per trade and zone. This is the number Run 2 and Phase 9 both need, and it can be estimated before launch.

For one trade, one zone, and one hour band, let:

- **n** be the number of contractors who receive a request,
- **a** be the chance that any one of them accepts within the acceptance window,
- **c** be the target chance that at least one accepts.

Then the chance at least one accepts is 1 - (1 - a)^n, so the contractors needed are **n ≥ ln(1 - c) / ln(1 - a)**.

Planning value: a, the acceptance rate, is set at 0.30 (R28), so the founding cohort target is 9 plumbing contractors for 95 percent coverage. It is measured by hour band with test requests in Stage 1, and the table shows how sharply the answer moves with it.

<!-- sheet: Density_Model -->
| Acceptance chance per contractor (a) | Contractors needed for 90 percent coverage | For 95 percent | For 99 percent |
|---|---|---|---|
| 0.10 | 22 | 29 | 44 |
| 0.15 | 15 | 19 | 29 |
| 0.20 | 11 | 14 | 21 |
| 0.30 | 7 | 9 | 13 |
| 0.40 | 5 | 6 | 10 |

How to read it:

- Acceptance is not one number. It will be lower at 2 a.m. than at 2 p.m., so the calculation runs per hour band, and the 90-minute guarantee may need to be offered only in the hours and zones where coverage is met.
- The model assumes contractors decide independently. In practice they do not: a freeze night fills everyone's schedule at once. Treat the result as a floor.
- Acceptance is not arrival. A contractor also has to be close enough to arrive within 90 minutes, which caps the zone radius. The radius is 10 miles in the founding zone (R27).

### What founding contractors get and commit to

Decided 2026-10-03 (R05 to R07, R12).

<!-- sheet: Design_Partners -->
| Founding contractors get | Founding contractors commit to |
|---|---|
| The first requests in their zone | Responding within 10 minutes when they mark themselves available |
| A say in how dispatch, payouts, and disputes work | Crediting the trip charge to the work when the member goes ahead |
| $0 a job through the founding period and for 12 months after it, written into the founding agreement | Keeping license and insurance documents current |
| Support by text from the founders | Answering a three-question text after their first five jobs |
| | A permission clause: whether SOS SMS may later cite their outcomes and name them, and in what form. Asked before the first job, because asking afterwards produces refusals |
