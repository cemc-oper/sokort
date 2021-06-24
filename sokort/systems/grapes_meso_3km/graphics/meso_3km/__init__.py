from pathlib import Path
import datetime
from typing import Union, Optional

import pandas as pd

from sokort.systems.grapes_meso_3km._plotter import SystemPlotter
from sokort.config import Config
from sokort._logging import get_logger
from sokort._util import (
    get_work_dir,
    get_data_path
)


logger = get_logger("grapes_meso_3km.meso_3km")


class Meso3kmPlotter(SystemPlotter):
    """
    """
    plot_types = None

    def __init__(
            self,
            task: dict,
            work_dir: str,
            config: dict,
            verbose: Union[bool, int] = False
    ):
        SystemPlotter.__init__(
            self,
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose
        )

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
        graphics_config: Config
            graphics config
        start_time: datetime.datetime or pd.Timestamp
        forecast_time: pd.Timedelta
            Forecast time duration, such as 3h.

        Returns
        -------
        SystemPlotter
        """
        system_config = graphics_config["systems"]["grapes_meso_3km"]
        component_config = system_config["components"]["meso_3km"]

        data_path = get_data_path(
            system_name=cls.system_name,
            start_time=start_time,
            forecast_time=forecast_time,
            data_directory=data_directory
        )
        if verbose:
            logger.debug(f"data directory: {data_path}")

        task = {
            "script_dir": component_config["system"]["script_dir"],
            "data_path": data_path,
            "start_datetime": start_time.isoformat(),
            "forecast_time": forecast_time,
        }

        work_dir = get_work_dir(
            graphics_config=graphics_config,
            work_directory=work_directory
        )
        if verbose:
            logger.debug(f"work directory: {work_dir.absolute()}")

        config = {
            "ncl_lib": graphics_config["ncl"]["ncl_lib"],
            "geodiag_root": graphics_config["ncl"]["geodiag_root"],
            "load_env_script": graphics_config["ncl"]["load_env_script"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose
        )
