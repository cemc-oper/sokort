from pathlib import Path
import os

import yaml


CONFIG_ENVIRONMENT_VARIABLE_NAME = "NWPC_GRAPHICS_CONFIG"


class Config(dict):
    def __init__(self, config_file_path: Path = None, **kwargs):
        super(Config).__init__(**kwargs)
        self["ncl"] = dict()
        self["systems"] = dict()
        self.config_file_path = config_file_path

    @classmethod
    def load(cls, config_file: str or Path):
        with open(config_file) as f:
            config_dict = yaml.safe_load(f)
            config = Config(config_file_path=Path(config_file))
            config["ncl"] = config_dict["ncl"]
            config.load_systems()
            return config

    def load_systems(self):
        systems_path = self.config_file_path.parent.joinpath("systems")
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


def load_config_from_env():
    if CONFIG_ENVIRONMENT_VARIABLE_NAME in os.environ:
        config = Config.load(os.environ[CONFIG_ENVIRONMENT_VARIABLE_NAME])
        return config
    return None
