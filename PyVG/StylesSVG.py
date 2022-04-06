import abc
from abc import ABC
from dataclasses import dataclass


@dataclass
class Styles:
    stroke: str = "stroke"
    stroke_width: str = "stroke-width"
    fill: str = "fill"
    pattern: str = "pattern"



########################################################################################################################
############# Attempt 1: Keyword arguments. ############################################################################
########################################################################################################################
class RectangleStyles(object):

    def __init__(self):
        super().__init__()
        self.style_map: dict[str, str] = {}

    def add_style(self, stroke: str = "green", stroke_width: int = 2, fill: str = "darkgreen"):
        self.style_map["stroke"] = stroke
        self.style_map["stroke-width"] = str(stroke_width)
        self.style_map["fill"] = fill



########################################################################################################################
############## Attempt 2: Using an abstract base class. ################################################################
########################################################################################################################
class Style(ABC):

    @abc.abstractmethod
    def get_style(self) -> str:
        pass



class Fill(Style):

    def __init__(self) -> None:
        super().__init__()
        self.value: str = ""
        """Sets the fill colour of the shape. Use colour name or rgb triplet."""


    def get_style(self) -> str:
        return f"fill={self.value}"



class Stoke(Style):

    def __init__(self):
        super().__init__()
        self.value: str = ""
        """Sets the colour of the Stoke. Use colour name or rgb triplet."""


    def get_style(self) -> str:
        return f"stoke={self.value}"



# TODO(Max): You can use a property for self.value to add the greater than or equal to zero validation.
class StrokeWidth(Style):

    def __init__(self):
        super().__init__()
        self.value: int = 2
        """Sets the Stroke Width. Use an int greater than or equal to 0."""


    def get_style(self) -> str:
        return f"stroke-width={self.value}"

