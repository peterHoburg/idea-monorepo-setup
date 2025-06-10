# Development Guidelines for idea-monorepo-setup

This document provides essential information for developers working on the idea-monorepo-setup project.

## Development workflow
The general development workflow.

1. Get an incomplete ticket from TICKETS.md
2. Run `make test` and `make lint` to make sure the project is in a good state to start. 
3. Write tests (TDD)
4. Write code
5. `make test` and `make lint` must pass!
6. Mark the ticket as complete. 

## Build/Configuration Instructions

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) for package management

### Setup

1. Clone the repository
2. Set up a virtual environment:
   ```bash
   uv sync
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```

### Build

The project uses hatchling as the build backend:

```bash
  make build
```

## Testing Information

### Test Framework

The project uses pytest with the following plugins:
- pytest-xdist: For parallel test execution
- pytest-cov: For code coverage reporting
- typeguard: For runtime type checking
- inline-snapshot: For snapshot testing

### Running Tests

Run all tests with:
```bash
make test
```

This executes `pytest -n auto`, which runs tests in parallel using all available CPU cores.

### Writing Tests

1. **Test File Structure**: Create test files in the `tests/` directory with the naming convention `test_*.py`.

2. **Test Function Naming**: Name test functions with the prefix `test_`.

3. **TDD Approach**: Follow Test-Driven Development:
   - Write tests first
   - Run tests to see them fail
   - Implement the code
   - Run tests again to see them pass
   - Refactor as needed

4. **Example Test**:
   ```python
   import logging
   import pytest
   
   from idea_monorepo_setup.utils import log
   
   def test_get_logger():
       """Test that get_logger returns a logger with the correct name."""
       logger = log.get_logger("test_logger")
       assert isinstance(logger, logging.Logger)
       assert logger.name == "test_logger"
   ```

### Code Coverage

The project requires a minimum of 80% code coverage. Check coverage with:

```bash
pytest --cov=idea_monorepo_setup
```

## Code Quality and Linting

Run all linting checks with:
```bash
make lint
```

This runs:
- ruff format: For code formatting
- ruff check: For linting
- ty check: For type checking
- pyright: For static type analysis

## Additional Development Information

### Project Structure

- `src/idea_monorepo_setup/`: Main package
  - `cli.py`: Command-line interface implementation
  - `utils/`: Utility modules
    - `log.py`: Logging setup and utilities

### Coding Style

The project follows strict coding standards enforced by ruff:
- Line length: 120 characters
- Python target version: 3.12
- Double quotes for strings
- Space indentation

### Type Annotations

All functions should include proper type annotations. Runtime type checking is enforced using typeguard.

### Logging

The project uses Python's standard logging module. To get a logger:

```python
from idea_monorepo_setup.utils import log

logger = log.get_logger(__name__)
logger.info("Your message here")
```

Configure logging with:

```python
log.setup_logging(log_level="INFO", log_file="path/to/logfile.log")
```

### CLI Entry Point

The project provides a command-line tool `ims` that can be used after installation:

```bash
ims --compose-file docker-compose.yml --idea-dir .idea --log-level INFO
```