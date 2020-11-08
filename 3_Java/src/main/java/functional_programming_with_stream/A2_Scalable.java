// Interfaces provides behaviour only, as they dont have states (member variables).
public interface Scalable {

    // Implicitly public abstract
    void setScale(double scale);
    
    // Implicitly public static final
    double DEFAULT_SCALE = 1.0;
    
    // Implicitly public
    static boolean isScalable(Object obj) {
        return obj instanceof Scalable;
    }
}
