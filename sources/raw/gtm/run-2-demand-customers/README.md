# SOS SMS, GTM input brief. Run 2 of 2: Demand (Members)

The discovery input for running the `gtm-builder` skill on the demand side of SOS SMS. No website yet. Revised 2026-10-11, the membership revision; the folder keeps its name so every link resolves.

SOS SMS is a two-sided home repair network. On the demand side, homeowners join before anything breaks, on a monthly or annual membership, with their card and home address on file. In an emergency a member texts one number, with no app, and the request goes at once to the licensed, insured contractors on the network for that trade and area. The first to accept commits to an arrival time, the $99 trip charge goes on the card on file and is credited to the job, and a 90-minute guarantee from the text covers a late arrival.

Four pack files, plus the completed run in `output/`. No placeholders for an agent to fill: per-message and per-zone details are merge fields from the resolution register.

| File | What it is |
|---|---|
| `GTM-BRIEF.md` | The skill's REQUIRED INPUTS, answered. Project information, competitor slate, member feature list, business context, claim constraints, and the cross-side dependencies with the contractor run |
| `SKILL-ADAPTATION.md` | How the nine phases change. The skill assumes a company buying software, and this buyer is a household joining a membership before the need |
| `RESEARCH-PROMPTS.md` | The external research steps, pre-filled: the member prompts (2026-10-11) first, then the pay per request prompts kept as the record |
| `.claude/skills/gtm-builder/SKILL.md` | The skill itself, checked in at the repository root so a session opened on this repo can run it |
| `output/` | The completed run: nine dashboards, the lead magnet, and the deck, as Markdown plus the XLSX and DOCX files the skill specifies. Start with `output/00-RUN-LOG.md` |

## How to run it

1. Finish Run 1 in `../run-1-supply-contractors/` through Step 5.2. It sets the launch metro, trades, and coverage area this run sells into.
2. Read the decisions in `GTM-BRIEF.md` Section 4: resolved on 2026-10-03 and revised by the membership revision on 2026-10-11 (`../marketplace/resolution-register.md`). Decisions 3, 4, and 9 change the most output.
3. Run Step 0 in `RESEARCH-PROMPTS.md` to name the competitors. The skill assumes you already know them.
4. Run Steps 1.1, 2.1, and 2.7 from the same file, then bring the findings back.
5. Invoke the skill. Point it at `GTM-BRIEF.md` and `SKILL-ADAPTATION.md` first, and keep its output in an `output/` folder next to them.

This is the second of two runs. `gtm-builder` builds one GTM per run, and the two sides are never blended: a value proposition for a plumber and a homeowner at once is true of neither. Phases 3, 6, and 7 can borrow structure from Run 1, never claims.

## The one rule that governs the whole run

SOS SMS is pre-launch: no members, no completed jobs, no arrival times on record, no testimonials. Unknown numbers are never invented: each carries a planning value with its basis, or the method that will count it. This bites hardest in Phase 6's eighteen proof fields, where an average arrival time, a count of members, or a savings figure is the first thing the template will reach for.
