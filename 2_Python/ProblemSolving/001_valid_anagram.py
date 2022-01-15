def are_anagrams1(s1: str, s2: str):
    """
    T(n) = O(n)
    S(n) = O(n)
    """
    if len(s1) != len(s2):
        return False
    freq1 = dict()
    freq2 = dict()
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2:
            return False
    return True


from collections import Counter


def are_anagrams2(s1: str, s2: str):
    """
    T(n) = O(n)
    S(n) = O(n)
    """
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def are_anagrams3(s1: str, s2: str):
    """
    T(n) = O(nlogn)
    S(n) = O(n)
    """
    if len(s1) != len(s2):
        return False
    return sorted(s1) != sorted(s2)
