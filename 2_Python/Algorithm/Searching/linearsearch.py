def linear_search1(array):
    def _(key):
        for index, value in enumerate(array):
            if value == key:
                return index
        return None
    return _


def linear_search2(array, key):
    """
    Linear search implementation using range in for loop

    :param array: unsorted array
    :param key: item to be found in array
    :return: index of the item in array, or -1 if item is not in the array
    """
    size = len(array)
    for i in range(size):
        if array[i] == key:
            return i
    return -1


def linear_search3(array, key):
    """
    Linear search implementation using enumerate in for loop

    :param array: unsorted array
    :param key: item to be found in array
    :return: index of the item in array, or None if item is not in the array
    """
    for index, value in enumerate(array):
        if value == key:
            return index
    return None
