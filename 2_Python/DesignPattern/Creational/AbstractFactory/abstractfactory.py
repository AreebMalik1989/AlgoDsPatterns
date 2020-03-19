"""
Abstract factory design pattern implementation

Intent:

    Abstract Factory is a creational design pattern that lets you produce
    families of related objects without specifying their concrete classes.

Structure:

1.  Abstract Products: declare interfaces for a set of distinct but related
    products which make up a product family.

2.  Concrete Products: are various implementations of abstract products, grouped
    by variants. Each abstract product must be implemented in all given
    variants (Victorian/Modern).

3.  Abstract Factory: interface declares a set of methods for creating each of
    the abstract products.

4.  Concrete Factories: implement creation methods of the abstract factory.
    Each concrete factory corresponds to a specific variant of products and
    creates only those product variants.

Note: Although concrete factories instantiate concrete products, signatures of
      their creation methods must return corresponding abstract products. This
      way the client code that uses a factory doesn’t get coupled to the
      specific variant of the product it gets from a factory. The Client can
      work with any concrete factory/product variant, as long as it
      communicates with their objects via abstract interfaces.
"""


from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1"


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2"


class AbstractProductB(ABC):
    """
    Here's the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products
    of the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> str:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concreate Products are created by corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1"

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2"

    """
    The variant, Product B2, is only able to work correctly with the variant,
    Product A2. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the({result})"


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of product may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible.
    Note that the signatures of the Concrete Factory's methods return an
    abstract product, while inside the method a concrete product is
    instantiated.
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with the factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
