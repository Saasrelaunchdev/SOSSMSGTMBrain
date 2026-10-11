# Resolution register

Distills `sources/raw/gtm/marketplace/resolution-register.md` (2026-10-03, revised by the membership revision on 2026-10-11). Load it for any SOS SMS value: a price, a rule, a planning number, how a pre-launch fact gets counted, or a merge field. The twelve decisions themselves are in `ops/decisions.md`.

Five kinds. **Decided:** used as written, on the side it belongs to. **Planning value:** used in planning and internal math, labelled as one, never shown as a result; the measured figure replaces it once a zone runs. **Counted at:** the method and stage are stated; no number is written until it is counted. **Merge field:** `{{field}}`, filled from a named record when sent, never typed by hand. **Retired:** removed by a later decision; the row stays so old references resolve, and it is never used in copy.

## Values

| ID | Kind | What | Resolved to |
|---|---|---|---|
| R01 | Decided | Trip charge | $99 a request, one per trade and zone, day or night; charged to the member's card on file when a contractor accepts; paid to the contractor; credited to the repair |
| R02 | Retired | SOS SMS fee | Retired 2026-10-11: no fee per request. Was $49 per dispatched request |
| R03 | Decided | Contractor fee | $25 per completed paid job after the founding period, deducted from the payout. Never per request or to join |
| R04 | Decided | Share of the repair | $0. The price for the work stays the contractor's |
| R05 | Decided | Founding terms | $0 a job through the founding period and 12 months after it, in the founding agreement |
| R06 | Decided | Founding period | The founding zone's first 6 months open to members |
| R07 | Decided | Founding list | Opens with the first cold email; closes 60 days after it |
| R08 | Planning value | Founding cohort | 9 plumbing contractors in the founding zone |
| R09 | Decided | Take per job | $0 in the founding period; $25 after it (the contractor fee). SOS SMS's revenue is the membership |
| R10 | Decided | Refund on a late arrival | The $99 trip charge, back automatically |
| R11 | Decided | No acceptance | Member told within 15 minutes; never charged |
| R12 | Decided | Contractor response window | 10 minutes, when marked available |
| R13 | Decided | First refusal on own customers | 5 minutes; held until dispatch supports it |
| R14 | Decided | Payout timing | Within 2 business days of arrival |
| R15 | Decided | Outside covered hours | Not dispatched; stop-the-water steps and the safety line; nothing charged. The membership page names covered hours |
| R16 | Decided | No card | Joining puts a card on file; a text from a non-member gets the free help by text (R57) |
| R17 | Decided | Relaunch after a miss | SOS SMS pays the second trip charge from membership revenue; held out of copy until dispatch supports it |
| R18 | Decided | Supply referral fee or reward | None at launch; thanks by text (member affiliates: R61) |
| R19 | Decided | Household membership | The demand-side product, monthly or annual (decision 2, revised 2026-10-11) |
| R20 | Decided | After-hours surcharge | None |
| R21 | Decided | Guarantee on the repair | Not offered; the membership pays for no repair or parts |
| R22 | Decided | Market | The United States |
| R23 | Decided | Website | The contractor page, the readiness scorecard, and the launch list from Stage 1; the membership page (with a ZIP check), the guarantee page, and five problem and prevention guides from Stage 2 |
| R24 | Decided | Taglines | Contractors: "Emergency jobs you choose, with the trip paid before you roll." Members: "One text, and help is on the way." Sub tag: "Join before you need it." |
| R25 | Decided | Founder roles | A supply lead and a demand lead (memberships: affiliates, email, search for sign-ups, the member line); both on supply first in Stage 1, while the demand lead signs affiliates and grows the launch list |
| R26 | Decided | Unattributed matrix rows | Excluded for good |
| R27 | Planning value | Zone radius | 10 miles |
| R28 | Planning value | Acceptance rate (a) | 0.30, measured per hour band in Stage 1 |
| R29 | Planning value | Misses caused by SOS SMS | 5 percent of requests |
| R30 | Retired | First text to paid | Retired 2026-10-11: a member does not confirm a request. Was 50 percent |
| R31 | Planning value | Processing and operations | 2.9 percent plus $0.30 a charge; $5.30 a request; contractor side $3.50 a completed job; $0.55 a member a month for messages, support, and platform |
| R32 | Planning value | Zone signal thresholds | Acceptance 90 percent or more; arrival 95 or more; refunds caused by SOS SMS 5 or fewer per 100 requests; monthly plan churn 6.5 percent or less; cost per new paid member at or under the ceiling (R63); contractor activity 60 or more |
| R33 | Planning value | Weeks to prove a zone | 4 consecutive weeks at threshold |
| R34 | Planning value | Sign-up pause | Automatic when acceptance is under 90 percent over 7 days: ads stop, affiliate links show the launch list |
| R35 | Planning value | Runway | At least 18 months at Stage A spending |
| R36 | Planning value | Contractor sign-up | About 5 minutes by text |
| R37 | Planning value | First paid trip | Within 30 days of the zone opening |
| R38 | Planning value | ICP revenue bands | Level 1 under $500,000 a year; Level 2 $500,000 to $3 million |
| R39 | Decided | Household income | Not a targeting criterion; members are targeted by zone and readiness triggers |
| R40 | Counted at | Licensed plumbing businesses in the metro | The state license list, Stage 0 |
| R41 | Counted at | Owner-occupied homes in the zone | Census tract data (ACS), Stage 0 |
| R42 | Counted at | Requests per month in a zone | The zone's first 8 weeks open; 0.25 a member a year until then (R58) |
| R43 | Counted at | Every SOS SMS result | Weekly from the first member and the first request, against R32 |
| R44 | Decided | Social-proof headlines | The drill's method line until a real, permissioned result exists |
| R45 | Decided | Proof points | The drill's named record (both Phase 6 files) |
| R46 | Decided | SOS SMS weaknesses in tables | Stated plainly: no track record yet; open only in zones at density; a fee every month or year, before anything breaks |
| R47 | Counted at | Warranty network discount | Each warranty company's rate card |
| R48 | Decided | Company snapshot | Two founders, Bryan and Ali; no channels tried; burn stays out of the GTM (R35 sets the requirement) |
| R49 | Decided | Price range before arrival | Not offered at launch; the trip charge is stated on the membership page |
| R50 | Decided | Reaching a person | Text HELP: a person replies by text within 15 minutes in covered hours; STOP ends all texts (S72) |
| R51 | Planning value | Membership, monthly | $10 a month until the launch price is set in Stage 0; copy `{{monthly price}}` (plumber clubs $8.25 to $19.99, S75 to S77; utility plans $16.99 to $22.99, S78) |
| R52 | Planning value | Membership, annual | $100 a year, two months free (S90); copy `{{annual price}}` |
| R53 | Decided | What membership includes | One-text dispatch; an arrival time on acceptance; the 90-minute guarantee; a person by text; the readiness kit. Not included: the repair, parts, a guarantee on the work. Paid on use: the $99 trip charge, credited to the repair |
| R54 | Decided | Joining | The membership page, or from Text READY; about 3 minutes (planning value); card, home address, and consent on file; one address per membership; the contact card at once |
| R55 | Decided | When memberships open | Per zone, at the density number for the first trade, with covered hours named. Before then, the launch list: email, no charge, no service promised |
| R56 | Decided | Cancelling and renewal | Any time, on the membership page or by texting HELP; monthly ends at the end of the paid month; annual members reminded before `{{renewal date}}` (S87) |
| R57 | Decided | A text from a non-member | The safety line, the stop-the-water steps, and how to join; dispatch is for members; nothing charged |
| R58 | Planning value | Requests per member | 0.25 a year (S82, S83) |
| R59 | Planning value | Monthly plan churn | 6.5 percent a month (S89, C) |
| R60 | Planning value | Annual renewal | 75 percent (S89, C) |
| R61 | Planning value | Affiliate commission | $20 per new paid member, after the first paid month; disclosed (S88); never to anyone referring at a home purchase settlement (S86, S94) |
| R62 | Decided | Member referral reward | None at launch; thanks by text |
| R63 | Planning value | Acquisition ceiling per new paid member | About $43 by channel and zone, reviewed weekly: the first 6 months of contribution on the monthly plan ($8.51 a month at 6.5 percent churn) |
| R64 | Planning value | Member base per zone | About 430 members, about one request a month per founding contractor (9 × 12 ÷ 0.25) |

## Merge fields
`{{first name}}`, `{{name}}`, `{{business}}`: the contractor list, the contractor's sign-up, or the member record. `{{SOS SMS number}}`, `{{number}}`: the registered number (decision 9). `{{zone}}`, `{{zone name}}`, `{{zone neighborhoods}}`, `{{launch metro}}`, `{{covered hours}}`: the zone record (decisions 1 and 3). `{{trade}}`, `{{trades}}`: the sign-up or the zone's open trades. `{{url}}`, `{{link}}`, `{{terms link}}`, `{{contractor page}}`: the SOS SMS site (R23). `{{code}}`, `{{partner}}`: the partner or affiliate agreement. `{{founding close date}}`: R07. `{{score}}`, `{{top two}}`, `{{top three}}`, `{{result}}`: the respondent's own scorecard or Lead Cost Check answers. `{{their number}}`: the member's own number. `{{sender name}}`, `{{postal address}}`, `{{opt-out link}}`: the email sending setup (S73). `{{contractor name}}`, `{{arrival time}}`, `{{rating}}`: the request record. `{{monthly price}}`, `{{annual price}}`: the zone's price record, set in Stage 0 (R51, R52). `{{renewal date}}`: the member record (R56).
