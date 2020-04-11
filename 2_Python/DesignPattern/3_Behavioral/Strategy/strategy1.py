"""
Strategy design pattern implementation

Intent:

    Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a
    separate class, and make their objects interchangeable.

Structure:

1.  Context: Maintains a reference to one of the concrete strategies and communicates with this object only via the
    strategy interface.
    The context calls the execution method on the linked strategy object each time it needs to run the algorithm. The
    context doesn't know what type of strategy it works with or how the algorithm is executed.

2.  Strategy interface: Is common to all concrete strategies. It declares a method the context uses to execute a
    strategy.

3.  Concrete Strategies: Implement different variations of an algorithm the context uses.

4.  Client: Creates a specific strategy object and passes it to the context. The context exposes a setter which lets
    clients replace the strategy associated with the context at runtime.
"""


from abc import ABC, abstractmethod
from typing import List


class Context:
    """
    The context defines the interface of interest to clients.
    """
    def __init__(self, strategy):
        """
        Usually, the Context accepts a strategy through the constructor, but also provides a setter to change it at
        runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self):
        """
        The Context maintain a reference to one of the Strategy objects. The Context doesn't know the concrete class of
        a strategy. It should work with all strategies via the Strategy interface.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def do_some_business_logic(self):
        """
        The context delegates some work to the Strategy object instead of implementing multiple versions of the
        algorithm on its own.
        """
        print("Context: Sorting data using strategy (not sure how it'll do it.")
        result = self._strategy.do_algorithm(['b', 'a', 'e', 'c', 'd'])
        print(",".join(result))


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions of some algorithm.
    The Context uses this interface to call the algorithm defined by concrete Strategies.
    """
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List):
        return reversed(sorted(data))


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order to make the right choice.
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
