#!/usr/bin/env python3
"""
SOS SMS house checks, run after audit_brain.py.

audit_brain.py checks the generic brain contract. This script checks the
rules that are specific to SOS SMS and that the generic audit does not see:

  1. No en dashes (the generic audit only checks em dashes).
  2. The name is always "SOS SMS": the first word never appears alone.
  3. Every source ID (S01 to S99) cited in the brain exists in the register.
  4. No unfilled template placeholders, and no "coming soon" standing in for {TBD}.

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

    for path in files(root):
        rel = path.relative_to(root)
        for i, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if "–" in line:
                errors.append(f"en dash in {rel}:{i}")
            if SOS_ALONE.search(line) and not ALLOWED_SOS_LINE.search(line):
                errors.append(f"'SOS' without 'SMS' in {rel}:{i}")
            if known:
                for sid in SOURCE_ID.findall(line):
                    if sid not in known:
                        errors.append(f"unknown source ID S{sid} in {rel}:{i}")
            if "{{" in line:
                errors.append(f"template placeholder in {rel}:{i}")
            if COMING_SOON.search(line) and not ALLOWED_SOON_LINE.search(line):
                errors.append(f"'coming soon' in {rel}:{i}; unknowns stay {{TBD}}")

    print(f"SOS SMS checks: {root}\n")
    for msg in errors:
        print(f"  [ERROR] {msg}")
    print(f"\n{len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
