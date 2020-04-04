package designpattern.structural.bridge;

class Color {

    private String color;

    public Color(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return color;
    }
}

class Red extends Color {
    public Red() {
        super("Red");
    }
}

class Blue extends Color {
    public Blue() {
        super("Blue");
    }
}

class Shape {

    protected Color color;

    public Shape(Color color) {
        this.color = color;
    }
}

class Square extends Shape{

    public Square(Color color) {
        super(color);
    }

    public String toString() {
        return "I am " + color + " square";
    }
}

class Circle extends Shape {

    public Circle(Color color) {
        super(color);
    }

    public String toString() {
        return "I am " + color + " circle";
    }
}

public class Bridge {

    public static void main(String[] args) {
        System.out.println("Create different types of shapes with different colors.");
        Shape redSquare = new Square(new Red());
        Shape blueSquare = new Square(new Blue());
        Shape redCircle = new Circle(new Red());
        Shape blueCircle = new Circle(new Blue());
        System.out.println(redSquare);
        System.out.println(blueSquare);
        System.out.println(redCircle);
        System.out.println(blueCircle);
    }
}