package algorithm.sorting;

public class QuickSort {

    public static void sort(int[] array) {

        if(array == null || array.length == 0) return;

        quickSort(array, 0, array.length - 1);
    }

    /**
     * The main function that implements quick sort
     *
     * @param array : Array to be sorted
     * @param low : Starting index
     * @param high : Ending index
     */
    private static void quickSort(int[] array, int low, int high) {

        if(low < high) {

            // pi is partitioning index, array[pi] is now at right place
            int pi = partition(array, low, high);

            // Recursively sort elements before and after partition
            quickSort(array, low, pi - 1);
            quickSort(array, pi+1, high);
        }
    }

    /**
     * This function takes the last element as pivot,
     * places the pivot element at its correct position
     * in sorted array, and places all smaller (smaller
     * than pivot) elements to the left of pivot, and
     * all greater elements to the right of pivot
     *
     * @param array : Array to be partitioned
     * @param low : Starting index
     * @param high : Ending index
     * @return : Partitioning index
     */
    private static int partition(int[] array, int low, int high) {

        int pivot = array[high];
        int i = low-1; // index of smaller element

        for(int j=low; j<high; j++) {

            // If current element is smaller than or equal to pivot
            if(array[j] <= pivot) {

                i++;

                // swap array[i] and array[j]
                swap(array, i, j);
            }
        }

        swap(array, i+1, high);

        return i+1;
    }

    private static void swap(int[] array, int i, int j) {

        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
