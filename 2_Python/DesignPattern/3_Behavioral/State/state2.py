from abc import ABCMeta, abstractmethod


class EmotionalState(metaclass=ABCMeta):

    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass


class HappyState(EmotionalState):

    def say_hello(self):
        return "Hello, friend!"

    def say_goodbye(self):
        return "Bye, friend!"


class SadState(EmotionalState):

    def say_hello(self):
        return "Hello. Sniff, sniff."

    def say_goodbye(self):
        return "Bye. Sniff, sniff."


class Person(EmotionalState):

    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def say_hello(self):
        return self._state.say_hello()

    def say_goodbye(self):
        return self._state.say_goodbye()


if __name__ == "__main__":

    person = Person(HappyState())
    print(f"Hello in happy state {person.say_hello()}")
    print(f"Goodbye in happy state {person.say_goodbye()}")

    person.set_state(SadState())
    print(f"Hello in sad state: {person.say_hello()}")
    print(f"Goodbye in sad state: {person.say_goodbye()}")
