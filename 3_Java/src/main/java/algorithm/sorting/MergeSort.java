package algorithm.sorting;

public class MergeSort {

    public static void sort(int[] array) {

        if(array == null || array.length == 0) return;

        mergeSort(array, 0, array.length -1);
    }

    private static void mergeSort(int[] array, int low, int high) {

        if(low < high) {

            // Find the mid point
            int mid = low + (high - low)/2;

            // Below step sorts the left side of the array
            mergeSort(array, low, mid);

            // Below step sorts the right side of the array
            mergeSort(array, mid+1, high);

            // Now merge both sides
            mergeParts(array, low, mid, high);
        }
    }

    private static void mergeParts(int[] array, int low, int mid, int high) {

        // Find the sizes of two sub arrays to be merged
        int size1 = mid - low + 1;
        int size2 = high - mid;

        // Create temp arrays
        int[] L = new int[size1];
        int[] R = new int[size2];

        // Copy data to temp arrays
        for(int i=0; i<size1; i++) L[i] = array[low+i];
        for(int j=0; j<size2; j++) R[j] = array[mid+1+j];

        /* Merge the temp arrays */

        // Initialize the indexes of first and second sub-arrays
        int i=0, j=0;

        // Initialize the index of merged sub array
        int k=low;

        while (i<size1 && j<size2) {

            if(L[i] <= R[j]){

                array[k] = L[i];
                i++;

            } else {

                array[k] = R[j];
                j++;
            }

            k++;
        }

        // Copying remaining elements of L[] if any
        while(i < size1) {

            array[k] = L[i];
            i++;
            k++;
        }

        // Copying remaining elements of R[] if any
        while(j < size2) {

            array[k] = R[j];
            j++;
            k++;
        }
    }
}
