# The terms on one page (contractors)

Status: **approved 2026-10-04 as the live test of the resolved brain; the member-side lines revised 2026-10-11 (the membership revision).** Produced using only this repository, from `templates/terms-on-one-page.md`, `reference/pricing-and-economics.md`, `reference/marketplace-cross-side.md`, `reference/objection-handling.md`, and `reference/resolution-register.md`, then run through `ops/QA-checklist.md`. Publishes on the contractor page from Stage 1 (R23), after counsel review, with the same words in the founding contractor agreement.

---

## SOS SMS terms for contractors, on one page

SOS SMS is building an emergency dispatch line by text for licensed, insured plumbing contractors in {{zone}}. These are the terms it will run on, in full.

**What you'll pay.** Nothing to join, and nothing for a request you see, decline, or lose. No subscription and no per-lead fee. During the founding period, the zone's first 6 months open to members, you pay $0 a job. After it, $25 per completed paid job, taken from the trip charge payout. Founding contractors keep $0 a job for 12 months after the founding period.

**When you'll be paid.** The trip charge goes on the SOS SMS member's card when you accept, before you roll. SOS SMS will hold it and release it to you when you arrive by the time you committed to. It reaches your bank within 2 business days of arrival.

**How requests will work.** Every matched contractor sees a request at once, and the first to accept with an arrival time inside the window gets it. Before you accept, you see the problem, any photos or video the member sent, and the approximate area; the address comes after you accept. Each request stays open to you for 10 minutes, in the hours you mark available. Decline anything; declining does not change which requests reach you.

**What you'll commit to.** An arrival time when you accept. Crediting the trip charge to the work if the member goes ahead. A current license and insurance, checked at sign-up, every 6 months, and on each policy's expiry date. Your price for the work stays yours; the trip charge is set by SOS SMS, one per trade and zone: $99 for plumbing.

**If you're late.** If you miss the time you committed to, the member's refund comes from your trip charge. If SOS SMS caused the miss, SOS SMS pays the refund.

**If there's a dispute.** Text SOS SMS. A founder settles it from the request log: the member's request text, your acceptance, your committed arrival time, and your arrival.

**Citing your results.** Before your first job, we'll ask whether SOS SMS may quote your outcomes.

**To stop.** Text STOP at any time.

To join, text JOIN to {{number}}. It takes about 5 minutes, with no call.

---

## QA record
Ticked against `ops/QA-checklist.md`: no em or en dashes; no banned words; the full name every time; every number is a decided register value (decisions 2 to 7, R05, R06, R12, R14, R36); merge fields only for `{{zone}}` and `{{number}}`, both registered; channel in the mix (the contractor page); one side; future tense for what SOS SMS is building; "request", never "lead", for SOS SMS; no volume or earnings claim; no "escrow", "exclusive", or "pre-qualified"; the late-arrival rule matches the member guarantee (decision 3, cross-side row 1).

## What the test found
One gap, fixed before this page was written: the template had no line for the 10-minute response window (R12), which a contractor needs to judge night availability. Added to `templates/terms-on-one-page.md`. The brain carried every other fact the page needed.
