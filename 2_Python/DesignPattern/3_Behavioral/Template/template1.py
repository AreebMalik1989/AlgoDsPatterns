"""
Template design pattern implementation

Intent:

    Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets
    subclasses override specific steps of the algorithm without changing its structure.

Structure:

1.  Abstract class: Declares methods that act as steps of an algorithm, as well as the actual template method which
    calls these methods in a specific order. The steps may either be declared abstract or have some default
    implementation.

2.  Concrete classes: Can override all of the steps, but not the template method itself.
"""


from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    The AbstractClass defines a template method that contains a skeleton of some algorithm, composed of calls to
    (usually) abstract primitive operations.
    Concrete subclasses should implement these operations, but leave the template method itself intact.
    """

    def template_method(self) -> None:
        """
        The template method defines the skeleton of an algorithm.
        """
        self.__base_operation1()
        self.required_operation1()
        self.__base_operation2()
        self.hook1()
        self.required_operation2()
        self.__base_operation3()
        self.hook2()

    # These are private operations and already have implementations.

    def __base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def __base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def __base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    # These operations have to be implemented in subclasses.

    @abstractmethod
    def required_operation1(self) -> None:
        pass

    @abstractmethod
    def required_operation2(self) -> None:
        pass

    # These are `hooks`. Subclasses may override them, but it's not mandatory since the hooks already have default (but
    # empty implementation. Hooks provide additional extension point in some crucial places of the algorithm

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    Concrete classes have to implement all abstract operations of the base class. They can also override some
    operations with a default implementation.
    """
    def required_operation1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operation2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    """
    Usually, concrete classes override only a fraction of base class operations.
    """
    def required_operation1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operation2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overriden Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    """
    The client code calls the template method to execute the algorithm. Client code does not have to know the concrete
    class of the object it works with, as long it works with objects through the interface of their base class.
    """

    # ...
    abstract_class.template_method()
    # ...


if __name__ == "__main__":

    print("Same client code can work with different subclasses.")
    print("Client working with ConcreteClass1 object:")
    client_code(ConcreteClass1())
    print()

    print("Client working with ConcreteClass2 object:")
    client_code(ConcreteClass2())
