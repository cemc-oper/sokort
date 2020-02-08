import datetime
import tempfile
from pathlib import Path
import shutil
import os

from nwpc_graphics.systems.grapes_gfs_gmf._plotter import SystemPlotter


class GamsPlotter(SystemPlotter):
    def __init__(self, task: dict, work_dir: str, config: dict):
        SystemPlotter.__init__(self, task, work_dir, config)

    @classmethod
    def create_plotter(
            cls,
            graphics_config: dict,
            start_date: str,
            start_time: str,
            forecast_time: str):
        """Create plotter

        Parameters
        ----------
        graphics_config: dict
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
        start_datetime_4dvar = start_datetime - datetime.timedelta(hours=3)
        start_time_4dvar = start_datetime_4dvar.strftime("%Y%m%d%H")

        system_config = graphics_config["systems"]["grapes_gfs_gmf"]
        component_config = system_config["components"]["gams"]

        task = {
            "ncl_dir": component_config["ncl_dir"],
            "script_dir": system_config["system"]["script_dir"],
            "data_path": system_config["data"]["data_path"].format(
                start_time_4dvar=start_time_4dvar
            ),
            "start_datetime": start_datetime.isoformat(),
            "forecast_time": forecast_time,
        }

        work_dir = tempfile.mkdtemp()

        config = {
            "ncl_lib": graphics_config["ncl"]["ncl_lib"],
            "geodiag_root": graphics_config["ncl"]["geodiag_root"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
        )

    def _prepare_environment(self):
        # TODO: modify
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

        component_directory = Path(__file__).parent
        run_ncl_script_path = Path(component_directory, self.run_script_name)
        shutil.copy2(f"{str(run_ncl_script_path)}", self.run_script_name)
        shutil.copy2(f"{str(self.load_env_script_path)}", self.load_env_script_path.name)

    def _generate_environ(self):
        envs = SystemPlotter._generate_environ(self)
        envs.update({
            "output_path": "./"
        })
