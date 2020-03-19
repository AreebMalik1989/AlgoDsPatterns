"""Adapter design pattern implementation"""


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
