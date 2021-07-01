package search

func LinearSearch1(array []int, key int) int {
	for index, value := range array {
		if value == key {
			return i
		}
	}
	return -1
}

func LinearSearch2(array []int, key int) int {
	size := len(array)
	for i := 0; i < size; i++  {
		if array[i] == key {
			return i
		}
	}
	return -1
}
