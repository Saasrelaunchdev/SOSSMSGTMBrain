# Lead Magnet Specification: the Home Emergency Readiness Scorecard (member side)

A ScoreApp scorecard built from the Phase 1 demand driver, the readiness check. It tells a homeowner how ready their home is for a plumbing or water emergency, gives them a short plan, and ends with the step that matters most for SOS SMS: joining before anything breaks, or the launch list where memberships are not open yet. It also runs as a five-question text version (Text READY). Revised 2026-10-11, the membership revision, and 2026-10-20, the tiers revision: the scorecard leads with leaks, the most feared emergency (49 percent of homeowners, S82), and its plan and the membership cover plumbing, HVAC, and electrical.

Rules for this asset: no damage-cost figures without a source; no claim that SOS SMS prevents damage; the safety line on the results page; the plans and prices as decided (R51, R52, R65, R66); the guarantee only with its plans.

Where it sits: the top of SOS SMS's own email list (Channel 2), the first thing a partner can share (Channel 1, in the partner kit), and the offer on every prevention guide (Channel 3).

## Scorecard overview

<!-- sheet: Overview -->
| Element | Specification |
|---|---|
| Scorecard Name | How Ready Is Your Home for a 2 a.m. Leak? |
| Target ICP | Level 1 (a new homeowner without a go-to contractor) and Level 2 (an established homeowner whose contractor does not answer at night), in open zones and zones about to open |
| Problem it Reveals | Not knowing where the shutoff is, an aging water heater, and no one to text at night |
| Immediate Value to User | A readiness score, a three-step plan for their home, and a shutoff guide, in under two minutes |
| Conversion Path to SOS SMS | Results page, then the ZIP check: in an open zone, join (Plus at $150 a year shown first; plans from $100 a year or $10 a month); in a zone not yet open, the launch list; outside, the plan alone. The emails follow |

## Questions

Seven questions, maximum score 100. A higher score means more exposed.

<!-- sheet: Questions -->
| # | Question | Answer Options | Scoring Logic | What It Reveals |
|---|---|---|---|---|
| 1 | Do you know where your main water shutoff is? | Yes, and I've used it / Yes, never used it / Roughly / No / What's a main shutoff? | 0 / 6 / 12 / 18 / 20 | Whether a leak can be stopped before help arrives |
| 2 | When did you last check that the shutoff turns? | Within a year / A few years ago / Never / Not sure | 0 / 6 / 12 / 14 | Whether the shutoff will turn when it is needed |
| 3 | How old is your water heater? | Under 5 years / 5 to 10 / Over 10 / Not sure | 0 / 4 / 10 / 8 | The age of the appliance in the home that holds the most water |
| 4 | How old is your home? | Under 15 years / 15 to 40 / Over 40 / Not sure | 0 / 4 / 8 / 6 | Older plumbing, heating, and wiring; the median owner-occupied home is 42 years old (S63) |
| 5 | Do you have a plumber, HVAC company, and electrician who answer at night or on weekends? | Yes, reliably / Sometimes / Daytime only / None | 0 / 6 / 12 / 16 | The gap SOS SMS fills, in three trades |
| 6 | If a pipe burst at 2 a.m., what would you do first? | Shut off the water, then call my plumber / Shut off the water, then search / Search for a plumber / Call my landlord or warranty / Not sure | 0 / 6 / 10 / 8 / 14 | Whether they have a plan |
| 7 | Do you have a number saved for home emergencies? | Yes / No | 0 / 16 | The step membership answers |

Maximum: 20 + 14 + 10 + 8 + 16 + 14 + 16 = 98, normalized to 100 on the results page.

## Results tiers

<!-- sheet: Tiers -->
| Score Range | Tier Name | Message | CTA |
|---|---|---|---|
| 0 to 39 | Ready | "Your home is in good shape for a leak. One thing to add: someone to text if your plumber, HVAC company, or electrician can't come at night." | Soft: see what membership includes |
| 40 to 69 | Partly Ready | "You're partway there. Your biggest gaps: {{top two}}. Here's a three-step plan, starting with finding and testing your shutoff tonight." | Medium: get the shutoff guide, then check your ZIP |
| 70 to 100 | Exposed | "If something broke tonight, you'd be starting from scratch. Three steps fix most of that, and the first takes five minutes. The last is joining before you need it." | Strong: check your ZIP and join before you need it |

The results page carries the safety line: "For fire, a gas smell, or anyone hurt, call 911 first. Smell gas? Get out first, then call."

## Post-scorecard email sequence

Email, with consent collected on the scorecard; every email carries the full name SOS SMS, a postal address, and an opt-out (S73). No marketing texts without a separate written opt-in (S31).

<!-- sheet: Emails -->
| Email # | Day | Subject Line | Content Focus | CTA |
|---|---|---|---|---|
| 1 | 0 | Your home readiness score: {{score}} | Results delivery and interpretation: their score, their top gaps, the three-step plan | Find your shutoff tonight (guide) |
| 2 | 2 | The first ten minutes of a leak | Deeper insight in place of a case study (none exist yet): shut off the water, move valuables, photograph the damage for insurance, then get help. EPA's 24 to 48 hour drying guidance (S58) | Keep the steps where you can find them |
| 3 | 5 | One text, when something breaks at home | Solution introduction: how membership works in one text, for plumbing, HVAC, or electrical; the three plans and the $99 trip charge on use; the guarantee with its plans and scope; what SOS SMS does not do | Check your ZIP: join in an open zone, or the launch list |
| 4 | 8 | Before the next cold snap | Final reminder: pre-freeze steps, sent only when seasonally true; otherwise "Ready before it happens?" | See what membership includes |

## ScoreApp implementation notes

<!-- sheet: Implementation -->
| Item | Specification |
|---|---|
| Lead capture | First name, ZIP code, email. The ZIP decides the ending: an open zone shows the membership; a zone not yet open, the launch list; outside, the readiness plan alone |
| Branching | Question 6 "Call my landlord or warranty" adds a line: renters call the landlord first; warranty holders check coverage first, and a warranty pays for repairs while SOS SMS gets someone there |
| Data use | Used for their result and one email sequence. Not sold, not shared, no ad targeting |
| Copy rules | Narrowed claims only; no arrival averages; no damage costs without a source; the plans and prices as decided; safety line on the results page |
| Measurement | Starts, completions, tier distribution, launch list joins, and new paid members attributed to the scorecard |
