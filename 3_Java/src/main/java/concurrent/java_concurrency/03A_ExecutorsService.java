public class FixedThreadPoolExecutor {
    
    private static Runnable cpuBoundTask = () -> System.out.println("Thread Name: " + Thread.currentThread().getName());
    
    public static void main(String[] args) {
        
        ExecutorService service = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

        final int TASK_COUNT = 1000;
        for (int i = 0; i < TASK_COUNT; i++) {
            service.submit(cpuBoundTask);
        }

        System.out.println("Thread Name: " + Thread.currentThread().getName());

        service.shutdown();
    }
}
