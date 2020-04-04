package designpattern.structural.facade;

class Facade {

    private SubSystem1 system1;
    private SubSystem2 system2;

    public Facade(SubSystem1 system1, SubSystem2 system2) {
        this.system1 = system1;
        this.system2 = system2;
    }

    public String operation() {
        StringBuffer results = new StringBuffer();
        results.append("Facade intializes subsytems:" + "\n");
        results.append(system1.operation1() + "\n");
        results.append(system2.operation1() + "\n");
        results.append("Facade orders subsystems to perform the action:" + "\n");
        results.append(system1.operation_n() + "\n");
        results.append(system2.operation_z() + "\n");

        return results.toString();
    }
}

class SubSystem1 {

    public String operation1() {
        return "Subsystem1: Ready!";
    }

    public String operation_n() {
        return "Subsystem1: Go!";
    }
}

class SubSystem2 {

    public String operation1() {
        return "Subsystem2: Get ready!";
    }

    public String operation_z() {
        return "Subsystem2: Fire!";
    }
}

class Demo {

    public static void main(String[] args) {

        SubSystem1 system1 = new SubSystem1();
        SubSystem2 system2 = new SubSystem2();
        Facade facade = new Facade(system1, system2);
        System.out.println(facade.operation());
    }
}