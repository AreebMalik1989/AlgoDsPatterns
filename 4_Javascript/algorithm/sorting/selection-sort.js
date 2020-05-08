function selectionSort(array) {
    size = array.length
    for(i=0; i<size-1; i++) {
        index = i
        for(j=i+1; j<size; j++) {
            if(array[index] > array[j]){
                index = j
            }
        }
        smallerNumber = array[index]
        array[index] = array[i]
        array[i] = smallerNumber
    }
}
