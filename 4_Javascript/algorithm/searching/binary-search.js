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
