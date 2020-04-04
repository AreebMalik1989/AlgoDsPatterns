package designpattern.creational.factory;

/**
 * Common interface for all buttons
 */
interface SystemInfo {
    void show();
}

/**
 * Windows info implementation
 */
class WindowsInfo implements SystemInfo {

    @Override
    public void show() {
        System.out.println("You are using Windows operating system.");
    }
}

/**
 * Linux info implementation
 */
class LinuxInfo implements SystemInfo {

    @Override
    public void show() {
        System.out.println("You are using Linux operating system.");
    }
}

class SystemInfoFactory {
    public static SystemInfo getSystemInfo() {
        if(System.getProperty("os.name").startsWith("Window")) {
            return new WindowsInfo();
        } else if (System.getProperty("os.name").startsWith("Linux")) {
            return new LinuxInfo();
        }
        return null;
    }
}

class FactoryDemo1 {

    public static void main(String args[]) {
        SystemInfo systemInfo = SystemInfoFactory.getSystemInfo();
        systemInfo.show();
    }
}