record User(String userName) {}

class UserContextHolder {
    public static ThreadLocal<User> holder = new ThreadLocal<>();
}

class Service1 {
    public void process() {
        // Get user
        User user = new User("username");
        UserContextHolder.holder.set(user);
        // Do some processing
    }
}

class Service2 {
    public void process() {
        User user = UserContextHolder.holder.get();
        // Do some processing
    }
}

class Service3 {
    public void process() {
        User user = UserContextHolder.holder.get();
        // Do some processing
        UserContextHolder.holder.remove();;
    }
}
