# Example: cold email sequence (contractors)

Status: **voice reference, approved 2026-10-04; member wording revised 2026-10-11 (the membership revision); revised 2026-10-21 for three trades, the contractor fee from the first job (no founding terms or list), and the late-arrival rule of the tiers revision (2026-10-20).** From Run 1 Phase 8, checked against the brain, with every value decided. Sends once the terms on one page and the Lead Cost Check are published and the sending setup is in place (Stage 1). Template: `templates/cold-email.md`.

Every email ends with: {{sender name}}, SOS SMS, {{postal address}}. Not interested? {{opt-out link}} (S73).

---

**Email 1, day 0. Subject: What did each job from your leads cost?**
> Hi {{first name}}, one question for {{business}}: what did each booked job from your lead platforms cost last month, counting the leads that never answered?
>
> This two-minute check works it out from four numbers you already know: {{link}}. Your answers stay yours.
>
> We're building SOS SMS, emergency jobs by text in {{zone}}, with no lead fees and the trip charge collected before you roll. SOS SMS will be paid by members' monthly or annual fees, and by you only per completed paid job.

**Email 2, day 3. Subject: How a job works in three texts**
> Here is how a job will work once SOS SMS opens in {{zone}}. An SOS SMS member texts what broke. Every matched contractor in the area sees it at once, and the first to accept gets the job. Everyone else pays nothing, because nobody pays to look.
>
> The trip charge will be on the member's card before you roll. (Image: the three texts, labeled as a mockup.) See how it works: {{contractor page}}.

**Email 3, day 7. Subject: The terms, on one page**
> What you'll pay: nothing to join or to see a request; $25 per completed paid job, taken from the $99 trip charge, so $74 of it reaches you. When you're paid: the trip charge is released when you arrive and reaches your bank within two business days. What you commit to: an arrival time when you accept, crediting the trip charge to the work if the member goes ahead, and current license and insurance. If you're late: you keep the trip charge, the late arrival is recorded, and two in 90 days pause your requests until we review them; if you accept and don't come, the trip charge goes back to the member.
>
> All of it in writing: {{terms link}}.

**Email 4, day 12. Subject: When SOS SMS opens in {{zone}}**
> We're opening memberships in {{zone}} once enough plumbing, HVAC, and electrical contractors have joined to cover every hour of the day. Every contractor joins on the same terms, written on one page.
>
> To join, text JOIN to {{number}}; it takes about 5 minutes, with no call. Last email unless you reply.

---

## Why this works
- **Their number first.** Email 1 asks about the contractor's own cost and gives them a tool that is useful even if they never join. No claim about SOS SMS results.
- **The weak point, said plainly.** Email 2 states the shared request instead of hiding it, and makes it harmless.
- **Terms, not pitch.** Email 3 is what a burned contractor actually wants: what they pay, when they are paid, what they owe, in decided numbers.
- **Pre-launch framing.** "We're building", "once SOS SMS opens", "will have paid": the design, never a working service (`rules/writing-rules.md`).
- **No urgency at all.** Every contractor joins on the same terms, any time, so there is no deadline to invent (R07, retired); Email 4 says when the zone opens, then stops.
- **One set of terms.** The same $25 from the first job in every trade, and nothing in any email depends on which plan a member is on.
- "Request" for SOS SMS, "leads" only for the platforms the contractor already pays. Every per-email detail is a merge field filled from the contractor list record.
