public class AtomicJava {
    
    private static class Counter {

        private AtomicInteger c = new AtomicInteger(0);

        public void increment() {
            c.getAndIncrement();
        }

        public int value() {
            return c.get();
        }
    }
    
    public static void main(String args[]) throws Exception {
        
        Counter c = new Counter();
        
        final int THREAD_COUNT = 1000
        for(int i=0; i<THREAD_COUNT; i++) {
            new Thread(() -> counter.increment()).start();
        }
        
        Thread.sleep(5000);
        System.out.println("Final number (should be 1000): " + counter.value());
    }
}
        
