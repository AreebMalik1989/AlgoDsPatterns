package search

func RecursiveBinarySearch(sortedArray []int, key, start, end int) int {
	if end < start || len(sortedArray) == 0 {
		return -1
	}
	mid := (start + end) / 2
	if sortedArray[mid] > key {
		return RecursiveBinarySearch(sortedArray, key, start, mid-1)
	} else if sortedArray[mid] < key {
		return RecursiveBinarySearch(sortedArray, key, mid+1, end)
	} else {
		return mid
	}
}

func BinarySearch(sortedArray []int, key int) int {
	start := 0
	end := len(sortedArray) - 1
	for start <= end {
		mid := (start+end) / 2
		if sortedArray[mid] > key {
			end = mid - 1
		} else if sortedArray[mid] < key {
			start = mid + 1
		} else {
			return mid
		}
	}
	return -1
}
