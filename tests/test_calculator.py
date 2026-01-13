# Copyright (c) 2026 Kenny B (kennyb7322)
# Confidential and Proprietary (template). If this repository is public, remove confidentiality markings.
# See LICENSE and CONFIDENTIALITY.md for details.

from agi.tools.builtins.calculator import CalculatorTool, CalculatorArgs
from agi.tools.base import ToolContext


def test_calculator_basic() -> None:
    tool = CalculatorTool()
    ctx = ToolContext(run_id="test", agent_name="test-agent")
    out = tool.run(CalculatorArgs(expression="(2+3)*4"), ctx)
    assert out == "20"
