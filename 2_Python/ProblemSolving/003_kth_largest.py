"""
Kth largest element
e.g., arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4
output = 6

explanation:
1st largest = 9
2nd largest = 7
3rd largest = 7
4th largest = 6
"""


def kth_largest1(arr: list, k: int) -> int:
    """
    T(n, k) = O(kn)
    S(n, k) = O(1)
    """
    for i in range(k - 1):
        arr.remove(max(arr))
    return max(arr)


def kth_largest2(arr: list, k: int) -> int:
    """
    T(n, k) = O(nlog(n))
    S(n, k) = depends on space complexity of sort function
    """
    n = len(arr)
    arr.sort()
    return arr[n - k]


import heapq


def kth_largest3(arr: list, k: int) -> int:
    """
    T(n, k) = O(n + klogn)
    S(n, k) = O(n)
    """
    arr = [-e for e in arr]
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
