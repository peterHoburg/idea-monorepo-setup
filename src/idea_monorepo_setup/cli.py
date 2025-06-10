"""Command line interface implementation module.

This module handles command line arguments and orchestrates the workflow
for configuring IDEA for monorepo projects.
"""

import argparse

from idea_monorepo_setup.utils import log


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments.

    Args:
        args: Command line arguments (if None, uses sys.argv)

    Returns:
        Parsed arguments

    """
    # This is a placeholder implementation
    # Actual implementation will be done following TDD approach
    parser = argparse.ArgumentParser(description="Configure IDEA project structure for monorepos with Docker services")
    parser.add_argument(
        "--compose-file",
        type=str,
        default="docker-compose.yml",
        help="Path to docker-compose.yml file (default: docker-compose.yml)",
    )
    parser.add_argument(
        "--idea-dir",
        type=str,
        default=".idea",
        help="Path to IDEA directory (default: .idea)",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Logging level (default: INFO)",
    )
    return parser.parse_args(args)


def main(args: list[str] | None = None) -> int:
    """Main entry point for the CLI.

    Args:
        args: Command line arguments (if None, uses sys.argv)

    Returns:
        Exit code (0 for success, non-zero for error)

    """
    # This is a placeholder implementation
    # Actual implementation will be done following TDD approach
    parsed_args = parse_args(args)
    log.setup_logging(log_level=parsed_args.log_level)
    logger = log.get_logger(__name__)
    logger.info("Starting idea-monorepo-setup")
    return 0
