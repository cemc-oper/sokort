import datetime

import ipywidgets as widgets
from IPython.display import display

from sokort.systems import (
    grapes_meso_3km,
    grapes_gfs_gmf,
)
from sokort._presenter import JupyterWidgetsPresenter
from sokort._util import fix_system_name

system_mapper = {
    "grapes_gfs_gmf": {
        "module": grapes_gfs_gmf,
        "start_hours": ['00', '06', '12', "18"],
    },
    "grapes_meso_3km": {
        "module": grapes_meso_3km,
        "start_hours": ['00', '03', '06', '09', '12', '15', "18", '21'],
    }
}


def interactive_ui(system):
    system = fix_system_name(system)
    system_module = system_mapper[system]["module"]

    plotters = system_module.plotters

    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)

    start_date_option = widgets.DatePicker(
        description='Start Date:',
        value=yesterday,
        disabled=False
    )

    start_hour_option = widgets.Dropdown(
        options=system_mapper[system]["start_hours"],
        value='00',
        description='Start Hour:',
        disabled=False,
    )

    forecast_time_option = widgets.Text(
        value="24h",
        description="Forecast Time:",
        disabled=False,
    )

    plot_type_options = widgets.Dropdown(
        options=list(plotters.keys()),
        value=list(plotters.keys())[0],
        description="Plot Type:",
        disabled=False,
    )

    out = widgets.Output()

    button = widgets.Button(
        description='Plot',
        disabled=False,
        button_style='',  # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Plot the image',
        icon='',  # (FontAwesome names without the `fa-` prefix)
    )

    @out.capture()
    def plot(event):
        out.clear_output()
        start_date = start_date_option.value

        system_module.show_plot(
            plot_type_options.value,
            start_time=f'{start_date.strftime("%Y%m%d")}{start_hour_option.value}',
            forecast_time=forecast_time_option.value,
            presenter=JupyterWidgetsPresenter(),
        )

    button.on_click(plot)

    layout = widgets.VBox([
        widgets.HBox([
            widgets.VBox([
                start_date_option,
                start_hour_option,
                forecast_time_option,
            ]),
            widgets.VBox(
                [
                    plot_type_options,
                    widgets.HBox(
                        [
                            button,
                        ],
                        layout=widgets.Layout(
                            justify_content="flex-end"
                        )
                    )
                ],
                layout=widgets.Layout(
                    justify_content="space-between"
                )
            )
        ]),
        out,
    ])

    display(layout)
