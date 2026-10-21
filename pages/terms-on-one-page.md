# The terms on one page (contractors)

Status: **approved 2026-10-04 as the live test of the resolved brain; the member-side lines revised 2026-10-11 (the membership revision); revised 2026-10-21 for three trades, the contractor fee from the first job, and the late-arrival rule of the tiers revision (2026-10-20).** Produced using only this repository, from `templates/terms-on-one-page.md`, `reference/pricing-and-economics.md`, `reference/marketplace-cross-side.md`, `reference/objection-handling.md`, and `reference/resolution-register.md`, then run through `ops/QA-checklist.md`. Publishes on the contractor page from Stage 1 (R23), after counsel review, with the same words in the contractor agreement.

---

## SOS SMS terms for contractors, on one page

SOS SMS is building an emergency dispatch line by text for licensed, insured plumbing, HVAC, and electrical contractors in {{zone}}. These are the terms it will run on, in full, the same for every contractor in every trade.

**What you'll pay.** Nothing to join, and nothing for a request you see, decline, or lose. No subscription, no seat fee, and no per-lead fee. From your first job, $25 per completed paid job, taken from the trip charge payout, so $74 of each $99 trip charge reaches you. Your terms never depend on which plan the member is on.

**When you'll be paid.** The trip charge goes on the SOS SMS member's card when you accept, before you roll. SOS SMS will hold it and release it to you, less the fee, when you arrive. It reaches your bank within 2 business days of arrival.

**How requests will work.** Requests match the trades and area you set. Every matched contractor sees a request at once, and the first to accept with an arrival time inside the window gets it. Before you accept, you see the problem, any photos or video the member sent, and the approximate area; the address comes after you accept. Each request stays open to you for 10 minutes, in the hours you mark available. Decline anything; declining does not change which requests reach you.

**What you'll commit to.** An arrival time when you accept. Crediting the trip charge to the work if the member goes ahead. A current license for each trade you take, and insurance, checked at sign-up, every 6 months, and on each policy's expiry date. Your price for the work stays yours; the trip charge is set by SOS SMS, one per trade and zone: $99 in each of plumbing, HVAC, and electrical.

**If you're late.** If you arrive after the time you gave, the trip charge still pays for the work, and the late arrival is recorded. If you accept and do not come, the trip charge goes back to the member and you are paid nothing. Two late arrivals or no-shows in a rolling 90 days pause your requests until a person from SOS SMS reviews them.

**If there's a dispute.** Text SOS SMS. A founder settles it from the request log: the member's request text, your acceptance, your committed arrival time, and your arrival.

**Citing your results.** Before your first job, we'll ask whether SOS SMS may quote your outcomes.

**To stop.** Text STOP at any time.

To join, text JOIN to {{number}}. It takes about 5 minutes, with no call.

---

## QA record
Ticked against `ops/QA-checklist.md`: no em or en dashes; no banned words; the full name every time; every number is a decided register value (decisions 2 to 7, R05, R06, R12, R14, R36); merge fields only for `{{zone}}` and `{{number}}`, both registered; channel in the mix (the contractor page); one side; future tense for what SOS SMS is building; "request", never "lead", for SOS SMS; no volume or earnings claim; no "escrow", "exclusive", or "pre-qualified"; the late-arrival rule matches the member guarantee (decision 3, cross-side row 1).

Revised 2026-10-21 (the founding terms retired; the tiers revision, 2026-10-20): three trades; the fee from the first job, $74 of each $99 to the contractor (R03), replacing R05 and R06, both retired; the license for each trade (decision 7); the late-arrival rule now matches decision 3 as revised: a late contractor keeps the trip charge less the fee, a no-show is paid nothing, and two in a rolling 90 days pause requests until review (R10, R17, R67). Re-ticked: every number a decided register value (decisions 2 to 7, R03, R12, R14, R36, R67); no founding anything; nothing tied to the member's plan; every other tick unchanged.

## What the test found
One gap, fixed before this page was written: the template had no line for the 10-minute response window (R12), which a contractor needs to judge night availability. Added to `templates/terms-on-one-page.md`. The brain carried every other fact the page needed.
