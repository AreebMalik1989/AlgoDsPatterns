def quick_sort1(arr: tuple):
    if len(arr) == 0:
        return ()
    curr, *rest = arr
    left = tuple(filter(lambda item: item <= curr, rest))
    right = tuple(filter(lambda item: item > curr, rest))
    return quick_sort(left) + (curr,) + quick_sort(right)


def quick_sort2(array, low, high):
    """
    Quick sort implementation

    :param array: unsorted array
    :param low: lower index
    :param high: higher index
    :return: None
    """

    def partition(array, low, high):

        i = low - 1
        pivot = array[high]

        for j in range(low, high):

            if array[j] <= pivot:

                i = i+1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]
        return i+1

    if low < high:

        pi = partition(array, low, high)

        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)
