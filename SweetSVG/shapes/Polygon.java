package shapes;

import java.util.ArrayList;

public class Polygon extends AbstractShape {

    private ArrayList<PointI> points = new ArrayList<>();

    private ArrayList<StyleAttribute> styleAttributes = new ArrayList<>();



    public Polygon add_point(int x, int y) {
        points.add(new PointI(x, y));
        return this;
    }

    public Polygon addStyleAttribute(String key, String value) {
        styleAttributes.add(new StyleAttribute(key, value));
        return this;
    }



    private String point2String(PointI pointI) {
        return pointI.getX() + "," + pointI.getY();
    }

    @Override
    public String toSvg() {
        StringBuilder stringBuilder = new StringBuilder("<polygon points=\"");
        for (PointI point : points) {
            stringBuilder.append(point2String(point)).append(" ");
        }

        stringBuilder.append("\" style=\"");
        for (StyleAttribute styleAttribute : styleAttributes) {
            stringBuilder.append(styleAttribute.toCss()).append(";");
        }

        stringBuilder.append("\" />");
        return stringBuilder.toString();
    }

}
