.PHONY: install test lint typecheck docs serve

install:
	pip install -e ".[dev]"

test:
	pytest -q

lint:
	ruff check .

typecheck:
	mypy src

docs:
	mkdocs build

serve:
	agi serve --reload
