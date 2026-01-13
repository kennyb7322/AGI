# Copyright (c) 2026 Kenny B (kennyb7322)
# Confidential and Proprietary (template). If this repository is public, remove confidentiality markings.
# See LICENSE and CONFIDENTIALITY.md for details.

from pathlib import Path

from agi.bootstrap import build_agent
from agi.eval.harness import load_cases, run_eval


def main() -> None:
    agent = build_agent(Path("configs/app.default.yaml"), workspace_dir=Path("workspace"))
    cases = load_cases(Path("eval/sample_cases.jsonl"))
    results = run_eval(agent, cases)

    passed = sum(1 for r in results if r.ok)
    print(f"Passed {passed}/{len(results)}")
    for r in results:
        status = "OK" if r.ok else "FAIL"
        print(f"- {status} {r.id}: {r.final}")


if __name__ == "__main__":
    main()
