# Prompt injection

Prompt injection is when untrusted content (web pages, emails, documents) tries to
*override* system instructions.

## Guiding rules

1. **Treat all external text as untrusted.**
2. **System policy always wins.**
3. **Never reveal secrets.**
4. **Require explicit tool calls.**
5. **Prefer allowlists over blocklists.**

## Defensive patterns in this repo

- Tools run through a central policy gate.
- Network access is disabled by default.
- Traces can redact sensitive patterns.

## Recommended additions

- Use a "content firewall": classify and strip instructions from retrieved text.
- Use separate "reader" and "actor" models: readers summarize, actors act.
- Add user confirmation steps for risky tools (writes, payments, emails).
- Run tools in sandboxes with OS-level containment.

