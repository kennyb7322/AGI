# Copyright (c) 2026 Kenny B (kennyb7322)
# Confidential and Proprietary (template). If this repository is public, remove confidentiality markings.
# See LICENSE and CONFIDENTIALITY.md for details.

"""Example: research assistant (requires enabling network policy)."""

from pathlib import Path

from agi.bootstrap import build_agent


def main() -> None:
    agent = build_agent(Path("configs/app.network.yaml"), workspace_dir=Path("workspace"))
    task = (
        "Fetch the NIST AI RMF page and summarize the key purpose of the framework. "
        "Use the http_get tool only for nist.gov."
    )
    result = agent.run(task)
    print(result.final)


if __name__ == "__main__":
    main()
