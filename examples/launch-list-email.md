# Example: the launch list sequence (members)

Status: **voice reference, written 2026-10-11 for the membership revision.** Written from the brain with every value decided or a merge field. Sent from Stage 1, once email sending is set up (S73); the shutoff steps are reviewed by a licensed plumber first; the opening email goes only on the day memberships open in the zone (R55). Template: `templates/member-email.md`.

Scenario: a homeowner in the founding zone takes the readiness scorecard in Stage 1, while memberships are not open yet, and joins the launch list.

Footer on every email:
> SOS SMS · {{postal address}} · You are getting this because you joined the SOS SMS launch list for {{zone name}}. Unsubscribe: {{opt-out link}}

---

## Email 1, on joining the launch list
**Subject:** You're on the SOS SMS launch list for {{zone name}}

> Hi {{first name}},
>
> Thanks for joining the SOS SMS launch list. Memberships aren't open in {{zone name}} yet, so there is no charge and no service yet.
>
> We open a zone only once enough licensed, insured plumbers have joined there, and we name the hours we cover. When that happens, you will hear from us first.
>
> Here is how SOS SMS will work. You join once, with your card and home address. When something breaks, you text what happened, and the licensed, insured plumbers on SOS SMS near you see it at once; the first who can come accepts and texts you an arrival time.
>
> Next from us: where your main water shutoff is, and how to turn it.
>
> For fire, a gas smell, or anyone hurt, call 911 first.
>
> {{sender name}}, SOS SMS

## Email 2, two days later: the shutoff guide
**Subject:** Where is your main water shutoff?

> Hi {{first name}},
>
> When a pipe bursts, the main water shutoff is what stops the water. Find yours now, while nothing is wrong.
>
> 1. Look where the water line enters the house: often near the water heater, in the basement, or in a crawl space or utility closet.
> 2. A round handle turns clockwise until it stops. A lever turns a quarter turn, so it sits across the pipe.
> 3. Turn it gently to check that it moves. If it is stuck, or you cannot find it, ask a licensed plumber to look before winter.
> 4. Show everyone in the house where it is.
>
> For fire, a gas smell, or anyone hurt, call 911 first. Smell gas? Get out first, then call 911 and your gas company.
>
> {{sender name}}, SOS SMS

## Email 3, the day memberships open in the zone
**Subject:** SOS SMS memberships are open in {{zone name}}

> Hi {{first name}},
>
> Memberships are open in {{zone name}}, and the launch list hears first. Covered: {{zone neighborhoods}}, {{covered hours}}.
>
> **How it works in one text.** You join once, with your card and home address. When something breaks, you text what happened, and the licensed, insured plumbers on SOS SMS near you see it at once; the first who can come accepts and texts you an arrival time.
>
> **What it costs.** {{monthly price}} a month or {{annual price}} a year. When you use it, a $99 trip charge goes on your card when a plumber accepts and counts toward the repair; there is no fee per request.
>
> **The guarantee.** If your plumber is not there within 90 minutes of your text, the $99 trip charge comes back to you automatically, in {{zone neighborhoods}} during {{covered hours}}.
>
> **What it is not.** Not a warranty or insurance: SOS SMS pays for no repair or parts. The plumber prices the repair on site.
>
> **Cancel any time**, on the membership page or by texting HELP.
>
> Join before you need it: {{link}}
>
> For fire, a gas smell, or anyone hurt, call 911 first.
>
> {{sender name}}, SOS SMS

---

## Why this works
- **Honest about what the list is.** No charge and no service until the zone opens (R55), said in the first email, so the opening email is news, not a reversal.
- **Help before any ask.** Email 2 is useful whether or not they ever join, and it is what makes them ready.
- **The opening email answers a careful buyer's questions in order**, and meets the weak point, a cost every month whether or not anything breaks (R46), with what it includes, the trip charge only on use, and cancel any time.
- **CAN-SPAM in every email** (S73): the full name, a postal address, and an opt-out.
- **No urgency the facts do not carry.** No countdown, no "spots left", no member counts.
- **Merge fields, never typed.** Names, the zone, the covered hours, the prices, and the link fill from the records when sent.
