package algorithm.searching;

public class LinearSearch {

    public static int linearSearch(int[] array, int key) {

        int size = array.length;

        for(int i=0; i<size; i++) {

            if(array[i] == key) {

                return i;
            }

        }

        return -1;
    }

}