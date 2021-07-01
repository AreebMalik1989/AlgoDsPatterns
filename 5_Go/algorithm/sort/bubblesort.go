package sort

func BubbleSort(arr []int) {
	size := len(arr)
	swapped := true
	for i := 0; i < size, swapped == true; i++ {
		swapped = false
		for j := 0; j < size-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
	}
}
