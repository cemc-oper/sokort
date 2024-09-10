import datetime
from sokort.systems.cma_gfs import show_plot


def run():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    start_time = yesterday.strftime("%Y%m%d")
    start_hour = "00"
    forecast_time = "24h"
    plot_type = "gams.div_250"

    show_plot(plot_type, start_time, start_hour, forecast_time)


if __name__ == "__main__":
    run()
