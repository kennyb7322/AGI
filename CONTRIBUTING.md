# Contributing

> If this repository is private/proprietary, adjust this file or remove it.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Quality gates

- `ruff check .`
- `mypy src`
- `pytest -q`

## Adding a new tool

1. Create a tool under `src/agi/tools/`
2. Add a Tool Card under `docs/templates/TOOL_CARD_TEMPLATE.md`
3. Update `configs/` policy allow/deny rules
4. Add unit tests under `tests/`

## Security

Do not accept changes that:
- add unsafe default policies,
- add tools that can cause irreversible harm without explicit approvals,
- expose secrets in logs/traces.

