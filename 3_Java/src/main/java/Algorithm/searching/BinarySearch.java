package searching;

public class BinarySearch {

    public static int binarySearch(int[] sortedArray, int key) {

        int start = 0;
        int end = sortedArray.length - 1;

        while(start <= end) {

            int mid = (start + end) / 2;

            if(sortedArray[mid] > key) {

                end = mid - 1;

            } else if(sortedArray[mid] < key) {

                start = mid + 1;

            } else {

                return mid;

            }
        }

        return -1;
    }

}
