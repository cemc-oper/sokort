import datetime
from nwpc_graphics.systems.grapes_meso_3km import draw_plot


def run():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    start_time = yesterday.strftime("%Y%m%d")
    start_hour = "00"
    forecast_time = "12h"
    # plot_type = "meso_3km.prep_3h_10mw"
    plot_type = "cn_500height_850wind"

    draw_plot(plot_type, start_time + start_hour, forecast_time)


if __name__ == "__main__":
    run()
