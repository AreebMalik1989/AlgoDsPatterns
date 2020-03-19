"""
What the Gang of Four's original Singleton Pattern might look like in Python.

Intent:

    Singleton is a creational design pattern that lets you ensure that a class
    has only one instance, while providing a global access point to this
    instance.

Implementation:

1.  Make the default constructor private, to prevent other objects from using
    the new operator with the Singleton class.

2.  Create a static creation method that acts as a constructor. Under the hood,
    this method calls the private constructor to create an object and saves it
    in a static field. All following calls to this method return the cached
    object.

    Nowadays, the Singleton pattern has become so popular that people may call
    something a singleton even if it solves just one of the listed problems.
"""


class Logger:
    """
    Usage:
    
        log = Logger.instance()
    """
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here
        return cls._instance
