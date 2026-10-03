# Lead Magnet Specification: the Home Emergency Readiness Scorecard (customer side)

A ScoreApp scorecard built from the Phase 1 demand driver, Text READY. It tells a homeowner how ready their home is for a plumbing or water emergency, gives them a short plan, and ends with the one step that matters most for SOS SMS: saving the number before anything breaks. It also runs as a five-question text version (Text READY).

Rules for this asset: no damage-cost figures without a source; no claim that SOS SMS prevents damage; the safety line on the results page.

Where it sits under the product-led motion: a top-of-funnel asset in Channel 2 (problem-solving pages) and in the seasonal prevention campaign. It is not distributed through partners.

## Scorecard overview

<!-- sheet: Overview -->
| Element | Specification |
|---|---|
| Scorecard Name | How Ready Is Your Home for a 2 a.m. Leak? |
| Target ICP | Level 1 (no go-to contractor, often new to the home) and Level 2 (contractor who does not answer at night), inside the founding zone |
| Problem it Reveals | Not knowing where the shutoff is, an aging water heater, and no one to text at night |
| Immediate Value to User | A readiness score, a three-step plan for their home, and a shutoff guide, in under two minutes |
| Conversion Path to SOS SMS | Results page, then "save the number now" (text READY), then the contact card in their phone; the next emergency text is their second contact with SOS SMS, not their first |

## Questions

Seven questions, maximum score 100. A higher score means more exposed.

<!-- sheet: Questions -->
| # | Question | Answer Options | Scoring Logic | What It Reveals |
|---|---|---|---|---|
| 1 | Do you know where your main water shutoff is? | Yes, and I've used it / Yes, never used it / Roughly / No / What's a main shutoff? | 0 / 6 / 12 / 18 / 20 | Whether a leak can be stopped before help arrives |
| 2 | When did you last check that the shutoff turns? | Within a year / A few years ago / Never / Not sure | 0 / 6 / 12 / 14 | Whether the shutoff will turn when it is needed |
| 3 | How old is your water heater? | Under 5 years / 5 to 10 / Over 10 / Not sure | 0 / 4 / 10 / 8 | The age of the appliance in the home that holds the most water |
| 4 | How old is your home? | Under 15 years / 15 to 40 / Over 40 / Not sure | 0 / 4 / 8 / 6 | Older plumbing; the median owner-occupied home is 42 years old (S63) |
| 5 | Do you have a plumber who answers at night or on weekends? | Yes, reliably / Sometimes / Daytime only / No plumber | 0 / 6 / 12 / 16 | The gap SOS SMS fills |
| 6 | If a pipe burst at 2 a.m., what would you do first? | Shut off the water, then call my plumber / Shut off the water, then search / Search for a plumber / Call my landlord or warranty / Not sure | 0 / 6 / 10 / 8 / 14 | Whether they have a plan |
| 7 | Do you have a number saved for home emergencies? | Yes / No | 0 / 16 | The conversion step |

Maximum: 20 + 14 + 10 + 8 + 16 + 14 + 16 = 98, normalized to 100 on the results page.

## Results tiers

<!-- sheet: Tiers -->
| Score Range | Tier Name | Message | CTA |
|---|---|---|---|
| 0 to 39 | Ready | "Your home is in good shape for a leak. One thing to add: a number to text if your plumber can't come at night." | Soft: save the SOS SMS number (text READY) |
| 40 to 69 | Partly Ready | "You're partway there. Your biggest gaps: [top two]. Here's a three-step plan, starting with finding and testing your shutoff tonight." | Medium: get the shutoff guide by text (text READY) |
| 70 to 100 | Exposed | "If something broke tonight, you'd be starting from scratch. Three steps fix most of that, and the first takes five minutes." | Strong: text READY now to save the number and get the shutoff guide |

The results page carries the safety line: "For fire, a gas smell, or anyone hurt, call 911 first. Smell gas? Get out first, then call."

## Post-scorecard email sequence

Email, with consent collected on the scorecard. No marketing texts without a separate opt-in (S31).

<!-- sheet: Emails -->
| Email # | Day | Subject Line | Content Focus | CTA |
|---|---|---|---|---|
| 1 | 0 | Your home readiness score: [score] | Results delivery and interpretation: their score, their top gaps, the three-step plan | Find your shutoff tonight (guide) |
| 2 | 2 | The first ten minutes of a leak | Deeper insight in place of a case study (none exist yet): shut off the water, move valuables, photograph the damage for insurance, then get help. EPA's 24 to 48 hour drying guidance (S58) | Save the number for the "get help" step |
| 3 | 5 | One text, when something breaks at home | Solution introduction: how SOS SMS works in three texts; the trip charge shown first; the guarantee with its scope; what SOS SMS does not do | Text READY to [number] |
| 4 | 8 | Before the next cold snap | Final reminder: pre-freeze steps, sent only when seasonally true; otherwise "Is the number saved?" | Text READY |

## ScoreApp implementation notes

<!-- sheet: Implementation -->
| Item | Specification |
|---|---|
| Lead capture | First name, ZIP code, email. ZIP outside the founding zone shows the readiness plan without the SOS SMS offer |
| Branching | Question 6 "Call my landlord or warranty" adds a line: renters call the landlord first; warranty holders check coverage first |
| Data use | Used for their result and one email sequence. Not sold, not shared, no ad targeting |
| Copy rules | Narrowed claims only; no arrival averages; no damage costs without a source; safety line on the results page |
| Measurement | Starts, completions, tier distribution, READY texts attributed to the scorecard |
