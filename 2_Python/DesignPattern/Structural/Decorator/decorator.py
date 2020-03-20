"""
Decorator design pattern implementation

Intent:

    Decorator is a structural design pattern that lets you attach new behaviors
    to objects by placing these objects inside special wrapper objects that
    contain the behaviors.

Implementation:

1.  Component: declares the common interface for both wrappers and wrapped
    objects.

2.  Concrete Component: is a class of objects being wrapped. It defines the
    basic behavior, which can be altered by decorators.

3.  Base Decorator class: has a field for referencing a wrapped object. The
    field’s type should be declared as the component interface so it can
    contain both concrete components and decorators. The base decorator
    delegates all operations to the wrapped object.

4.  Concrete Decorators: define extra behaviors that can be added to components
    dynamically. Concrete decorators override methods of the base decorator and
    execute their behavior either before or after calling the parent method.

5.  The Client can wrap components in multiple layers of decorators, as long as
    it works with all objects via the component interface.
"""


from abc import ABC, abstractmethod


class Component(ABC):
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations.
    There might be several variations of these classes.
    """
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    The base decorate class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """
    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        """
        The Decorator delegates all work to the wrapped component.
        """
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """
    Decorators can execute their behaviour either before or after the call to a
    wrapped object.
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component):
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """
    print(f"RESULT: {component.operation()}")


if __name__ == "__main__":
    # This way client code can support both simple components...
    simple = ConcreteComponent()
    client_code(simple)

    # ...as well as decorate ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)
