/**
 * Threads that waste CPU cycles
 */

// a simple thread that wastes CPU cycles forever
class CPUWaster extends Thread {
    public void run() {
        while (true) {}
    }
}

public class A01_MultipleThreads {

    private static final Runtime RUNTIME = Runtime.getRuntime();
    private static final int USE_CORES = RUNTIME.availableProcessors()==1? 1 :RUNTIME.availableProcessors()/2;

    public static void main(String[] args) {
        displayProcessInfo();
        startNewThreads();
        displayProcessInfo();
    }

    private static void startNewThreads() {
        System.out.println("\nStarting " + USE_CORES + " CPUWaster threads...\n");
        for (int i = 0; i< USE_CORES; i++)
            new CPUWaster().start();
    }

    private static void displayProcessInfo() {
        long usedKB = (RUNTIME.totalMemory() - RUNTIME.freeMemory()) / 1024 ;
        System.out.format("  Process ID: %d\n", ProcessHandle.current().pid());
        System.out.format("Thread Count: %d\n", Thread.activeCount());
        System.out.format("Memory Usage: %d KB\n", usedKB);
    }
}
