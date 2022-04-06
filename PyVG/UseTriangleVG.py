from PyVG.HashFileTriangles import *


def make_all_none():
    make_triangle_hash()


def yellow_fg_blue_bg():
    make_triangle_hash(foreground_colours=YELLOWS, background_colour="rgb(25,25,80)")


def blue_fg_yellow_bg():
    # make_triangle_hash(foreground_colours=BLUES, background_colour="Orange")
    # make_triangle_hash(foreground_colours=BLUES, background_colour="Khaki") # Good.
    make_triangle_hash(foreground_colours=BLUES, background_colour="LemonChiffon")


def green_fg_grey_bg():
    make_triangle_hash(foreground_colours=GREENS, background_colour="Gray")



def main():
    make_all_none()


if __name__ == '__main__':
    main()
