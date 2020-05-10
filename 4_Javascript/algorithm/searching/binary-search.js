/**
 * Binary search implementation using iteration
 * @param {T[]} sortedArray - Sorted array
 * @param {Number} key - Item to be found in the sorted array
 * @returns {Number} Index of the item in the array, or -1 if item is not found in the sorted array
 * @author Areeb Malik
 */
function binarySearch(sortedArray, key) {
    let start = 0;
    let end = sortedArray.length - 1;
    while(start <= end) {
        let mid = Math.floor((start+end)/2);
        if(sortedArray[mid] > key) {
            end = mid - 1;
        } else if(sortedArray[mid] < key) {
            start = mid + 1;
        } else {
            return mid;
        }
    }
    return -1
}

/**
 * Binary search implementation using recursion
 * @param {T[]} sortedArray - Sorted array
 * @param {*} key - Item to be found in the sorted array
 * @param {*} start - Starting index
 * @param {*} end - Ending index
 * @returns {Number} index of the item in the sorted array, or -ve value if item is not found in the sorted array
 * @author Areeb Malik
 */
function recursiveBinarySearch(sortedArray, key, start, end) {
    if(start<end) {
        let mid = Math.floor((start+end)/2);
        if(sortedArray[mid] > key) {
            return recursiveBinarySearch(sortedArray, key, start, mid);
        } else if(sortedArray[mid] < key) {
            return recursiveBinarySearch(sortedArray, key, mid+1, end);
        } else {
            return mid;
        }
    }
    return -(start+1);
}
