# tools

| Tool | What it checks | Run |
|---|---|---|
| `audit_brain.py` | The generic brain contract: required files, broken links, the `llms.txt` index, size budgets, em dashes and banned words in the brain's prose, placeholders, ledger staleness, adapters, the state layer | `python3 tools/audit_brain.py .` |
| `check_sos_sms.py` | SOS SMS house rules the generic audit does not see: en dashes, the first word of the name used alone, unknown source IDs, and anything unresolved: a placeholder, open-decision wording, a square-bracket slot, a merge field the resolution register does not list, or "coming soon" | `python3 tools/check_sos_sms.py .` |

Both need only Python 3, no packages. Both exit 1 on errors, so they can gate a pull request (see the CI pattern in `README.md` at the repo root).

`audit_brain.py` is copied from the Go-to-Market Brain skill (`alielshenawy1/Ali-GTM-Brain-Skill`, `skills/go-to-market-brain/scripts/`), MIT License, copyright 2026 alielshenawy1: see `LICENSE-audit_brain.txt`. One local change (2026-10-04): `check_placeholders` skips the merge fields listed in `reference/resolution-register.md`, which are filled at send time by design. To update it, copy the newer version over this one and reapply that change.
