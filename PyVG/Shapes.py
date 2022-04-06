import abc
from dataclasses import dataclass



@dataclass
class Point:
    x: int
    y: int



class Shape(abc.ABC):

    @abc.abstractmethod
    def generate_shape(self) -> str:
        pass



class Rectangle(Shape):

    def __init__(self) -> None:
        super().__init__()
        self.shape: str = ""
        self.bounds: str = ""
        self.styles: dict[str, str] = {}


    # Note(Max): Could these be kwargs?
    def define_bounds(self, x: int, y:int, width: int, height: int) -> 'Rectangle':
        self.bounds = f"x=\"{x}\" y=\"{y}\" width=\"{width}\" height=\"{height}\""
        return self


    # Note(Max): This is a very naive way of doing this as it doesn't give the user any feed back.
    # It lacks info on what keys can be given and what values they can accept.
    def add_style(self, key: str, value: str) -> 'Rectangle':
        self.styles[key] = value
        return self


    def generate_shape(self) -> str:
        self.shape = ""
        self.shape += self.bounds + " "
        self.__add_styles()
        self.__wrap_with_tag()
        return self.shape


    def __add_styles(self) -> None:
        for key, value in self.styles.items():
            self.shape += key + "=\"" + value + "\" "


    def __wrap_with_tag(self) -> None:
        self.shape = "<rect " + self.shape + "/>\n"



class BackgroundRectangle(Shape):

    def __init__(self, background_colour: str = "Orange"):
        super().__init__()
        self.background_colour = background_colour


    def set_background(self, colour: str):
        self.background_colour = colour


    def generate_shape(self) -> str:
        return f"<rect width=\"100%\" height=\"100%\" fill=\"{self.background_colour}\" />\n"



class Polygon(Shape):

    def __init__(self) -> None:
        super().__init__()
        self.shape: str = ""
        self.points: list[tuple[int, int]] = []
        self.styles: dict[str, str] = {}


    def add_point(self, x: int, y: int) -> 'Polygon':
        self.points.append((x, y))
        return self


    def add_style(self, key: str, value: str) -> 'Polygon':
        self.styles[key] = value
        return self


    def generate_shape(self) -> str:
        self.__build_points()
        self.__build_styles()
        self.__wrap_shape()
        return self.shape


    def __build_points(self) -> None:
        for point in self.points:
            self.shape += f"{point[0]},{point[1]}" + " "
        self.shape = self.shape.removesuffix(" ")
        self.shape = "points=\"" + self.shape + "\"" + " "


    def __build_styles(self):
        for key, value in self.styles.items():
            self.shape += key + "=\"" + value + "\"" + " "


    def __wrap_shape(self) -> None:
        self.shape = "<polygon " + self.shape + "/>\n"



class Triangle(Polygon):

    def __init__(self) -> None:
        super().__init__()


    def define_shape_points(self, point_a: Point, point_b: Point, point_c: Point) -> 'Triangle':
        self.points.append((point_a.x, point_a.y))
        self.points.append((point_b.x, point_b.y))
        self.points.append((point_c.x, point_c.y))
        return self


    def define_shape_tuples(
            self, point_a: tuple[int, int], point_b: tuple[int, int], point_c: tuple[int, int]
    ) -> 'Triangle':
        self.points.append(point_a)
        self.points.append(point_b)
        self.points.append(point_c)
        return self


