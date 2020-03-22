# Generic tree node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
# Delete operation
class AVLTree:

    # Recursive function to insert item in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, item):

        # Step 1 - Perform normal BST
        if not root:
            return Node(item)
        elif item < root.value:
            root.left = self.insert(root.left, item)
        else:
            root.right = self.insert(root.right, item)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and item < root.left.value:
            return self.right_rotate(root)

        # Case 2 - Right Right
        if balance < -1 and item > root.right.value:
            return self.left_rotate(root)

        # Case 3 - Left Right
        if balance > 1 and item > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and item < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Recursive function to delete a node with
    # given item from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, item):

        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif item < root.value:
            root.left = self.delete(root.left, item)

        elif item > root.value:
            root.right = self.delete(root.right, item)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        # Now, if the tree has only one node,
        # simply return it
        if root is None:
            return root

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.right_rotate(root)

            # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.left_rotate(root)

            # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

            # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):

        y = z.right
        t2 = y.left

        # Perform rotation
        y.left = z
        z.right = t2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))

        # Return the new root
        return y

    def right_rotate(self, z):

        y = z.left
        t3 = y.right

        # Perform rotation
        y.right = z
        z.left = t3

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))

        # Return the new root
        return y

    def get_height(self, root):

        if not root:
            return 0

        return root.height

    def getBalance(self, root):

        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):

        if root is None or root.left is None:
            return root

        return self.get_min_value_node(root.left)

    def pre_order(self, root):

        if not root:
            return

        print("{0} ".format(root.value), end='')
        self.pre_order(root.left)
        self.pre_order(root.right)
