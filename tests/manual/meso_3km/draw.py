import datetime
import pandas as pd
from sokort.systems.cma_meso import draw_plot


def run():
    day = pd.to_datetime("2021-05-14 00:00:00")
    start_time = day.strftime("%Y%m%d")
    start_hour = "00"
    forecast_time = "12h"
    # plot_type = "meso_3km.prep_3h_10mw"
    plot_type = "cn_radar_reflectivity"

    draw_plot(plot_type, start_time + start_hour, forecast_time)


if __name__ == "__main__":
    run()
