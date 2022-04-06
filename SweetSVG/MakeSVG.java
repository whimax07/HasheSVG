import shapes.Polygon;

import java.io.File;

public class MakeSVG {

    public static void main(String[] args) {
        BaseSVG baseSVG = new BaseSVG();

        Polygon triangle = new Polygon()
                .add_point(20, 20)
                .add_point(130, 40)
                .add_point(70, 140);

        triangle
                .addStyleAttribute("fill", "blue")
                .addStyleAttribute("stroke", "DarkBlue")
                .addStyleAttribute("stroke-width", "2");

        baseSVG.addElement(triangle);

        baseSVG.writeImage(new File("TestTriangle.svg"));

    }

}
