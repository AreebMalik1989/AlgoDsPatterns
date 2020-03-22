package datastructure.stack;

public class GenericStack1<T extends Object> {

    private T array[];
    private int size;
    private int top;

    /**
     * constructor to create stack with size
     * @param size
     */
    @SuppressWarnings("unchecked")
    public GenericStack1(int size) {

        this.array = (T[]) new Object[size];
        this.size = size;
        this.top = -1;
    }

    /**
     * This method adds new entry to the top
     * of the stack
     * @param entry
     */
    public void push(T entry) {

        if(this.isStackFull()) {
            System.out.println("Stack is full. Increasing the capacity.");
            this.increaseStackCapacity();
        }

        System.out.println("Adding entry: " + entry);
        this.array[++top] = entry;
    }

    /**
     * This method removes an entry from the
     * top of the stack.
     * @return
     * @throws Exception
     */
    public T pop() throws Exception {

        if(this.isStackEmpty()){
            throw new Exception("Stack is empty. Cannot remove element.");
        }

        T entry = array[top--];
        System.out.println("Removing entry: " + entry);
        return entry;
    }

    /**
     * This method returns top of the stack
     * without removing it.
     * @return
     */
    public T peek(){
        return array[top];
    }

    /**
     * This method returns true if the stack is full
     * @return
     */
    public boolean isStackFull() {
        return (top == size-1);
    }

    /**
     * This method returns true if the stack is
     * empty
     * @return
     */
    public boolean isStackEmpty() {
        return (top == -1);
    }

    private void increaseStackCapacity() {

        @SuppressWarnings("unchecked")
        T[] newStack = (T[]) new Object[this.size*2];
        for(int i=0; i<size; i++) {
            newStack[i] = this.array[i];
        }

        this.array = newStack;
        this.size = this.size*2;
    }
}
