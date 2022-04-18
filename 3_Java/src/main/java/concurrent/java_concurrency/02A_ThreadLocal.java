public class UserService {

    private static final ExecutorService threadPool = Executors.newFixedThreadPool(10);

    public static void main(String[] args) {
        final int THREAD_COUNT = 1000;
        for (int i=0; i<THREAD_COUNT; i++) {
            int id = i;
            threadPool.submit(() -> {
                String birthDate = new UserService().birthDate(id);
                System.out.println(birthDate);
            });
        }
        Thread.sleep(1000);
    }

    public String birthDate(int userId) {
        Date birthDate = birthDateFromDB(userId);
        final SimpleDateFormat df = ThreadSafeFormatter.dateFormatter.get();
        return df.format(birthDate);
    }

}

class ThreadSafeFormatter {

    public static ThreadLocal<SimpleDateFormat> dateFormatter = new ThreadLocal<SimpleDateFormat>() {

        @Override
        protected SimpleDateFormat initialValue() {
            return new SimpleDateFormat("yyyy-MM-dd");
        }

        @Override
        public SimpleDateFormat get() {
            return super.get();
        }
    };
}
