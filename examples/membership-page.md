# Example: the membership page, zone template (members)

Status: **voice reference, rewritten 2026-10-11 for the membership revision; revised 2026-10-21 for the three trades and the three plans, in the words of the pricing handoff's membership page table.** It replaces the zone landing page of 2026-10-04, which sold dispatch during an emergency. Written from the brain with every value decided or a merge field. Publishes only for an open zone (R55), after carrier registration (decision 9), with the member terms and the automatic renewal disclosures reviewed by counsel (S87). Template: `templates/membership-page.md`.

---

## One text, and help is on the way.
Join SOS SMS before anything breaks. When something does, plumbing, HVAC, or electrical, you text what happened, and the licensed, insured contractors on SOS SMS for that trade near you see it at once.

(ZIP check: "Is your home covered? Enter your ZIP.")
- Open zone: "Memberships are open in {{zone name}}." The join button.
- A zone not open yet: "SOS SMS isn't open in your area yet. Join the launch list: no charge, and no service until we open."
- Outside every zone: "SOS SMS doesn't cover your area yet. Here is how to get your home ready anyway." The readiness steps.

For fire, a gas smell, or anyone hurt, call 911 first.

### How it works in one text
1. You join once, now, with your card and your home address.
2. When something breaks, you text what happened to {{SOS SMS number}}. That one text is the whole request.
3. The licensed, insured contractors on SOS SMS for that trade near you see it at once. The first who can come accepts and texts you an arrival time, with their name and their Google rating where they have one.

### Three plans
(Toggle: "A year, two months free" shown first · "A month")

| | Basic | Plus · Most popular | Premier |
|---|---|---|---|
| A year (two months free) | $100 a year | $150 a year | $350 a year |
| A month | $10 a month | $15 a month | $35 a month |
| Trades | Plumbing, HVAC, and electrical | Plumbing, HVAC, and electrical | Plumbing, HVAC, and electrical |
| Phones that can text for your home | Your phone | Up to 5 phones in your home | Up to 10 phones, across two homes |
| The late-arrival credit | Not included | Your last 6 months of membership, up to $90 on the monthly plan; $75 on the annual plan | Your last 12 months of membership, up to $420 on the monthly plan; $350 on the annual plan |
| Trip charge paid by SOS SMS | Not included | Not included | One a membership year. Annual: from the day you join. Monthly: after 6 paid months. |
| A second home | Not included | Not included | A second home in {{zone neighborhoods}} |
| Dispatch starts | Annual: from the day you join. Monthly: 30 days after you join. | Annual: from the day you join. Monthly: 30 days after you join. | Annual: from the day you join. Monthly: 30 days after you join. |
| | Join Basic | Join Plus | Join Premier |

When you use it: a $99 trip charge, on your card when a contractor accepts. It counts toward the repair if you go ahead. Premier: one a year paid by SOS SMS.

There is no fee per request, and no plan is faster than another: every plan's text reaches every matched contractor at once. The repair price comes from the contractor, on site.

### The 90-minute guarantee, on Plus and Premier
If the contractor is late, the trip charge pays for the work, and we credit the membership you paid for the 6 months before your request (12 months on Premier) to your next bills. If a contractor accepts and does not come, the trip charge comes back in full, and the credit applies. Covered: any hour, anywhere in {{zone neighborhoods}}. (Link: read the guarantee in full.)

On every plan: if no contractor accepts, you pay nothing, and we tell you within 15 minutes. If no one is there after 90 minutes, text NEXT and your request goes to the other contractors. If a contractor accepts and does not come, the trip charge comes back in full.

### What every plan includes, and what none does
Included: one text starts dispatch, with your card and address already on file; plumbing, HVAC, and electrical, in one membership; one text reaches every matched contractor at once, at any hour; an arrival time inside 90 minutes, the moment a contractor accepts; never charged if no contractor accepts; NEXT after a miss; license and insurance checked before they can take a job; the contractor's Google rating, where they have one; the trip charge credited to the repair if you go ahead; a person by text when you text HELP, with a reply within 15 minutes, at any hour; the readiness kit at joining, and a readiness check by text once a year.

Not included on any plan: the repair, parts, or a guarantee on the work. SOS SMS is not a warranty or insurance. A warranty pays for covered repairs; SOS SMS gets a vetted contractor to your door.

### Cancel or change plans any time
Cancel on this page, or text HELP and a person will cancel it for you. Annual ends at the end of the paid year, monthly at the end of the paid month; no partial refunds. Annual members get a reminder before {{renewal date}}, with the price and how to cancel. Upgrade any time: on an annual plan the new plan starts at once, with the difference for the rest of the year charged; on a monthly plan, 30 days after you upgrade. A downgrade starts at the end of the paid period.

### Who we are
SOS SMS dispatches licensed, insured contractors. The contractor does the work. We check the license for each trade they take, and their insurance, before they can take a job, every six months, and on each policy's expiry date.

### Your information
Only the contractor who takes your job gets your address. We don't sell your information, and we don't use it for ads.

### Join
Your plan, your card (and a backup card, if you like), your home address (two on Premier), the phones that can text for your home, and your agreement to the member terms. Then we text you the contact card to save.
(Button: "Join before you need it")

Covered: any hour, anywhere in {{zone neighborhoods}}. To reach a person, text HELP. How it works · The guarantee · Member terms · Privacy

---

**On a partner's page**, above the ZIP check: "Welcome from {{partner}}." Directly under it: "{{partner}} is paid a fee for each new SOS SMS member who joins through this link." Every link on the page carries {{code}}.

**Design notes** (the pricing handoff): Plus in the middle, flagged "Most popular", on the annual plan first. The plan prices and the $99 trip charge on separate lines, never one total. The safety line never animates. The plan mix and every contribution figure stay off the page.

## Why this works
- **Written for a calm reader.** People land here from a partner, an email, a guide, or a readiness search, before anything breaks. So the page sells being ready, not dispatch tonight: the promise, then the ZIP check, because memberships exist only in open zones (R55).
- **The safety line still sits at the top**, because some readers arrive in the middle of a problem.
- **Each section answers one question, in the order a careful buyer asks it:** how it works, which plan and what it costs, what if they are late, what it does not do, how to leave, who you are, who sees my address.
- **Two prices, never one total.** The plan, and the trip charge only when used, credited to the repair (decisions 2, 5, and 6).
- **The plans differ by what stands behind the arrival time, never by speed.** The credit, the phones, and Premier's second home and trip charge slide by plan; dispatch is the same on all three, and the guarantee is named only where a plan has it (decision 3).
- **The weak point answered before the card.** A membership costs something every month whether or not anything breaks (R46). The page answers with what it includes, the trip charge only on use, and cancel any time, all above the join button (S87).
- **It never calls SOS SMS a plumber, a warranty, insurance, or an emergency service**, and the prices are the decided ones, written as they are (R51, R52, R65, R66).
