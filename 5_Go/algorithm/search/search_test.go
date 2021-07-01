package search

import "testing"

type searchTest struct {
	data		[]int
	key		int
	expected	int
	name		string
}

const searchTests = []searchTest {
	{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 1, 0, "Sanity"},
	{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5, 4, "Sanity"},
	{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 10, 9, "Sanity"},
	{[]int{1, 4, 5, 6, 7, 10}, -25, -1, "Absent"},
	{[]int{1, 4, 5, 6, 7, 10}, 25, -1, "Absent"},
	{[]int{}, 2, -1, "Empty"},
}

func testRecursiveBinarySearch(t *testing.T) {
	for _, test := range searchTests {
		actual := RecursiveBinarySearch(test.data, test.key, 0, len(test.data)-1)
		if actual != test.expected {
			t.Errorf("Test %s failed", test.name)
		}
	}
}

func TestBinarySearch(t *testing.T) {
	for _, test := range searchTests {
		actual := BinarySearch(test.data, test.key, 0, len(test.data)-1)
		if actual != test.expected {
			t.Errorf("test %s failed", test.name)
		}
	}
}

func TestLinearSearch1(t *testing.T) {
	for _, test := range searchTests {
		actual := LinearSearch1(test.data, test.key)
		if actual != test.expected {
			t.Errorf("test %s failed", test.name)
		}
	}
}

func TestLinearSearch2(t *testing.T) {
	for _, test := range searchTests {
		actual := LinearSearch2(test.data, test.key)
		if actual != test.expected {
			t.Errorf("test %s failed", test.name)
		}
	}
}
