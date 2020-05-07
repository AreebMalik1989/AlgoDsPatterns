/**
 * Linear search implementation
 */
function linearSearch(array, key) {
    size = array.length
    for(i=0; i<size; i++) {
        if(array[i] == key) {
            return i
        }
    }
    return null
}
