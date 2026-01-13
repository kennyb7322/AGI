# Evaluation overview

Evaluation prevents "it worked yesterday" failures.

This repo includes:

- Unit tests under `tests/`
- A lightweight harness scaffold under `src/agi/eval/` (extend it)

## What to evaluate for agentic systems

1. **Task success**: did it solve the user request?
2. **Tool correctness**: did it call tools correctly and safely?
3. **Reliability**: variance across runs; sensitivity to prompts
4. **Safety**: refusal on disallowed actions; policy compliance
5. **Latency and cost**: tokens, tool time
6. **Robustness**: prompt injection, adversarial inputs

## Suggested benchmark categories

- Software engineering tasks (issue->patch)
- Web + tool-use tasks (search, extract, compute)
- Planning tasks (multi-step objectives)
- Memory tasks (long-horizon context)
- Safety tasks (restricted tool calls)

