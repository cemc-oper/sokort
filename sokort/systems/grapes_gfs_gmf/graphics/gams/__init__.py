import datetime
from pathlib import Path
from typing import Dict, Union, Optional
import os

import pandas as pd

from sokort._logging import get_logger
from sokort.config import Config
from sokort.systems.grapes_gfs_gmf._plotter import SystemNclPlotter
from sokort._util import (
    get_work_dir,
    get_data_path
)


logger = get_logger("grapes_gfs_gmf")


class GamsPlotter(SystemNclPlotter):
    """
    Plotter for component GAMS.
    """
    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemNclPlotter.__init__(self, task, work_dir, config, **kwargs)

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_time: datetime.datetime or pd.Timestamp,
            forecast_time: pd.Timedelta,
            data_directory: Optional[Union[str, Path]] = None,
            work_directory: Optional[Union[str, Path]] = None,
            verbose: Union[bool, int] = False
    ):
        """Create plotter

        Parameters
        ----------
        graphics_config: dict
            graphics config
        start_time: datetime.datetime or pd.Timestamp
            Start hour
        forecast_time: pd.Timedelta
            Forecast time duration, such as 3h.
        data_directory:
        work_directory:
        verbose:

        Returns
        -------
        SystemNclPlotter
        """
        data_path = get_data_path(
            system_name=cls.system_name,
            start_time=start_time,
            forecast_time=forecast_time,
            data_directory=data_directory
        )
        if verbose:
            logger.debug(f"data directory: {data_path}")

        system_config = graphics_config["systems"]["grapes_gfs_gmf"]
        component_config = system_config["components"]["gams"]

        task = {
            "ncl_dir": os.path.expandvars(component_config["ncl_dir"]),
            "script_dir": os.path.expandvars(system_config["system"]["script_dir"]),
            "data_path": data_path,
            "start_datetime": start_time.isoformat(),
            "forecast_time": forecast_time,
        }

        # work dir
        work_dir = get_work_dir(
            graphics_config=graphics_config,
            work_directory=work_directory
        )
        if verbose:
            logger.debug(f"work directory: {work_dir.absolute()}")

        config = {
            "ncl_lib": os.path.expandvars(graphics_config["ncl"]["ncl_lib"]),
            "geodiag_root": os.path.expandvars(graphics_config["ncl"]["geodiag_root"]),
            "load_env_script": graphics_config["ncl"]["load_env_script"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose
        )

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_ncl.sh")
