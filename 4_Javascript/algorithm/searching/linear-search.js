/**
 * Linear search implementation
 */
function linearSearch(array, key) {
    let size = array.length;
    for(let i=0; i<size; i++) {
        if(array[i] == key) {
            return i;
        }
    }
    return null;
}
