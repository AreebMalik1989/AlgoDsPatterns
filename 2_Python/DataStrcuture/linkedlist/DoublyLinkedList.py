class Node:
    def __init__(self, data=None, prev_node=None, next_node=None):
        """
        Constructor for the Node of doubly linked list

        :param data: data value of the node
        :param prev: previous node in Doubly Linked List
        :param next: next node in Doubly Linked List
        """

        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Adding a node at the front of the list

        :param data: value of the node
        """

        # 1. Allocate a node
        # 2. Put in the data
        new_node = Node(data)

        # 3. Make next of new node as head and previous as Null
        new_node.next = self.head
        new_node.prev = None

        # 4. Change prev of head node to new node
        if self.head:
            self.head.prev = new_node

        # 5. Move the head to point to the new node
        self.head = new_node

    def insert_after(self, prev_node, data):
        """
        Insert a new node after the given node

        :param prev_node: after this node, new node to be inserted
        :param data: value of the new node
        :return: None
        """

        # 1. Check if the given prev node is None
        if prev_node is None:
            return

        # 2. Allocate a new node
        # 3. Put in the data
        new_node = Node(data)

        # 4. Make next of new_node as next of prev_node
        new_node.next = prev_node.next

        # 5. Make the next of prev_node as next of new_node
        prev_node.next = new_node

        # 6. Make prev_node as previous of new_node
        new_node.prev = prev_node

        # 7. Change previous of new_node's next node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self, data):
        """
        Add a node at the end of DLL

        :param data: value of the new node
        :return: None
        """

        # 1. Allocate node
        # 2. Put in the data
        new_node = Node(data)

        # 3. This new node is going to be last node, so make next of it as Null
        new_node.next = None

        # 4. If the DLL is empty, then make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node
        new_node.prev = last

    def delete_node(self, node):
        """
        Delete node in DLL

        :param node: node to be deleted
        :return: None
        """

        # Base case
        if self.head is None or node is None:
            return

        # If node to be deleted if head node
        if self.head == node:
            self.head = self.head.next

        # change next node only if node to be deleted is NOT the last node
        if node.next:
            node.next.prev = node.prev

        # change prev node only if node to be deleted is NOT the first node
        if node.prev:
            node.prev.next = node.next

    def delete_node_at_position(self, position):
        """
        Delete node in DLL at given position

        :param position: index of the node
        :return: None
        """

        # If list is Null or invalid position is given
        if self.head is None or position < 0:
            return

        current = self.head
        i = 1

        # Traverse up to the node at given position from the beginning
        while current is not None and i < position:
            current = current.next
            i += 1

        # If position is greater than number of nodes
        if current is None:
            return

        self.delete_node(current)

    def reverse(self):
        """
        Reverse a doubly linked list

        :return: None
        """

        temp = None
        current = self.head

        # Swap next and prev for all nodes of DLL
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        # Before changing heads check for the cases like
        # empty list and list with only one node
        if temp:
            self.head = temp.prev

    def print_list(self):
        """
        Prints the DLL

        :return: None
        """

        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
