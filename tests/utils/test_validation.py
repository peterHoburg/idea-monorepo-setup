"""
Tests for project structure validation.
"""

from unittest.mock import patch

from idea_monorepo_setup.utils import validation


def test_validate_project_structure(tmpdir):
    """Test validating project structure."""
    project_dir = tmpdir.mkdir("project")

    with patch("idea_monorepo_setup.utils.validation.logger") as mock_logger:
        result = validation.validate_project_structure(str(project_dir))
        assert result is True
        mock_logger.info.assert_called_once()


def test_validate_docker_compose_exists(tmpdir):
    """Test validating that docker-compose.yml exists."""
    compose_file = tmpdir.join("docker-compose.yml")
    compose_file.write("version: '3'")

    result, error = validation.validate_docker_compose(str(compose_file))
    assert result is True
    assert error is None


def test_validate_docker_compose_not_exists():
    """Test validating that docker-compose.yml does not exist."""
    with patch("idea_monorepo_setup.utils.validation.logger") as mock_logger:
        result, error = validation.validate_docker_compose("nonexistent-file.yml")
        assert result is False
        assert error is not None
        assert "not found" in error["error"]
        mock_logger.error.assert_called_once()


def test_validate_python_services(sample_services):
    """Test validating and identifying Python services."""
    python_services = validation.validate_python_services(sample_services)
    assert isinstance(python_services, list)
    assert "service1" in python_services
    assert "service2" in python_services


def test_validate_prerequisites():
    """Test validating prerequisites."""
    with patch("idea_monorepo_setup.utils.validation.logger") as mock_logger:
        result = validation.validate_prerequisites()
        assert result is True
