package sort

import (
	"reflect"
	"testing"
)

type sortTest struct {
	data		[]int
	expected	[]int
	name		string
}

const sortTests := []sortTest{
	{[]{2, 1, 3, 0, 5, 6, 4, 7, 9, 8}, []{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, "Sanity"},
	{[]{}, []{}, "Empty"},

}

func testBubbleSort(t *testing.T) {
	for _, test := range sortTests {
		BubbleSort(test.data)
		if !reflect.DeepEqual(test.data, test.expected) {
			t.Errorf("Expected: %v, Got: %v", test.expected, test.data)
		}
	}
}
	
func testSelectionSort(t *testing.T) {
	for _, test := range sortTests {
		SelectionSort(test.data)
		if !reflect.DeepEqual(test.data, test.expected) {
			t.Errorf("Expected: %v, Got: %v", test.expected, test.data)
		}
	}
}
