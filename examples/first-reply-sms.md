# Example: member texts, from joining to the first emergency (members)

Status: **voice reference, rewritten 2026-10-11 for the membership revision.** It replaces the first reply of 2026-10-04, which asked for a YES and sent a payment link. Written from the brain with every value decided or a merge field. It ships when the zone opens to members (R55), after carrier registration (decision 9) and once a licensed plumber has reviewed the shutoff steps (Stage 0). Template: `templates/first-reply-sms.md`.

Scenario: a homeowner in the founding zone joins on a Sunday afternoon in October. In January, at 1:10 a.m. and inside the zone's covered hours, water comes through their kitchen ceiling.

---

## On joining, in October

**W1**
> SOS SMS here, {{first name}}. Your membership for {{zone name}} is active. This number sends automated texts; to reach a person, text HELP.

**W2**, with the contact card attached
> Save this contact so SOS SMS is in your phone before you need it. When something breaks, this is the number you text.

**W3**
> How it works: text us what broke. It goes at once to the licensed, insured plumbers on SOS SMS near your home, and the first who can come accepts and texts you an arrival time. Your card and address are already on file, so that one text is the whole request.

**W4**
> When you use it, a $99 trip charge goes on your card when a plumber accepts, and counts toward the repair. If they are not there within 90 minutes of your text, the $99 comes back to you automatically, in {{zone neighborhoods}} during {{covered hours}}.

**W5**
> For fire, a gas smell, or anyone hurt, call 911 first.

## The emergency, in January

The member's only text:
> water coming through the kitchen ceiling

**Message 1, at once**
> SOS SMS here, {{first name}}: this is an automated reply, and your request is going now to the licensed, insured plumbers on SOS SMS near your home. To reach a person, text HELP. For fire, a gas smell, or anyone hurt, call 911 first.

**Message 2, the same moment**
> To slow the water now, turn off your main water shutoff, usually where the water line enters the house, often near the water heater or in the basement. Turn a round handle clockwise until it stops; turn a lever a quarter turn so it sits across the pipe. Keep clear of wet ceilings and anything electrical near the water.

**Message 3, on acceptance**
> {{contractor name}} accepted and is on the way. Arrival time: {{arrival time}}; Google rating: {{rating}}, where they have one. They get your address now; nobody else does.

**Message 4, the same moment**
> The $99 trip charge is now on your card on file, and counts toward the repair if you go ahead. If {{contractor name}} is not there within 90 minutes of your text, it comes back to you automatically, in {{zone neighborhoods}} during {{covered hours}}.

**Message 5, after the job**
> Thanks for using SOS SMS. Did your contractor arrive within the window? Would you tell a neighbor?

**If no plumber can come**, in place of messages 3 and 4, within 15 minutes
> SOS SMS here: no plumber on SOS SMS could take your request in time, and your card has not been charged. Keep the water off at the main shutoff. To reach a person, text HELP.

## A text from someone who is not a member (R57)

Scenario: a neighbor who was forwarded the contact card but never joined texts "basement drain backing up" at 11:40 p.m.

**N1**
> SOS SMS here, with an automated reply; to reach a person, text HELP. For fire, a gas smell, or anyone hurt, call 911 first.

**N2**
> Until the drain is cleared, stop using water in the house: no flushing, no taps, no dishwasher or washing machine. Keep people and pets away from the water, and stay clear of anything electrical near it.

**N3**
> SOS SMS sends plumbers to members only, so for tonight, call a licensed local plumber directly. Nothing has been charged. When things are calm, text READY for a five-question home check and how membership works.

---

## Why this works
- **The work happens at joining.** The card, the home address, and consent go on file in October (R54), so in January the member's whole request is six words. No offer, no link, nothing to confirm, no payment screen.
- **Who before what.** Message 1 names SOS SMS, says it is automated, says the request is already going to the plumbers, says how to reach a person, and gives the safety line (S72, decision 8). There is no link anywhere in the emergency, so nothing looks like the scam pattern of a link from an unknown number (S59).
- **Value at once.** Message 2 helps before anyone accepts: shutoff and safety only, never repairs.
- **Two prices, never one.** The membership was paid before the need and never appears in an emergency text. The trip charge is named on use, at acceptance, credited to the repair. There is no fee per request.
- **The clock is the member's text.** "Within 90 minutes of your text" is decision 3 in the member's own words, with its scope in the same sentence.
- **The truth to a non-member.** Dispatch is for members, so the reply gives the safety line and the steps, says plainly to call a plumber directly tonight, charges nothing, and leaves joining for a calmer moment with READY.
- **Merge fields, never typed.** Names, the zone, the covered hours, the arrival time, and the rating fill from the member, zone, and request records when sent.
- **One idea per message**, short lines, the full name every time.
