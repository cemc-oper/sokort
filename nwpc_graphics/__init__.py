from pathlib import Path
from nwpc_graphics._config import Config, load_config_from_env
from nwpc_graphics._logging import get_logger

__version__ = "0.2.0"


nwpc_graphics_config = load_config_from_env()
logger = get_logger()


def get_config():
    if nwpc_graphics_config is None:
        logger.warning(
            "Please set environment variable NWPC_GRAPHICS_CONFIG, "
            "or use load_config function to load config manually.")
        raise ValueError("config is not loaded.")
    else:
        return nwpc_graphics_config


def load_config(config_path: str or Path):
    global nwpc_graphics_config
    nwpc_graphics_config = Config.load(config_path)
