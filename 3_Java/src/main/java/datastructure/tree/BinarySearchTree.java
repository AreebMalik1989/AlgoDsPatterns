package datastructure.tree;

public class BinarySearchTree {

    private Node root;

    public boolean insert(int value) {

        if(root == null) {
            root = new Node(value);
            return true;
        } else {
            return insert(root, value);
        }

    }

    private boolean insert(Node node, int value) {

        if(value < node.value) {
            if(node.left == null) {
                node.left = new Node(value);
                return true;
            } else {
                return insert(node.left, value);
            }
        } else if(value > node.value) {
            if(node.right == null) {
                node.right = new Node(value);
                return true;
            } else {
                return insert(node.right, value);
            }
        } else {
            return false;
        }
    }

    public void printInOrder(Node node){

        if(node != null) {
            printInOrder(node.left);
            System.out.println("Traversed: " + node.value);
            printInOrder(node.right);
        }

    }

}

class Node {

    Node left;
    Node right;
    int value;

    public Node(int value){

        this.value = value;
    }
}

