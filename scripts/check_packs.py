#!/usr/bin/env python3
"""Check that every language pack is complete.

Run from the repository root:  python3 scripts/check_packs.py
Exits with status 1 if a pack has problems.
"""
import re
import sys
from pathlib import Path

LANGUAGES = Path(__file__).resolve().parent.parent / "skills" / "sounds-like-me" / "languages"
REQUIRED = ("ai-patterns.md", "punctuation.md")
CODE = re.compile(r"^[a-z]{2}(-[A-Z]{2})?$")
PLACEHOLDER = re.compile(r"\[LANGUAGE\]|\[Pattern name\]|\[Invented example\]|\[Rules\.\]")
MIN_ENTRIES = 10


def check_pack(pack: Path) -> list[str]:
    problems = []
    if not CODE.match(pack.name):
        problems.append(f"folder name '{pack.name}' is not an ISO code like 'it' or 'pt-BR'")
    for name in REQUIRED:
        path = pack / name
        if not path.is_file():
            problems.append(f"missing {name}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.lstrip().startswith("# "):
            problems.append(f"{name} does not start with a title")
        if PLACEHOLDER.search(text):
            problems.append(f"{name} still contains template placeholders")
        if name == "ai-patterns.md":
            entries = len(re.findall(r"^- \*\*", text, flags=re.M))
            if entries < MIN_ENTRIES:
                problems.append(f"{name} has {entries} entries, expected at least {MIN_ENTRIES}")
    return problems


def main() -> int:
    packs = sorted(p for p in LANGUAGES.iterdir() if p.is_dir() and not p.name.startswith("_"))
    if not packs:
        print("no language packs found")
        return 1
    failed = False
    for pack in packs:
        problems = check_pack(pack)
        if problems:
            failed = True
            print(f"FAIL {pack.name}")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"ok   {pack.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
