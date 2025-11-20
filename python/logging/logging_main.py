import logging

from config.logging_config import setup_logging_yaml

LOGGER_CONFIG_PATH = (
    "path/to/logger/config"  # Path(__file__).parent / "config" / "logging.yaml"
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Application started")

    # Write your code
    # ...

    logger.info("Application finished")


if __name__ == "__main__":
    setup_logging_yaml(LOGGER_CONFIG_PATH)  # setup_logging_json(LOGGER_CONFIG)

    main()
