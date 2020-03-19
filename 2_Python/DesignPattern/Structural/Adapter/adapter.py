"""Adapter design pattern implementation"""


import random


class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """
    def request_number(self) -> str:
        return f"Your request number: {random.randint(0, 100)}"


class Adaptee:
    """
    The adaptee contains some useful behaviour, but its interface is
    incompatible with the existing client code. The adaptee needs some
    adaptation before the client code can use it.
    """
    def get_request_number(self) -> int:
        return random.randint(0, 100)


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request_number(self) -> str:
        return f"Your request number: {adaptee.get_request_number()}"


def client_code(target: Target):
    """
    The client code supports all classes that follow the Target's interface.
    """

    print(target.request_number())


if __name__ == "__main__":
    print("Client: I can work just fine with the Target's object:")
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print("Client: The adaptee class has a wierd interface. See I don't understand it:")
    print(f"Adaptee: {adaptee.get_request_number()}", end="\n\n")

    print("Client: But I can work with the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
