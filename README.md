<div align="center">

# Python Starter Project Boilerplate Template - v3.0.0

A Python boilerplate starter project template to setup a baseline Python project for you to get started.

[![Build Status](https://github.com/AaronSaikovski/pystarter/workflows/build/badge.svg)](https://github.com/AaronSaikovski/pystarter/actions)
[![Licence](https://img.shields.io/github/license/AaronSaikovski/pystarter)](LICENSE)

</div>
Python projects are tricky to setup correctly and as such the creation of this project came about. I hope you enjoy this and enjoy using it as much as I do.
This has been recently updated to use the awesome UV tool packaging and dependency toolchain.

## Usage

Click the [Use this template](https://github.com/AaronSaikovski/pystarter/generate) button at the top of this project's GitHub page to get started.

## Software Requirements:

- [Python v3.13.x](https://www.python.org/) or higher needs to be installed.
- [UV](https://github.com/astral-sh/uv) or higher needs to be installed
- [Taskfile](https://taskfile.dev/) to run the build chain commands listed below.

## Installation:

The toolchain is driven by using [Taskfile](https://taskfile.dev/) and all commands are managed via the file `Taskfile.yml`

The list of commands is as follows:

```bash
* activate:           Activates the virtual environment.
* clean:              Cleans the environment, deletes the environment.
* create:             Inits the python project using UV and creates and activates a new virtual environment.
* default:            Call Create as default cmd.
* deps:               Install the dependencies.
* docker-build:       builds a docker image based on the docker file
* docker-run:         builds a docker image based on the docker file
* lint:               Lints the project using ruff --fix and sorts imports
* release:            uses pyinstaller to package your Python application into a single package
* run:                Run the script main.py
* test:               Tests the project.
* update:             updates dependency versions
* vulncheck:          Checks for vulnerabilities in the project
```

Execute using the taskfile utility:

```bash
task <command_from_above_list>
```

To get started type:

- `task create` - this will create a new environment, fetch the dependencies and activate the virtual environment in one step.
- `task run` - to run project in the src folder.
- `task clean` - to delete everything - venv, deps etc.

## Attribution

- original concept derived from here: https://github.com/Justintime50/python-template
