# Partner counter card and newsletter blurb (contractors)

Status: **approved 2026-10-04, updated with decided values.** The live test of the brain build (2026-10-03): produced using only this repository, from `templates/partner-kit.md`, `reference/channel-engine-contractors.md`, `reference/value-proposition-contractors.md`, and `ops/copy-bank.md`, then run through `ops/QA-checklist.md`. Ships once a partner agreement is signed and the partner's code is issued.

## Counter card

> **What did your leads really cost last month?**
>
> Scan to run the two-minute Lead Cost Check. Four numbers you already know; your answers stay yours.
>
> (QR code: the Lead Cost Check, with partner code {{code}})
>
> SOS SMS is building an emergency dispatch line by text for {{zone}}. When it opens: no subscription, no per-lead fee, and the trip charge collected before you roll. SOS SMS will be paid by the customer on each request, and by you only per completed paid job after the founding period.
>
> Text JOIN-{{code}} to {{number}} to get on the founding contractor list.
>
> SOS SMS · {{url}}

## Newsletter and job-board blurb

> SOS SMS is building an emergency dispatch line by text for licensed plumbing and water-emergency contractors in {{zone}}. When it opens, seeing a request costs nothing and the customer pays the trip charge before you roll; SOS SMS will be paid by the customer on each request, and by contractors only per completed paid job after the founding period. Start with the two-minute Lead Cost Check, which shows what each booked job from your leads really costs: {{link}} (code {{code}}).

## QA record

First draft of the blurb read: "SOS SMS is the emergency dispatch line where you pay nothing to see a request and the customer pays the trip charge before you roll." It failed two checks:

| Check | Result | Fix |
|---|---|---|
| Nothing described as live (`rules/feature-status.md`) | Fail: present tense for PLANNED capabilities | "is building ... When it opens" |
| "No lead fees" carries how SOS SMS is paid (`rules/do-not-say.md`) | Fail: no revenue sentence | Revenue sentence added (decision 2) |

Second draft, every line ticked: no em or en dashes; no banned words; full name each time; numbers none; merge fields only for per-partner details; channel in the mix (partnership program); no endorsement implied; one side (contractors), stage 1; "request", never "lead", for SOS SMS ("leads" only for the platforms they pay); no volume or earnings claim; one call to action per piece (the check on the blurb, JOIN on the card).

## What the test found missing from the brain
The rules said copy is written for launch day and held until the capability ships. But Stage 1 recruits founding contractors **before** launch, so contractor recruiting copy must go out pre-launch. The brain did not say how. Added as a rule: pre-launch recruiting copy describes the design as what SOS SMS is building, in the future tense ("when it opens"), never as a working service. Logged in `ops/signal-log.md` and `ops/decisions.md`.
