.ONESHELL:

.DEFAULT_GOAL := create

# Set runtime versions
PYTHON = ./venv/bin/python3
PIP = ./venv/bin/pip3
VIRTUAL_BIN := ./venv/bin

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## create - create and activate the virtual environment
create: requirements.txt
	python3 -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
	$(PIP) install -r requirements.txt
	$(PIP) install --upgrade pip

## activate - Activate the virtual environment
activate: create
	. ./venv/bin/activate

## run - run the script
run: activate
	$(PYTHON) main.py

## clean - Cleans the environment
clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -rf .venv
	rm -rf venv
	rm -rf .pytest_cache
	rm -rf ./dist
	rm -rf ./build
	rm -rf .ruff_cache
	rm -rf .mypy_cache
	
	
## freeze - freeze the environment to requirements.txt
freeze: activate
	$(PIP) freeze > requirements.txt

## install - install the packages fromrequirements.txt
install: activate
	$(PIP) install -r requirements.txt

## test - Test the project
test: activate
	$(VIRTUAL_BIN)/pytest

## lint - Lint the project using ruff --fix
lint: activate
	$(VIRTUAL_BIN)/ruff . --fix

## typecheck - use mypy to typecheck the code
typecheck: activate
	mypy .

## installer - uses pyinstaller to package your Python application into a single package
installer: activate
	pyinstaller ./main.py

.PHONY: help run clean format test lint freeze typecheck installer