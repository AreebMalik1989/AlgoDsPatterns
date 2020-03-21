"""
Flyweight design pattern implementation

Intent:

    Flyweight is a structural design pattern that lets you fit more objects
    into the available amount of RAM by sharing common parts of state between
    multiple objects instead of keeping all of the data in each object.

Structure:

1.  Flyweight class: contains the portion of the original object’s state that
    can be shared between multiple objects. The same flyweight object can be
    used in many different contexts. The state stored inside a flyweight is
    called “intrinsic.” The state passed to the flyweight’s methods is called
    “extrinsic.”

2.  Context class: contains the extrinsic state, unique across all original
    objects. When a context is paired with one of the flyweight objects, it
    represents the full state of the original object.

3.  Flyweight Factory: manages a pool of existing flyweights. With the factory,
    clients don’t create flyweights directly. Instead, they call the factory,
    passing it bits of the intrinsic state of the desired flyweight. The
    factory looks over previously created flyweights and either returns an
    existing one that matches search criteria or creates a new one if nothing
    is found.

4.  Client: calculates or stores the extrinsic state of flyweights. From the
    client’s perspective, a flyweight is a template object which can be
    configured at runtime by passing some contextual data into parameters of
    its methods.
"""


import json
from typing import Dict


class Flyweight:
    """
    The Flyweight stores a common portion of the state (also called intrinsic
    state) that belongs to multiple real business entities. The Flyweight
    accepts the rest of the states (extrinsic state, unique for each entity)
    via its method parameters.
    """
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique({u}) state.")


class FlyweightFactory:
    """
    The Flyweight Factory creates and manages the Flyweight objects. It ensures
    that flyweights are shared correctly. When the client request a flyweight,
    the factory either returns an existing instance or creates a new one, if it
    doesn't exists yet.
    """
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        Returns a Flyweight's string hash for the given state.
        """
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        Returns an exiting Flyweight with a given state or creates a new one.
        """
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owener: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # The client code either stores or calculates extrinsic state and passes it
    # to the flyweight's method
    flyweight.operation([plates, owener])


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red"
    )

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red"
    )

    print("\n")

    factory.list_flyweights()
