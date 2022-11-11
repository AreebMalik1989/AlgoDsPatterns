public class IOBoundExample {
    public static void main(String[] args) {
        ExecutorService cpuBound = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        ExecutorService ioBound = Executors.newCachedThreadPool();
        for(int i=0; i<100; i++) {
            CompletableFuture.supplyAsync(() -> getOrder(), ioBound)    // performed in ioBound thread pool
                    .thenApply(order -> enrich(order), cpuBound)    // performed in cpuBound thread pool
                    .thenApply(order -> performPayment(order), ioBound) // performed in ioBound thread pool
                    .exceptionally(e -> new FailedOrder())  // catch exception in any of above steps
                    .thenApply(order -> dispatch(order))    // performed in default fork join pool
                    .thenAccept(order -> sendEmail(order)); // performed in default fork join pool
        }
    }
}
