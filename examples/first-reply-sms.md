# Example: member texts, from joining to the first emergency (members)

Status: **voice reference, rewritten 2026-10-11 for the membership revision; revised 2026-10-21 for the three trades and the three plans: the welcome names `{{plan}}`, the guarantee is named only for Plus and Premier, and a late arrival keeps its trip charge.** It replaces the first reply of 2026-10-04, which asked for a YES and sent a payment link. Written from the brain with every value decided or a merge field. It ships when the zone opens to members (R55), after carrier registration (decision 9) and once a licensed contractor in each trade has reviewed the first steps (Stage 0). Template: `templates/first-reply-sms.md`.

Scenario: a homeowner in the launch zone joins Plus, on the annual plan, on a Sunday afternoon in October, so dispatch covers them from that day (R54). In January, at 1:10 a.m., water comes through their kitchen ceiling.

---

## On joining, in October

**W1**
> SOS SMS here, {{first name}}. Your {{plan}} membership for {{zone name}} is active. This number sends automated texts; to reach a person, text HELP.

**W2**, with the contact card attached
> Save this contact so SOS SMS is in your phone before you need it. When something breaks, this is the number you text.

**W3**
> How it works: text us what broke, plumbing, HVAC, or electrical, from any phone on your membership. It goes at once to the licensed, insured contractors on SOS SMS for that trade near your home, and the first who can come accepts and texts you an arrival time. Your card and address are already on file, so that one text is the whole request.

**W4**
> When you use it, a $99 trip charge goes on your card when a contractor accepts, and counts toward the repair. If no one is there after 90 minutes, text NEXT.

**W5**, Plus and Premier only (Premier writes 12 months)
> Your 90-minute guarantee: if your contractor arrives after the 90 minutes or does not come, we credit the membership you paid for the 6 months before your request to your next bills. Any hour, anywhere in {{zone neighborhoods}}.

**W6**
> For fire, a gas smell, or anyone hurt, call 911 first.

## The emergency, in January

The member's only text:
> water coming through the kitchen ceiling

**Message 1, at once**
> SOS SMS here, {{first name}}: this is an automated reply, and your request is going now to the licensed, insured {{trade}} contractors on SOS SMS near your home. To reach a person, text HELP. For fire, a gas smell, or anyone hurt, call 911 first.

**Message 2, the same moment**, the first steps for a plumbing problem (for no heat, no cooling, or a dead circuit, the safety steps only)
> To slow the water now, turn off your main water shutoff, usually where the water line enters the house, often near the water heater or in the basement. Turn a round handle clockwise until it stops; turn a lever a quarter turn so it sits across the pipe. Keep clear of wet ceilings and anything electrical near the water.

**Message 3, on acceptance**
> {{contractor name}} accepted and is on the way. Arrival time: {{arrival time}}; Google rating: {{rating}}, where they have one. They get your address now; nobody else does.

**Message 4, the same moment** (Basic leaves out the guarantee sentence; Premier writes 12 months)
> The $99 trip charge is now on your card on file, and counts toward the repair if you go ahead. Your 90-minute guarantee: if {{contractor name}} is not there within 90 minutes of your text, we credit your last 6 months of membership to your next bills. If no one is there after 90 minutes, text NEXT.

**Message 5, after the job**
> Thanks for using SOS SMS. Did your contractor arrive within the window? Would you tell a neighbor?

**If no contractor can come**, in place of messages 3 and 4, within 15 minutes
> SOS SMS here: no contractor on SOS SMS could take your request in time, and your card has not been charged. Keep the water off at the main shutoff. To reach a person, text HELP.

**If the contractor arrives after the 90 minutes**, Plus and Premier
> SOS SMS here: {{contractor name}} arrived after the 90 minutes. The trip charge still pays for the work, and we have credited {{credit amount}} to your next bills, under your 90-minute guarantee. Nothing to claim.

**If the member texts NEXT** after the 90 minutes (the last sentence on Plus and Premier only)
> SOS SMS here: your $99 trip charge is coming back to your card in full, and your request is going now to the other contractors on SOS SMS. A new acceptance is a new request, with its own $99 trip charge and its own 90 minutes. We have also credited {{credit amount}} to your next bills.

## A text from someone who is not a member (R57)

Scenario: a neighbor who was forwarded the contact card but never joined texts "basement drain backing up" at 11:40 p.m.

**N1**
> SOS SMS here, with an automated reply; to reach a person, text HELP. For fire, a gas smell, or anyone hurt, call 911 first.

**N2**
> Until the drain is cleared, stop using water in the house: no flushing, no taps, no dishwasher or washing machine. Keep people and pets away from the water, and stay clear of anything electrical near it.

**N3**
> SOS SMS sends contractors to members only, so for tonight, call a licensed local plumber directly. Nothing has been charged. When things are calm, text READY for a five-question home check and how membership works.

---

## Why this works
- **The work happens at joining.** The card, the home address, and consent go on file in October (R54), so in January the member's whole request is six words. No offer, no link, nothing to confirm, no payment screen.
- **Who before what.** Message 1 names SOS SMS, says it is automated, says the request is already going to the contractors in its trade, says how to reach a person, and gives the safety line (S72, decision 8). There is no link anywhere in the emergency, so nothing looks like the scam pattern of a link from an unknown number (S59).
- **Value at once.** Message 2 helps before anyone accepts: shutoff and safety only, never repairs.
- **Two prices, never one.** The membership was paid before the need and never appears in an emergency text. The trip charge is named on use, at acceptance, credited to the repair. There is no fee per request.
- **The clock is the member's text.** "Within 90 minutes of your text" is decision 3 in the member's own words, with its scope in the same thread.
- **The guarantee only where the plan has it.** W5 and the credit texts go to Plus and Premier; a Basic member reads the trip charge, NEXT, and the safety line, never a guarantee. A late arrival keeps its trip charge, because it pays for the work (decision 3).
- **The truth to a non-member.** Dispatch is for members, so the reply gives the safety line and the first steps, says plainly to call a plumber directly tonight, charges nothing, and leaves joining for a calmer moment with READY.
- **Merge fields, never typed.** Names, the plan, the zone, the trade, the arrival time, the rating, and the credit amount fill from the member, zone, and request records when sent.
- **One idea per message**, short lines, the full name every time.
