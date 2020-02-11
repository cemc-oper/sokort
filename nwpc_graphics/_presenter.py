
class Presenter(object):
    def __init__(self):
        pass

    def show_plot(self, images: list):
        pass


class IPythonPresenter(Presenter):
    def __init__(self):
        super(IPythonPresenter).__init__()

    def show_plot(self, images: list):
        from IPython.display import Image, display
        for an_image in images:
            display(Image(filename=f"./{an_image['path']}"))


class PILPresenter(Presenter):
    def __init__(self):
        super(PILPresenter).__init__()

    def show_plot(self, images: list):
        from PIL import Image
        for an_image in images:
            image = Image.open(f"./{an_image['path']}")
            image.show()
