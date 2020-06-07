all: tests deps

tests:
	flake8 --exclude=__init__.py spypy
	flake8 tests
	mypy spypy tests
	mypy examples/count
	mypy examples/stamp
	pytest tests

deps:
	pip install -r requierements.txt

run_examples:
	python examples/run.py


.PHONY: tests deps run_examples