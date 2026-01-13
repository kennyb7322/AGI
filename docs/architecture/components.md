# Components

This section maps folders to responsibilities.

## `agi/core/`

- `agent.py`: agent loop; parses JSON actions; executes tools; stops at `max_steps`
- `types.py`: simple message and result dataclasses
- `errors.py`: framework exceptions

## `agi/llm/`

- `base.py`: provider interface
- `mock.py`: deterministic provider for tests/CI
- `openai_compatible.py`: lightweight HTTP client for `/v1/chat/completions`
- `factory.py`: create provider from config

## `agi/tools/`

- `base.py`: tool interface + typed args via Pydantic
- `registry.py`: tool registration and lookup
- `builtins/`: calculator, file read/write, http_get

## `agi/safety/`

- `policy.py`: policy gate for tool use (network/file restrictions)
- `redaction.py`: best-effort redaction for logs and traces

## `agi/memory/`

- `sqlite_store.py`: simple persistent memory baseline
- `in_memory.py`: ephemeral memory for tests/demos

## `agi/planning/`

- `simple.py`: a single-step planner (placeholder)
- (extend here for HTN, tree search, reflection, etc.)

## `agi/observability/`

- `logging.py`: structured JSON logs
- `tracing.py`: JSONL traces to disk

## `agi/api/`

- `app.py`: FastAPI server; creates agent from config

## `agi/eval/` (scaffold)

- use this for benchmark harnesses and regression evaluation

