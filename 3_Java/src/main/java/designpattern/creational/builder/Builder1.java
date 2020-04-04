package designpattern.creational.builder;

final class Student {
    // final instance fields
    private final int id;
    private final String name;
    private final String address;

    public Student(Builder builder) {
        this.id = builder.id;
        this.name = builder.name;
        this.address = builder.address;
    }

    public static class Builder {
        private int id;
        private String name;
        private String address;

        public Builder(){}

        public Builder setId(int id){
            this.id = id;
            return this;
        }

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder setAddress(String address) {
            this.address = address;
            return this;
        }

        public Student build(){
            return new Student(this);
        }
    }

    public static void main(String[] args) {
        Student s = new Student.Builder()
                    .setId(1)
                    .setName("test")
                    .setAddress("Test Address")
                    .build();

        System.out.println("id: " + s.id);
        System.out.println("name: " + s.name);
        System.out.println("address: " + s.address);
    }
}