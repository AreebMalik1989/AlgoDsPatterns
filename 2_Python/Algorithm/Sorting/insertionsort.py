def insertion_sort(array):
    """
    Insertion sort implementation

    :param array: unsorted array
    :return: None
    """
    size = len(array)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

