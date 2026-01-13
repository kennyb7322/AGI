# Safety overview

Agentic systems become dangerous when they can:

- access sensitive data,
- take irreversible actions,
- or operate without oversight.

This repo implements a **minimal safety baseline**:

- **Policy gate** for every tool call
- **Network off** by default
- **File writes off** by default
- **Domain allowlist** when network is enabled
- **Redaction** for common secret patterns in logs/traces

## What this does *not* solve

- Model alignment
- Social engineering / deceptive outputs
- Advanced prompt injection attacks
- Secure sandboxing for arbitrary code execution
- Robust permissioning in multi-tenant environments

Treat this as a starting point and expand it based on your risk profile.

