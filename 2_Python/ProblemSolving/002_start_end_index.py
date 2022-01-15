"""
First and last index of element in sorted list
e.g., [1, 2, 2, 3, 3, 3]
"""


def first_and_last_linear(sorted_arr: list, key) -> list[int]:
    """
    T(n) = O(n)
    S(n) = O(1)
    """
    for i, v in enumerate(sorted_arr):
        if v == key:
            start = i
            while i+1 < len(sorted_arr) and sorted_arr[i+1] == key:
                i += 1
            return [start, i]
    return [-1, -1]


def first_and_last_binary(sorted_arr: list, key) -> list[int]:
    """
    T(n) = O(log(n))
    S(n) = O(1)
    """
    if len(sorted_arr) == 0 or sorted_arr[0] > key or sorted_arr[-1] < key:
        return [-1, -1]
    start = find_first_index(sorted_arr, key)
    end = find_last_index(sorted_arr, key)
    return [start, end]


def find_first_index(sorted_arr: list, key) -> int:
    if sorted_arr[0] == key:
        return 0
    start, end = 0, len(sorted_arr)-1
    while start <= end:
        mid = (start + end) // 2
        if sorted_arr[mid] == key and sorted_arr[mid - 1] < key:
            return mid
        elif sorted_arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def find_last_index(sorted_arr: list, key) -> int:
    if sorted_arr[-1] == key:
        return len(sorted_arr) - 1
    start, end = 0, len(sorted_arr) - 1
    while start <= end:
        mid = (start+end) // 2
        if sorted_arr[mid] == key and sorted_arr[mid + 1] > key:
            return mid
        elif sorted_arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1
