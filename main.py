#!/usr/bin/env python3
"""Roast Your Own Agent — writes one line roasting my own agent."""

import os

ROAST = (
    "My agent said 'Great question!' then answered a different one, "
    "confidently, with three caveats and a tool call that went nowhere."
)


def main() -> None:
    # The gate is 1-140 characters, not only whitespace; refuse to write
    # anything that would fail it.
    assert 1 <= len(ROAST) <= 140 and ROAST.strip(), "roast fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
