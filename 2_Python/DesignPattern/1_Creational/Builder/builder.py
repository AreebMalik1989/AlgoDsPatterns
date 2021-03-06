"""
Builder design pattern implementation

Intent:

    Builder is a creational design pattern that lets you construct complex
    objects step by step. The pattern allows you to produce different types and
    representations of an object using the same construction code.

Structure:

1.  Builder interface: declares product construction steps that are common to
    all types of builders.

2.  Concrete Builders: provide different implementations of the construction
    steps. Concrete builders may produce products that don’t follow the common
    interface.

3.  Director class: defines the order in which to call construction steps, so
    you can create and reuse specific configurations of products.

4.  The Client must associate one of the builder objects with the director.
    Usually, it’s done just once, via parameters of the director’s constructor.
    Then the director uses that builder object for all further construction.
    However, there’s an alternative approach for when the client passes the
    builder object to the production method of the director. In this case, you
    can use a different builder each time you produce something with the
    director.
"""


from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Any


class Builder(metaclass=ABCMeta):
    """
    The builder interface specifies methods for creating the different parts of
    the Product object.
    """
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class Product1:
    """
    It makes sense to use the builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can
    produce unrelated products. In other words, results of various builders may
    not always follow the same interface.
    """
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank Product object which is
        used in further assembly.
        """
        self._reset()

    def _reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete builders are supposed to provide their own methods for
        retreiving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder
        interface.
        (At least in statically typed programming language)

        Usually, after returning end result to the client, a builder instance
        is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behaviour is not mendatory,
        and you can make your builders wait for explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self._reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add('PartA1')

    def produce_part_b(self) -> None:
        self._product.add('PartB1')

    def produce_part_c(self) -> None:
        self._product.add('PartC1')


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The director works with any builder instance that the client code
        passes to it. This way, the client code may alter the final type type
        of the newly assembled product.
        """
        self._builder = builder

    """
    The director can construct several product variations using the same
    building steps.
    """
    def build_minimum_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product:")
    director.build_minimum_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product:")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the builder pattern can be used without a Director class.
    print("Custom product:")
    builder.produce_part_a()
    builder.produce_part_c()
    builder.product.list_parts()
