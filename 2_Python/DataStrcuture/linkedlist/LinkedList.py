class LinkedListNode:

    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class LinkedList:

    def __init__(self):
        self.head: LinkedListNode = None

    def push(self, data):
        """
        Add new node at the beginning

        :param data: value of node to be added
        """

        # 1. Allocate the node
        # 2. Put in the data
        new_node = LinkedListNode(data)

        # 3. Make next of new node as head
        new_node.next = self.head

        # 4. Move the head to point to new node
        self.head = new_node

    def insert_after(self, prev_node: LinkedListNode, data):
        """
        Inserts a new node after the given prev_node

        :param prev_node: previous node
        :param data: value of new node to be added
        """

        # 1. Check if the given prev_node exists
        if prev_node is None:
            return

        # 2. Create new node
        # 3. Put in the data
        new_node = LinkedListNode(data)

        # 4. Make next of new_node as next of prev_node
        new_node.next = prev_node.next

        # 5. Make next of prev_node as new_node
        prev_node.next = new_node

    def append(self, data):
        """
        Appends a new node at the end

        :param data: value of new node to be appended
        """

        # 1. Create a new node
        # 2. Put in that data
        new_node = LinkedListNode(data)

        # 3. If the linked list is empty, then make the new node as head
        if self.head is None:
            self.head = new_node

        # 4. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 5. Change the next of last node
        last.next = new_node

    def find(self, data):
        """
        Search for the first element with data matching 'item'.
        Return the element or 'None' if not found.
        Takes O(n) time

        :param data: value of node to be searched in linked list
        """

        curr = self.head
        while curr and curr.data != data:
            curr = curr.next

        return curr  # Will be None if not found

    def delete_node(self, data):
        """
        Remove the first occurrence of item in the list.
        Takes O(n) time

        :param data: item to be deleted
        """

        # Find the element and keep the reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next

        # Unlink from the list
        # If head node itself holds the item to be deleted
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def delete_node_at_position(self, position):
        """
        Delete the node at the given position

        :param position: index of the node
        """

        # If linked list is empty
        if self.head is None or position < 0:
            return

        # Store head node
        curr = self.head

        # If head need to be removed
        if position == 0:
            self.head = curr.next
            curr = None
            return

        # Find previous node of the node to be deleted
        for i in range(position-1):
            curr = curr.next
            if curr is None:
                break

        # If position is more than number of nodes
        if curr is None:
            return
        if curr.next is None:
            return

        # Node curr.next is to be deleted
        # Store pointer to the next of node to be deleted
        curr.next = curr.next.next

        # Unlink the node from the linked list
        curr.next = None
        curr.next = next

    def reverse(self):
        """
        Reverse the list in-place

        Takes O(n) time
        """

        curr = self.head
        prev_node = None
        next_node = None

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    def get_count(self):
        """
        Counts number of nodes in linked list

        :return: number of nodes in linked list
        """

        curr = self.head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        return count

    def detect_loop(self) -> bool:
        """
        Detects loop in linked list

        :return: true if there is a loop in linked list
        """

        s = set()
        curr = self.head

        while curr:

            if curr in s:
                return True

            s.add(curr)
            curr = curr.next

        return False

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
