package designpattern.creational.singleton;

import java.io.Serializable;

/*
* Bill Pugh Singleton
* This is the most widely used approach as it doesn’t use synchronization.
* When the singleton class is loaded, inner class is not loaded and hence
* doesn’t create object when loading the class. Inner class is created only
* when getInstance() method is called. So it may seem like eager initialization
* but it is lazy initialization.
*/
class SingletonExample {

    private SingletonExample(){}

    // Inner class to provide instance of class
    private static class BillPughSingleton {
        private static final SingletonExample INSTANCE = new SingletonExample();
    }

    public static SingletonExample getInstance() {
        return BillPughSingleton.INSTANCE;
    }
}

/**
 * Enum, as written in java docs, provided implicit support for thread safety
 * and only one instance is guaranteed. Java enum singleton is also a good
 * way to have singleton with minimal effort.
 */
enum EnumSingleton {
    INSTANCE;
    public void someMethod(String s) {
        // some class member
    }
}

/**
 * With so many possible approaches and error cases, below template is
 * recomended, which is serializable.
 */
class SerializableSingleton implements Serializable {

    /**
     * This is required in cases where your class structure changes between
     * serialization and deserialization. A changed class structure will cause
     * the JVM to give an exception in the de-serializing process.
     * 
     * It will prevent the compiler from throwing the exception by telling it
     * that both classes are same, and will load the available instance
     * variables only.
     */
    private static final long serialVersionUID = 1L;

    private SerializableSingleton(){}
    
    private static class SerializableSingletonHolder {
        public static final SerializableSingleton INSTANCE = new SerializableSingleton();
    }

    public static SerializableSingleton getInstance() {
        return SerializableSingletonHolder.INSTANCE;
    }

    /**
     * This method will be invoked when you will de-serialize the object.
     * Inside of this method, you must return the existing instance to ensure
     * a single instance application wide.
     */
    protected Object readResolve() {
        return getInstance();
    }
}

// Early instantiation
class Early {
    
    private static final Early INSTANCE = new Early();

    private Early(){}

    public static Early getInstance() {
        return INSTANCE;
    }
}

// Lazy instantiation
class Lazy {

    private static Lazy INSTANCE;

    private Lazy(){}

    public static Lazy getInstance() {
        if(INSTANCE == null) {
            INSTANCE = new Lazy();
        }
        return INSTANCE;
    }
}

// Thread safe singleton
class ThreadSafe {

    private static ThreadSafe INSTANCE;

    private ThreadSafe(){}

    // synchronized method to control simultaneous access
    synchronized public static ThreadSafe getInstance() {
        if(INSTANCE == null) {
            INSTANCE = new ThreadSafe();
        }
        return INSTANCE;
    }
}

/*
* Thread safe with Double check locking
* In this mechanism, we overcome the overhead problem of synchronized code. In
* this method, getInstance is not synchronized but the block which creates
* instance is synchronized so that minimum number of threads have to wait and
* that’s only for first time.
*/
class DoubleCheckLocking {

    private static DoubleCheckLocking INSTANCE;

    private DoubleCheckLocking(){}

    public static DoubleCheckLocking getInstance() {
        if(INSTANCE == null) {
            // synchronized block to remove overhead
            synchronized(DoubleCheckLocking.class) {
                if(INSTANCE == null) {
                    INSTANCE = new DoubleCheckLocking();
                }
            }
        }
        return INSTANCE;
    }
}