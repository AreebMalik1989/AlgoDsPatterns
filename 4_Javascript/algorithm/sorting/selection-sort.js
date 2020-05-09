function selectionSort(array) {
    let size = array.length;
    for(let i=0; i<size-1; i++) {
        let index = i;
        for(let j=i+1; j<size; j++) {
            if(array[index] > array[j]){
                index = j;
            }
        }
        let smallerNumber = array[index];
        array[index] = array[i];
        array[i] = smallerNumber;
    }
}
