"""
Iterator design pattern implementation

Intent:

    Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its
    underlying representation (list, stack, tree, etc.).

Structure:

1.  Iterator interface: Declares the operations required for traversing a collection: fetching the next element,
    retrieving the current position, restarting iteration, etc.

2.  Concrete Iterators: Implement specific algorithms for traversing a collection. The iterator object should track the
    traversal progress on its own. This allows several iterators to traverse the same collection independently of each
    other.

3.  Collection interface: Declares one or multiple methods for getting iterators compatible with the collection. Note
    that the return type of the methods must be declared as the iterator interface so that the concrete collections can
    return various kinds of iterators.

4.  Concrete Collections: Return new instances of a particular concrete iterator class each time the client requests
    one. You might be wondering, where’s the rest of the collection’s code? Don’t worry, it should be in the same class.
    It’s just that these details aren’t crucial to the actual pattern, so we’re omitting them.

5.  Client: Works with both collections and iterators via their interfaces. This way the client isn’t coupled to
    concrete classes, allowing you to use various collections and iterators with the same client code.
    Typically, clients don’t create iterators on their own, but instead get them from collections. Yet, in certain
    cases, the client can create one directly; for example, when the client defines its own special iterator.
"""


from collections.abc import Iterable, Iterator
from typing import Any, List


"""
To create an iterator in python, there are two abstract classes from the built-in 'collections' module - Iterable,
Iterator. We need to implement the '__iter__()' method in the iterated object (collection), and the '__next__()' method
in the iterator.
"""


class AlphabeticalOrderIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes store the current traversal position at all
    times.
    """

    """
    '_position' attribute stores the current traversal position. An iterator may have a lot of other fields for storing
    iteration state, especially when it is supposed to work with a particular kind of collection.
    """
    _position: int = None

    """
    This attribute indicates the traversal direction
    """
    _reverse: bool = False

    def __init__(self, words_collection, reverse: bool = False) -> None:
        self._collection = words_collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        This method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must
        raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    Concrete Collections provide on or several methods for retrieving fresh iterator instances, compatible with the
    collection class.
    """
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        This method returns iterator object itself, by default we return the iterator in the ascending order.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


if __name__ == "__main__":

    # The client code may or may not know about the Concrete Iterator or Collection classes, depending on the level of
    # indirection you want to keep in your program.
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print()

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()))
