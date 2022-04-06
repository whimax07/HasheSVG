import os.path
from typing import Optional

from typing.io import TextIO

from PyVG.Shapes import Shape, BackgroundRectangle


class BuildSVG(object):

    def __init__(self):
        super().__init__()
        self.shapes: list[Shape] = []
        self.background: Optional[Shape] = None
        self.body = ""
        self.image: str = ""


    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)


    def set_background(self, colour: str) -> None:
        self.background = BackgroundRectangle(colour)


    def generate_image(self) -> None:
        self.__combine_shapes()

        base_csv: BaseCSV = BaseCSV()
        self.image = base_csv.wrap_with_img_base(self.body)


    def __combine_shapes(self) -> None:
        if self.background is not None:
            self.body += self.background.generate_shape()

        for shape in self.shapes:
            self.body += shape.generate_shape()


    def write_image_file(self, file_name: str, folder_root: str = "") -> None:
        """Call :func:`generate_image()` before this method."""
        file_path: str = os.path.join(folder_root, file_name)
        file: TextIO  = open(file_path + ".svg", "w")
        file.write(self.image)



class BaseCSV(object):

    def __init__(self):
        super().__init__()
        self.HEIGHT = 256
        self.WIDTH = 256
        self.baseString: str = ""


    def wrap_with_img_base(self, img: str) -> str:
        return self.__make_img_header() + img + self.__make_img_footer()


    def __make_img_header(self) -> str:
        header: str = "<svg " \
                      f"height=\"{self.HEIGHT}\" width=\"{self.WIDTH}\" " \
                      "xmlns=\"http://www.w3.org/2000/svg\">" \
                      "\n"
        return header


    @staticmethod
    def __make_img_footer() -> str:
        return "</svg>"

