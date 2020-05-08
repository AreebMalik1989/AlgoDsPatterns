function insertionSort(array) {
    size = array.length
    for(i=1; i<size; i++) {
        for(j=i; j>0; j--) {
            if(array[j] < array[j-1]) {
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            }
        }
    }
}
