def selection_sort(array):
    """
    Selection sort implementation

    :param array: unsorted array
    :return: None
    """

    size = len(array)

    for i in range(size-1):

        index = i

        for j in range(i+1, size):

            if array[index] > array[j]:

                index = j

        array[i], array[index] = array[index], array[i]
