"""
Factory design pattern implementation

Intent:

    Factory Method is a creational design pattern that provides an interface
    for creating objects in a superclass, but allows subclasses to alter the
    type of objects that will be created.

Structure:

1.  Product : declares the interface, which is common to all objects that can be
    produced by the creator and its subclasses.

2.  Concrete Products: are different implementations of the product interface.

3.  Creator class: declares the factory method that returns new product
    objects. It’s important that the return type of this method matches the
    product interface.

    You can declare the factory method as abstract to force all subclasses to
    implement their own versions of the method. As an alternative, the base
    factory method can return some default product type.

    Note, despite its name, product creation is not the primary responsibility
    of the creator. Usually, the creator class already has some core business
    logic related to products. The factory method helps to decouple this logic
    from the concrete product classes. Here is an analogy: a large software
    development company can have a training department for programmers.
    However, the primary function of the company as a whole is still writing
    code, not producing programmers.

4.  Concrete Creators: override the base factory method so it returns a
    different type of product.

    Note that the factory method doesn’t have to create new instances all the
    time. It can also return existing objects from a cache, an object pool, or
    another source.
"""


from abc import ABC, abstractmethod


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete products provide various implementations of the Product interface.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


class Creator(ABC):
    """
    The creator class declares factory method that is supposed to return an
    object of Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    @abstractmethod
    def factory_method(self):
        """
        Note the Creator may also provide some default implementation of the
        factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a product object.
        product = self.factory_method()

        # Now use the product
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of the concrete product classes.
    """
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of concrete creator, albeit though
    its base interface. As long as the client keeps working with the creator
    via the base interface, you can pass it any creator's subclass.
    """
    print(f"Client: I am not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
