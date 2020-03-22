"""
Composite design pattern implementation

Intent:

    Composite is a structural design pattern that lets you compose objects into
    tree structures and then work with these structures as if they were
    individual objects.

Structure:

1.  Component interface: describes operations that are common to both simple
    and complex elements of the tree.

2.  Leaf: is a basic element of a tree that doesn’t have sub-elements.

    Usually, leaf components end up doing most of the real work, since they
    don’t have anyone to delegate the work to.

3.  The Container (aka composite) is an element that has sub-elements: leaves
    or other containers. A container doesn’t know the concrete classes of its
    children. It works with all sub-elements only via the component interface.

    Upon receiving a request, a container delegates the work to its
    sub-elements, processes intermediate results and then returns the final
    result to the client.

4.  The Client works with all elements through the component interface. As a
    result, the client can work in the same way with both simple or complex
    elements of the tree.
"""


from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    pass


class Component(Component):
    """
    The base Component class declares common operations for both simple and
    complex objects of the composition.
    """
    def __init__(self) -> None:
        self._parent = None

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base component can declare an interface for setting and
        accessing the parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """
        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management operations
    right in the base Component class. This way, you won't need to expose any
    concrete component classes to the client code, even during the object tree
    assembly. The downside is that these methods will be empty for the leaf-level
    components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """
        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behaviour or leave it to
        concrete classes (by declaring the method containing the behaviour as
        "abstract").
        """
        pass


class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """
    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """
    def __init__(self) -> None:
        super().__init__()
        self._children: List[Component] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The Composite executes it primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code1(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """
    print(f"RESULT: {component.operation()}")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple
    or complex, without depending on their concrete classes.
    """
    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}")


if __name__ == "__main__":

    # This way client code can support the leaf components...
    simple = Leaf()

    print("Client: I've got a leaf")
    client_code1(simple)
    print("\n")

    # ...as well as complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code1(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
