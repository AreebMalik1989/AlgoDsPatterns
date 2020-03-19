"""Singleton design pattern implementation"""


class Foo:
    """
    Using module as a singleton, this works because after the first time a file
    is imported, Python doesn't re-execute the code.

    Usage:

        from singleton import my_singleton
        my_singleton.bar()
    """
    def bar(self):
        pass


my_singleton = Foo()
