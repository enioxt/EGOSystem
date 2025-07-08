#!/usr/bin/env python3
"""Pre-commit hook to ensure only whitelisted paths are committed to the public repo.

Fail the commit if any staged file is outside the allowed set.
Allowed:
  • README.md, LICENSE, ROADMAP.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md
  • All content inside docs/** and daily-reports/**
  • All content inside .github/**
Adjust the list below as needed.
"""
from __future__ import annotations
import pathlib
import subprocess
import sys

ALLOWED_ROOT_FILES = {
    "README.md",
    "LICENSE",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    ".gitignore",
}
ALLOWED_DIR_PREFIXES = (
    "docs/",
    "daily-reports/",
    ".github/",
)

def get_staged_files() -> list[str]:
    result = subprocess.run([
        "git",
        "diff",
        "--cached",
        "--name-only",
    ], capture_output=True, text=True, check=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

def is_allowed(path: str) -> bool:
    # Exact match for root files
    if path in ALLOWED_ROOT_FILES:
        return True
    # Allowed directory prefixes
    return any(path.startswith(prefix) for prefix in ALLOWED_DIR_PREFIXES)

def main() -> int:
    violations: list[str] = []
    for p in get_staged_files():
        # Normalise path separator
        norm = p.replace("\\", "/")
        if not is_allowed(norm):
            violations.append(norm)

    if violations:
        print("Error: The following files are outside the public whitelist:\n", file=sys.stderr)
        for v in violations:
            print(f"  - {v}", file=sys.stderr)
        print("\nPlease move them to an allowed location or update the whitelist.", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
