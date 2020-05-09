function insertionSort(array) {
    let size = array.length;
    for(let i=1; i<size; i++) {
        for(let j=i; j>0; j--) {
            if(array[j] < array[j-1]) {
                let temp = array[j];
                array[j] = array[j-1];
                array[j-1] = temp;
            }
        }
    }
}
