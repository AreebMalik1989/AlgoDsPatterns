def bubble_sort(array):
    """
    Bubble sort implementation

    :param array: unsorted array
    :return: None
    """

    size = len(array)

    for i in range(size):

        # Last i elements are already in place
        for j in range(size-i-1):

            if array[j] > array[j+1]:

                array[j], array[j+1] = array[j+1], array[j]
