package designpattern.structural.prototype;

import java.util.ArrayList;
import java.util.List;

class Employees implements Cloneable {

    private List<String> empList;

    public Employees() {
        empList = new ArrayList<String>();
    }

    public Employees(List<String> empList) {
        this.empList = empList;
    }

    public void loadData() {
        // read all employees from database and put into the list
        empList.add("Pankaj");
        empList.add("Raj");
        empList.add("David");
        empList.add("Lisa");
    }

    public List<String> getEmpList() {
        return empList;
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        List<String> temp = new ArrayList<String>();
        for(String s: this.getEmpList()) {
            temp.add(s);
        }
        return new Employees(temp);
    }
}

class Demo {
    
    public static void main(String[] args) throws CloneNotSupportedException {
        Employees emps = new Employees();
        emps.loadData();

        // Use the clone method to get the Employee object
        Employees emps1 = (Employees) emps.clone();
        Employees emps2 = (Employees) emps.clone();

        List<String> list1 = emps1.getEmpList();
        list1.add("John");

        List<String> list2 = emps2.getEmpList();
        list2.remove("Pankaj");

        System.out.println("emps:  " + emps.getEmpList());
        System.out.println("emps1: " + emps1.getEmpList());
        System.out.println("emps2: " + emps2.getEmpList());
    }
}