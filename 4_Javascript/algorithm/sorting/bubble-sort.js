function bubbleSort(array) {
    size = array.length
    for(i=0; i<size; i++) {
        for(j=0; j<size-i-1; j++) {
            if(array[j] > array[j+1]) {
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            }
        }
    }
}
