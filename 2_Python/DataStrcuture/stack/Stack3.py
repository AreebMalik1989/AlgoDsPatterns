class MyStack:
    """
    Stack implementation using List
    """

    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.container.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.container[len(self.container) - 1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.container)
