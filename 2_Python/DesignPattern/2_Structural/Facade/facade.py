"""
Facade design pattern implementation

Intent:

    Facade is a structural design pattern that provides a simplified interface
    to a library, a framework, or any other complex set of classes.

Implementation:

1.  Facade: provides convenient access to a particular part of the subsystem’s
    functionality. It knows where to direct the client’s request and how to
    operate all the moving parts.

2.  Additional: Facade class can be created to prevent polluting a single
    facade with unrelated features that might make it yet another complex
    structure. Additional facades can be used by both clients and other
    facades.

3.  Complex Subsystem: consists of dozens of various objects. To make them all
    do something meaningful, you have to dive deep into the subsystem’s
    implementation details, such as initializing objects in the correct order
    and supplying them with data in the proper format.

    Subsystem classes aren’t aware of the facade’s existence. They operate
    within the system and work with each other directly.

4.  The Client uses the facade instead of calling the subsystem objects
    directly.
"""


class Subsystem1:
    pass


class Subsystem2:
    pass


class Facade:
    """
    The Facade class provides a simple interface to the complex logic of one or
    several subsystems. The Facade delegates the client request to the
    appropriate objects within the subsystems. The Facade is also responsible
    for managing their lifecycle. All of this shields the client from the
    undesired complexity of the subsystem.
    """
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Depending on your application's need, you can provide the Facade with
        existing subsystem objects or force the Facade to create them on its
        own.
        """
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:
        """
        The Facade's methods are convinient shorcuts to the sophisticated
        functionality of the subsytems. However, clients get only to a fraction
        of a subsystem's capabilities.
        """
        results = []
        results.append("Facade intializes subsytems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1(Subsystem1):
    """
    The Subsystem can accept requests either from the Facade or client
    directly. In any case, to the Subsystem, the Facade is yet another
    client, and it's not a part of the subsystem.
    """
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2(Subsystem2):
    """
    Some facades can work with multiple subsystems at the same time.
    """
    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existance of the
    subsystem. This approach lets you keep the complexity under control.
    """
    print(facade.operation())


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
