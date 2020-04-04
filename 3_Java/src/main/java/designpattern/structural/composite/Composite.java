package designpattern.structural.composite;

import java.util.ArrayList;
import java.util.List;

interface Employee {
    void showEmployeeDetails();
}

class Developer implements Employee {
    
    private String name;
    private long empId;
    private String position;

    public Developer(String name, long empId, String position) {
        this.name = name;
        this.empId = empId;
        this.position = position;
    }

    @Override
    public void showEmployeeDetails() {
        System.out.println(
            "name: " + name + "\n" + "empId: " + empId + "\n" + "position: " + position
        );
    }
}

class Manager implements Employee {
    
    private String name;
    private long empId;
    private String position;

    public Manager(String name, long empId, String position) {
        this.name = name;
        this.empId = empId;
        this.position = position;
    }

    @Override
    public void showEmployeeDetails() {
        System.out.println(
            "name: " + name + "\n" + "empId: " + empId + "\n" + "position: " + position
        );
    }
}

class CompanyDirectory implements Employee {

    private List<Employee> employeeList = new ArrayList<Employee>();

    @Override
    public void showEmployeeDetails() {
        for(Employee emp: employeeList) {
            emp.showEmployeeDetails();
        }
    }

    public void addEmployee(Employee emp) {
        employeeList.add(emp);
    }

    public void removeEmployee(Employee emp) {
        employeeList.remove(emp);
    }
}

class Company {
    public static void main(String[] args) {
        Developer dev1 = new Developer("Lokesh Sharma", 100, "Pro Developer"); 
        Developer dev2 = new Developer("Vinay Sharma", 101, "Developer"); 
        CompanyDirectory engDirectory = new CompanyDirectory(); 
        engDirectory.addEmployee(dev1); 
        engDirectory.addEmployee(dev2); 
          
        Manager man1 = new Manager("Kushagra Garg", 200, "SEO Manager"); 
        Manager man2 = new Manager("Vikram Sharma ", 201, "Kushagra's Manager"); 
          
        CompanyDirectory accDirectory = new CompanyDirectory(); 
        accDirectory.addEmployee(man1); 
        accDirectory.addEmployee(man2); 
      
        CompanyDirectory directory = new CompanyDirectory(); 
        directory.addEmployee(engDirectory); 
        directory.addEmployee(accDirectory); 
        directory.showEmployeeDetails(); 
    }
}