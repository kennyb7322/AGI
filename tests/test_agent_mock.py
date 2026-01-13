# Copyright (c) 2026 Kenny B (kennyb7322)
# Confidential and Proprietary (template). If this repository is public, remove confidentiality markings.
# See LICENSE and CONFIDENTIALITY.md for details.

from pathlib import Path

from agi.bootstrap import build_agent


def test_agent_with_mock_llm_runs_calculator() -> None:
    agent = build_agent(Path("configs/app.default.yaml"), workspace_dir=Path("workspace_test"))
    result = agent.run("What is 23*19? Use the calculator tool.")
    assert "437" in result.final  # 23*19 = 437
