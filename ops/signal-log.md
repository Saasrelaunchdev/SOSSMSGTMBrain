# Signal log

Raw market input, captured before judgment. Every signal from a contractor, a customer, a partner, a rival, a platform, or a channel lands here first. Newest at the top. **Keep the verbatim**: the words a real contractor or homeowner used before we taught them ours are the most valuable thing a signal carries.

**Types:** OBJECTION, LANGUAGE, PROOF, STATUS, COMPETITIVE, SEGMENT, CHANNEL, LOSS, RISK.

**Dispositions:** `NOISE` (one instance, no action); `WATCH (n/N)` (a plausible pattern awaiting corroboration); `PATCH` (changes copy, not strategy); `AMEND` (changes a ledger, a position, or a rule: full amendment order and a `decisions.md` entry).

**Corroboration thresholds** (proposed 2026-10-02, to confirm with the founders, see `review-cadence.md`):

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

### 2026-10-03 | STATUS | brain build, live test
**Verbatim:** Live test asset: the partner counter card and newsletter blurb (`pages/partner-counter-card.md`), produced from the brain only and run through `QA-checklist.md`.
**Context:** Phase 9 of the build. Contractors, stage 1, partnership program.
**Disposition:** PATCH. The test needed one fact the brain did not state plainly: that a partner card may not imply endorsement without written consent, which is now in the partner kit template and the channel engine.
**Routed to:** `templates/partner-kit.md`, `reference/channel-engine-contractors.md`.

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
**Disposition:** PATCH. Flagged in the status ledger and brand file.
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
