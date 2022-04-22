public class JavaExecutorService {
    
    public static void main(String[] args) {
        
        ExecutorService service = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

        final int TASK_COUNT = 1000;
        for (int i = 0; i < TASK_COUNT; i++) {
            service.submit(() -> System.out.println("Thread Name: " + Thread.currentThread().getName()));
        }

        System.out.println("Thread Name: " + Thread.currentThread().getName());

        service.shutdown();
    }
}
