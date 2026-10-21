# Lead Magnet Specification: the Job Leak Scorecard (contractor side)

A ScoreApp scorecard built from the Phase 1 demand driver, the Lead Cost Check. It gives a contractor an immediate read on how much of their effort and spend leaks away before a job is paid, and it points at the two leaks SOS SMS is built to stop: paying for requests that never become work, and driving out without getting paid.

Rules for this asset: outputs are scores and the contractor's own numbers, never projected earnings or "more jobs". No case studies exist, so none are used.

## Scorecard overview

<!-- sheet: Overview -->
| Element | Specification |
|---|---|
| Scorecard Name | The Job Leak Scorecard: how much of your work leaks away before you get paid? |
| Target ICP | ICP Level 2 contractors who pay for leads; Level 1 owner-operators get a shorter path focused on unpaid trips and missed after-hours calls |
| Problem it Reveals | Lead spend on requests that never become jobs, unpaid trips, and emergency calls missed after hours |
| Immediate Value to User | A score from 0 to 100, their own cost per booked job, and the three biggest leaks in their business, in under three minutes |
| Conversion Path to SOS SMS | Result screen, then the matching self-serve call to action by tier (rate card, terms on one page, or the automated lead spend report), then sign-up by text. No calls |

## Questions

Seven questions, maximum score 100. A higher score means more leakage.

<!-- sheet: Questions -->
| # | Question | Answer Options | Scoring Logic | What It Reveals |
|---|---|---|---|---|
| 1 | In a typical month, how much do you spend on lead platforms or search ads? | $0 / Under $250 / $250 to $750 / $750 to $2,000 / Over $2,000 | 0 / 5 / 10 / 15 / 20 | Exposure to per-lead cost |
| 2 | Of the leads you pay for, how many become booked jobs? | I don't buy leads / More than half / About a third / About one in five / Fewer than one in ten | 0 / 2 / 6 / 10 / 14 | Close rate, which turns cost per lead into cost per booked job |
| 3 | Last month, how many trips did you make without getting paid (no one home, customer declined, could not collect)? | None / 1 / 2 to 3 / 4 to 6 / 7 or more | 0 / 4 / 8 / 12 / 16 | Unpaid trips, the leak SOS SMS's trip charge closes |
| 4 | When do you collect your trip or service call fee? | Before I roll / On arrival / Only if they hire me / I waive it / I don't have one | 0 / 3 / 8 / 10 / 12 | How exposed the contractor is to unpaid trips |
| 5 | Who answers your phone after 6 p.m.? | A dispatcher or answering service / Me, always / Me, when I can / Voicemail / Nobody | 4 / 6 / 8 / 12 / 14 | After-hours coverage, and the cost of providing it |
| 6 | How many emergency calls a week do you miss or turn away? | None / 1 to 2 / 3 to 5 / 6 to 10 / More than 10 | 0 / 4 / 8 / 11 / 14 | Emergency demand the contractor cannot capture |
| 7 | If emergency requests arrived by text with the trip charge already paid, how many nights a week would you take them? | None / 1 / 2 to 3 / 4 to 5 / 6 to 7 | 0 / 3 / 5 / 8 / 10 | Fit and capacity for SOS SMS |

Question 2's first option ("I don't buy leads") routes Level 1 owner-operators: their result emphasizes questions 3 to 6.

The result screen also shows the contractor's cost per booked job, when questions 1 and 2 allow it: monthly spend divided by booked jobs, using the midpoint of their answers, labeled "estimate from your answers".

## Results tiers

<!-- sheet: Tiers -->
| Score Range | Tier Name | Message | CTA |
|---|---|---|---|
| 0 to 39 | Tight Ship | "You keep most of what you earn. Your biggest leak is {{top-scoring question}}. If you ever want emergency work on nights you choose, with the trip paid before you roll, SOS SMS is built for that." | Soft: download the emergency rate card template |
| 40 to 69 | Leaking at the Edges | "Some of your spend and some of your trips go unpaid. Your two biggest leaks: {{top two}}. Here is exactly how SOS SMS handles both: no charge to see a request, and the trip charge collected before you leave." | Medium: read the terms on one page; run the full Lead Cost Check with your invoices |
| 70 to 100 | Paying to Work | "A large share of your money and nights goes to work that never pays. Your biggest leaks: {{top three}}. Your last three months of lead receipts will show exactly where." | Strong: get the automated lead spend report, then text JOIN to {{number}} |

## Post-scorecard email sequence

Email, because the scorecard collects an email address with consent. Texts only if the contractor separately opts in to texts on the scorecard form (S31).

<!-- sheet: Emails -->
| Email # | Day | Subject Line | Content Focus | CTA |
|---|---|---|---|---|
| 1 | 0 | Your Job Leak Score: {{score}} | Results delivery and interpretation: their score, their tier, their top leaks, their estimated cost per booked job | See your full results |
| 2 | 2 | Where the money goes between a lead and a job | Deeper insight in place of a case study (none exist yet): the arithmetic from cost per lead to cost per booked job, run on their own answers | Run the Lead Cost Check with your invoices |
| 3 | 5 | A dispatch line where seeing a job costs nothing | Solution introduction: how a job works in three texts; the terms on one page; the obligations, stated plainly | Read the terms, then text JOIN to {{number}} |
| 4 | 8 | When SOS SMS opens in {{zone}} | Final note: what every contractor gets and commits to, on the same terms, and that the zone opens to members once every hour is covered | Text JOIN to be on SOS SMS when it opens |

No urgency of any kind: there is no deadline, because every contractor joins on the same terms whenever they join (R07, retired).

## ScoreApp implementation notes

<!-- sheet: Implementation -->
| Item | Specification |
|---|---|
| Lead capture | Name, business name, trade, ZIP code, email. Optional mobile number with a separate, unchecked text-consent box |
| Branching | Question 2 answer "I don't buy leads" shows the Level 1 result variant |
| Data use | Answers are used for the contractor's own result and this email sequence. Not sold, not shared |
| Copy rules | Narrowed claims only (brief Section 5); no earnings or volume claims; no em dashes |
| Measurement | Starts, completions, tier distribution, call bookings by tier |
