from pathlib import Path
from typing import Union

from sokort._config import Config, load_config_from_env_or_home
from sokort._logging import get_logger

__version__ = "0.3.0"


nwpc_graphics_config: Config = load_config_from_env_or_home()
logger = get_logger()


def get_config() -> Config:
    if nwpc_graphics_config is None:
        logger.warning(
            "Please set environment variable NWPC_GRAPHICS_CONFIG, "
            "or use load_config function to load config manually.")
        raise ValueError("config is not loaded.")
    else:
        return nwpc_graphics_config


def load_config(config_path: Union[str, Path]):
    global nwpc_graphics_config
    nwpc_graphics_config = Config.load(config_path)
