/**
 * Merge sort implementation
 * @param {T[]} array Unsorted array
 * @author Areeb Malik
 */
function mergeSort(array) {

    let size = array.length;

    if(size > 1) {

        let mid = Math.floor(size/2);
        let left = array.slice(0, mid);
        let right = array.slice(mid);

        mergeSort(left);
        mergeSort(right);

        let i = j = k = 0;

        while((i < left.length) && (j < right.length)) {
            if(left[i] < right[j]) {
                array[k] = left[i];
                i++;
            } else {
                array[k] = right[j];
                j++;
            }
            k++;
        }

        while(i < left.length) {
            array[k] = left[i];
            i++;
            k++;
        }

        while(j < right.length) {
            array[k] = right[j];
            j++;
            k++;
        }
    }
}
