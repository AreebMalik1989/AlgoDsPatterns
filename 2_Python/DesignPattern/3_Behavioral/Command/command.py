"""
Command design pattern implementation

Intent:

    Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information
    about the request. This transformation lets you parameterize methods with different requests, delay or queue a
    request’s execution, and support undoable operations.

Structure:

1.  Sender class (aka invoker): Is responsible for initiating requests. This class must have a field for storing a
    reference to a command object. The sender triggers that command instead of sending the request directly to the
    receiver. Note that the sender isn’t responsible for creating the command object. Usually, it gets a pre-created
    command from the client via the constructor.

2.  Command interface: Usually declares just a single method for executing the command.

3.  Concrete Commands: Implement various kinds of requests. A concrete command isn’t supposed to perform the work on its
    own, but rather to pass the call to one of the business logic objects. However, for the sake of simplifying the
    code, these classes can be merged.
    Parameters required to execute a method on a receiving object can be declared as fields in the concrete command. You
    can make command objects immutable by only allowing the initialization of these fields via the constructor.

4.  Receiver class: Contains some business logic. Almost any object may act as a receiver. Most commands only handle the
    details of how a request is passed to the receiver, while the receiver itself does the actual work.

5.  Client: Creates and configures concrete command objects. The client must pass all of the request parameters,
    including a receiver instance, into the command’s constructor. After that, the resulting command may be associated
    with one or multiple senders.
"""


from abc import ABC, abstractmethod


class Command(ABC):
    """
    The command interface declares a method for executing the command.
    """
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations to other objects, called "receivers".
    """
    def __init__(self, receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or several receiver objects along with any context data via the constructor.
        """
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        """
        print("ComplexCommand: Complex stuff should be done by a receiver object.")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    The Receiver classes contain some important business logic. They know how to perform all kinds of operations,
    associated with carrying out a request. In fact any class may serve as a receiver.
    """
    def do_something(self, a: str) -> None:
        print(f"Receiver: Working on ({a}.)")

    def do_something_else(self, b: str) -> None:
        print(f"Receiver: Also working on ({b}.)")


class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request to the command.
    """
    _on_start = None
    _on_finish = None

    # Initialize commands
    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The invoker passes a request to a receiver
        indirectly, by executing a command.
        """
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any command.
    """
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))

    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Send report"))

    invoker.do_something_important()
