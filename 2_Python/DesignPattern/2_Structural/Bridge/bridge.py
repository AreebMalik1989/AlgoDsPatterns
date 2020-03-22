"""
Bridge design pattern implementation

Intent:

    Bridge is a structural design pattern that lets you split a large class or
    a set of closely related classes into two separate hierarchies—abstraction
    and implementation—which can be developed independently of each other.

Problem:

    Say you have a geometric Shape class with multiple subclasses Circle,
    Square, Rectangle, etc.
    You want to extend this class hierarchy to incorporate colors, so you
    want to create Red, Blue, Green, etc. subclasses.
    However, since you already have multiple subclasses, you'll need to create
    exponential numbers of subclasses, with combinations, RedCircle, RedSquare,
    RedRectangle,..., BlueCircle, BlueSquare, BlueRectangle, ..., etc...

    This problem occurs because we’re trying to extend the shape classes in two
    independent dimensions: by form and by color. That’s a very common issue
    with class inheritance.

Solution:

    The Bridge pattern attempts to solve this problem by switching from
    inheritance to the object composition. What this means is that you extract
     one of the dimensions into a separate class hierarchy, so that the
     original classes will reference an object of the new hierarchy, instead of
     having all of its state and behaviors within one class.

Structure:

1.  AbstractField class
2.  ConcreteField classes
3.  AbstractMain class having instance of AbstractField class
4.  ConcreteMain classes
"""


class Color:

    def __init__(self, color: str) -> None:
        self.color = color

    def __repr__(self) -> str:
        return self.color


class Red(Color):

    def __init__(self):
        super().__init__("Red")


class Blue(Color):

    def __init__(self):
        super().__init__("Blue")


class Shape:

    def __init__(self, color: Color) -> None:
        self.color = color

class Square(Shape):

    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):
        return f"I am a {self.color} Square"

class Circle(Shape):

    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):
        return f"I am a {self.color} Circle"


if __name__ == "__main__":

    print("Create different types of shapes with different colors")
    red_square = Square(Red())
    blue_square = Square(Blue())
    red_circle = Circle(Red())
    blue_circle = Circle(Blue())

    print(red_square)
    print(blue_square)
    print(red_circle)
    print(blue_circle)
