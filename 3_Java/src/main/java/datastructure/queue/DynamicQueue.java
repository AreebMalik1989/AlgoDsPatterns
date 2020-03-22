package queue;

public class DynamicQueue {

    private int [] array;
    private int front, end, size;

    // maxSize is the maximum number of items
    // that can be in the queue at any given time
    public DynamicQueue(int maxSize) {
        front = end = 0;
        size = maxSize+1;
        array = new int[size];
    }

    // Return true/false on whether the queue is empty
    public boolean isEmpty() {
        return front == end;
    }

    // Return the number of elements inside the queue
    public int size() {
        if (front > end)
            return (end + size - front);
        return end - front;
    }

    public int peek() {
        return array[front];
    }

    // Add an element to the queue
    public void enqueue(int value) {
        array[end] = value;
        if (++end == size) end = 0;
        if (end == front) {
            System.out.println("Queue too small! Increasing the capacity");
            increaseCapacity();
        }
    }

    // Make sure you check is the queue is not empty before calling dequeue!
    public int dequeue() {
        int ret_val = array[front];
        if (++front == size) front = 0;
        return ret_val;
    }

    private void increaseCapacity() {

        int[] newStack = new int[size*2];
        for(int i=0; i<size; i++)
            newStack[i] = array[i];

        array = newStack;
        size = newStack.length;
    }
}
