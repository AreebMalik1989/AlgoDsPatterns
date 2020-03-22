class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


class Stack:
    """
    Stack implementation using LinkedList
    """

    def __init__(self):
        self.TOS = None

    def push(self, data):
        """
        Push data into stack

        :param data: data of node
        :return: None
        """

        new_node = Node(data)
        new_node.next = self.TOS
        self.TOS = new_node

    def pop(self):
        """
        Pop the top of stack

        :return: top node of stack
        """

        # If the stack is empty
        if self.is_empty():
            print("inside empty")
            return
        else:
            print("inside non emtpy")
            top_node = self.TOS
            self.TOS = self.TOS.next
            return top_node

    def peek(self):
        """
        Peek the top of stack

        :return: top node of stack
        """

        return self.TOS

    def size(self):
        """
        Returns the size of stack

        :return: size of stack
        """

        current_node = self.TOS
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def is_empty(self):
        """
        Check if the stack is empty

        :return: true if the stack is empty
        """
        return self.TOS is None

    def print_stack(self):
        """
        Prints the stack

        :return: None
        """

        current_node = self.TOS
        while current_node:
            print(current_node, end=' ')
            current_node = current_node.next
        print()

