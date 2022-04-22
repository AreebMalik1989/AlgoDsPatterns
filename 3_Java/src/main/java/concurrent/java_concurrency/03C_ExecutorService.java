public class JavaScheduledThreadPool {
    
    private static Runnable task = () -> System.out.println("Thread Name: " + Thread.currentThread().getName());
    private static boolean shouldCancel = true;

    public static void main(String[] args) {

        ScheduledExecutorService service = Executors.newWorkStealingPool()

        final int INITIAL_DELAY = 10;
        final int DELAY = 12;
        final int PERIOD = 15;

        // Task run after DELAY seconds
        service.schedule(task, DELAY, TimeUnit.SECONDS);

        // Task run repeatedly every PERIOD seconds
        service.scheduleAtFixedRate(task, INITIAL_DELAY, PERIOD, TimeUnit.SECONDS);

        // task run repeatedly DELAY seconds after previous task completes
        ScheduledFuture<?> scheduledFuture = service.scheduleWithFixedDelay(task, INITIAL_DELAY, DELAY, TimeUnit.SECONDS);
        
        if(shouldCancel) {
            boolean shouldInterrupt = false;
            scheduledFuture.cancel(shouldInterrupt);
        }

        service.shutdown();
    }
}
