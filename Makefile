.ONESHELL:

.DEFAULT_GOAL := create

# Set Project Variables
PROJECT_PYTHON_VER = ">=3.11,<3.13"
PROJECT_NAME = "pystarter"
PROJECT_DESC = "a sample python project"
PROJECT_AUTHOR = "A User <auser@someorg.com>"
PROJECT_VERSION = "1.0.0"
PROJECT_LICENSE ="MIT"
MAIN_SRC_DIR = "./src/"

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## create - Inits the poetry virtual environment and install baseline packages
create:  
	poetry config virtualenvs.in-project true
	poetry init --name=$(PROJECT_NAME) --description=$(PROJECT_DESC) --author=$(PROJECT_AUTHOR) --python=$(PROJECT_PYTHON_VER) --license=$(PROJECT_LICENSE) --no-interaction 
	
## deps - Install the dependencies 
deps: 	
	poetry add pytest pytest-cov black ruff bandit pyinstaller --group dev
	poetry update

## activate - Activates the virtual environment
activate: 
	. ./.venv/bin/activate

## install - installs the poetry environment with dependencies
install: 
	poetry install

## run - Run the script main.py
run:  activate
	poetry run python $(MAIN_SRC_DIR)/main.py
	
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
	rm -rf main.spec
	cat pyproject_base.toml > pyproject.toml


## test - Tests the project
test: activate
	poetry run python -m pytest tests

## update - updates dependency versions
update: activate
	poetry update -v

## lint - Lints the project using ruff --fix
lint: activate
	poetry run ruff . --fix
	poetry run black --line-length 128 --target-version py39 .

## vulncheck - Checks for vulnerabilities in the project
vulncheck: 
	poetry run bandit -r .	

## release - uses pyinstaller to package your Python application into a single package
release: activate
	poetry run pyinstaller $(MAIN_SRC_DIR)/main.py

.PHONY: help run clean test lint installer deps install vulncheck