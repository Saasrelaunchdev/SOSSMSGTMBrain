# Signal log

Raw market input, captured before judgment. Every signal from a contractor, a customer, a partner, a rival, a platform, or a channel lands here first. Newest at the top. **Keep the verbatim**: the words a real contractor or homeowner used before we taught them ours are the most valuable thing a signal carries.

**Types:** OBJECTION, LANGUAGE, PROOF, STATUS, COMPETITIVE, SEGMENT, CHANNEL, LOSS, RISK.

**Dispositions:** `NOISE` (one instance, no action); `WATCH (n/N)` (a plausible pattern awaiting corroboration); `PATCH` (changes copy, not strategy); `AMEND` (changes a ledger, a position, or a rule: full amendment order and a `decisions.md` entry).

**Corroboration thresholds** (set 2026-10-02, adopted 2026-10-04, see `review-cadence.md`):

| Signal class | Threshold to act |
|---|---|
| Opinion, preference, language, objection | 3 independent instances within 60 days, from the same side |
| Verifiable fact: status, policy, proof, competitive, risk | 1 verified instance, act immediately |
| Lost contractor or lost customer reason | 2 instances, or 1 from a founding contractor |
| Channel performance | A full measurement cycle in one zone, never a single week |

Default disposition is NOISE. A signal from one side never changes the other side's copy without the cross-side check. Triage runs weekly; a WATCH item that has not moved in two cycles expires to NOISE, and the expiry is written here.

The entries below were seeded at build from the research and the walkthrough work. Real contractor and customer signals start with the founding zone.

---

## Entries

### 2026-10-04 | STATUS | resolved brain, live test
**Verbatim:** The terms on one page, produced from the brain alone after every value was resolved (`pages/terms-on-one-page.md`).
**Context:** Contractors, the contractor page, Stage 1. Every number came from the register; the only merge fields were the zone and the number.
**Disposition:** PATCH. One gap: the template had no line for the 10-minute response window (R12). Added to `templates/terms-on-one-page.md`.
**Routed to:** `templates/terms-on-one-page.md`, `pages/terms-on-one-page.md`.

### 2026-10-03 | STATUS | pricing model, live test
**Verbatim:** First draft of the contractor pricing table: "The customer pays an SOS SMS fee on each request. Contractors pay the contractor fee per completed paid job", with no row for a late arrival.
**Context:** Contractors, the contractor page and the terms on one page. Produced from the brain for the pricing model and run through `QA-checklist.md`. Failed two checks: present tense in pre-launch recruiting copy; a customer promise (the 90-minute refund) the contractor's terms did not show, since the terms on one page must say what happens if they are late.
**Disposition:** PATCH. The rules held; the draft broke them. Fixed in the table: future tense, and an "If you are late" row, held until decision 3 filled it the same day.
**Routed to:** `Fit137/SOSSMSGTMBuild`, `gtm/tools/google_folder/pricing.py` (the pricing table and handoff).

### 2026-10-03 | STATUS | brain build, live test
**Verbatim:** First draft of the partner blurb: "SOS SMS is the emergency dispatch line where you pay nothing to see a request and the customer pays the trip charge before you roll."
**Context:** Contractors, stage 1, partnership program. Produced from the brain only (`pages/partner-counter-card.md`) and run through `QA-checklist.md`. Failed two checks: present tense for planned capabilities; no revenue sentence.
**Disposition:** AMEND. The brain had no rule for recruiting copy that must go out before launch. Added the pre-launch framing rule.
**Routed to:** `rules/writing-rules.md`, master context Section 0, `QA-checklist.md`, `decisions.md`, `adapters/portable-control-layer.md`.

### 2026-10-02 | RISK | research README
**Verbatim:** "Every fact below was read from a search engine's summary of the listed page, not from the page itself."
**Context:** Both sides. Every sourced figure.
**Disposition:** AMEND. Grade A and B figures go into external copy only after the page is opened and the figure confirmed.
**Routed to:** `rules/writing-rules.md`, `reference/research-and-sources.md`.

### 2026-10-02 | STATUS | source conflict, lead magnet spec and marketplace walkthrough
**Verbatim:** "call bookings by tier" (contractor scorecard measurement row); "an audit call for contractors" (marketplace walkthrough, slide 8).
**Context:** Contractors. Both predate the product-led revision.
**Disposition:** PATCH. The no-calls decision governs; measure JOIN texts by tier.
**Routed to:** `reference/lead-magnets.md`.

### 2026-10-01 | STATUS | walkthrough NOTES
**Verbatim:** "Dark (projector) passes every check except the chart lightness band, deliberately ... Awaiting approval."
**Context:** Brand v1, internal.
**Disposition:** PATCH. Flagged in the status ledger and brand file. Closed 2026-10-04: the dark palette is kept as validated.
**Routed to:** `rules/feature-status.md`, `reference/brand-identity.md`.

### 2026-10-01 | STATUS | founders, product-led revision
**Verbatim:** "Product-led growth, no sales team ... No calls, shop visits, or audits."
**Context:** Both sides.
**Disposition:** AMEND. Channel plan, journeys, and lead magnets rewritten.
**Routed to:** `decisions.md`, `rules/writing-rules.md` channel discipline.

### 2026-10-01 | COMPETITIVE | Google Local Services policy (S70)
**Verbatim:** Local Services leads "may not be sold and must be fulfilled by the advertiser's own vetted technicians"; re-routing to businesses not listed in the ad is not allowed.
**Context:** Customers, paid search.
**Disposition:** AMEND. Local Services Ads are out of the mix; standard search needs written confirmation (decision 11).
**Routed to:** `rules/do-not-say.md`, `reference/channel-engine-paid-search.md`.

### 2026-10-01 | COMPETITIVE | Search Engine Journal (S09)
**Verbatim:** Google consolidated Google Guaranteed, Google Screened, and License Verified into one Google Verified badge, and discontinued the Money Back Guarantee, from 2025-10-20.
**Context:** Both sides; competitor claims.
**Disposition:** PATCH. The old badges are banned as current facts.
**Routed to:** `rules/glossary.md`, `rules/do-not-say.md`.

### 2026-10-01 | CHANNEL | Search Engine Land (S72)
**Verbatim:** Message assets "need verified business details and response-time commitments; automated replies must identify themselves; human handoff must be defined".
**Context:** Customers, text-from-ad and the first reply.
**Disposition:** AMEND. The first reply says it is automated and how to reach a person.
**Routed to:** `rules/writing-rules.md`, `templates/first-reply-sms.md`.

### 2026-10-01 | RISK | FTC (S59)
**Verbatim:** "Consumers reported $470 million lost to scams that started with a text in 2024 ... payment links."
**Context:** Customers, stage 3. The blocker is a payment link from an unknown number.
**Disposition:** AMEND. Who SOS SMS is comes before any link; no link in the first message.
**Routed to:** `rules/do-not-say.md`, `templates/first-reply-sms.md`.

### 2026-10-01 | RISK | web search for the name
**Verbatim:** A search for "SOS SMS" "returned several unrelated local plumbing companies with 'SOS' in their names."
**Context:** Both sides; ads, email, pages.
**Disposition:** AMEND. Always the full name; no bids on "SOS plumbing"; decision 10.
**Routed to:** `rules/glossary.md`, `rules/writing-rules.md`.

### 2026-10-01 | OBJECTION | contractor reviews of lead platforms (S03 to S08)
**Verbatim:** Paying for "leads that never reply"; the same request "sent to three to five contractors".
**Context:** Contractors, Level 2. Research-derived, not from SOS SMS contractors.
**Disposition:** WATCH (0/3). Built into positioning from research; confirm the language with real contractor replies before it enters the copy bank as customer language.
**Routed to:** none yet.
