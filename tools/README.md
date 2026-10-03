# tools

| Tool | What it checks | Run |
|---|---|---|
| `audit_brain.py` | The generic brain contract: required files, broken links, the `llms.txt` index, size budgets, em dashes and banned words in the brain's prose, placeholders, ledger staleness, adapters, the state layer | `python3 tools/audit_brain.py .` |
| `check_sos_sms.py` | SOS SMS house rules the generic audit does not see: en dashes, the first word of the name used alone, unknown source IDs, template placeholders, "coming soon" standing in for {TBD} | `python3 tools/check_sos_sms.py .` |

Both need only Python 3, no packages. Both exit 1 on errors, so they can gate a pull request (see the CI pattern in `README.md` at the repo root).

`audit_brain.py` is copied unchanged from the Go-to-Market Brain skill (`alielshenawy1/Ali-GTM-Brain-Skill`, `skills/go-to-market-brain/scripts/`), MIT License, copyright 2026 alielshenawy1: see `LICENSE-audit_brain.txt`. To update it, copy the newer version over this one.
