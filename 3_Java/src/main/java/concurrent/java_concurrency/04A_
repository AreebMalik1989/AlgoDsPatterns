class SharedQueue<T> {

    private final int capacity;
    private LinkedList<T> queue = new LinkedList<>();
    private ReentrantLock lock = new ReentrantLock();
    private Condition queueEmptyCondition = lock.newCondition();
    private Condition queueFullCondition = lock.newCondition();

    public SharedQueue(int capacity) {
        this.capacity = capacity;
    }

    public void add(T item) throws InterruptedException {
        try {
            lock.lock();
            while (queue.size() == capacity) { // Need to use 'while' instead of 'if' to guard against spurious wake up
                queueFullCondition.await();
            }
            queue.addFirst(item);
            queueEmptyCondition.signalAll();
        } finally {
            lock.unlock();
        }
    }

    public T remove() throws InterruptedException {
        try {
            lock.lock();
            while (queue.size() == 0) { // Need to use 'while' instead of 'if' to guard against spurious wake up
                queueEmptyCondition.await();
            }
            return queue.removeLast();
        } finally {
            queueFullCondition.signalAll();
            lock.unlock();
        }
    }
}

class Producer<T> extends Thread{

    private final SharedQueue<T> queue;
    private Supplier<T> supplier;

    public Producer(SharedQueue<T> queue, Supplier<T> supplier) {
        this.queue = queue;
        this.supplier = supplier;
    }

    @Override
    public void run() {
        try {
            while (true) {
                Thread.sleep(1000);
                T item = supplier.get();
                queue.add(item);
                System.out.println("Produced: " + item);
            }
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}

class Consumer<T> extends Thread {

    private final SharedQueue<T> queue;

    public Consumer(SharedQueue<T> queue) {
        this.queue = queue;
    }

    @Override
    public void run() {
        try {
            while(true) {
                Thread.sleep(2000);
                T item = queue.remove();
                System.out.println("Consumed: " + item);
            }
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}

public class TempUtil {

    public static void main(String[] args) {

        Supplier<Integer> supplier = () -> 1;
        SharedQueue<Integer> queue = new SharedQueue<>(5);
        Producer<Integer> producer = new Producer<>(queue, supplier);
        Consumer<Integer> consumer = new Consumer<>(queue);

        producer.start();
        consumer.start();
    }
}
