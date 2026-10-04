# Resolution register

Distills `sources/raw/gtm/marketplace/resolution-register.md` (2026-10-03). Load it for any SOS SMS value: a price, a rule, a planning number, how a pre-launch fact gets counted, or a merge field. The twelve decisions themselves are in `ops/decisions.md`.

Four kinds. **Decided:** used as written, on the side it belongs to. **Planning value:** used in planning and internal math, labelled as one, never shown as a result; the measured figure replaces it once a zone runs. **Counted at:** the method and stage are stated; no number is written until it is counted. **Merge field:** `{{field}}`, filled from a named record when sent, never typed by hand.

## Values

| ID | Kind | What | Resolved to |
|---|---|---|---|
| R01 | Decided | Trip charge | $99 a request, one per trade and zone, day or night; paid to the contractor; credited to the repair |
| R02 | Decided | SOS SMS fee | $49 per dispatched request, a separate line; charged only when a contractor accepts |
| R03 | Decided | Contractor fee | $25 per completed paid job after the founding period, deducted from the payout. Never per request or to join |
| R04 | Decided | Share of the repair | $0. The price for the work stays the contractor's |
| R05 | Decided | Founding terms | $0 a job through the founding period and 12 months after it, in the founding agreement |
| R06 | Decided | Founding period | The founding zone's first 6 months open to customers |
| R07 | Decided | Founding list | Opens with the first cold email; closes 60 days after it |
| R08 | Planning value | Founding cohort | 9 plumbing contractors in the founding zone |
| R09 | Decided | Take per job | $49 in the founding period; $74 after it |
| R10 | Decided | Refund on a late arrival | The $99 trip charge, back automatically |
| R11 | Decided | No acceptance | Customer told within 15 minutes; never charged |
| R12 | Decided | Contractor response window | 10 minutes, when marked available |
| R13 | Decided | First refusal on own customers | 5 minutes; held until dispatch supports it |
| R14 | Decided | Payout timing | Within 2 business days of arrival |
| R15 | Decided | Outside covered hours | Not dispatched; stop-the-water steps and the safety line; nothing charged |
| R16 | Decided | No card | A card or phone wallet through the payment link; without one, free help by text |
| R17 | Decided | Relaunch after a miss | SOS SMS pays the second trip charge from its fee; held out of copy until dispatch supports it |
| R18 | Decided | Referral fee or reward | None at launch; thanks by text |
| R19 | Decided | Household membership | Not offered at launch |
| R20 | Decided | After-hours surcharge | None |
| R21 | Decided | Guarantee on the repair | Not offered |
| R22 | Decided | Market | The United States |
| R23 | Decided | Website | The contractor page from Stage 1; the zone page, guarantee page, and five problem guides from Stage 2 |
| R24 | Decided | Taglines | Contractors: "Emergency jobs you choose, with the trip paid before you roll." Customers: "Text once, and a vetted contractor is on the way." |
| R25 | Decided | Founder roles | A supply lead and a demand lead; both on supply in Stage 1 |
| R26 | Decided | Unattributed matrix rows | Excluded for good |
| R27 | Planning value | Zone radius | 10 miles |
| R28 | Planning value | Acceptance rate (a) | 0.30, measured per hour band in Stage 1 |
| R29 | Planning value | Misses caused by SOS SMS | 5 percent of requests |
| R30 | Planning value | First text to paid | 50 percent |
| R31 | Planning value | Processing and operations | 2.9 percent plus $0.30 a charge; $5.30 a request |
| R32 | Planning value | Zone signal thresholds | Acceptance 90 percent or more; arrival 95 or more; refunds caused by SOS SMS 5 or fewer per 100; first text to paid 50 or more; owned share 30 by month 6 and 50 by month 12; contractor activity 60 or more |
| R33 | Planning value | Weeks to prove a zone | 4 consecutive weeks at threshold |
| R34 | Planning value | Ad pause | Automatic when acceptance is under 90 percent over 7 days |
| R35 | Planning value | Runway | At least 18 months at Stage A spending |
| R36 | Planning value | Contractor sign-up | About 5 minutes by text |
| R37 | Planning value | First paid trip | Within 30 days of the zone opening |
| R38 | Planning value | ICP revenue bands | Level 1 under $500,000 a year; Level 2 $500,000 to $3 million |
| R39 | Decided | Household income | Not a targeting criterion |
| R40 | Counted at | Licensed plumbing businesses in the metro | The state license list, Stage 0 |
| R41 | Counted at | Owner-occupied homes in the zone | Census tract data (ACS), Stage 0 |
| R42 | Counted at | Requests per month in a zone | The zone's first 8 weeks open |
| R43 | Counted at | Every SOS SMS result | Weekly from the first request, against R32 |
| R44 | Decided | Social-proof headlines | The drill's method line until a real, permissioned result exists |
| R45 | Decided | Proof points | The drill's named record (both Phase 6 files) |
| R46 | Decided | SOS SMS weaknesses in tables | Stated plainly: no track record yet; open only in zones at density |
| R47 | Counted at | Warranty network discount | Each warranty company's rate card |
| R48 | Decided | Company snapshot | Two founders, Bryan and Ali; no channels tried; burn stays out of the GTM (R35 sets the requirement) |
| R49 | Decided | Price range before arrival | Not offered at launch; the trip charge is stated before dispatch |
| R50 | Decided | Reaching a person | Text HELP: a person replies by text within 15 minutes in covered hours; STOP ends all texts (S72) |

## Merge fields
`{{first name}}`, `{{name}}`, `{{business}}`: the contractor list or sign-up record. `{{SOS SMS number}}`, `{{number}}`: the registered number (decision 9). `{{zone}}`, `{{zone name}}`, `{{zone neighborhoods}}`, `{{launch metro}}`, `{{covered hours}}`: the zone record (decisions 1 and 3). `{{trade}}`, `{{trades}}`: the sign-up or the zone's open trades. `{{url}}`, `{{link}}`, `{{terms link}}`, `{{contractor page}}`: the SOS SMS site (R23). `{{code}}`, `{{partner}}`: the partner agreement. `{{founding close date}}`: R07. `{{score}}`, `{{top two}}`, `{{top three}}`, `{{result}}`: the contractor's own scorecard or Lead Cost Check answers. `{{their number}}`: the customer's own number. `{{sender name}}`, `{{postal address}}`, `{{opt-out link}}`: the email sending setup (S73). `{{contractor name}}`, `{{arrival time}}`, `{{rating}}`: the request record.
