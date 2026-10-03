# Partner counter card and newsletter blurb (contractors)

Status: **DRAFT, not approved.** The live test of the brain build (2026-10-03): produced using only this repository, from `templates/partner-kit.md`, `reference/channel-engine-contractors.md`, `reference/value-proposition-contractors.md`, and `ops/copy-bank.md`, then run through `ops/QA-checklist.md`. Ships only after a partner agreement, decision 2, and founder approval.

## Counter card

> **What did your leads really cost last month?**
>
> Scan to run the two-minute Lead Cost Check. Four numbers you already know; your answers stay yours.
>
> [QR code: Lead Cost Check, partner code [code]]
>
> SOS SMS is building an emergency dispatch line by text for [zone]. When it opens: no subscription, no per-lead fee, and the trip charge collected before you roll. [How SOS SMS is paid, one sentence.]
>
> Text JOIN-[code] to [number] to get on the founding contractor list.
>
> SOS SMS · [website]

## Newsletter and job-board blurb

> SOS SMS is building an emergency dispatch line by text for licensed plumbing and water-emergency contractors in [zone]. When it opens, seeing a request costs nothing and the customer pays the trip charge before you roll; [how SOS SMS is paid]. Start with the two-minute Lead Cost Check, which shows what each booked job from your leads really costs: [link] (code [code]).

## QA record

First draft of the blurb read: "SOS SMS is the emergency dispatch line where you pay nothing to see a request and the customer pays the trip charge before you roll." It failed two checks:

| Check | Result | Fix |
|---|---|---|
| Nothing described as live (`rules/feature-status.md`) | Fail: present tense for PLANNED capabilities | "is building ... When it opens" |
| "No lead fees" carries how SOS SMS is paid (`rules/do-not-say.md`) | Fail: no revenue sentence | [how SOS SMS is paid] bracket added |

Second draft, every line ticked: no em or en dashes; no banned words; full name each time; numbers none; channel in the mix (partnership program); no endorsement implied; one side (contractors), stage 1; "request", never "lead", for SOS SMS ("leads" only for the platforms they pay); no volume or earnings claim; brackets visible; one call to action per piece (the check on the blurb, JOIN on the card).

## What the test found missing from the brain
The rules said copy is written for launch day and held until the capability ships. But Stage 1 recruits founding contractors **before** launch, so contractor recruiting copy must go out pre-launch. The brain did not say how. Added as a rule: pre-launch recruiting copy describes the design as what SOS SMS is building, in the future tense ("when it opens"), never as a working service. Logged in `ops/signal-log.md` and `ops/decisions.md`.
