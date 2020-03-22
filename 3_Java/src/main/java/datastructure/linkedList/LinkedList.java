package datastructure.linkedlist;

public class LinkedList {
    
    Node head;

    public class Node {

        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    public void push(int newData) {

        Node newNode = new Node(newData);
        newNode.next = head;
        head = newNode;

    }

    public void insertAfter(Node previousNode, int newData) {

        if(previousNode == null) {
            System.out.println("The given previous node cannot be null");
            return;
        }

        Node newNode = new Node(newData);
        newNode.next = previousNode.next;
        previousNode.next = newNode;
    }

    public void append(int newData) {

        Node newNode = new Node(newData);

        if(head == null) {
            head = new Node(newData);
            return;
        }

        newNode.next = null;

        Node last = head;
        while(last.next != null) {
            last = last.next;
        }

        last.next = newNode;
    }

    public void deleteNode(int key) {

        Node temp = head, prev = null;

        if(temp != null && temp.data == key) {
            head = temp.next;
            return;
        }

        while(temp != null && temp.data != key) {
            prev = temp;
            temp = temp.next;
        }

        if(temp == null) return;

        prev.next = temp.next;
    }

    public void deleteNodeAt(int position) {

        if(head == null) {
            return;
        }

        Node temp = head;

        if(position == 0){
            head = temp.next;
            return;
        }

        for(int i=0; temp!=null && i<position-1; i++) {
            temp = temp.next;
        }

        if(temp == null || temp.next == null) {
            return;
        }

        Node next = temp.next.next;
        temp.next = next;
    }

    public void deleteList() {
        head = null;
    }

    public int getCount() {

        Node temp = head;
        int count = 0;

        while(temp != null) {
            count++;
            temp = temp.next;
        }

        return count;
    }

    public int search(int key) {

        int postion = 0;
        Node current = head;

        while(current != null) {

            if(current.data == key) {
                return postion;
            }

            postion++;
            current = current.next;
        }

        return -1;
    }

    public int getNth(int index) throws Exception{

        Node current = head;
        int position = 0;

        while(current != null) {

            if(position == index){
                return current.data;
            }

            position++;
            current = current.next;
        }

        throw new Exception("Element not found");
    }

    public void printList() {

        Node temp = head;
        while(temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }
}
