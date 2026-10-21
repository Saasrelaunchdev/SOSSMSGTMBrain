# Glossary, canonical vocabulary

The words SOS SMS uses for its own things. Mirror them exactly in every asset, on both sides of the marketplace.
last_reviewed: 2026-10-21

## Canonical terms

| Term | Rule |
|---|---|
| SOS SMS | Always the full name, two words, both in capitals. Never the first word alone: unrelated local plumbing companies use it (decision 10) |
| contractor | The licensed, insured tradesperson or shop on the supply side. Not "pro", "partner", "vendor", or "provider" in copy |
| member | A homeowner who has joined SOS SMS: the demand side (the membership revision, 2026-10-11). Before joining, "homeowner". Never "user", "client", "subscriber", "customer", or "lead" for SOS SMS's own members. In contractor copy, "an SOS SMS member" on first mention, then "the member"; a contractor's own clients stay "your customers" |
| membership | What a member pays for, on one of three plans, monthly or annual, billed to the card on file: Basic $10 a month or $100 a year, Plus $15 or $150, Premier $35 or $350 (R51, R52, R65, R66; decided 2026-10-21). Copy states the prices as written; a message to one member writes `{{plan}}` |
| plan | Basic, Plus, or Premier. Every plan gets the same dispatch: one text to every matched contractor at once, in plumbing, HVAC, and electrical, at any hour. **Basic**, the entry plan: the member's phone, no credit. **Plus**, shown first and flagged "Most popular": the 90-minute guarantee with a 6-month credit, up to 5 phones (R65). **Premier**: a 12-month credit, a trip charge a membership year paid by SOS SMS, a second home, up to 10 phones (R66). The plans differ by what stands behind the arrival time and who can text, never by how fast a request goes out (R53) |
| phones on file | The phones that can text for the home: 1 on Basic, up to 5 on Plus, up to 10 across two homes on Premier (R69). A text from any of them starts dispatch |
| card on file, address on file | The card and home address a member saves when joining, so the emergency is one text (R54) |
| request text | The member's one text that starts dispatch. The 90-minute window starts here (decision 3) |
| request | What a contractor receives when a member texts. Never "lead": contractors associate leads with paying to look |
| accept | What a contractor does to take a request. The first to accept gets the job |
| dispatch | What SOS SMS does. SOS SMS dispatches; the contractor does the work. SOS SMS is never "the plumber" |
| matched contractors | The contractors on SOS SMS matched to the request by trade and service area |
| trip charge | What the member pays for the visit, on use: $99, one per trade and zone, the same in plumbing, HVAC, and electrical, day or night, set by SOS SMS (decision 5); charged to the card on file when a contractor accepts; credited to the repair if the member goes ahead. It stands on a late arrival, because it pays for the work, and comes back in full on a no-show |
| contractor fee | $25 per completed paid job, from the first job, for every contractor in every trade, deducted from the trip charge payout: the contractor receives $74 of the $99. Never per request, never to join (decision 2) |
| arrival time | The time a contractor commits to when accepting |
| 90-minute window | The window every arrival time sits inside: 90 minutes from the member's request text, or from the moment a declined card authorizes (decision 3, R16) |
| guarantee, late-arrival credit | The 90-minute guarantee, on Plus and Premier only: when a contractor arrives after the 90 minutes, does not come, or the member texts NEXT after them, SOS SMS credits the membership paid in the 6 months (Plus) or 12 months (Premier) before the request to the next bills or the renewal, never cash; a message writes `{{credit amount}}`. Always with the clock start, what it pays, and the covered area in the same sentence. Never written for Basic |
| zone | The unit of launch: a small area inside one metro. The launch zone is a 10-mile radius around the first contractors' shops in the founders' home metro (decision 1) |
| open zone | A zone where memberships are open: each of the three trades meets the density number in every hour band, every day (R55). An open zone is covered at every hour (R15) |
| launch list | The email list for a zone that is not open yet. No charge, no service promised (R55) |
| density number, hour band | Contractors needed per trade, zone, and hour band (a slice of the day: 2 a.m. and 2 p.m. are different bands) for a target chance that at least one accepts. The first cohort is 9 per trade, 27 places (R08) |
| NEXT | What a member texts if no one is there after the 90 minutes: the first trip charge comes back in full, that contractor is paid nothing, and the request goes to the other matched contractors at once (R17) |
| acceptance rate | The chance one contractor accepts a request in time. Planning value 0.30 (R28), replaced by the measured figure per hour band from Stage 1 |
| affiliate | A partner who passes SOS SMS on to homeowners with a code and a disclosed commission per new paid member (R61). Never a real estate agent, lender, title or settlement agent, or anyone referring at a home purchase settlement |
| first reply | The automated reply to a member's request text, at once: that it is going to the contractors on SOS SMS now, the safety line, how to reach a person, then the first steps for the problem. No offer, no link, nothing to confirm |
| welcome texts | The texts a member gets on joining: the plan, when dispatch starts, the contact card, how it works in one text, the safety line, text HELP for a person |
| Text READY | The readiness keyword: a five-question home check and a shutoff guide by text, ending with the contact card and how to join |
| readiness kit | What a member gets on joining: the shutoff guide, Text READY, the contact card (R53) |
| contact card, forwardable card | The saved contact every member gets on joining, so the emergency starts with a saved number; the card a member forwards to a neighbor |
| membership page | The member-side page: the ZIP check, the three plans with Plus in the middle on the annual plan, the trip charge on use on its own line, how it works in one text, the guarantee with its scope, what is not included, cancel any time |
| the terms on one page | The contractor's terms: what they pay, when they are paid, what they commit to, what happens if they are late |
| Lead Cost Check, Job Leak Scorecard | The contractor-side demand driver, a two-minute calculator of true cost per booked job; and the contractor lead magnet |
| safety line | "For fire, a gas smell, or anyone hurt, call 911 first." Gas variant: "Smell gas? Get out first, then call 911 and your gas company." |
| planning value, counted at | A number SOS SMS plans with, labelled with its basis (`reference/resolution-register.md`), never presented as a measured result; the measured figure replaces it once a zone runs. A fact that cannot exist before launch is given as the method and the stage that count it; no number is written until then |
| {{merge field}} | A per-zone, per-member, per-contractor, or per-message value, filled from a named record when the message is sent. Never typed by hand |

## Retired terms (2026-10-11, 2026-10-20, 2026-10-21)

| Retired | Why | Use |
|---|---|---|
| SOS SMS fee | There is no fee per request (R02, retired) | the membership, and the trip charge on use |
| confirming text, reply YES | A member's request text is the whole request | request text |
| payment link (for dispatch) | The card is on file from joining | card on file |
| owned share, first text to paid | Paid search no longer buys requests (R30, retired) | cost per new paid member, by channel |
| customer (for SOS SMS's demand side) | The demand side is members | member; "homeowner" before joining |
| founding contractor, founding period, founding terms, founding list, founding zone | Retired with the membership revision: every contractor pays the fee from the first job and joins any time (R05 to R07) | the first cohort; the launch zone; the terms |
| covered hours, `{{covered hours}}`, `{{monthly price}}`, `{{annual price}}` | An open zone is covered at every hour (R15); the prices are decided (R51, R52, R65, R66) | open zone; the price as written, or `{{plan}}` |
| refund (on a late arrival) | A late arrival keeps the trip charge; Plus and Premier get a credit (decision 3) | the late-arrival credit; on a no-show, "the $99 comes back in full" |
| first refusal; stop-the-water steps (for every request) | Every request goes to all matched contractors at once (R13); three trades, not one | first to accept; the first steps for the problem |

## Banned near-synonyms

| Reached for | Why it is wrong | Use |
|---|---|---|
| SOS (alone) | Name collision with unrelated plumbing companies | SOS SMS |
| lead, hot lead, qualified lead | Means paying to look; it is the model SOS SMS replaces | request |
| exclusive | Requests go to all matched contractors at once | shared openly, first to accept |
| escrow | A legal term for licensed arrangements | SOS SMS holds the trip charge until you arrive |
| pre-qualified, pre-screened customer | Unsubstantiated quality claim (S01) | matched to the trades and area you set |
| service fee, call-out fee, per-request fee | Blurs the trip charge with the membership | trip charge, or membership, named separately |
| subscriber, subscription (in member copy) | Reads as a media plan, and hides what the member gets | member, membership |
| warranty, protection plan, insurance, coverage | SOS SMS does not pay for repairs (R21, R53) | membership: one text, an arrival time inside 90 minutes, and on Plus and Premier the 90-minute guarantee |
| guaranteed arrival time | The arrival time is a commitment; on Plus and Premier the window is backed by a credit | arrival time, and the 90-minute window |
| emergency service, 24/7 emergency plumber, electrician, or HVAC | SOS SMS dispatches; it is not an emergency service | an emergency home repair membership, by text |
| every contractor in your area | Only contractors on SOS SMS, and only at density | the vetted contractors on SOS SMS for your trade |
| Google Guaranteed, Google Screened | Retired by Google on 2025-10-20 (S09), and not ours | license and insurance checked by SOS SMS |
| your trip charge (to contractors) | One trip charge per trade and zone, set by SOS SMS (decision 5) | your price for the work |

## Distinctions that must never blur

| Pair | The difference |
|---|---|
| arrival time vs 90-minute window | The contractor commits to an arrival time inside the window. On Plus and Premier, SOS SMS stands behind the window with the late-arrival credit. A claim true of one is false of the other |
| membership vs trip charge | The membership is paid before the need, every month or year. The trip charge is paid only on use, goes to the contractor, and is credited to the repair. Never one number for both |
| membership vs warranty | A warranty pays for a covered repair. The membership gets a vetted contractor to the door with one text; it pays for no repair, on any plan |
| late arrival vs no-show | Late: the trip charge stands, because it pays for the work. No-show: the $99 comes back in full and the contractor is paid nothing. Plus and Premier get the credit on both |
| contractor vs member | Two audiences, two value propositions, never one asset |
| dispatch vs repair | SOS SMS dispatches. The contractor repairs. There is no guarantee on the work |
| PLANNED vs live | Nothing is live. Copy is written for launch day and held until the capability ships |

The distinction that matters most: **the arrival time is the contractor's promise; the 90-minute guarantee is SOS SMS's promise, on Plus and Premier.** Every guarantee claim hinges on keeping them apart.
