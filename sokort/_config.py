from pathlib import Path
from typing import Optional, Union, Dict
import os
import datetime
import uuid

import yaml

from sokort._logging import get_logger
logger = get_logger()


CONFIG_ENVIRONMENT_VARIABLE_NAME = "NWPC_GRAPHICS_CONFIG"


class Config(dict):
    def __init__(self, config_file_path: Path = None, **kwargs):
        super(Config).__init__(**kwargs)
        self["ncl"] = dict()
        self["config"] = dict()
        self["systems"] = dict()
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
            self._expand_ncl_config(self["ncl"])

    def _expand_ncl_config(self, ncl_config: Dict):
        if "load_env_script" not in ncl_config:
            return ncl_config
        load_env_script = ncl_config["load_env_script"]
        if len(load_env_script) == 0:
            return ncl_config

        ncl_config["load_env_script"] = self.config_file_path.parent.joinpath(load_env_script).absolute()
        return ncl_config

    def _load_systems(self):
        systems_path = self.config_file_path.parent.joinpath(self["config"]["systems_dir"])
        if not systems_path.exists():
            raise FileNotFoundError(f"systems directory is not found.")

        for item in systems_path.iterdir():
            if item.is_dir():
                continue
            if item.suffix != ".yaml":
                continue
            with open(item) as f:
                c = yaml.safe_load(f)
                self["systems"][item.stem] = c

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


def load_config_from_env_or_home() -> Optional[Config]:
    """
    Load ``Config`` object from file path set in environment variable ``CONFIG_ENVIRONMENT_VARIABLE_NAME``.
    Or load from ``${HOME}/.config/nwpc-oper/sokort/config.yaml``.
    """
    if CONFIG_ENVIRONMENT_VARIABLE_NAME in os.environ:
        config = Config.load(os.environ[CONFIG_ENVIRONMENT_VARIABLE_NAME])
        return config
    else:
        home_config = Path(Path.home(), ".config", "nwpc-oper", "sokort", "config.yaml")
        logger.info(f"config file path: {home_config}")
        if home_config.exists():
            config = Config.load(home_config)
            return config
        else:
            return None
