package sorting;

public class SelectionSort {

    public static void selectionSort(int[] array) {

        int size = array.length;

        for(int i=0; i < size-1; i++) {

            int index = i;

            for(int j = i+1; j<size; j++) {

                if(array[index] > array[j]) {

                    index = j;

                }

            }

            int smallerNumber = array[index];
            array[index] = array[i];
            array[i] = smallerNumber;

        }

    }

}
