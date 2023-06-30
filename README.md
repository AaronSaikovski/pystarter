<div align="center">

# Python Starter Project Boilerplate Template

A Python boilerplate starter project template to setup a baseline Python project for you to get started.

[![Build Status](https://github.com/AaronSaikovski/pystarter/workflows/build/badge.svg)](https://github.com/AaronSaikovski/pystarter/actions)
[![Coverage Status](https://coveralls.io/repos/github/AaronSaikovski/pystarter/badge.svg?branch=main)](https://coveralls.io/github/AaronSaikovski/pystarter?branch=main)
[![Licence](https://img.shields.io/github/license/AaronSaikovski/pystarter)](LICENSE)

</div>
Python projects are tricky to setup correctly and as such the creation of this project came about. I hope you enjoy this and enjoy using it as much as I do.
This has been recently updated to use the awesome [Poetry](https://python-poetry.org/) packaging and dependency toolchain.

## Usage

Click the [Use this template](https://github.com/AaronSaikovski/pystarter/generate) button at the top of this project's GitHub page to get started.

## Prequisites

- Python v3.10 or higher needs to be installed - https://www.python.org/
- Poetry v1.5.1 or higher needs to be installed - https://python-poetry.org/docs/#installation

## Setup

The `Makefile` contains all the steps to get going - simple run `make help` to get more information.

1. Run `make create` to create and install the poetry environment. This will configure and setup the base poetry environment to get started and will install the base packages.
2. Ensure your Python interpreter is set to `.venv:poetry` in Visual studio code.
3. Run `make activate` to activate the virtual environment.
4. Run `make run` to run `main.py` in your root directory.
5. Run `make test` to execute the unit tests in the `tests` folder.
6. Run `make lint` to run the [ruff].(https://github.com/astral-sh/ruff) linting tool and make fixes.
7. Run `make clean` to clean out the project and reset it to a base setup. **This process will overwrite the pyproject.toml file**
8. Run `make installer` to build the project using [Pyinstaller](https://pyinstaller.org/).

## Attribution

- Advanced poetry setup: https://testdriven.io/blog/python-project-workflow/
- original concept derived from here: https://github.com/Justintime50/python-template
