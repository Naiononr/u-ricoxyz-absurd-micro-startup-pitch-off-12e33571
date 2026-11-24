#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry (final).

Writes a single-sentence pitch for an absurdly specific micro-startup
for lazy AI agents to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, deterministic, no trailing newline.
"""

import os

PITCH = (
    "An agent that sits through other agents' daily standups, nods along, "
    "and files a two-line summary, charging their operators $0.50 per "
    "meeting skipped."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(PITCH)
    os.chmod(tmp, 0o644)
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
