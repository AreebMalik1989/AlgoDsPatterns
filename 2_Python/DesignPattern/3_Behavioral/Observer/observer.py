"""
Observer design pattern implementation

Intent:

    Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects
    about any events that happen to the object they’re observing.

Structure:

1.  Publisher: Issues events of interest to other objects. These events occur when the publisher changes its state or
    executes some behaviors. Publishers contain a subscription infrastructure that lets new subscribers join and current
    subscribers leave the list.
    When a new event happens, the publisher goes over the subscription list and calls the notification method declared
    in the subscriber interface on each subscriber object.

2.  Subscriber interface: Declares the notification interface. In most cases, it consists of a single update method. The
    method may have several parameters that let the publisher pass some event details along with the update.

3.  Concrete Subscribers: Perform some actions in response to notifications issued by the publisher. All of these
    classes must implement the same interface so the publisher isn’t coupled to concrete classes.
    Usually, subscribers need some contextual information to handle the update correctly. For this reason, publishers
    often pass some context data as arguments of the notification method. The publisher can pass itself as an argument,
    letting subscriber fetch any required data directly.

4.  Client: Creates publisher and subscriber objects separately and then registers subscribers for publisher updates.
"""


from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been attached to.
"""


class ConcreteObserverA(Observer):
    def update(self, subject) -> None:
        if subject.get_state() < 3:
            print("ConcreteObserverA: Reacted to the event.")


class ConcreteObserverB(Observer):
    def update(self, subject) -> None:
        if subject.get_state() == 0 or subject.get_state() >= 2:
            print("ConcreteObserverB: Reacted to the event.")


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored more comprehensively (categorized by event
    type, etc.).
    """

    def get_state(self) -> int:
        return self._state

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("Subject: Detached an observer.")
        self._observers.remove(observer)

    """
    The subscription management methods.
    """
    def notify(self) -> None:
        """
        Triggers an update in each subscriber.
        """
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can really do. Subjects commonly holds some
        important business logic, that triggers a notification method whenever something important is about to happen
        (or after it)
        """
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


if __name__ == "__main__":

    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.attach(observer_a)
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
