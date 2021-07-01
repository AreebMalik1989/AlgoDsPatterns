package sort

func InsertionSort(arr []int) {
	size := len(arr)
	for i := 1; i < size; i++ {
		for j = i; j > 0; j-- {
			if arr[j] < arr[j-1] {
				arr[j], arr[j-1] = arr[j-1], arr[j]
			}
		}
	}
}
