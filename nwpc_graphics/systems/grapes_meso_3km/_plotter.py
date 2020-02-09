from pathlib import Path
import os
import shutil
import datetime

from nwpc_graphics._plotter import BasePlotter
from nwpc_graphics._config import Config


class SystemPlotter(BasePlotter):
    """
    System plotter for GRAPES MESO 3KM
    """
    plot_types = None

    def __init__(self, task: dict, work_dir: str, config: dict):
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
        """
        BasePlotter.__init__(
            self,
            task=task,
            work_dir=work_dir,
            config=config,
        )

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_date: str,
            start_time: str,
            forecast_time: str):
        """Create plotter

        Parameters
        ----------
        graphics_config: Config
            graphics config
        start_date: str
            Start date, YYYYMMDD
        start_time: str
            Start hour, HH
        forecast_time: str
            Forecast time duration, such as 3h.

        Returns
        -------
        SystemPlotter
        """
        start_datetime = datetime.datetime.strptime(f"{start_date}{start_time}", "%Y%m%d%H")
        start_time = start_datetime.strftime("%Y%m%d%H")

        system_config = graphics_config["systems"]["grapes_meso_3km"]
        task = {
            "script_dir": system_config["system"]["script_dir"],
            "data_path": system_config["data"]["data_path"].format(
                start_time=start_time
            ),
            "start_datetime": start_datetime.isoformat(),
            "forecast_time": forecast_time,
        }
        work_dir = graphics_config.generate_run_dir()
        config = {
            "ncl_lib": graphics_config["ncl"]["ncl_lib"],
            "geodiag_root": graphics_config["ncl"]["geodiag_root"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config
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

        shutil.copy2(f"{script_dir}/ps2gif_NoRotation_NoPlot.scr", "ps2gif_NoRotation_NoPlot.src")
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
