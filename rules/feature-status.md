# Feature status ledger

Governs what can be promised. Update this file the moment status changes, before any copy follows.
last_reviewed: 2026-10-11

Legend:
- SHIPPED: live now, claimable in the present tense. **Nothing is SHIPPED.**
- IN BUILD: committed and being built. Mark "coming at launch" or omit.
- PLANNED: in the product design, with every rule decided; built in Stage 0 or at the stage named. Copy may describe it for launch day only, held until it ships.
- HELD: decided and planned, but kept out of copy until the named condition is met.
- NOT AT LAUNCH: decided out of the launch product. Out of every piece of copy.

Source: the product features matrix, both runs' Phase 1, the cross-side check, and the resolution register (`reference/resolution-register.md`), decided 2026-10-03 and revised by the membership revision on 2026-10-11. Every rule below is decided; nothing waits on a founder.

## Member side
Revised 2026-10-11, the membership revision: the demand side is a monthly or annual membership, joined before the need.

- Membership, monthly or annual: PLANNED. Billed to the card on file; planning values $10 a month or $100 a year until the launch price is set in Stage 0 (R51, R52); copy writes `{{monthly price}}` and `{{annual price}}` (decision 2).
- Joining: PLANNED. On the membership page, or from Text READY; the card, the home address, and consent to the member terms on file; one address per membership; the contact card sent at once (R54).
- Memberships open per zone: PLANNED. Only once the density number is met for the first trade and the covered hours are named; before then, the launch list: email, no charge, no service promised (R55).
- Cancelling and renewal: PLANNED. Cancel any time on the membership page, or by texting HELP to reach a person; a monthly membership ends at the end of the paid month; annual members get a renewal reminder before `{{renewal date}}` (R56).
- Welcome texts: PLANNED. Membership active, the contact card, how it works in one text, the safety line, text HELP for a person.
- One number to text: PLANNED. One local number in the launch metro's area code, registered for A2P 10DLC (decision 9).
- One request text starts dispatch: PLANNED. The card and address are on file, so the member's one text is the whole request: no forms, no payment entry, nothing to confirm.
- Broadcast to matched contractors, all at once, first to accept: PLANNED. The first to accept with an arrival time inside the remaining window gets the job (decision 4).
- Arrival time texted on acceptance, with the contractor's name: PLANNED.
- 90-minute guarantee with automatic refund: PLANNED. The 90 minutes start at the member's request text; the $99 trip charge comes back automatically; covered areas and hours are the zone's, named on the membership page (decision 3).
- Trip charge on use, credited to the repair: PLANNED. $99 for plumbing, one per trade and zone, day or night, set by SOS SMS (decision 5); stated on the membership page before joining; charged to the card on file when a contractor accepts (decision 6). No fee per request (decision 2).
- No acceptance: PLANNED. The member is told within 15 minutes and is never charged (R11).
- Requests outside covered hours: PLANNED. Not dispatched; the member gets the stop-the-water steps and the safety line and pays nothing (R15).
- A text from a non-member: PLANNED. The safety line, the stop-the-water steps, and how to join; dispatch is for members (R57).
- Contractor's Google rating sent with acceptance, where they have one: PLANNED.
- Stop-the-water first reply: PLANNED.
- Safety triage (gas, smoke, fire, injury): PLANNED. The safety reply goes first, and nothing is broadcast until the member confirms they are safe and the utility or 911 has been called (decision 8).
- Readiness kit (the shutoff guide, Text READY, the contact card), forwardable card: PLANNED (R53).
- Automatic refund text: PLANNED.
- Member identity hidden until acceptance: PLANNED. Contractors see the problem, any photos or video, and an approximate distance and cross-street area; the address on file goes only to the contractor who accepts (decision 4).
- Affiliate program (a code and a disclosed commission per new paid member): PLANNED. $20, paid after the member's first paid month (planning value, R61); never to anyone referring at a home purchase settlement.
- Second contractor after a miss (the relaunch): HELD. SOS SMS pays the second contractor's trip charge from membership revenue; out of copy until dispatch supports it (R17).
- Price range before arrival: NOT AT LAUNCH (R49). The $99 trip charge is stated on the membership page instead.
- Repair coverage, parts, or discounts on repairs: NOT AT LAUNCH. The membership does not pay for repairs (R21, R53).
- Member referral reward: NOT AT LAUNCH. Members are thanked by text (R62).
- Guarantee on the repair: NOT AT LAUNCH. The guarantee covers the arrival window only (R21).

## Contractor side
- Sign-up by text (JOIN), documents, payout setup, agreement: PLANNED. About 5 minutes by text (R36).
- License and insurance checks before the first request: PLANNED. Rechecked every 6 months and on each policy's expiry date (decision 7).
- Accept or decline freely, without changing which requests arrive: PLANNED.
- Response window: PLANNED. 10 minutes, when marked available (R12).
- Zero cost to join: PLANNED. $0 to join, $0 per request seen or declined, no subscription or seat fee (decision 2).
- Contractor fee: PLANNED. $0 a job in the founding period (the founding zone's first 6 months open to members); then $25 per completed paid job, deducted from the trip charge payout. Founding contractors keep $0 a job for 12 months after the founding period (decision 2, R05, R06).
- Trip charge collected before the contractor rolls, released on arrival: PLANNED. Stripe Connect: authorized on the member's card on file when the request text arrives, captured at acceptance, held, released on arrival (decision 6).
- Payout timing: PLANNED. Within 2 business days of arrival (decision 6, R14).
- Add-a-technician flow: PLANNED.
- Fifth-trip referral prompt: PLANNED. No referral reward at launch; contractors are thanked by text (R18).
- Lead Cost Check calculator: PLANNED.
- Photos or video before accepting: PLANNED, when the member sends them (decision 4).
- Accepting requests by reply text, no app: PLANNED.
- First refusal on a contractor's own customers: HELD. 5 minutes of first refusal; a contractor points their own customers to SOS SMS membership for after-hours cover only once dispatch supports it (R13).
- Paid priority for contractors: NOT AT LAUNCH.

## Stage 0 work, decided and not yet done
- Register the SOS SMS number for A2P 10DLC before any test text (decision 9, S32).
- Get Google's written confirmation that SOS SMS may advertise its membership with standard search ads (S70, S71) (decision 11).
- Set the launch price: `{{monthly price}}` and `{{annual price}}` in the zone's price record (R51, R52).
- Test membership billing: card on file, monthly and annual billing, renewal reminders, cancel any time (R56).
- Write the affiliate program terms: the disclosure, the commission, and no payments at a home purchase settlement (R61; S86, S88, S94).
- Set up email sending for the launch list and member email (S73).
- Set up Stripe Connect: save a card at joining, and test a trip charge through authorize, capture, hold, release, and payout (decision 6).
- Run the US trademark search and the search check in the zone (decision 10).
- Counsel review of the terms on one page, the member terms with the automatic renewal disclosures (S87), and the guarantee.

## Internal assets
- GTM walkthrough deck (25 slides, 22 dashboards; pricing on slide 23 and M3; the twelve decisions on slide 24 and M4): BUILT, internal only, not a member surface. Every value resolved 2026-10-04.
- Brand identity v1 (logo, palette, type, brand book): BUILT. Dark palette kept as validated (2026-10-04).

## Demo rule
Nothing here may be screen-recorded, narrated, or shown as if a contractor or member could use it today. Any mockup carries "Pre-launch. Not live." on screen.
