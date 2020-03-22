package algorithm.sorting;

public class BubbleSort {

    public static void bubbleSort(int[] array){

        int size = array.length;

        for(int i=0; i < size; i++){

            for(int j=0; j < size-i-1; j++){

                if(array[j] > array[j+1]){

                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;

                }

            }

        }

    }

}
