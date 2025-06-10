# Project Structure for idea-monorepo-setup

## Main Package Structure

```
src/idea_monorepo_setup/
├── __init__.py             # Main entry point with CLI handling
├── cli.py                  # Command line interface implementation
├── config.py               # Configuration management
├── docker/
│   ├── __init__.py
│   ├── compose.py          # Docker Compose file parsing
│   └── dockerfile.py       # Dockerfile parsing and analysis
├── idea/
│   ├── __init__.py
│   ├── sdk.py              # SDK configuration generation
│   ├── module.py           # Module configuration generation
│   └── xml_utils.py        # XML handling utilities
├── utils/
│   ├── __init__.py
│   ├── logging.py          # Logging setup and utilities
│   └── validation.py       # Project structure validation
└── exceptions.py           # Custom exceptions
```

## Tests Structure

```
tests/
├── __init__.py
├── conftest.py             # Test fixtures and configuration
├── test_cli.py             # CLI tests
├── test_config.py          # Configuration tests
├── docker/
│   ├── __init__.py
│   ├── test_compose.py     # Docker Compose parsing tests
│   └── test_dockerfile.py  # Dockerfile parsing tests
├── idea/
│   ├── __init__.py
│   ├── test_sdk.py         # SDK configuration tests
│   ├── test_module.py      # Module configuration tests
│   └── test_xml_utils.py   # XML utilities tests
├── utils/
│   ├── __init__.py
│   ├── test_logging.py     # Logging tests
│   └── test_validation.py  # Validation tests
└── fixtures/
    ├── docker-compose.yml  # Sample Docker Compose file
    ├── Dockerfile.python   # Sample Python Dockerfile
    └── idea/               # Sample IDEA configuration files
        ├── misc.xml
        ├── modules.xml
        └── sample.iml
```

## Example Project Structure

```
examples/
└── monorepo-example/
    ├── docker-compose.yml          # Root Docker Compose file
    ├── service1/
    │   ├── Dockerfile              # Python service 1
    │   ├── requirements.txt
    │   └── src/
    │       └── service1/
    │           └── __init__.py
    ├── service2/
    │   ├── Dockerfile              # Python service 2
    │   ├── requirements.txt
    │   └── src/
    │       └── service2/
    │           └── __init__.py
    └── non-python-service/
        └── Dockerfile              # Non-Python service
```

## Module Responsibilities

### Main Package

- **__init__.py**: Main entry point that sets up logging and calls the CLI handler
- **cli.py**: Handles command line arguments and orchestrates the workflow
- **config.py**: Manages configuration options and settings
- **exceptions.py**: Defines custom exceptions for the package

### Docker Package

- **compose.py**: Parses docker-compose.yml files and extracts service information
- **dockerfile.py**: Analyzes Dockerfiles to determine Python version and dependencies

### IDEA Package

- **sdk.py**: Generates SDK configurations for IDEA
- **module.py**: Generates module configurations for IDEA
- **xml_utils.py**: Utilities for reading, modifying, and writing XML files

### Utils Package

- **logging.py**: Sets up logging configuration
- **validation.py**: Validates project structure and prerequisites

### Tests

- Tests mirror the package structure
- Fixtures provide sample files for testing
- Integration tests verify end-to-end functionality

### Examples

- Provides a realistic monorepo example for testing and demonstration