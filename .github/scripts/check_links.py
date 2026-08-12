#!/usr/bin/env python3
"""Internal markdown link checker.

Validates that relative links inside the repo point to existing files.
External (http/https/mailto) and pure anchor (#...) links are skipped,
so the check works fully offline and does not depend on network reachability.
"""
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    root = Path(".")
    broken = 0
    total = 0
    for f in sorted(root.rglob("*.md")):
        text = f.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(text):
            url = m.group(1).strip()
            if url.startswith(("http://", "https://", "mailto:", "#")):
                continue
            total += 1
            path_part = url.split("#")[0].rstrip("/")
            if not path_part:
                continue
            if not (f.parent / path_part).exists():
                broken += 1
                print(f"  ✗ {f} -> {url}")
    print(f"内部相对链接 {total} 个，断链 {broken} 个")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
