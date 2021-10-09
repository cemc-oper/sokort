from pathlib import Path
import os
import shutil
import datetime
from typing import Dict, Union, Optional

import pandas as pd

from sokort._plotter import NclPlotter
from sokort.config import Config
from sokort._logging import get_logger
from sokort._util import (
    get_work_dir,
    get_data_path
)

logger = get_logger("grapes_gfs_gmf")


class SystemNclPlotter(NclPlotter):
    """
    System plotter for GRAPES GFS GMF.
    """
    plot_types = None
    system_name = "grapes_gfs_gmf"

    def __init__(
            self,
            task: Dict,
            work_dir: Union[str, Path],
            config: Dict,
            verbose: Union[bool, int] = False
    ):
        """
        Parameters
        ----------
        task: dict
            task config dict
            {
                "ncl_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
                "script_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
                "data_path": "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/",
                "start_datetime": "2021-06-23 00:00:00",
                "forecast_time": "3h",
            }
        work_dir: str
            work directory
        config: dict
            service config
            {
                "ncl_lib": "/home/wangdp/project/graph/ncllib",
                "geodiag_root": "/home/wangdp/project/graph/GEODIAG",
            }
        """
        NclPlotter.__init__(
            self,
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose
        )

        # magic options
        self.forecast_time_interval = 12
        self.forecast_data_format = "grib2"
        self.forecast_data_center = "ecmwf"

        if self.forecast_hour is not None:
            self.min_forecast_time = self.forecast_hour
            self.max_forecast_time = self.forecast_hour
        else:
            self.min_forecast_time = None
            self.max_forecast_time = None

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_time: Union[datetime.datetime, pd.Timestamp],
            forecast_time: pd.Timedelta = None,
            data_directory: Optional[Union[str, Path]] = None,
            work_directory: Optional[Union[str, Path]] = None,
            verbose: Union[bool, int] = False
    ):
        """Create plotter

        Parameters
        ----------
        graphics_config
            graphics config
        start_time
        forecast_time
            Forecast time duration, such as 3h.
        data_directory
            data directory for whole cycle.
        work_directory
            work directory to run plot script.
        verbose
            logger setting

        Returns
        -------
        SystemNclPlotter
        """
        system_config = graphics_config["systems"][cls.system_name]

        data_path = get_data_path(
            system_name=cls.system_name,
            start_time=start_time,
            forecast_time=forecast_time,
            data_directory=data_directory
        )
        if verbose:
            logger.debug(f"data directory: {data_path}")

        # task

        ncl_dir = os.path.expandvars(system_config["system"]["ncl_dir"])
        script_dir = os.path.expandvars(system_config["system"]["script_dir"])
        task = {
            "ncl_dir": ncl_dir,
            "script_dir": script_dir,
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

        # config settings

        ncl_lib_dir = os.path.expandvars(graphics_config["ncl"]["ncl_lib"])
        geodiag_root = os.path.expandvars(graphics_config["ncl"]["geodiag_root"])
        config = {
            "ncl_lib": ncl_lib_dir,
            "geodiag_root": geodiag_root,
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

        ncl_dir = self.task["ncl_dir"]
        # str, "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script"

        script_dir = self.task["script_dir"]
        # str "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script"

        # create environment
        Path(self.work_dir).mkdir(parents=True, exist_ok=True)
        os.chdir(self.work_dir)

        # shutil.copy2(f"{script_dir}/ps2gif_NoRotation_NoPlot.scr", "ps2gif_NoRotation_NoPlot.src")
        try:
            shutil.copy2(f"{ncl_dir}/{ncl_script_name}", f"{ncl_script_name}")
        except shutil.SameFileError:
            pass

        try:
            shutil.copy2(f"{str(self.run_script_path)}", self.run_script_path.name)
        except shutil.SameFileError:
            pass

        try:
            shutil.copy2(f"{str(self.load_env_script_path)}", self.load_env_script_path.name)
        except shutil.SameFileError:
            pass

    def _generate_environ(self):
        ncl_script_name = self.ncl_script_name  # "GFS_GRAPES_PWAT_SFC_AN_AEA.ncl"

        ncl_lib = self.config["ncl_lib"]  # "/home/wangdp/project/graph/ncllib"
        graphic_product_lib_root = ncl_lib

        geodiag_root = self.config["geodiag_root"]  # "/home/wangdp/project/graph/GEODIAG"
        geodiag_tools = str(Path(geodiag_root, "tools"))

        data_path = self.task["data_path"]
        # str "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/"

        envs = os.environ
        envs.update({
            "GEODIAG_ROOT": geodiag_root,
            "GEODIAG_TOOLS": geodiag_tools,
            "GRAPHIC_PRODUCT_LIB_ROOT": graphic_product_lib_root,
            "GRAPHIC_PRODUCT_SCRIPT_ROOT": graphic_product_lib_root,
            "FORECAST_DATA_FORMAT": self.forecast_data_format,
            "FORECAST_DATA_CENTER": self.forecast_data_center,
            "start_time": self.start_time,
            "min_forecast_time": self.min_forecast_time,
            "max_forecast_time": self.max_forecast_time,
            "forecast_time_interval": f"{self.forecast_time_interval}",
            "data_path": data_path,
            "ncl_script_name": ncl_script_name,
        })
        return envs

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_ncl.sh")
