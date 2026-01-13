# Copyright (c) 2026 Kenny B (kennyb7322)
# Confidential and Proprietary (template). If this repository is public, remove confidentiality markings.
# See LICENSE and CONFIDENTIALITY.md for details.

"""Example: dev assistant pattern (read-only).

This demo reads a file and summarizes it. File writes are blocked by policy by default.
"""

from pathlib import Path

from agi.bootstrap import build_agent


def main() -> None:
    agent = build_agent(Path("configs/app.default.yaml"), workspace_dir=Path("workspace"))
    task = "Read README.md via file_read and summarize what this repo is for."
    result = agent.run(task)
    print(result.final)


if __name__ == "__main__":
    main()
