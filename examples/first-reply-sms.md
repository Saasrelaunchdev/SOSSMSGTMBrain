# Example: the first reply (customers)

Status: **voice reference, approved 2026-10-04.** Written from the brain with every value decided (decisions 3, 5, 8; R50). It ships when the zone opens, after carrier registration (decision 9) and once a licensed plumber has reviewed the shutoff steps (Stage 0). Template: `templates/first-reply-sms.md`.

Scenario: a customer in the founding zone texts "water coming through the kitchen ceiling" at 1:10 a.m.

---

**Message 1**
> SOS SMS here. This is an automated reply. To reach a person, text HELP. For fire, a gas smell, or anyone hurt, call 911 first.

**Message 2**
> To slow the water now: turn off your main water shutoff. It is usually where the water line enters the house, often near the water heater or in the basement. Turn a round handle clockwise until it stops; turn a lever a quarter turn so it sits across the pipe. Keep clear of wet ceilings and anything electrical near the water.

**Message 3**
> If you want a plumber tonight: we send your request to the licensed, insured plumbers on SOS SMS near you, all at once. The first who can come accepts and texts you an arrival time. The trip charge is $99, credited to the repair if you go ahead, plus a $49 SOS SMS fee. If they are not there within 90 minutes of your YES, the $99 trip charge comes back. Reply YES to agree. We send no payment link until you do.

**Message 4, after YES**
> Thanks. Here is the SOS SMS payment link for the $99 trip charge and the $49 SOS SMS fee: {{link}}. Your card is charged only when a plumber accepts. If no one accepts, we tell you within 15 minutes and you pay nothing.

**Message 5, on acceptance**
> {{contractor name}} is on the way. Arrival time: {{arrival time}}. Google rating: {{rating}}, where they have one. They get your address now; nobody else does.

---

## Why this works
- **Who before what.** Message 1 names SOS SMS, says it is automated, says how to reach a person, and gives the safety line before anything else (S72, decision 8). The scam pattern is a link from an unknown number (S59); there is no link until message 4, after agreement.
- **Value before payment.** Message 2 helps whether or not they buy. That is the demand driver. The steps cover shutoff and safety only, never repairs.
- **Mechanics, not adjectives.** Who comes, how they are chosen, what it costs in two named lines, what is credited, what happens if they are late or nobody accepts. No "fast", no "best", no average.
- **The clock is the confirming text.** "Within 90 minutes of your YES" is decision 3 in the customer's own terms.
- **Merge fields, never typed.** The link, the contractor's name, their committed arrival time, and their rating fill from the request record when the message is sent.
- **One idea per message**, short lines, the full name every time.
