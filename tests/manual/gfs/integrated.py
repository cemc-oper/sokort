import datetime
from nwpc_graphics.systems.grapes_gfs_gmf import show_plot


def run():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    start_time = yesterday.strftime("%Y%m%d")
    start_hour = "00"
    forecast_time = "24h"
    plot_type = "pwat_sfc_an_aea"

    show_plot(plot_type, start_time, start_hour, forecast_time)


if __name__ == "__main__":
    run()
