package shapes;

public class PointI extends AbstractPoint {

    private final int x;

    private final int y;



    public PointI(int x, int y) {
        this.x = x;
        this.y = y;
    }



    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
