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
    def __init__(self, out: widgets.Output = widgets.Output()):
        super(JupyterWidgetsPresenter).__init__()
        self.out = out

    def show_plot(self, images: list):
        children = []
        titles = []
        for index, an_image in enumerate(images):
            file = open(f"./{an_image['path']}", "rb")
            image = file.read()
            image_widget = widgets.Image(
                value=image,
                format='png',
            )
            children.append(image_widget)
            if "name" in an_image:
                titles.append(an_image["name"])
            else:
                titles.append(str(index))
        tab = widgets.Tab()
        tab.children = children
        for index, title in enumerate(titles):
            tab.set_title(index, title)
        display(tab)


class PILPresenter(Presenter):
    def __init__(self):
        super(PILPresenter).__init__()

    def show_plot(self, images: list):
        for an_image in images:
            image = PILImage.open(f"./{an_image['path']}")
            image.show()
