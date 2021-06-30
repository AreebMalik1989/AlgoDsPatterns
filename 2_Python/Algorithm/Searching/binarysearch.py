def recursive_binary_search(sorted_array: tuple, key, start=0, end=None) -> int:
    if end is None:
        end = len(sorted_array)
    mid = start + (end - start) // 2
    return (
        -1 if start >= end else
        recursive_binary_search(sorted_array, key, start, mid) if sorted_array[mid] > key else
        recursive_binary_search(sorted_array, key, mid+1, end) if sorted_array[mid] < key else
        mid
    )


def binary_search(sorted_array, key):
    """
    Binary search implementation using iteration

    :param sorted_array: sorted array
    :param key: item to be found in the sorted array
    :return: index of the item in the array, or -1 if item is not found in the sorted array
    """
    start = 0
    end = len(sorted_array) - 1
    while start <= end:
        mid = (start + end) // 2
        if sorted_array[mid] > key:
            end = mid - 1
        elif sorted_array[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1
