# Template: affiliate kit (members)

Everything a partner needs to pass SOS SMS on to homeowners before the need: a utility or city, a homeowner or neighborhood association, a local publication or newsletter, a home content creator, a home improvement retailer, an insurance agent for existing policyholders, an employer's benefit platform. Load `reference/channel-engine-members.md` and `reference/value-proposition-members.md`. Example: `examples/affiliate-kit.md`.

## Preconditions
- [ ] A signed affiliate agreement with the commission, when it is paid ($20 per new paid member, after the first paid month; planning value, R61), and the disclosure rule (S88).
- [ ] Not a real estate agent, lender, title or settlement agent, or anyone referring at a home purchase settlement (RESPA, S86, S94). They may share SOS SMS without payment.
- [ ] Insurance agents: existing policyholders only, outside any settlement.
- [ ] The partner's code issued; every link carries it.
- [ ] Memberships open in the zone, or the kit points to the launch list only.

## Pieces
1. **One paragraph.** What SOS SMS is: a membership that makes a home emergency one text. How it works; the prices as `{{monthly price}}` and `{{annual price}}`; the $99 trip charge on use, credited to the repair; the guarantee with its scope; cancel any time.
2. **The disclosure line.** "{{partner}} is paid a fee for each new SOS SMS member who joins through this link." Next to every mention, never in a footnote.
3. **The email block.** A subject line, three short paragraphs (the readiness gap, one text, the terms), and one link with the code. Sent by the partner to its own list, with its own opt-out (S73).
4. **The newsletter blurb.** Two sentences and the link with the code.
5. **The new-account insert** (utilities and cities). "New home? Save one number before anything breaks." The readiness scorecard and the code.
6. **The welcome-packet card** (associations). The same line, the scorecard, Text READY.
7. **What not to say.** Never "warranty", "insurance", "covers repairs", "24/7" without the hours, an arrival average, or a planning price as the price; always the full name SOS SMS; the safety line on anything that describes the emergency text.

## Fields
- Partner name and type:
- Zone(s), and whether memberships are open there:
- Code(s):
- Partner approvals needed (wording, placement, name use):
- Commission terms (from the agreement):

Guardrails: one side only (members). Narrowed claims only; no repair coverage; the disclosure every time. Check `rules/do-not-say.md` (affiliates) and `rules/writing-rules.md`; run `ops/QA-checklist.md` (affiliates block).
