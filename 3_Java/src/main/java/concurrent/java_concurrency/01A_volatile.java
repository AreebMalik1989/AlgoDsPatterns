/**
Without volatile keyword when the main thread updates the number and ready variables,
there is no guarantee about what the reader thread may see.
In other words, the reader thread may see the updated value right away,
or with some delay, or never at all!
*/

public class TaskRunner {
    
    private static volatile int number;
    private static volatile boolean ready;
    
    private static class Reader extends Thread {
        
        @Override
        public void run() {
            while(!ready) Thread.yield();
            System.out.println(number);
        }
    }
    
    public static void main(String[] args) {
        new Reader().start();
        number = 42;
        ready = true;
    }
}
        
