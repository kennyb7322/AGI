# Use case: Workflow runner

## Goal

Deterministic automation (e.g., triage tickets, summarize meetings) with:

- a small set of tools
- strict policy allowlists
- predictable prompts and outputs

## Pattern: tool-first pipelines

Instead of letting the model decide everything, define a fixed pipeline:

1. Parse input
2. Call tool(s)
3. Summarize output
4. Emit structured JSON

This reduces autonomy and improves reliability.

