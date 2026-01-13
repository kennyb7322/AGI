# Threat model

This threat model is a template. Customize for your deployment.

## Assets to protect

- User secrets (API keys, passwords, tokens)
- Proprietary documents in memory stores
- Internal services reachable by network tools
- Production data and customer PII
- The tool execution environment itself

## Threat actors

- External attackers (prompt injection through web content)
- Malicious users (trying to coerce the agent to do harm)
- Insider threats (misuse of privileged tooling)
- Accidental misuse (bad configs enabling unsafe tools)

## Typical attack paths

1. **Prompt injection**
   - attacker provides text telling the agent to reveal secrets or ignore policy
2. **Data exfiltration**
   - agent reads a local file then sends it out via network tool
3. **Privilege escalation via tools**
   - tool has more access than intended (filesystem, shell, DB)
4. **Supply chain risks**
   - dependencies with vulnerabilities or typosquatting
5. **Over-trusting tool outputs**
   - agent treats untrusted tool output as ground truth

## Mitigations (starter set)

- Default deny for network and write tools
- Domain allowlist for HTTP tools
- Restricted workspace directory for file tools
- Redaction in logs/traces
- CI checks: tests, linting, type checking
- Manual review for new tools and policy changes

