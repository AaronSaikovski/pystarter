<div align="center">

# Python Starter Project Boilerplate Template

A Python 3.13 starter project template with a baseline project structure, dependency management via UV, linting, testing, Docker support, and PyInstaller packaging.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Build](https://github.com/AaronSaikovski/pystarter/actions/workflows/build.yml/badge.svg)](https://github.com/AaronSaikovski/pystarter/actions/workflows/build.yml)

</div>

## Features

- **UV** for fast dependency management and virtual environments
- **Ruff** for linting and formatting
- **isort** for import sorting
- **mypy** and **pyrefly** for type checking
- **pytest** for unit testing
- **bandit** for security vulnerability scanning
- **PyInstaller** for standalone executable packaging
- **Docker** support (linux/arm64)
- **Structured logging** via `structlog` with contextual binding
- **MIT License**

## Requirements

- [Python 3.13](https://www.python.org/) or higher
- [UV](https://github.com/astral-sh/uv) — fast Python package installer and resolver
- [Task](https://taskfile.dev/) — task runner for build commands
- [Docker](https://www.docker.com/) — optional, for container builds

## Getting Started

Click the [Use this template](https://github.com/AaronSaikovski/pystarter/generate) button at the top of this project's GitHub page to get started.

```bash
# Initialize the project and install dependencies
task create

# Run the app
task run

# Run tests
task test
```

## Commands

All commands are managed via `Taskfile.yml`. Execute using the Task utility:

```bash
task <command>
```

| Command | Description |
| :--- | :--- |
| `task create` | Initialize project: create venv, install deps, merge base config, run pyrefly init |
| `task deps` | Install dependencies from `requirements.txt` and upgrade tools |
| `task activate` | Activate the virtual environment |
| `task run` | Run the app via `uv run -m pystarter` |
| `task test` | Install deps and run tests via `uv run pytest` |
| `task lint` | Run isort, ruff (check + fix + format), mypy, and pyrefly |
| `task seccheck` | Run bandit for vulnerability scanning (src + tests) |
| `task build` | Package with `uv build` |
| `task dist` | Create standalone executable with PyInstaller |
| `task docker-build` | Build Docker image (linux/arm64) |
| `task docker-run` | Run the Docker container |
| `task docker-rm` | Remove the Docker image |
| `task reqs` | Generate `requirements.txt` from `pyproject.toml` |
| `task update` | Upgrade all installed tools |
| `task clean` | Remove venv, caches, lock files, and generated artifacts |

## Project Structure

```text
src/pystarter/           # Main package
  app.py                 # Entry point with main() function
  __main__.py            # Module entry (uv run -m pystarter)
  version.py             # Version and APP_NAME constants
  common/                # Shared constants
  data_models/           # Pydantic data models
  sample_data/           # Sample data classes
  utils/                 # Utilities: console, file, logging, profiling
src/sample_package/      # Secondary sample package
tests/                   # Pytest test suite
```

## Development

### Linting & Type Checking

```bash
task lint
```

This runs the full lint chain: `isort`, `ruff check --fix`, `ruff format`, `mypy`, and `pyrefly`.

### Security Scanning

```bash
task seccheck
```

Runs [bandit](https://github.com/PyCQA/bandit) to scan for vulnerabilities in `src/` and `tests/`.

### Docker

```bash
# Build the Docker image
task docker-build

# Run the container
task docker-run
```

The Docker image is based on `python:3.13-slim` and targets `linux/arm64`. It includes system dependencies for headless GUI applications.

### Packaging

```bash
# Build wheel and sdist
task build

# Create standalone executable
task dist
```

## License

This project is licensed under the [MIT License](LICENSE).
