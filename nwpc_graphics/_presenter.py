import ipywidgets as widgets
from IPython.display import Image, display
from PIL import Image as PILImage


class Presenter(object):
    def __init__(self):
        pass

    def show_plot(self, images: list):
        pass


class IPythonPresenter(Presenter):
    def __init__(self):
        super(IPythonPresenter).__init__()

    def show_plot(self, images: list):
        for an_image in images:
            display(Image(filename=f"./{an_image['path']}"))


class JupyterWidgetsPresenter(Presenter):
    def __init__(self, out: widgets.Output):
        super(JupyterWidgetsPresenter).__init__()
        self.out = out

    def show_plot(self, images: list):
        for an_image in images:
            self.out.append_display_data(Image(filename=f"./{an_image['path']}"))


class PILPresenter(Presenter):
    def __init__(self):
        super(PILPresenter).__init__()

    def show_plot(self, images: list):
        for an_image in images:
            image = PILImage.open(f"./{an_image['path']}")
            image.show()
