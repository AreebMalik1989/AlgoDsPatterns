package designpattern.structural.abstractfactory;

public class AbstractFactory {

    private static Application configureApplication() {
        
        String osName = System.getProperty("os.name").toLowerCase();
        if(osName.contains("linux")){
            return new Application(new LinuxFactory());
        } else if(osName.contains("windows")) {
            return new Application(new WindowsFactory());
        }
        return null;
    }

    public static void main(String[] args) {
        Application app = configureApplication();
        app.paint();
    }
}

class Application {

    private Button button;
    private Checkbox checkbox;

    public Application(GuiFactory factory) {
        button = factory.createButton();
        checkbox = factory.createCheckbox();
    }

    public void paint() {
        button.paint();
        checkbox.paint();
    }
}

interface GuiFactory {
    Button createButton();
    Checkbox createCheckbox();
}

interface Button {
    void paint();
}

interface Checkbox {
    void paint();
}

class WindowsFactory implements GuiFactory {

    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}

class LinuxFactory implements GuiFactory {

    @Override
    public Button createButton() {
        return new LinuxButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new LinuxCheckbox();
    }
}

class WindowsButton implements Button {
    @Override
    public void paint() {
        System.out.println("You have created Windows button.");
    }
}

class LinuxButton implements Button {
    @Override
    public void paint() {
        System.out.println("You have created Linux button.");
    }
}

class WindowsCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("You have created Windows checkbox");
    }
}

class LinuxCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("You have created Linux checkbox");
    }
}

