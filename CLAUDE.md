# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`pystarter` is a Python 3.13 starter project boilerplate template. It provides a baseline project structure with dependency management via UV, linting, testing, Docker support, and PyInstaller packaging.

## Project Structure

```
src/pystarter/           # Main package
  app.py                 # Entry point with main() function
  __main__.py            # Module entry (uv run -m pystarter)
  version.py             # Version and APP_NAME constants
  common/                # Shared constants
  data_models/           # Pydantic data models
  sample_data/           # Sample data classes
  utils/                 # Utilities: console_helper, logging_helper, logging_factory, file_helper, profiling_helper
src/sample_package/      # Secondary sample package
tests/                   # Pytest test suite
```

## Key Commands (via Taskfile.yml)

| Command | Description |
|---------|-------------|
| `task create` | Initialize project: create venv, install deps from `requirements.txt`, merge base config |
| `task deps` | Install dependencies from `requirements.txt` |
| `task run` | Run the app via `uv run -m pystarter` |
| `task test` | Install deps and run tests via `uv run pytest` |
| `task lint` | Run isort, ruff (check + format), mypy |
| `task seccheck` | Run bandit for vulnerability scanning |
| `task build` | Package with `uv build` |
| `task dist` | Create standalone executable with PyInstaller (`pyinstaller --onefile`) |
| `task docker-build` | Build Docker image (linux/arm64) |
| `task clean` | Remove venv, caches, lock files |

The project uses `uv` for dependency management and virtual environments. Dependencies are declared in `pyproject.toml` (generated from `pyproject_base.toml` during `task create`) and pinned in `requirements.txt`.

## Architecture Notes

- **Logging**: Two logging systems coexist — `logging_helper.py` provides a simple `@log` decorator with standard `logging`, while `logging_factory.py` provides structured JSON logging via `structlog` with contextual binding (e.g., request_id).
- **Entry point**: `main()` in `app.py` is the application entry. It loads `.env` via `python-dotenv`, uses structured logging, and demonstrates console output, class usage, and module imports.
- **Build system**: Uses `hatchling` as the build backend. Version is dynamically read from `pystarter.version.VERSION` via `setuptools.dynamic`.
- **Docker**: The Dockerfile is based on `python:3.13-slim` and installs system dependencies for GUI/headless apps (libgtk, libgbm, etc.). Entry point is `python -m pystarter`.

## Linting Rules

All code changes must pass the full lint chain: `isort`, `ruff check`, `ruff format`, and `mypy`, as well as all unit tests. Run `task lint` and `task test` before committing. The project uses ruff for linting and formatting.

## Workflow Orchestration

### 1. Plan Node Default

- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately – don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy

- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop

- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done

- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)

- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes – don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing

- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests – then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.
