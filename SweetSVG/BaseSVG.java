import shapes.Polygon;
import shapes.AbstractShape;

import java.io.*;
import java.util.ArrayList;

public class BaseSVG {

    private final ArrayList<AbstractShape> shapes = new ArrayList<>();

    private static final int IMG_HEIGHT = 200;

    private static final int IMG_WIDTH = 200;



    public void addElement(Polygon polygon) {
        shapes.add(polygon);
    }



    public void writeImage(File outputFile) {
        try (BufferedWriter outputStream = new BufferedWriter(new FileWriter(outputFile))) {
            outputStream.write(combineImage());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private String combineImage() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(String.format("<svg height=\"%s\" width=\"%s\" xmlns=\"http://www.w3.org/2000/svg\">",
                IMG_HEIGHT, IMG_WIDTH)).append("\n");
        for (AbstractShape shape : shapes) {
            stringBuilder.append(shape.toSvg()).append("\n");
        }

        stringBuilder.append("</svg>");
        return stringBuilder.toString();
    }

}
