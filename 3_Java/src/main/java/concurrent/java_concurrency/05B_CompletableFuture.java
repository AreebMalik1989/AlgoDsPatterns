public class IncorrectImplementation {
    public static void main(String[] args) {
        ExecutorService service = Executors.newFixedThreadPool(2);
        try {
            Future<Order> future1 = service.submit(getOrderTask());
            Order order = future1.get();    // blocking

            Future<Order> future2 = service.submit(enrichTask(order));
            order = future2.get();  // blocking

            Future<Order> future3 = service.submit(performPaymentTask(order));
            order = future3.get();  // blocking

            Future<Order> future4 = service.submit(dispatchTask(order));
            order = future4.get();  // blocking

            Future<Order> future5 = service.submit(sendEmailTask(order));
            order = future5.get();  // blocking
            
        } catch (ExecutionException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
