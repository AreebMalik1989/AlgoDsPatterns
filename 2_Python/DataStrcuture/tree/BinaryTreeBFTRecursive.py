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
    Binary tree implementation, with recursive Breadth-First-Traversal (Level-Order-Traversal)
    """

    def __init__(self):
        self.root = None

    def print_level_order(self, node=None):
        """
        Print level order for binary tree

        :param node: Node of binary tree
        :return: None
        """

        if not node:
            node = self.root

        if not node:
            return

        h = self.height(node)
        for i in range(1, h+1):
            self.print_given_level(node, i)

    def print_given_level(self, node, level):
        """
        Print nodes at given level

        :param node: Node of binary tree
        :param level: Level of the node
        :return: None
        """

        if not node:
            return

        if level == 1:
            print(node.data)
        elif level > 1:
            self.print_given_level(node.left, level-1)
            self.print_given_level(node.right, level-1)

    def height(self, node):
        """
        Compute the height of the tree, i.e., the number of nodes along the longest path from the root node down to the
        farthest leaf node

        :param node: Node of the tree
        :return: Height of the tree
        """

        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            l_height = self.height(node.left)
            r_height = self.height(node.right)

            # Use the larger one
            if l_height > r_height:
                return l_height+1
            else:
                return r_height+1
