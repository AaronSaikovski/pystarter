<div align="center">

# Python Starter Project Boilerplate Template

A Python starter project template with a baseline project structure, dependency management via UV, linting, testing, Docker support, and PyInstaller packaging.

[![License](https://img.shields.io/github/license/AaronSaikovski/pystarter)](LICENSE)
[![Build](https://github.com/AaronSaikovski/pystarter/actions/workflows/build.yml/badge.svg)](https://github.com/AaronSaikovski/pystarter/actions/workflows/build.yml)

</div>

This project provides a ready-to-use Python 3.13 project structure with sensible defaults for development, testing, and deployment.

## Usage

Click the [Use this template](https://github.com/AaronSaikovski/pystarter/generate) button at the top of this project's GitHub page to get started.

## Requirements

- [Python 3.13](https://www.python.org/) or higher
- [UV](https://github.com/astral-sh/uv) — fast Python package installer and resolver
- [Task](https://taskfile.dev/) — task runner for build commands

## Commands

All commands are managed via `Taskfile.yml`:

| Command | Description |
| :--- | :--- |
| `task create` | Initialize project: create venv, install deps, merge base config |
| `task deps` | Install dependencies from `requirements.txt` |
| `task run` | Run the app via `uv run -m pystarter` |
| `task test` | Run tests via `pytest` |
| `task lint` | Run isort, ruff (format + fix), mypy, and pyrefly |
| `task seccheck` | Run bandit for vulnerability scanning (src + tests) |
| `task build` | Package with `uv build` |
| `task dist` | Create standalone executable with PyInstaller |
| `task docker-build` | Build Docker image (linux/arm64) |
| `task reqs` | Generate `requirements.txt` from `pyproject.toml` |
| `task update` | Upgrade all installed tools |
| `task clean` | Remove venv, caches, and generated files |

Execute using the Task utility:

```bash
task <command>
```

To get started:

- `task create` — initialize the project and install dependencies
- `task run` — run the project
- `task clean` — remove all generated files

## Project Structure

```text
src/pystarter/           # Main package
  app.py                 # Entry point with main() function
  __main__.py            # Module entry (uv run -m pystarter)
  version.py             # Version and APP_NAME constants
  common/                # Shared constants
  data_models/           # Pydantic data models
  sample_data/           # Sample data classes
  utils/                 # Utilities: console, logging, file, profiling
src/sample_package/      # Secondary sample package
tests/                   # Pytest test suite
```
