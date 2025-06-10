"""Custom exceptions module.

This module defines custom exceptions for the idea-monorepo-setup package.
"""


class IdeaMonorepoSetupError(Exception):
    """Base exception for all idea-monorepo-setup errors."""


class ConfigurationError(IdeaMonorepoSetupError):
    """Exception raised for configuration errors."""


class DockerComposeError(IdeaMonorepoSetupError):
    """Exception raised for docker-compose.yml parsing errors."""


class DockerfileError(IdeaMonorepoSetupError):
    """Exception raised for Dockerfile parsing errors."""


class IdeaConfigError(IdeaMonorepoSetupError):
    """Exception raised for IDEA configuration errors."""


class ValidationError(IdeaMonorepoSetupError):
    """Exception raised for validation errors."""
