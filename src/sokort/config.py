from pathlib import Path
from typing import Optional, Union, Dict
import os
import datetime
import uuid

import yaml

from sokort._logging import get_logger
logger = get_logger()


CONFIG_ENVIRONMENT_VARIABLE_NAME = "NWPC_GRAPHICS_CONFIG"

PLOT_ENGINE = ["ncl", "python"]


class Config(dict):
    def __init__(self, config_file_path: Path = None, **kwargs):
        super(Config).__init__(**kwargs)
        self["config"] = dict()
        self["systems"] = dict()
        for engine in PLOT_ENGINE:
            self[engine] = dict()
        self.config_file_path = config_file_path

    @classmethod
    def load(cls, config_file: Union[str, Path]):
        config = Config(config_file_path=Path(config_file))
        config._load_config()
        config._load_systems()
        return config

    def _load_config(self):
        with open(self.config_file_path) as f:
            config_dict = yaml.safe_load(f)
            self.update(config_dict)
            for engine in PLOT_ENGINE:
                Config.expand_program_config(self.config_file_path, self[engine])

    @classmethod
    def expand_program_config(cls, config_file_path: Path, program_config: Dict) -> Dict:
        if "load_env_script" not in program_config:
            return program_config

        load_env_script = program_config["load_env_script"]
        if len(load_env_script) == 0:
            return program_config

        program_config["load_env_script"] = expand_path_in_config(load_env_script, config_file_path)
        return program_config

    def _load_systems(self):
        systems_path = self.config_file_path.parent.joinpath(self["config"]["systems_dir"])
        if not systems_path.exists():
            raise FileNotFoundError(f"systems directory is not found.")

        for item in systems_path.iterdir():
            if item.is_dir():
                continue
            if item.suffix != ".yaml":
                continue
            self["systems"][item.stem] = Config.load_system_config(item)

    @classmethod
    def load_system_config(cls, file_path):
        with open(file_path) as f:
            c = yaml.safe_load(f)
            c["config_file_path"] = file_path

            for engine in PLOT_ENGINE:
                if engine in c:
                    Config.expand_program_config(file_path, c[engine])

            return c

    def generate_run_dir(self) -> Path:
        """
        Create a temporary run directory under `general.run_base_dir` in config.
        """
        run_base_dir = os.path.expandvars(self["general"]["run_base_dir"])
        Path(run_base_dir).mkdir(parents=True, exist_ok=True)

        temp_string = str(uuid.uuid4())
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        temp_directory = f"{current_datetime}_{temp_string}"
        run_dir = Path(run_base_dir, temp_directory)
        run_dir.mkdir(parents=True, exist_ok=True)
        return run_dir


def expand_path_in_config(path, config_file_path):
    expanded_path = os.path.expandvars(path)
    expanded_path = config_file_path.parent.joinpath(expanded_path).absolute()
    return expanded_path


def load_config_from_env_or_home() -> Optional[Config]:
    """
    Load ``Config`` object from file path set in environment variable ``CONFIG_ENVIRONMENT_VARIABLE_NAME``.
    Or load from ``${HOME}/.config/nwpc-oper/sokort/config.yaml``.
    """
    if CONFIG_ENVIRONMENT_VARIABLE_NAME in os.environ:
        config_path = os.environ[CONFIG_ENVIRONMENT_VARIABLE_NAME]
        logger.debug(f"config file path: {config_path}")
        config = Config.load(config_path)
        return config
    else:
        config_path = Path(Path.home(), ".config", "nwpc-oper", "sokort", "config.yaml")
        if config_path.exists():
            logger.debug(f"config file path: {config_path}")
            config = Config.load(config_path)
            return config
        else:
            return None


nwpc_graphics_config: Config = load_config_from_env_or_home()


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
