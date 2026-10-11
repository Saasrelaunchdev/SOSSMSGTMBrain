# Example: cold email sequence (contractors)

Status: **voice reference, approved 2026-10-04; member wording revised 2026-10-11 (the membership revision).** From Run 1 Phase 8, checked against the brain, with every value decided. Sends once the terms on one page and the Lead Cost Check are published and the sending setup is in place (Stage 1). Template: `templates/cold-email.md`.

Every email ends with: {{sender name}}, SOS SMS, {{postal address}}. Not interested? {{opt-out link}} (S73).

---

**Email 1, day 0. Subject: What did each job from your leads cost?**
> Hi {{first name}}, one question for {{business}}: what did each booked job from your lead platforms cost last month, counting the leads that never answered?
>
> This two-minute check works it out from four numbers you already know: {{link}}. Your answers stay yours.
>
> We're building SOS SMS, emergency jobs by text in {{zone}}, with no lead fees and the trip charge collected before you roll. SOS SMS will be paid by members' monthly or annual fees, and by you only per completed paid job after the founding period.

**Email 2, day 3. Subject: How a job works in three texts**
> Here is how a job will work once SOS SMS opens in {{zone}}. An SOS SMS member texts what broke. Every matched contractor in the area sees it at once, and the first to accept gets the job. Everyone else pays nothing, because nobody pays to look.
>
> The trip charge will be on the member's card before you roll. (Image: the three texts, labeled as a mockup.) See how it works: {{contractor page}}.

**Email 3, day 7. Subject: The terms, on one page**
> What you'll pay: nothing to join or to see a request. As a founding contractor, $0 a job through the founding period and 12 months after, then $25 per completed paid job. When you're paid: the trip charge is released when you arrive by your committed time and reaches your bank within two business days. What you commit to: an arrival time when you accept, crediting the trip charge to the work if the member goes ahead, and current license and insurance. If you're late: the member's refund comes from the trip charge.
>
> All of it in writing: {{terms link}}.

**Email 4, day 12. Subject: Founding contractors in {{zone}}**
> We're opening memberships in {{zone}} once enough contractors have joined to cover it. Founding contractors get the first requests there and founding terms if they join by {{founding close date}}.
>
> To join, text JOIN to {{number}}; it takes about 5 minutes, with no call. Last email unless you reply.

---

## Why this works
- **Their number first.** Email 1 asks about the contractor's own cost and gives them a tool that is useful even if they never join. No claim about SOS SMS results.
- **The weak point, said plainly.** Email 2 states the shared request instead of hiding it, and makes it harmless.
- **Terms, not pitch.** Email 3 is what a burned contractor actually wants: what they pay, when they are paid, what they owe, in decided numbers.
- **Pre-launch framing.** "We're building", "once SOS SMS opens", "will have paid": the design, never a working service (`rules/writing-rules.md`).
- **No false urgency.** Email 4 uses only the real founding list close date, 60 days after the first email (R07), then stops.
- "Request" for SOS SMS, "leads" only for the platforms the contractor already pays. Every per-email detail is a merge field filled from the contractor list record.
