public class A1_IterationVsRecursion {
    
    // Iterative version requires constant space
    public static int iterativeSum(int[] array) {
        int sum = 0;
        for(int i=0; i<array.length; i++) {
            sum += array[i];
        }
        return sum;
    }
    
    // Recursive version requires linear space
    public static int recursiveSum(final int[] array, final int start) {
        if(start <= 0)
            return 0;
        else
            return array[start] + recursiveSum(array, start + 1);
    }
}
