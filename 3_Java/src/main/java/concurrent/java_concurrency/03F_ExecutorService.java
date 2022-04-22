public class JavaSingleThreadExecutor {
    
    private static final BlockingQueue<Integer> queue = new LinkedBlockingQueue<>();

    private static final Runnable task = () -> {
        try {
            Thread.sleep(1000);
            queue.put(new Random().nextInt());
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    };

    public static void main(String[] args) throws Exception{

        ExecutorService service = Executors.newSingleThreadExecutor();

        final int TASK_COUNT = 10;
        for (int i = 0; i < TASK_COUNT; i++) {
            service.execute(task);
        }

        for (int i = 0; i < TASK_COUNT; i++) {
            System.out.println("" + queue.take());
        }

        service.shutdown();
    }
}
