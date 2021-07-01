package sort

func SelectionSort(arr []int) {
	size := len(arr)
	for i := 0; i < size-1; i++ {
		index := i
		for j := i+1; j < size; j++ {
			if arr[index] > arr[j] {
				arr[j], arr[index] = arr[index], arr[j]
			}
		}
		smallerNumber := arr[index]
		arr[index] = arr[i]
		arr[i] = smallerNumber
	}
}
