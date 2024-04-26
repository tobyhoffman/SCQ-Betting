.PHONY: lint format

PYTHON_DIR = scq_betting
MYPY_CACHE = .mypy_cache

lint:
	poetry run ruff $(PYTHON_DIR)
	poetry run ruff --select I $(PYTHON_DIR)
	mkdir $(MYPY_CACHE); poetry run mypy $(PYTHON_DIR) --cache-dir $(MYPY_CACHE)

format:
	poetry run ruff format $(PYTHON_DIR)
	poetry run ruff --select I --fix $(PYTHON_DIR)

spell_check:
	poetry run codespell --toml pyproject.toml

spell_fix:
	poetry run codespell --toml pyproject.toml -w