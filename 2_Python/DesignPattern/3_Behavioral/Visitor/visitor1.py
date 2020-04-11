"""
Visitor design pattern implementation

Intent:

    Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

Structure:

1.  Visitor interface: Declares a set of visiting methods that can take concrete elements of an object structure as
    arguments. These methods may have the same names if the program is written in a language that supports overloading,
    but the type of their parameters must be different.

2.  Concrete Visitor: Implements several versions of the same behaviors, tailored for different concrete element
    classes.

3.  Element interface: Declares a method for “accepting” visitors. This method should have one parameter declared with
    the type of the visitor interface.

4.  Concrete Element: Must implement the acceptance method. The purpose of this method is to redirect the call to the
    proper visitor’s method corresponding to the current element class. Be aware that even if a base element class
    implements this method, all subclasses must still override this method in their own classes and call the
    appropriate method on the visitor object.

5.  Client: Usually represents a collection or some other complex object (for example, a Composite tree). Usually,
    clients aren’t aware of all the concrete element classes because they work with objects from that collection via
    some abstract interface.
"""


from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The component interface declares an `accept` method that should take the base visitor interface as an argument.
    """
    @abstractmethod
    def accept(self, visitor) -> None:
        pass


class ConcreteComponentA(Component):
    """
    Each Concrete Component must implement the `accept` method in such a way that it calls the visitor's method
    corresponding to the component's class.
    """
    def accept(self, visitor) -> None:
        """
        Note that we are calling `visit_concrete_component_a` which matches the current class name. This way we let the
        visitor know the class of the component it works with.
        """
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        """
        Concrete Components may have special methods that don't exists in their base class or interface. The Visitor is
        still able to use these methods since it's aware of the component's concrete class.
        """
        return 'A'


class ConcreteComponentB(Component):
    def accept(self, visitor) -> None:
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return 'B'


class Visitor(ABC):
    """
    The Visitor interface declares a set of visiting methods that correspond to component classes. The signature of
    visiting method allows the visitor to identify the exact class of the component that it's dealing with.
    """
    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


"""
Concrete Visitors implement several versions of the same algorithm, which can work with all concrete component classes.
You can experience the biggest benefit of the Visitor pattern when using it with a complex object structure, such as a
Composite tree. In this case, it might be helpful to store some intermediate state of the algorithm while executing
visitor's methods over various objects of the structure.
"""


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    The client code can run visitor operations over any set of elements without figuring out their concrete classes.
    The accept operation directs a call to the appropriate operation in the visitor object.
    """

    # ...
    for component in components:
        component.accept(visitor)
    # ...


if __name__ == "__main__":

    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)
