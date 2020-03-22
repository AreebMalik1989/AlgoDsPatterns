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
    Binary tree implementation, with iterative Breadth-First-Traversal (Level-Order-Traversal)
    """

    def __init__(self):
        self.root = None

    def print_level_order(self, node=None):
        """
        Iterative method to print the height of binary tree

        :param node: Node of the Binary Tree
        :return: None
        """

        if node is None:
            node = self.root

        if node is None:
            return

        # Create empty queue for level order traversal
        q = list()

        # Enqueue node and initialize height
        q.append(node)

        while len(q) > 0:

            # Print front of queue and remove from the queue
            print(q[0].data),
            node = q.pop(0)

            # Enqueue left child
            if node.left:
                q.append(node.left)

            # Enqueue right child
                q.append(node.right)
