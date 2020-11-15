def merge_sort1(arr: tuple) -> tuple:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    l = merge_sort1(left)
    r = merge_sort1(right)
    return merge1(l, r)


def merge1(l: tuple, r: tuple) -> tuple:
    temp = list()
    i = j = 0
    while i <= len(l)-1 and j <= len(r)-1:
        if l[i] <= r[j]:
            temp.append(l[i])
            i += 1
        else:
            temp.append(r[j])
            j += 1
    while i <= len(l)-1:
        temp.append(l[i])
        i += 1
    while j <= len(r)-1:
        temp.append(r[j])
        j += 1
    return tuple(temp)


def merge_sort2(array):
    """
    Merge sort implementation

    :param array: unsorted array
    :return: None
    """

    size = len(array)

    if size > 1:

        mid = size // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:

                array[k] = left[i]
                i += 1

            else:

                array[k] = right[j]
                j += 1

            k += 1

        while i < len(left):

            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):

            array[k] = right[j]
            j += 1
            k += 1
