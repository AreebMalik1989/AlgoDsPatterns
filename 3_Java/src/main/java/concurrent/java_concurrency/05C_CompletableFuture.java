public class CorrectImplementation {
    public static void main(String[] args) {
        for(int i=0; i<100; i++) {
            CompletableFuture.supplyAsync(() -> getOrder())
                    .thenApply(order -> enrich(order))
                    .thenApply(order -> performPayment(order))
                    .thenApply(order -> dispatch(order))
                    .thenAccept(order -> sendEmail(order));
        }
    }
}
