from PyVG.BuildSVG import BuildSVG
from PyVG.Shapes import Rectangle, Triangle


def main():
    img_builder: BuildSVG = BuildSVG()

    rect: Rectangle = Rectangle().define_bounds(10, 10, 100, 100)

    rect.add_style("stroke", "DarkSlateBlue")  \
        .add_style("stroke-width", "2") \
        .add_style("fill", "DarkMagenta")

    img_builder.add_shape(rect)


    triangle: Triangle = Triangle().define_shape_tuples((10, 110), (110, 110), (10, 170))

    triangle.add_style("stroke", "DarkSlateBlue")  \
        .add_style("stroke-width", "2")  \
        .add_style("fill", "DarkSlateBlue")

    img_builder.add_shape(triangle)

    img_builder.generate_image()
    img_builder.write_image_file("TestVG")



if __name__ == '__main__':
    main()

