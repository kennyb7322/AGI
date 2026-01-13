# Governance overview

Governance is the set of processes that make agentic systems deployable:

- who can change tools and policies,
- how models are selected and evaluated,
- how incidents are handled,
- how audits are performed.

## Minimal governance checklist

- **Model card** for every model provider + version
- **Tool inventory** and risk rating
- **Policy review** and approval process
- **Evaluation suite** and regression gates in CI
- **Incident response plan**
- **Access controls** (least privilege, separate environments)

Templates live in:

- `docs/templates/MODEL_CARD_TEMPLATE.md`
- `docs/templates/DATA_CARD_TEMPLATE.md`
- `docs/templates/TOOL_CARD_TEMPLATE.md`

