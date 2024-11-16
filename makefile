sources = time_master

.PHONY: test format lint unittest coverage pre-commit clean
test: format unittest

format:
	ruff format $(sources) tests

lint:
	flake8 $(sources) tests

unittest:
	pytest

coverage:
	pytest --cov=$(sources) --cov-branch --cov-report=term-missing tests

pre-commit:
	pre-commit run --all-files

clean:
	rm -rf .pytest_cache
	rm -rf *.egg-info
	rm -rf .tox dist site
	rm -rf coverage.xml .coverage
