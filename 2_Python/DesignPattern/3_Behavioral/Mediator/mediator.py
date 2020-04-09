"""
Mediator design pattern implementation

Intent:

    Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern
    restricts direct communications between the objects and forces them to collaborate only via a mediator object.

Structure:

1.  Components: Are various classes that contain some business logic. Each component has a reference to a mediator,
    declared with the type of the mediator interface. The component isn’t aware of the actual class of the mediator,
    so you can reuse the component in other programs by linking it to a different mediator.

2.  Mediator interface: Declares methods of communication with components, which usually include just a single
    notification method. Components may pass any context as arguments of this method, including their own objects,
    but only in such a way that no coupling occurs between a receiving component and the sender’s class.

3.  Concrete Mediators: Encapsulate relations between various components. Concrete mediators often keep references to
    all components they manage and sometimes even manage their lifecycle.

4.  Components must not be aware of other components. If something important happens within or to a component, it must
    only notify the mediator. When the mediator receives the notification, it can easily identify the sender, which
    might be just enough to decide what component should be triggered in return.
    From a component’s perspective, it all looks like a total black box. The sender doesn’t know who’ll end up handling
    its request, and the receiver doesn’t know who sent the request in the first place.
"""


from abc import ABC, abstractmethod


class Mediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the mediator about various events. The
    Mediator may react to these events and pass the execution to other components.
    """
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):

    def __init__(self, component1, component2) -> None:
        self._component1 = component1
        self._component2 = component2
        self._component1.mediator = self
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    The BaseComponent provides the basic functionality of storing a mediator's instance inside component objects.
    """
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
Concrete Components implements various functionalities. They don't depend on other components. They also don't depend on
any concrete mediator classes.
"""


class Component1(BaseComponent):

    def do_a(self) -> None:
        print("Component1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):

    def do_c(self) -> None:
        print("Component2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component2 does D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":

    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print()

    print("Client triggers operation D.")
    c2.do_d()
