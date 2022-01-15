def is_valid1(combination):
    diff = 0
    for par in combination:
        if par == '(':
            diff += 1
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    return diff == 0


def generate(n: int) -> list:
    """
    T(n) = O(n*(2**n))
    S(n) = O(n*(2**n))
    """
    def rec(n, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n - 1, diff + 1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(n - 1, diff - 1, comb, combs)
            comb.pop()
    combs = list()
    comb = list()
    rec(2*n, 0, comb, combs)
    return combs
