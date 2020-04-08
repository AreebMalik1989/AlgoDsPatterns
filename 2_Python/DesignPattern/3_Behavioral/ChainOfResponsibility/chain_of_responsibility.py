"""
Chain of responsiblity design pattern

Intent:

    Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon
    receiving a request, each handler decides either to process the request or to pass it to the next handler in the
    chain.

Structure:

1.  Handler interface: Common for all concrete handlers. It usually contains just a single method for handling requests,
    but sometimes it may also have another method for setting the next handler on the chain.

2.  BaseHandler class: Optional class where you can put the boilerplate code that’s common to all handler classes.
    Usually, this class defines a field for storing a reference to the next handler. The clients can build a chain by
    passing a handler to the constructor or setter of the previous handler. The class may also implement the default
    handling behavior: it can pass execution to the next handler after checking for its existence.

3.  ConcreteHanlers: Contain the actual code for processing requests. Upon receiving a request, each handler must decide
    whether to process it and, additionally, whether to pass it along the chain.
    Handlers are usually self-contained and immutable, accepting all necessary data just once via the constructor.

4.  Client: May compose chains just once or compose them dynamically, depending on the application’s logic. Note that a
    request can be sent to any handler in the chain—it doesn’t have to be the first one.
"""


from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler class.
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handles in a convinient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class MonkeyHandler(AbstractHandler):
    def handle(self, request: str) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: str) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: str) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most cases, it is not even aware that the
    handler is part of a chain.
    """
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"{result}")
        else:
            print(f"{food} was left untouched")


if __name__ == "__main__":

    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # The client should be able to send a request to any handler, not just the first one in the chain.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)

    print("Sub-chain: Squirrel > Dog")
    client_code(squirrel)
