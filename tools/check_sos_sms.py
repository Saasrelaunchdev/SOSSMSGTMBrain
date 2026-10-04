#!/usr/bin/env python3
"""
SOS SMS house checks, run after audit_brain.py.

audit_brain.py checks the generic brain contract. This script checks the
rules that are specific to SOS SMS and that the generic audit does not see:

  1. No en dashes (the generic audit only checks em dashes).
  2. The name is always "SOS SMS": the first word never appears alone.
  3. Every source ID (S01 to S99) cited in the brain exists in the register.
  4. Nothing unresolved: no TBD, no open-decision wording, no square-bracket
     placeholder, and no "coming soon". Every value is in
     reference/resolution-register.md; a {{merge field}} must be one the
     register lists. Snapshots are dated history and skip the wording check.

    python3 tools/check_sos_sms.py [brain_dir]

Exit codes: 0 clean, 1 errors found. No third-party dependencies.
"""

import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", "sources", "node_modules", "__pycache__"}
REGISTER = Path("sources/raw/gtm/research/SOURCES.md")

# "SOS" not followed by " SMS". Quoted search terms and the rules that ban the
# bare form are allowed when the line says so.
SOS_ALONE = re.compile(r"\bSOS\b(?! SMS)")
ALLOWED_SOS_LINE = re.compile(
    r"SOS plumbing|first word|alone|name collision|with .SOS. in their names|SOS-SMS_GTM",
    re.I,
)
SOURCE_ID = re.compile(r"\bS(\d{2})\b")
RESOLUTION = Path("reference/resolution-register.md")
MERGE = re.compile(r"\{\{([^{}]+)\}\}")
GENERIC_MERGE = {"merge field", "merge fields", "field"}
TBD = re.compile(r"\{TBD\}|(?<![A-Za-z0-9+/])TBD(?![A-Za-z0-9+/])")
OPEN_WORDING = re.compile(
    r"open decision|design open|not decided|undecided|to be decided|decision pending|"
    r"recommended, not decided|awaits approval|awaiting approval|founder to decide",
    re.I,
)
# A lowercase square-bracket slot such as [zone] or [trip charge]. Markdown
# links, checkboxes, and citations in parentheses are not slots.
BRACKET_SLOT = re.compile(r"\[(?!x\])(?! \])[a-z][^\]]{0,60}\](?!\()")
COMING_SOON = re.compile(r"coming soon", re.I)
ALLOWED_SOON_LINE = re.compile(r"never|not .coming soon.|or .coming soon.|stand(s|ing) in", re.I)


def files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".mdc", ".txt"}:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = []

    register = root / REGISTER
    known = set()
    if register.exists():
        known = set(re.findall(r"^\|\s*S(\d{2})\s*\|", register.read_text(encoding="utf-8"), re.M))
    else:
        errors.append(f"source register missing: {REGISTER}")

    fields = set()
    resolution = root / RESOLUTION
    if resolution.exists():
        fields = {m.strip() for m in MERGE.findall(resolution.read_text(encoding="utf-8"))}
    else:
        errors.append(f"resolution register missing: {RESOLUTION}")

    for path in files(root):
        rel = path.relative_to(root)
        # Dated history keeps its own words: snapshots, and the signal log's verbatim entries.
        history = rel.parts[0] == "snapshots" or rel.as_posix() == "ops/signal-log.md"
        fence = None
        for i, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if line.lstrip().startswith("```"):
                fence = None if fence is not None else (line.strip()[3:].strip() or "text")
            # Shell, YAML, and JSON blocks are code, not copy: their brackets are syntax.
            code = fence in ("bash", "sh", "yaml", "yml", "json", "python")
            if "–" in line:
                errors.append(f"en dash in {rel}:{i}")
            if SOS_ALONE.search(line) and not ALLOWED_SOS_LINE.search(line):
                errors.append(f"'SOS' without 'SMS' in {rel}:{i}")
            if known:
                for sid in SOURCE_ID.findall(line):
                    if sid not in known:
                        errors.append(f"unknown source ID S{sid} in {rel}:{i}")
            for field in MERGE.findall(line):
                if field.strip() not in fields | GENERIC_MERGE:
                    errors.append(f"unregistered merge field {{{{{field}}}}} in {rel}:{i}")
            if path.name != "check_sos_sms.py":
                if TBD.search(line):
                    errors.append(f"unresolved TBD in {rel}:{i}; use the register value")
                if not history and OPEN_WORDING.search(line):
                    errors.append(f"open-decision wording in {rel}:{i}: {OPEN_WORDING.search(line).group(0)!r}")
                for m in ([] if history or code else BRACKET_SLOT.finditer(line)):
                    errors.append(f"bracket placeholder {m.group(0)} in {rel}:{i}; use a merge field or the decided value")
            if COMING_SOON.search(line) and not ALLOWED_SOON_LINE.search(line):
                errors.append(f"'coming soon' in {rel}:{i}; use the register value")

    print(f"SOS SMS checks: {root}\n")
    for msg in errors:
        print(f"  [ERROR] {msg}")
    print(f"\n{len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
