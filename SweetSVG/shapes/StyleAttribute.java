package shapes;

public record StyleAttribute(String key, String value) {

    public String toCss() {
        return key + ":" + value;
    }

}
