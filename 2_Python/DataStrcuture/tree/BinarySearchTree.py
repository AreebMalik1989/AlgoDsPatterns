class Node:
    """
    Node for binary search tree
    """

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    """
    BST implementation
    """

    def __init__(self):
        self.root = None

    def insert(self, value, node=None):
        """
        Insert node in BST

        :param value: value of node to be inserted
        :param node: node of BST
        :return: true if the node is inserted successfully
        """

        if node is None:

            if self.root is None:
                self.root = Node(value)
                return True
            else:
                return self.insert(value, self.root)

        else:

            if value < node.value:

                if node.left is None:
                    node.left = Node(value)
                    return True
                else:
                    return self.insert(value, node.left)

            elif value > node.value:

                if node.right is None:
                    node.right = Node(value)
                    return True
                else:
                    return self.insert(value, node.right)

            else:

                return False

    def delete_node(self, value, node=None):
        """
        Deletes the node with given value and return the new root

        :param value: data of the node to be deleted
        :return: new root
        """

        if node is None:
            node = self.root

        # Base case
        if node is None:
            return node

        if value < node.value:
            node.left = self.delete_node(value, node.left)
        elif value > node.value:
            node.right = self.delete_node(value, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

        # Node with two children: Get the in-order successor
        # (smallest in the right subtree)
        temp = self.min_value_node(node.right)

        # Copy the in-order successor's content to this node
        node.value = temp.value

        # Delete the in-order successor
        node.right = self.delete_node(temp.value, node.right)

    def min_value_node(self, node=None):
        """
        Returns the minimum value node

        :param node: node of the BST
        :return: minimum value node
        """

        if node is None:
            node = self.root

        current = node

        # Loop down to find the leftmost leaf
        while current.left:
            current = current.left

        return current

    def search(self, value):
        """
        Search node in binary search tree

        :param value: value of node to be search
        :return: true if the value is found
        """

        curr = self.head

        while curr:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True

        return False

    def print_in_order(self, node=None):
        """
        Print the BST in order

        :param node: node of BST
        :return: None
        """

        if node is None:
            node = self.root

        if node is not None:
            self.print_in_order(node.left)
            print("Traversed:", node.value)
            self.print_in_order(node.right)
