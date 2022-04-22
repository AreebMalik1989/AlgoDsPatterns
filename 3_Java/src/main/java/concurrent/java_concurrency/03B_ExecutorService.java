public class JavaCachedThreadPoolExecutor {
  
  static Runnable ioBoundTask = () -> System.out.println("Thread Name: " + Thread.currentThread().getName());

    public static void main(String[] args) {
        ExecutorService service = Executors.newCachedThreadPool();

        final int TASK_COUNT = 1000;
        for (int i = 0; i < TASK_COUNT; i++) {
            service.submit(ioBoundTask);
        }

        System.out.println("Thread Name: " + Thread.currentThread().getName());

        service.shutdown();
    }
}
