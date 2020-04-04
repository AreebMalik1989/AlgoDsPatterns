package designpattern.creational.factory;

/**
 * Product interface
 */
interface Shape {
    void draw();
}

enum ShapeType {
    LINE, CIRCLE, RECTANGLE, UNKNOWN
}

/**
 * Concrete product
 */
class Line implements Shape {
    @Override
    public void draw(){
        System.out.println("Drawing line.");
    }
}

class Circle implements Shape {
    @Override
    public void draw(){
        System.out.println("Drawing circle.");
    }
}

class Rectangle implements Shape {
    @Override
    public void draw(){
        System.out.println("Drawing Rectangle");
    }
}

/**
 * Factory class
 */
abstract class ShapeFactory {
    public static Shape getShape(ShapeType type) {
        Shape shape = null;
        switch(type){
            case CIRCLE:
                return new Circle();
            case LINE:
                return new Line();
            case RECTANGLE:
                return new Rectangle();
            default:
                return shape;
        }
    }
}

class Demo {
    
    public static void main(String[] args) {
        
        // Request for circle shape
        Shape circle = ShapeFactory.getShape(ShapeType.CIRCLE);
        if(circle != null) {
            circle.draw();
        } else {
            System.out.println("This shape cannot be drawn");
        }

        // Request non existant shape
        Shape triangle = ShapeFactory.getShape(ShapeType.UNKNOWN);
        if(triangle != null) {
            triangle.draw();
        } else {
            System.out.println("This shape cannot be drawn");
        }
    }
}