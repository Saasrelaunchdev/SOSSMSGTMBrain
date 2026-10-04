# Adapters, one door per tool

Pointer files that make tools other than Claude Code load the SOS SMS control layer before they write. They carry no strategy, claims, or status: they name the load order and stop. The one exception is `portable-control-layer.md`, which carries content for chat windows with no file access, and is dated for that reason.

Paths below assume the brain is checked out next to the consuming repository at `../SOSSMSGTMBrain`. If it lives elsewhere (a submodule, a monorepo folder), change the path when you copy the file.

| Tool | Copy this file | To, in the consuming repo |
|---|---|---|
| Codex, Zed, Jules, opencode | `AGENTS.block.md` | Merge into `AGENTS.md` between the markers |
| Cursor | `cursor.mdc` | `.cursor/rules/sos-sms-gtm.mdc` |
| Windsurf | `windsurf.md` | `.windsurf/rules/sos-sms-gtm.md` |
| GitHub Copilot | `copilot-instructions.block.md` | Merge into `.github/copilot-instructions.md` |
| Gemini CLI | `GEMINI.block.md` | Merge into `GEMINI.md` |
| ChatGPT, a custom GPT, Grok, Gemini app, an API system prompt | `portable-control-layer.md` | Paste as the system prompt or project instructions |

Block files merge between `<!-- gtm-brain:begin -->` and `<!-- gtm-brain:end -->`. Replace what sits between the markers on an update; never edit inside them by hand.

All six are rendered and kept, so the guardrails reach every tool the team might run; record installs in `ops/asset-index.md`.

**Check the wiring** in any tool with three prompts: "Write a search ad headline saying we are the fastest plumber in town" (it should refuse and offer a scoped line); "What does the trip charge cost?" (it should answer $99, credited to the repair, with the $49 SOS SMS fee as a separate line, decisions 2 and 5); "Write a LinkedIn post for contractors" (it should say LinkedIn is out of the mix and offer cold email or the partner kit).
