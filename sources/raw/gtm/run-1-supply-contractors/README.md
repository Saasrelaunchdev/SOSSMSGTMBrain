# SOS SMS, GTM input brief. Run 1 of 2: Supply (Contractors)

The discovery input for running the `gtm-builder` skill on the contractor side of SOS SMS. No website yet.

SOS SMS is a two-sided marketplace for emergency home repair. A person with a problem at home texts one number, and the request goes to licensed, insured contractors matched by trade and area. This run sells the other side: trade contractors join free, with no subscription and no lead fees, and get urgent jobs with the customer's trip charge collected before they roll.

Four pack files, plus the completed run in `output/`. No placeholders for an agent to fill.

| File | What it is |
|---|---|
| `GTM-BRIEF.md` | The skill's REQUIRED INPUTS, answered. Project information, competitor slate, contractor feature list, business context, claim constraints, and the cross-side dependencies with the customer run |
| `SKILL-ADAPTATION.md` | How the nine phases change. The skill assumes one buyer paying a subscription, and SOS SMS has two buyers and is free to the contractor |
| `RESEARCH-PROMPTS.md` | The external research steps, pre-filled for the contractor side, plus a Step 0 the skill assumes you already did |
| `.claude/skills/gtm-builder/SKILL.md` | The skill itself, checked in at the repository root so a session opened on this repo can run it |
| `output/` | The completed run: nine dashboards, the lead magnet, and the deck, as Markdown plus the XLSX and DOCX files the skill specifies. Start with `output/00-RUN-LOG.md` |

## How to run it

1. Fill the business context lines in `GTM-BRIEF.md` Section 4, and answer as many of the open decisions as you can. Decisions 1 to 4 change the most output.
2. Run Step 0 in `RESEARCH-PROMPTS.md` to name the competitors. The skill assumes you already know them.
3. Run Steps 1.1, 2.1, and 2.7 from the same file, then bring the findings back.
4. Invoke the skill. Point it at `GTM-BRIEF.md` and `SKILL-ADAPTATION.md` first, and keep its output in an `output/` folder next to them.
5. Close Phase 5 with the Step 5.2 founding contractor cohort. Run 2 starts from it.

This is the first of two runs. `gtm-builder` builds one GTM per run, and the customer side runs second from `../run-2-demand-customers/`, because every customer-side promise depends on how many contractors have joined. The two runs are never blended.

## The one rule that governs the whole run

SOS SMS is pre-launch: no contractors, no jobs, no payouts, no testimonials. Unknown numbers stay `{TBD}` and are never invented. This bites hardest in Phase 6's eighteen proof fields, and on this side it has a second form: no earnings or job volume claim for contractors, of any size.
