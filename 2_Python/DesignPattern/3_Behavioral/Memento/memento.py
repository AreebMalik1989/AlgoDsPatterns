"""
Memento design pattern implementation

Intent:

    Memento is a behavioral design pattern that lets you save and restore the previous state of an object without
    revealing the details of its implementation.

Structure:

1.  Originator: Class can produce snapshots of its own state, as well as restore its state from snapshots when needed.

2.  Memento: Is a value object that acts as a snapshot of the originator’s state. It’s a common practice to make the
    memento immutable and pass it the data only once, via the constructor.

3.  Caretaker: Knows not only “when” and “why” to capture the originator’s state, but also when the state should be
    restored.
    A caretaker can keep track of the originator’s history by storing a stack of mementos. When the originator has to
    travel back in history, the caretaker fetches the topmost memento from the stack and passes it to the originator’s
    restoration method.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Memento(ABC):
    """
    A memento interface provides a way to retrieve the memento's metadata, such as creation date or name. However, it
    doesn't expose the Originator's state.
    """
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass


class ConcreteMemento(Memento):

    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        The originator uses this method when restoring its state.
        """
        return self._state

    def get_name(self) -> str:
        """
        The rest of the methods are used by the Caretaker to display metadata.
        """
        return f"{self._date} / {self._state[0:9]}..."

    def get_date(self) -> str:
        return self._date


class Originator:
    """
    The Originator holds some important state that may change over time. It also defines a method for saving the state
    inside a memento and another method for restoring the state from it.
    """

    _state = None
    """
    For the sake of simplicity, the originator's state is stored inside a single variable.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        """
        The Originator's business logic may affect its internal state. Therefore, the client should backup the state
        before launching methods of the business logic via the save() method.
        """
        print("Originator: I am doing something important")
        self._state = self._generate_random_string(30)
        print(f"Originator: And my state has changed to: {self._state}")

    def _generate_random_string(self, length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        Saves the current state inside a memento.
        :return:
        """
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Restores the Originator's state from a memento object.
        """
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Caretaker:
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it doesn't have access to the originator's
    state, stored inside the memento. It works with all the mementos via the base memento interface.
    """
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:

        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of Mementos")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":

    originator = Originator("Super-duper-super-puper-super")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()
