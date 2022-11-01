public class SharedStack<T> {

    private final int capacity;
    private Stack<T> stack = new Stack<>();
    private ReentrantLock lock = new ReentrantLock();
    private Condition stackEmptyCondition = lock.newCondition();
    private Condition stackFullCondition = lock.newCondition();

    public SharedStack(int capacity) {
        this.capacity = capacity;
    }

    public void push(T item) throws InterruptedException {
        try {
            lock.lock();
            while (stack.size() == capacity) { // Need to use 'while' instead of 'if' to guard against spurious wake up
                stackFullCondition.await();
            }
            stack.push(item);
            stackEmptyCondition.signalAll();
        } finally {
            lock.unlock();
        }
    }

    public T pop() throws InterruptedException {
        try {
            lock.lock();
            while (stack.size() == 0) { // Need to use 'while' instead of 'if' to guard against spurious wake up
                stackEmptyCondition.await();
            }
            return stack.pop();
        } finally {
            stackFullCondition.signalAll();
            lock.unlock();
        }
    }
}
