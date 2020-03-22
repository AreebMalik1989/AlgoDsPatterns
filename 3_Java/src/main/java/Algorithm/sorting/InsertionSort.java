package sorting;

public class InsertionSort {

    public static void insertionSort(int[] array) {

        int size = array.length;

        for(int i=1; i<size; i++) {

            for(int j=i; j>0; j--) {

                if(array[j] < array[j-1]) {

                    int temp = array[j];
                    array[j] = array[j-1];
                    array[j-1] = temp;

                }

            }

        }

    }

}
