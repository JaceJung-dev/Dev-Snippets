import logging
import logging.config
from pathlib import Path
from typing import Optional

import yaml


def _ensure_log_dir(config: dict) -> None:
    """
    Ensure log directories exist for all handlers in config

    Args:
        config: Logging configuration dictionary
    """
    handlers = config.get("handlers", {})

    for handler_config in handlers.values():
        if "filename" in handler_config:
            log_file = Path(handler_config["filename"])
            log_dir = log_file.parent

            if not log_dir.exists():
                log_dir.mkdir(parents=True, exist_ok=True)


def setup_logging_yaml(
    config_path: Optional[str] = None, default_level: int = logging.INFO
) -> None:
    """
    Setup logging configuration from YAML file

    Args:
        config_path: Path to YAML config file
        default_level: Default logging if config file not found
    """
    if config_path is None:
        path = Path(__file__).parent / "logging.yaml"
    else:
        path = Path(config_path)

    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        _ensure_log_dir(config)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        logging.warning(f"Config file not found at {path}, using basic config")
