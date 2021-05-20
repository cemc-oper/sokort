from pathlib import Path
import os
import shutil
import datetime

import pandas as pd

from nwpc_data.data_finder import find_local_file

from sokort._plotter import BasePlotter
from sokort._config import Config


class SystemPlotter(BasePlotter):
    """
    System plotter for GRAPES GFS GMF.
    """
    plot_types = None

    def __init__(self, task: dict, work_dir: str, config: dict):
        """
        Parameters
        ----------
        task: dict
            task config dict
            {
                "ncl_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
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
        """
        BasePlotter.__init__(
            self,
            task=task,
            work_dir=work_dir,
            config=config,
        )

        # magic options
        self.forecast_time_interval = 12
        self.forecast_data_format = "grib2"
        self.forecast_data_center = "ecmwf"

        self.min_forecast_time = self.forecast_hour
        self.max_forecast_time = self.forecast_hour

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_time: datetime.datetime or pd.Timestamp,
            forecast_time: pd.Timedelta):
        """Create plotter

        Parameters
        ----------
        graphics_config: Config
            graphics config
        start_time: datetime.datetime or pd.Timestamp,
        forecast_time: pd.Timedelta
            Forecast time duration, such as 3h.

        Returns
        -------
        SystemPlotter
        """
        system_config = graphics_config["systems"]["grapes_gfs_gmf"]

        data_file = find_local_file(
            "grapes_gfs_gmf/grib2/orig",
            start_time=start_time,
            forecast_time=forecast_time,
        )
        data_path = str(data_file.parent) + "/"

        task = {
            "ncl_dir": system_config["system"]["ncl_dir"],
            "script_dir": system_config["system"]["script_dir"],
            "data_path": data_path,
            "start_datetime": start_time.isoformat(),
            "forecast_time": forecast_time,
        }

        work_dir = graphics_config.generate_run_dir()

        config = {
            "ncl_lib": graphics_config["ncl"]["ncl_lib"],
            "geodiag_root": graphics_config["ncl"]["geodiag_root"],
            "load_env_script": graphics_config["ncl"]["load_env_script"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
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

        with open("grapes_meso_date", "w") as f:
            f.write(f"{self.start_time}{self.forecast_hour}\n")
            f.write(f"{self.forecast_time}")

        shutil.copy2(f"{script_dir}/ps2gif_NoRotation_NoPlot.scr", "ps2gif_NoRotation_NoPlot.src")
        shutil.copy2(f"{ncl_dir}/{ncl_script_name}", f"{ncl_script_name}")

        shutil.copy2(f"{str(self.run_script_path)}", self.run_script_path.name)
        shutil.copy2(f"{str(self.load_env_script_path)}", self.load_env_script_path.name)

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
