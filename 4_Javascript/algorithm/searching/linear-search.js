/**
 * Linear search implementation using for loop
 * @param {T[]} array - Unsorted array
 * @param {Number} key - Item to be found in array
 * @returns {Number} index of the item in array, or None if item is not in the array
 * @author Areeb Malik
 */
function linearSearch1(array, key) {
    let size = array.length;
    for(let i=0; i<size; i++) {
        if(array[i] == key) return i;
    }
    return null;
}

/**
 * Linear search implementation using for of
 * @param {T[]} array - Unsorted array
 * @param {Number} key - Item to be found in array
 * @returns {Number} index of the item in array, or None if item is not in the array
 * @author Areeb Malik
 */
function linearSearch2(array, key) {
    for (const [index, value] of array.entries()) {
        if(value === key) return index;
    }
    return null;
}
