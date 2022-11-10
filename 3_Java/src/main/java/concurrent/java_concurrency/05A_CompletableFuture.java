public class Main {
    
    public static void main(String[] args) {
        ExecutorService service = Executors.newFixedThreadPool(2);
        Future<Integer> future = service.submit(new Task());
        try {
            Integer result = future.get();
            System.out.println("Result from task is: " + result);
        } catch (ExecutionException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static class Task implements Callable<Integer> {
        @Override
        public Integer call() throws Exception {
            return new Random().nextInt();
        }
    }
}
