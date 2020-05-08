function quickSort(array, low, high) {

    const partition = (a, l, h) => {

        let i = l - 1
        let pivot = a[h]

        for(j=l; j<h; j++) {

            if(a[j] <= pivot) {
                i = i+1;
                [a[i], a[j]] = [a[j], a[i]]
            }
        }

        [a[i+1], a[high]] = [a[high], a[i+1]]
        return i+1
    }

    if(low < high) {
        
        let pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)
    }
}
