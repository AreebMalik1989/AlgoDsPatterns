/**
 * Barron finishes cooking while Olivia cleans
 */

class KitchenCleaner extends Thread {
    public void run() {
        while (true) {
            System.out.println("Olivia cleaned the kitchen.");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
public class A05_DaemonThread {
    public static void main(String[] args) throws InterruptedException {
        Thread olivia = new KitchenCleaner();
        olivia.setDaemon(true); // Will not block main thread from exiting, and will terminate with main thread.
        olivia.start();

        System.out.println("Barron is cooking...");
        Thread.sleep(600);
        System.out.println("Barron is cooking...");
        Thread.sleep(600);
        System.out.println("Barron is cooking...");
        Thread.sleep(600);
        System.out.println("Barron is done!");
    }
}
