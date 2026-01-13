# Architecture overview

The repo is organized around **boundaries** that correspond to common failure modes in agentic systems:

1. **LLM boundary**: a provider wrapper that can be swapped.
2. **Tool boundary**: deterministic, typed tools, invoked explicitly.
3. **Safety boundary**: policy checks for every tool call.
4. **State boundary**: memory + traces persist what happened.
5. **Evaluation boundary**: tests and eval suites prevent regressions.

## Layered architecture

```mermaid
flowchart TB
  subgraph App["App / Integrations"]
    CLI[CLI]
    API[FastAPI]
  end

  subgraph Framework["AGI Framework (src/agi)"]
    Agent[Agent Runtime]
    Planner[Planner]
    Memory[Memory Store]
    Policy[Tool Policy]
    Tools[Tool Registry]
    Obs[Observability]
    Eval[Eval Harness]
    LLM[LLM Provider]
  end

  CLI --> Agent
  API --> Agent

  Agent --> Planner
  Agent --> LLM
  Agent --> Policy
  Agent --> Tools
  Agent --> Memory
  Agent --> Obs
  Eval --> Agent
  Tools --> External[(External Systems)]
```

## Runtime invariants (what should always be true)

- Tool invocations are **explicit** and **audited**.
- Policy checks happen **before** tool execution.
- Tool outputs are treated as **untrusted** and truncated when necessary.
- Logging can be configured to **redact** secrets.

