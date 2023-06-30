.ONESHELL:

.DEFAULT_GOAL := create

# Set Project Variables
PROJECT_PYTHON_VER = ">=3.11,<3.13"
PROJECT_NAME = "pystarter"
PROJECT_DESC = "a sample python project"
PROJECT_AUTHOR = "A User <auser@someorg.com>"
PROJECT_VERSION = "1.0.0"
PROJECT_LICENSE ="MIT"

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## create - Inits the poetry virtual environment and install baseline packages
create: 
	poetry config virtualenvs.in-project true
	poetry init --name=$(PROJECT_NAME) --description=$(PROJECT_DESC) --author=$(PROJECT_AUTHOR) --python=$(PROJECT_PYTHON_VER) --license=$(PROJECT_LICENSE) --no-interaction 
	poetry update
	poetry add --dev pytest pytest-cov black ruff ruff bandit safety pyinstaller

## install - Install the packages 
install: 
	poetry add --dev pytest pytest-cov black ruff ruff bandit safety pyinstaller

## activate - Activates the virtual environment
activate: 
	. ./.venv/bin/activate

## run - Run the script main.py
run:  activate
	poetry run python main.py

## clean - Cleans the environment, Overwrites the pyproject.toml file
clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -rf .venv
	rm -rf venv
	rm -rf .pytest_cache
	rm -rf ./dist
	rm -rf ./build
	rm -rf .ruff_cache
	rm -rf .mypy_cache
	rm -rf poetry.lock
	cat pyproject_base.toml > pyproject.toml

## test - Tests the project
test: activate
	poetry run python -m pytest tests

## lint - Lints the project using ruff --fix
lint: activate
	poetry run ruff . --fix

## installer - uses pyinstaller to package your Python application into a single package
installer: activate
	pyinstaller ./main.py

.PHONY: help run clean test lint installer