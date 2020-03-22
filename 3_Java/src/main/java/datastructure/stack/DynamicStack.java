package datastructure.stack;

public class DynamicStack {

    private int[] array;
    private int size;
    private int top;

    /**
     * constructor to create stack with size
     * @param size
     */
    public DynamicStack(int size) {

        this.array = new int[size];
        this.size = size;
        top = -1;
    }

    /**
     * This method adds new entry to the top
     * of the stack
     * @param entry : element to be added in stack
     */
    public void push(int entry) {

        if(this.isStackFull()){
            System.out.println("Stack is full. Increasing the capacity.");
            increaseCapacity();
        }

        System.out.println("Adding entry: " + entry);
        array[++top] = entry;
    }

    /**
     * This method removes an entry from the
     * top of the stack.
     * @return
     * @throws Exception
     */
    public int pop() throws Exception {

        if(this.isStackEmpty())
            throw new Exception("Stack is empty.");

        int entry = array[top--];
        System.out.println("Removing entry: " + entry);
        return entry;
    }

    /**
     * This method returns top of the stack
     * without removing it.
     * @return
     * @throws Exception
     */
    public int peek() throws Exception {
        
        if(this.isStackEmpty())
            throw new Exception("Stack is empty.");
        
        return array[top];
    }

    /**
     * This method returns true if the stack is
     * empty
     * @return
     */
    public boolean isStackEmpty() {
        return (top == -1);
    }

    /**
     * This method returns true if the stack is full
     * @return
     */
    public boolean isStackFull() {
        return (top == size-1);
    }

    private void increaseCapacity() {

        int[] newStack = new int[size*2];
        for(int i=0; i<size; i++)
            newStack[i] = array[i];

        array = newStack;
        size = newStack.length;
    }
}
