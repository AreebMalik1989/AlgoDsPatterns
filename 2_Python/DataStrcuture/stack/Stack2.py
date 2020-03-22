class Stack:
    """
    Stack implementation using Array
    """

    def __init__(self, size=10):
        self.size = size
        self.tos = -1
        self.array = [None] * size

    def push(self, data):
        """
        Push data in stack

        :param data: to be pushed
        :return: None
        """

        if self.is_stack_full():
            raise Exception('Stack is full')
        else:
            self.tos += 1
            self.array[self.tos] = data

    def pop(self):
        """
        Pop the top of the stack

        :return: data at the top of stack
        """

        if self.is_stack_empty():
            raise Exception('Stack is empty')

        else:
            data = self.array[self.tos]
            self.tos -= 1
            return data

    def peek(self):
        """
        Peek the top of the stack

        :return: data at the top of stack
        """

        if self.is_stack_empty():
            raise Exception('Stack is empty')

        else:
            return self.array[self.tos]

    def get_size(self):
        """
        Method to get the size of stack

        :return: size of stack
        """

        count = 0
        for i in self.array:
            if i is None:
                break

            count += 1

        return count

    def is_stack_full(self):
        """
        Check if the stack is full

        :return: true if the stack is full
        """

        return self.tos == self.size - 1

    def is_stack_empty(self):
        """
        Check if the stack is empty

        :return: true if the stack is empty
        """

        return self.tos == -1

