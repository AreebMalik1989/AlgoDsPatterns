class Node:
    def __init__(self, data, next_node=None):
        """
        Constructor of the node

        :param data:
        """

        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Add new node at the beginning

        :param data: value of the node
        :return: None
        """

        new_node = Node(data)

        # If there's no element in the circular linked list
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head

            # Traverse the list to find the last node
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = self.head

    def insert_after(self, prev_data, data):
        """
        Insert new node with data value

        :param prev_data: data of node after which new node to be inserted
        :param data: value of the new node
        :return: None
        """

        current_node = self.head

        while current_node:

            if current_node.next == self.head and current_node.data == prev_data:
                # new node is to be appended to the list
                self.append(data)
                return

            elif current_node.data == prev_data:

                new_node = Node(data)
                next_node = current_node.next

                # Update the next pointer
                current_node.next = new_node
                new_node.next = next_node

                return

            else:

                if current_node.next == self.head:
                    break

            current_node = current_node.next

    def append(self, data):
        """
        Insert node at the end of circular linked list

        :param data: value of the node to be added
        :return: None
        """

        new_node = Node(data)

        # If there's no element in the circular linked list
        if not self.head:
            self.head = new_node
            new_node.next = self.head

        else:
            current_node = self.head

            # Traverse the linked list to find the last node
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = self.head

    def delete_node(self, data):
        """
        Delete node in circular linked list

        :param data: value of the node to be deleted
        :return: None
        """

        current_node = self.head
        prev_node = None

        while current_node:

            # Node to be deleted is head node
            if current_node.data == data and current_node == self.head:

                # Case 1: The head is the only element in the circular linked list
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return

                # Case 2: There are more elements in the circular linked list
                else:
                    # Traverse to the end of list, update self.head, delete head
                    while current_node.next != self.head:
                        current_node = current_node.next

                    current_node.next = self.head.next
                    self.head = self.head.next
                    current_node = None
                    return

            # Node to be deleted in between nodes or last node
            elif current_node.data == data:
                prev_node.next = current_node.next
                current_node = None
                return

            else:
                if current_node.next == self.head:
                    break

            prev_node = current_node
            current_node = current_node.next

    def get_count(self) -> int:
        """
        Get the number of nodes in linked list

        :return: number of nodes in linked list
        """

        current_node = self.head
        result = 0

        if self.head is not None:
            while True:
                current_node = current_node.next
                result += 1
                if current_node == self.head:
                    break

        return result
