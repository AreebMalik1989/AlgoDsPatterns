p, f = 1.0, 1.0


def e(x: int, n: int) -> float:
    if n == 0:
        return 1
    global p, f
    r = e(x, n - 1)
    p = p * x
    f = f * n
    return r + (p / f)


s = 1


def eh(x: int, n: int) -> float:
    """
    Taylor's Series Honer's Rule
    """
    global s
    if n == 0:
        return s
    s = 1 + (x*s/n)
    return eh(x, n-1)


def ei(x: int, n: int) -> float:
    """
    Taylor's Series Iterative
    """
    s, numerator, denominator = 1, 1, 1
    for i in range(1, n+1):
        numerator *= x;
        denominator *= i;
        s += numerator/denominator;
    return s


if __name__ == '__main__':
    print(e(4, 15))
    print(eh(4, 15))
    print(ei(4, 15))
