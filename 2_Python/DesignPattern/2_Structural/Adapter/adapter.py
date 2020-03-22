"""
Adapter design pattern implementation

Intent:

    Adapter is a structural design pattern that allows objects with
    incompatible interfaces to collaborate.

Structure:

1.  Client: is a class that contains the existing business logic of the
    program.

2.  Client Interface: describes a protocol that other classes must follow to be
    able to collaborate with the client code.

3.  Service: is some useful class (usually 3rd-party or legacy). The client
    can’t use this class directly because it has an incompatible interface.

4.  Adapter: is a class that’s able to work with both the client and the
    service -> it implements the client interface, while wrapping the service
    object. The adapter receives calls from the client via the adapter
    interface and translates them into calls to the wrapped service object in a
    format it can understand.
"""


class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The adaptee contains some useful behaviour, but its interface is
    incompatible with the existing client code. The adaptee needs some
    adaptation before the client code can use it.
    """
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target):
    """
    The client code supports all classes that follow the Target's interface.
    """

    print(target.request())


if __name__ == "__main__":
    print("Client: I can work just fine with the Target's object:")
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print("Client: The adaptee class has a wierd interface. See I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
