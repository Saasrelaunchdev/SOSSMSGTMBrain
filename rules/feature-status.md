# Feature status ledger

Governs what can be promised. Update this file the moment status changes, before any copy follows.
last_reviewed: 2026-10-04

Legend:
- SHIPPED: live now, claimable in the present tense. **Nothing is SHIPPED.**
- IN BUILD: committed and being built. Mark "coming at launch" or omit.
- PLANNED: in the product design, with every rule decided; built in Stage 0 or at the stage named. Copy may describe it for launch day only, held until it ships.
- HELD: decided and planned, but kept out of copy until the named condition is met.
- NOT AT LAUNCH: decided out of the launch product. Out of every piece of copy.

Source: the product features matrix, both runs' Phase 1, the cross-side check, and the resolution register (`reference/resolution-register.md`), decided 2026-10-03. Every rule below is decided; nothing waits on a founder.

## Customer side
- One number to text: PLANNED. One local number in the launch metro's area code, registered for A2P 10DLC (decision 9).
- Broadcast to matched contractors, all at once, first to accept: PLANNED. The first to accept with an arrival time inside the remaining window gets the job (decision 4).
- Arrival time texted on acceptance, with the contractor's name: PLANNED.
- 90-minute guarantee with automatic refund: PLANNED. The 90 minutes start at the customer's confirming text; the $99 trip charge comes back automatically; covered areas and hours are the zone's, named on the zone page (decision 3).
- Trip charge stated by text before dispatch, credited to the repair: PLANNED. $99 for plumbing, one per trade and zone, day or night, set by SOS SMS (decision 5).
- SOS SMS fee: PLANNED. $49 per dispatched request, a separate line from the trip charge, charged only when a contractor accepts (decision 2).
- No acceptance: PLANNED. The customer is told within 15 minutes and is never charged (R11).
- Requests outside covered hours: PLANNED. Not dispatched; the customer gets the stop-the-water steps and the safety line and pays nothing (R15).
- Contractor's Google rating sent with acceptance, where they have one: PLANNED.
- Stop-the-water first reply: PLANNED.
- Safety triage (gas, smoke, fire, injury): PLANNED. The safety reply goes first, and nothing is broadcast until the customer confirms they are safe and the utility or 911 has been called (decision 8).
- Contact card, Text READY, forwardable card: PLANNED.
- Automatic refund text: PLANNED.
- Customer identity hidden until acceptance: PLANNED. Contractors see the problem, any photos or video, and an approximate distance and cross-street area; the address goes only to the contractor who accepts (decision 4).
- Customers without a card: PLANNED. Dispatch needs a card or a phone wallet through the payment link; without one, the customer gets the free help by text and pays nothing (R16).
- Second contractor after a miss (the relaunch): HELD. SOS SMS pays the second contractor's trip charge from the SOS SMS fee; out of copy until dispatch supports it (R17).
- Price range before arrival: NOT AT LAUNCH (R49). The $99 trip charge is stated before dispatch instead.
- Pay on arrival without a card: NOT AT LAUNCH (R16).
- Household membership: NOT AT LAUNCH (R19).
- Guarantee on the repair: NOT AT LAUNCH. The guarantee covers the arrival window only (R21).

## Contractor side
- Sign-up by text (JOIN), documents, payout setup, agreement: PLANNED. About 5 minutes by text (R36).
- License and insurance checks before the first request: PLANNED. Rechecked every 6 months and on each policy's expiry date (decision 7).
- Accept or decline freely, without changing which requests arrive: PLANNED.
- Response window: PLANNED. 10 minutes, when marked available (R12).
- Zero cost to join: PLANNED. $0 to join, $0 per request seen or declined, no subscription or seat fee (decision 2).
- Contractor fee: PLANNED. $0 a job in the founding period (the founding zone's first 6 months open); then $25 per completed paid job, deducted from the trip charge payout. Founding contractors keep $0 a job for 12 months after the founding period (decision 2, R05, R06).
- Trip charge collected before the contractor rolls, released on arrival: PLANNED. Stripe Connect: authorized at the confirming text, captured at acceptance, held, released on arrival (decision 6).
- Payout timing: PLANNED. Within 2 business days of arrival (decision 6, R14).
- Add-a-technician flow: PLANNED.
- Fifth-trip referral prompt: PLANNED. No referral reward at launch; contractors are thanked by text (R18).
- Lead Cost Check calculator: PLANNED.
- Photos or video before accepting: PLANNED, when the customer sends them (decision 4).
- Accepting requests by reply text, no app: PLANNED.
- First refusal on a contractor's own customers: HELD. 5 minutes of first refusal; SOS SMS is offered as a contractor's after-hours line only once dispatch supports it (R13).
- Paid priority for contractors: NOT AT LAUNCH.

## Stage 0 work, decided and not yet done
- Register the SOS SMS number for A2P 10DLC before any test text (decision 9, S32).
- Get Google's written confirmation that a dispatch service may run standard search ads for plumbing (S70, S71); verify message assets (S72) (decision 11).
- Set up Stripe Connect and test a trip charge through authorize, capture, hold, release, and payout (decision 6).
- Run the US trademark search and the search check in the zone (decision 10).
- Counsel review of the terms on one page and the guarantee.

## Internal assets
- GTM walkthrough deck (25 slides, 22 dashboards; pricing on slide 23 and M3; the twelve decisions on slide 24 and M4): BUILT, internal only, not a customer surface. Every value resolved 2026-10-04.
- Brand identity v1 (logo, palette, type, brand book): BUILT. Dark palette kept as validated (2026-10-04).

## Demo rule
Nothing here may be screen-recorded, narrated, or shown as if a contractor or customer could use it today. Any mockup carries "Pre-launch. Not live." on screen.
