def rbs(sa: tuple, k, s=0, e=None) -> int:
    if e is None:
        e = len(sa)
    m = s + (e - s) // 2
    return (
        -1 if s >= e else
        rbs(sa, k, s, m) if sa[m] > k else
        rbs(sa, k, m+1, e) if sa[m] < k else
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
