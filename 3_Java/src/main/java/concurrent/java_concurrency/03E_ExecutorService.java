public class JavaFutures {
    
    private static final Callable<Integer> task = () -> {
        Thread.sleep(1000);
        return new Random().nextInt();
    };

    private static final List<Callable<Integer>> callables = new LinkedList<>();

    public static void main(String[] args) throws Exception{

        ExecutorService service = Executors.newCachedThreadPool();

        final int TASK_COUNT = 1000;
        for (int i = 0; i < TASK_COUNT; i++) {
            callables.add(task);
        }

        List<Future<Integer>> futures = service.invokeAll(callables);
        for (var future : futures) {
            System.out.println("" + future.get());
        }
    }
}
