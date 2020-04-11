"""
State design pattern implementation

Intent:

    State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It
    appears as if the object changed its class.

Structure:

1.  Context: Stores a reference to one of the concrete state objects and delegates to it all state-specific work. The
    context communicates with the state object via the state interface. The context exposes a setter for passing it a
    new state object.

2.  State interface: Declares the state-specific methods. These methods should make sense for all concrete states
    because you don’t want some of your states to have useless methods that will never be called.

3.  Concrete States: Provide their own implementations for the state-specific methods. To avoid duplication of similar
    code across multiple states, you may provide intermediate abstract classes that encapsulate some common behavior.
    State objects may store a backreference to the context object. Through this reference, the state can fetch any
    required info from the context object, as well as initiate state transitions.

4.  Both context and concrete states can set the next state of the context and perform the actual state transition by
    replacing the state object linked to the context.
"""


from abc import ABC, abstractmethod


class Context(ABC):
    """
    The Context defines the interface of interest to clients. It also maintains a reference to an instance of a State
    subclass, which represents the current state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        """
        The Context allows changing the state object at runtime.
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    Context delegates part of its behaviour to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base state class declares method that all Concrete state should implement and also provides a back reference to
    the Context object, associated with the State. This back reference can be used by States to transition the Context
    to another State.
    """

    def __init__(self, context: Context = None) -> None:
        self._context = context

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Concrete States implement various behaviours, associated with a state of the Context.
"""


class ConcreteStateA(State):

    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the Context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):

    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the Context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
