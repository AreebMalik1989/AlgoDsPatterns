package searching;

public class RecursiveBinarySearch {

    public static int recursiveBinarySearch(int[] sortedArray, int key, int start, int end) {

        if(start < end) {

            int mid = start + (end - start) / 2;

            if (sortedArray[mid] > key) {

                return recursiveBinarySearch(sortedArray, key, start, mid);

            } else if (sortedArray[mid] < key) {

                return recursiveBinarySearch(sortedArray, key, mid+1, end);

            } else {

                return mid;

            }

        }

        return -(start + 1);

    }

}

