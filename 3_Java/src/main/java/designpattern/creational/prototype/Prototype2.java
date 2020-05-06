package designpattern.creational.prototype;

import java.util.ArrayList;
import java.util.List;

abstract class Shape {

    public int x;
    public int y;
    public String color;

    public Shape(){}

    public Shape(Shape shape) {
        if(shape != null) {
            this.x = shape.x;
            this.y = shape.y;
            this.color = shape.color;
        }
    }

    public abstract Shape clone();

    @Override
    public boolean equals(Object object) {
        if(!(object instanceof Shape)) return false;
        Shape shape = (Shape) object;
        return shape.x == x && shape.y == y && shape.color.equals(color);
    }
}

class Circle extends Shape {

    public int radius;

    public Circle(){}

    public Circle(Circle circle) {
        super(circle);
        if(circle != null) {
            this.radius = circle.radius;
        }
    }

    @Override
    public Shape clone() {
        return new Circle(this);
    }

    @Override
    public boolean equals(Object object) {
        if(!(object instanceof Circle) || !super.equals(object)) return false;
        Circle circle = (Circle) object;
        return circle.radius == radius;
    }
}

class Rectangle extends Shape {

    public int width;
    public int height;

    public Rectangle(){}

    public Rectangle(Rectangle rectangle) {
        super(rectangle);
        if(rectangle != null) {
            this.width = rectangle.width;
            this.height = rectangle.height;
        }
    }

    @Override
    public Shape clone() {
        return new Rectangle(this);
    }

    @Override
    public boolean equals(Object object) {
        if(!(object instanceof Shape) || !super.equals(object)) return false;
        Rectangle rectangle = (Rectangle) object;
        return rectangle.width == width && rectangle.height == height;
    }
}

class Prototype2 {

    public static void main(String[] args) {

        List<Shape> shapes = new ArrayList<>();
        List<Shape> shapesCopy = new ArrayList<>();

        Circle circle = new Circle();
        circle.x = 10;
        circle.y = 20;
        circle.radius = 50;
        circle.color = "red";
        shapes.add(circle);

        Circle anotherCircle = (Circle) circle.clone();
        shapes.add(anotherCircle);

        Rectangle rectangle = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 20;
        rectangle.color = "blue";
        shapes.add(rectangle);

        cloneAndCompare(shapes, shapesCopy);
    }

    private static void cloneAndCompare(List<Shape> shapes, List<Shape> shapesCopy) {
        for (Shape shape : shapes) {
            shapesCopy.add(shape.clone());
        }

        for (int i = 0; i < shapes.size(); i++) {
            if (shapes.get(i) != shapesCopy.get(i)) {
                System.out.println(i + ": Shapes are different objects (yay!)");
                if (shapes.get(i).equals(shapesCopy.get(i))) {
                    System.out.println(i + ": And they are identical (yay!)");
                } else {
                    System.out.println(i + ": But they are not identical (booo!)");
                }
            } else {
                System.out.println(i + ": Shape objects are the same (booo!)");
            }
        }
    }
}