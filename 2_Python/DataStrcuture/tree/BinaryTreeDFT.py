class Node:
    """
    Node for Binary Tree
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Class implementation of Binary Tree, With Depth-First-Traversal
    """

    def __init__(self):
        self.root = None

    def print_in_order(self, node=None):
        """
        In order tree traversal (left, root, right)

        :param node: Node of binary tree
        :return: None
        """

        if not node:
            node = self.root

        if node:

            # First recur on left child
            self.print_in_order(node.left)

            # Then print the data of node
            print(node.data)

            # Now recur on right child
            self.print_in_order(node.right)

    def print_pre_order(self, node=None):
        """
        Pre order tree traversal (root, left, right)

        :param node: Node of binary tree
        :return: None
        """

        if not node:
            node = self.root

        if node:

            # First print the data of node
            print(node.data)

            # Then recur on left child
            self.print_pre_order(node.left)

            # Finally recur on right child
            self.print_pre_order(node.right)

    def print_post_order(self, node=None):
        """
        Post order tree traversal (left, right, root)

        :param node: Node of binary tree
        :return: None
        """

        if not node:
            node = self.root

        if node:

            # First recur on left child
            self.print_post_order(node.left)

            # Then recur on right child
            self.print_post_order(node.right)

            # Finally print the data of the node
            print(node.data)
