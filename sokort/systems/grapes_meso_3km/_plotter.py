from pathlib import Path
from typing import Dict, Union, Optional
import os
import shutil
import datetime

import pandas as pd

from sokort._plotter import NclPlotter
from sokort.config import Config
from sokort._logging import get_logger
from sokort._util import (
    get_work_dir,
    get_data_path
)


logger = get_logger("grapes_meso_3km")


class SystemPlotter(NclPlotter):
    """
    System plotter for GRAPES MESO 3KM
    """
    plot_types = None
    system_name = "grapes_meso_3km"

    def __init__(
            self,
            task: Dict,
            work_dir: str,
            config: Dict,
            verbose: Union[bool, int] = False
    ):
        """
        Parameters
        ----------
        task: dict
            task config dict
            {
                "script_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
                "data_path": "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/",
                "start_datetime": datetime.datetime(2020, 1, 11, 0).isoformat(),
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
        verbose:
            print setting
        """
        NclPlotter.__init__(
            self,
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose,
        )

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_time: Union[datetime.datetime, pd.Timestamp],
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
        data_directory
        work_directory
        verbose

        Returns
        -------
        SystemPlotter
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

        script_dir = os.path.expandvars(system_config["system"]["script_dir"])
        task = {
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

        script_dir = self.task["script_dir"]
        # str /home/wangdp/project/graph/operation/NWP_GRAPES_MESO_3KM_POST/tograph/script/

        # create environment
        Path(self.work_dir).mkdir(parents=True, exist_ok=True)
        os.chdir(self.work_dir)

        with open("grapes_meso_date", "w") as f:
            f.write(f"{self.start_time}{self.forecast_hour}\n")
            f.write(f"{self.forecast_time}")

        # shutil.copy2(f"{script_dir}/ps2gif_NoRotation_NoPlot.scr", "ps2gif_NoRotation_NoPlot.src")
        shutil.copy2(f"{script_dir}/{ncl_script_name}", f"{ncl_script_name}")

        component_directory = Path(__file__).parent
        run_ncl_script_path = Path(component_directory, self.run_script_name)
        shutil.copy2(f"{str(run_ncl_script_path)}", self.run_script_name)
        shutil.copy2(f"{str(self.load_env_script_path)}", self.load_env_script_path.name)

    def _generate_environ(self):
        ncl_script_name = self.ncl_script_name

        script_dir = self.task["script_dir"]

        geodiag_root = self.config["geodiag_root"]  # "/home/wangdp/project/graph/GEODIAG"
        geodiag_tools = str(Path(geodiag_root, "tools"))

        data_path = self.task["data_path"]
        # str "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/"

        envs = os.environ
        envs.update({
            "GEODIAG_ROOT": geodiag_root,
            "GEODIAG_TOOLS": geodiag_tools,
            "start_time": self.start_time,
            "data_path": data_path,
            "script_dir": script_dir,
            "ncl_script_name": ncl_script_name,
        })
        return envs

    @classmethod
    def _get_run_script(cls):
        return Path(Path(__file__).parent, "run_ncl.sh")


AREA_LIST = [
    {
        "name": "east_china",
        "image_path_name": "EastChina"
    },
    {
        "name": "east_north_west",
        "image_path_name": "East_NorthWest"
    },
    {
        "name": "east_south_west",
        "image_path_name": "East_SouthWest"
    },
    {
        "name": "north_china",
        "image_path_name": "NorthChina"
    },
    {
        "name": "north_east",
        "image_path_name": "NorthEast"
    },
    {
        "name": "south_china",
        "image_path_name": "SouthChina"
    },
    {
        "name": "xi_zang",
        "image_path_name": "XiZang"
    },
    {
        "name": "xin_jiang",
        "image_path_name": "XinJiang"
    },
    {
        "name": "central_china",
        "image_path_name": "CentralChina"
    },
]
