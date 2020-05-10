/**
 * Bubble sort implementation
 * @param {T[]} array - Unsorted array
 * @author Areeb Malik
 */
function bubbleSort(array) {
    let size = array.length;
    for(let i=0; i<size; i++) {
        // Last i elements are already in place
        for(let j=0; j<size-i-1; j++) {
            if(array[j] > array[j+1]) {
                let temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}
