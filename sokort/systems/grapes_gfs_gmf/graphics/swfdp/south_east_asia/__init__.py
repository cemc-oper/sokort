import datetime
from pathlib import Path
from typing import Dict, Union, Optional
import os
import shutil

import pandas as pd

from sokort._logging import get_logger
from sokort.config import Config
from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort._util import (
    get_work_dir,
    get_data_path
)


logger = get_logger("grapes_gfs_gmf")


class SwfdpSeaPlotter(SwfdpPlotter):
    """
    Plotter for component SWFDP/SEA.
    """
    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SwfdpPlotter, self).__init__(task, work_dir, config, **kwargs)

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

        # component_directory = Path(__file__).parent
        # run_ncl_script_path = Path(component_directory, self.run_script_name)
        run_ncl_script_path = self._get_run_script()
        shutil.copy2(f"{str(run_ncl_script_path)}", self.run_script_name)
        shutil.copy2(f"{str(self.load_env_script_path)}", self.load_env_script_path.name)
