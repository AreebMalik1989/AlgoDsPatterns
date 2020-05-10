/**
 * Quick sort implementation
 * @param {T[]} array - Unsorted array
 * @param {Number} low - Lower index
 * @param {Number} high - Higher index
 * @author Areeb Malik
 */
function quickSort(array, low, high) {

    const partition = (array, low, high) => {

        let i = low - 1;
        let pivot = array[high];

        for(let j=low; j<high; j++) {

            if(array[j] <= pivot) {
                i = i+1;
                [array[i], array[j]] = [array[j], array[i]];
            }
        }

        [array[i+1], array[high]] = [array[high], array[i+1]];
        return i+1;
    }

    if(low < high) {
        let pi = partition(array, low, high);
        quickSort(array, low, pi-1);
        quickSort(array, pi+1, high);
    }
}
