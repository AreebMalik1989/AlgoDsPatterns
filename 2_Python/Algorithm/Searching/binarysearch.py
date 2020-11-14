rbs = lambda a: lambda k: lambda s=0: lambda e=len(a): (
    find_index(s + (e - s) // 2, a, k, s, e) if s < e else
    -(s+1)
)


find_index = lambda m, a, k, s, e: (
    rbs(a)(k)(s)(m) if a[m] > k else
    rbs(a)(k)(m + 1)(e) if a[m] < k else
    m
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


def recursive_binary_search(sorted_array, key, start=None, end=None):
    """
    Binary search implementation using recursion

    :param sorted_array: sorted array
    :param key: item to be found in the sorted array
    :param start: starting index
    :param end: ending index
    :return: index of the item in the sorted array, or -ve value if item is not found in the sorted array
    """

    if start is None:
        start = 0
    if end is None:
        end = len(sorted_array) - 1

    if start < end:

        mid = start + (end - start) / 2

        if sorted_array[mid] > key:

            return recursive_binary_search(sorted_array, key, start, mid)

        elif sorted_array[mid] < key:

            return recursive_binary_search(sorted_array, key, mid+1, end)

        else:

            return mid

    return -(start+1)
