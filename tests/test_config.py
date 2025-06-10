"""
Tests for the configuration management.
"""

import argparse

from idea_monorepo_setup.config import Config, create_config


def test_config_defaults():
    """Test that the default configuration values are set correctly."""
    config = Config()
    assert config.compose_file == "docker-compose.yml"
    assert config.idea_dir == ".idea"
    assert config.log_level == "INFO"
    assert config.log_file is None


def test_config_from_args():
    """Test that configuration is updated from command line arguments."""
    config = Config()
    args = argparse.Namespace(
        compose_file="custom-compose.yml", idea_dir="custom-idea", log_level="DEBUG", log_file="app.log"
    )

    config.from_args(args)

    assert config.compose_file == "custom-compose.yml"
    assert config.idea_dir == "custom-idea"
    assert config.log_level == "DEBUG"
    assert config.log_file == "app.log"


def test_config_validate_success(tmpdir):
    """Test that configuration validation succeeds with valid inputs."""
    compose_file = tmpdir.join("docker-compose.yml")
    compose_file.write("version: '3'")

    idea_dir = tmpdir.join(".idea")
    idea_dir.mkdir()

    config = Config()
    config.compose_file = str(compose_file)
    config.idea_dir = str(idea_dir)

    assert config.validate() is True


def test_config_validate_failure():
    """Test that configuration validation fails with invalid inputs."""
    config = Config()
    config.compose_file = "nonexistent-file.yml"

    assert config.validate() is False


def test_config_to_dict():
    """Test that configuration is correctly converted to a dictionary."""
    config = Config()
    config.compose_file = "docker-compose.yml"
    config.idea_dir = ".idea"
    config.log_level = "INFO"
    config.log_file = "app.log"

    config_dict = config.to_dict()

    assert config_dict == {
        "compose_file": "docker-compose.yml",
        "idea_dir": ".idea",
        "log_level": "INFO",
        "log_file": "app.log",
    }


def test_create_config():
    """Test that create_config returns a new Config instance."""
    config = create_config()
    assert isinstance(config, Config)
