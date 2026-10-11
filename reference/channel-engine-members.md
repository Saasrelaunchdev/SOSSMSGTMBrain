# Channel engine: members (affiliates, email, search and SEO pages, member loops)

Load for: any affiliate kit, partner send, launch list or member email, membership or zone page, prevention or problem guide, sign-up ad, welcome or first-reply text, and every member template. Distills Run 2 Phase 8 (`phase-8-assets-library.md`, the membership revision, 2026-10-11). Templates: `templates/affiliate-kit.md`, `templates/member-email.md`, `templates/membership-page.md`, `templates/problem-guide.md`, `templates/search-ad.md`, `templates/first-reply-sms.md`.

## Thesis
Homeowners join before the need, so SOS SMS meets them where they already trust someone, through partners and email, long before anything breaks. A number saved in a phone before the pipe bursts is worth more than an ad seen during the flood. In the middle of an emergency, a homeowner is better served by calling a contractor from the search results than by joining anything, so no ad sells dispatch in an emergency. No sales team and no calls to households: partners join an affiliate program, and the product does the converting.

## The three channels, plus the loops
1. **Affiliates, before the need (lead).** Utilities and cities (the partner-led model behind more than 1,300 HomeServe partners, S93), homeowner and neighborhood associations, local publications and newsletters, home content creators, home improvement retailers, insurance agents for existing policyholders, employers' benefit platforms. Each gets the kit, a code, and a disclosed commission: $20 per new paid member, after the first paid month (planning value, R61).
2. **Email, before the need (lead).** SOS SMS's own homeowner list from the readiness scorecard and the launch list; partner sends to the partner's own list; member email (welcome, seasonal notes with opt-in, the renewal reminder). CAN-SPAM throughout (S73).
3. **Search and SEO pages, for sign-ups (support).** Prevention and problem guides read before the need, the membership page, zone pages; paid search (Google, then Microsoft) on readiness and plan searches ("plumbing protection plan", "home warranty alternatives", "how to prevent frozen pipes"), and paid social, geofenced to open zones. Organic social and community posts by SOS SMS itself.
4. **Member loops.** The contact card, Text READY, the forwardable card (no reward at launch, R62), the two questions after a job, the renewal.

## Hard rules
- **Zones first.** Memberships open only in zones at the density number, with covered hours named (R55). Affiliate links land on the ZIP check: an open zone shows the membership, a zone not yet open the launch list, outside the readiness steps alone. Sign-ups pause automatically when acceptance falls: ads stop, affiliate links show the launch list (R34).
- **No payment at a home purchase.** Never pay a real estate agent, lender, title or settlement agent, or anyone referring at a home purchase settlement (RESPA Section 8, S86, S94). They may share SOS SMS without payment. Insurance agents are paid only for existing policyholders, outside any settlement.
- **Disclosure.** Every affiliate discloses that they are paid, next to the mention (S88).
- **Sign-ups, never dispatch.** Ads sell the membership before the need; emergency dispatch searches ("emergency plumber near me", "24 hour plumber") are negative keywords (decision 11). Never Local Services Ads (S70). Google's written confirmation before any spend (S71).
- **No retargeting, no pixels.** Location targeting only.
- **Never pose as the plumber, a warranty, or insurance.** SOS SMS is a membership that dispatches licensed, insured contractors; the contractor does the work; SOS SMS pays for no repair (R21).
- **Claims.** No superlatives, no arrival averages, no "24/7" unless the zone's covered hours are. The guarantee appears with its scope on the membership page (decision 3). Prices as `{{monthly price}}` and `{{annual price}}`.
- **Subscription law.** Clear terms before the card, express consent, a renewal reminder before `{{renewal date}}`, and cancel any time, on the membership page or by texting HELP (R56, S87).
- **Safety.** The safety line on the membership page and in one ad description.
- **Brand terms.** No bids on "SOS plumbing" (decision 10).
- **Optimize for a new paid member**, never a click, a ZIP check, or a launch list join. Cost per new paid member by channel, commissions included, against the ceiling of about $43 (R63), decides spend.

## Sign-up ad drafts, zone template (headlines max 30 characters, descriptions max 90)

| Text | Condition |
|---|---|
| Join Before Your Pipes Burst | |
| One Text When Something Breaks | |
| Plumbing Emergency Membership | |
| Dispatch to Licensed Plumbers | |
| One Text Reaches Local Pros | Open zones only |
| Trip Charge Only When Used | |
| Arrival Time When They Accept | |
| No App. No Phone Tree. | |
| No Forms at 2 a.m. | |
| Cancel Any Time | |
| Ready Before the First Freeze | Seasonal |
| Only One Pro Gets Your Info | Only once the broadcast that hides identity ships (decision 4) |
| Membership in {{zone name}} | Per zone; at most 30 characters once filled |
| 90 Minutes or Trip Charge Back | The guarantee (decision 3); scope on the membership page |
| Join before you need it. In an emergency, one text reaches vetted local plumbers at once. | |
| Your card and address are on file, so the emergency is one text. Cancel any time. | |
| The $99 trip charge applies only when you use it, and counts toward the repair. | |
| Not a warranty. We get a vetted plumber to your door; they price the repair on site. | |
| Fire, gas smell, or anyone hurt? Call 911 first. For leaks and backups, members text us. | The safety description |

## Method: plan, write, edit
1. **Plan.** Confirm the zone is open, or that the asset only promises the launch list. Pick the channel and its landing page (the membership page with the partner's code, the launch list, or a guide). List the merge fields.
2. **Write.** Ready, not afraid: the gap in the home's readiness, then one text, then the price and the trip charge on use, then how to cancel. Use the `value-proposition-members.md` drills.
3. **Edit.** Count characters. Run `ops/QA-checklist.md`, the affiliate, email, and ads blocks included.

## Production order
1. Stage 0: the member terms and the automatic renewal disclosures (S87), membership billing, the affiliate terms (S86, S88, S94), email sending (S73), carrier registration (S32), the launch price. Without them, nothing sells a membership.
2. The membership page, the guarantee in full, how it works in one text.
3. In Stage 1: the readiness scorecard, the first five prevention and problem guides, the launch list sequence.
4. The affiliate program page and the kit; the first partners signed for the founding zone, codes ready before it opens.
5. Member loops: the welcome texts, the first reply, the reply to a non-member, the contact card, the refund text, READY.
6. When the zone opens: the opening email to the launch list, affiliates live, then sign-up ads after Google's written confirmation, paid social, and the Microsoft import.

## Out, and why
Ads that sell dispatch during an emergency (a contractor from the results is the faster route then); sales calls, demos, meetings, door-to-door; marketing texts without written consent (S31); retargeting and pixels; Local Services Ads (S70); any payment at a home purchase settlement (S86, S94); LinkedIn.
