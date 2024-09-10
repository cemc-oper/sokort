import datetime
from pathlib import Path
from typing import Dict, Union, Optional
import os
import shutil

import pandas as pd

from sokort._logging import get_logger
from sokort.config import Config
from sokort.systems.cma_gfs._plotter import SystemNclPlotter
from sokort.util import (
    get_work_dir,
    get_data_path
)


logger = get_logger("cma_gfs")


class SwfdpPlotter(SystemNclPlotter):
    """
    Plotter for component SWFDP.
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

        system_config = graphics_config["systems"]["cma_gfs"]
        component_config = system_config["components"]["swfdp"]

        task = {
            "ncl_dir": os.path.expandvars(component_config["ncl_dir"]),
            "script_dir": os.path.expandvars(component_config["ncl_dir"]),
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
            "ncl_lib": os.path.expandvars(component_config["ncl_lib"]),
            "geodiag_root": os.path.expandvars(graphics_config["ncl"]["geodiag_root"]),
            "load_env_script": graphics_config["ncl"]["load_env_script"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose
        )

    def _prepare_environment(self):
        ncl_script_name = self.ncl_script_name  # "GFS_GRAPES_PWAT_SFC_AN_AEA.ncl"

        script_dir = self.task["script_dir"]
        # str /home/wangdp/project/graph/operation/NWP_GRAPES_MESO_3KM_POST/tograph/script/

        # create environment
        Path(self.work_dir).mkdir(parents=True, exist_ok=True)
        os.chdir(self.work_dir)

        with open("grapes_date", "w") as f:
            f.write(f"{self.start_time}{self.forecast_hour}\n")
            f.write(f"{self.forecast_time}")

        # shutil.copy2(f"{script_dir}/ps2gif_NoRotation_NoPlot.scr", "ps2gif_NoRotation_NoPlot.src")
        shutil.copy2(f"{script_dir}/{ncl_script_name}", f"{ncl_script_name}")

        component_directory = Path(__file__).parent
        run_ncl_script_path = Path(component_directory, self.run_script_name)
        shutil.copy2(f"{str(run_ncl_script_path)}", self.run_script_name)
        shutil.copy2(f"{str(self.load_env_script_path)}", self.load_env_script_path.name)

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_ncl.sh")
