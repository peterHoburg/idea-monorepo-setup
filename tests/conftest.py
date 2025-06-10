"""
Test fixtures and configuration for idea-monorepo-setup tests.
"""

import os
from typing import Any

import pytest

from idea_monorepo_setup.config import Config


@pytest.fixture
def test_config() -> Config:
    """
    Fixture providing a test configuration.

    Returns:
        Test configuration instance
    """
    config = Config()
    config.compose_file = os.path.join("tests", "fixtures", "docker-compose.yml")
    config.idea_dir = os.path.join("tests", "fixtures", "idea")
    config.log_level = "DEBUG"
    return config


@pytest.fixture
def sample_services() -> dict[str, dict[str, Any]]:
    """
    Fixture providing sample services data.

    Returns:
        Dictionary of sample services
    """
    return {
        "service1": {"build": {"context": "./service1", "dockerfile": "Dockerfile"}, "volumes": ["./service1:/app"]},
        "service2": {"build": {"context": "./service2", "dockerfile": "Dockerfile"}, "volumes": ["./service2:/app"]},
        "non-python-service": {"image": "nginx:latest", "ports": ["80:80"]},
    }


@pytest.fixture
def sample_python_versions() -> dict[str, str]:
    """
    Fixture providing sample Python versions for services.

    Returns:
        Dictionary mapping service names to Python versions
    """
    return {"service1": "3.9", "service2": "3.10"}
