def fact(n: int) -> int:
    if n == 0:
        return 1
    return fact(n - 1) * n


def nCr(n: int, r: int) -> int:
    if n == r or r == 0:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)


def i_nCr(n: int, r: int) -> int:
    numerator = fact(n)
    denominator = fact(r) * fact(n - r)
    return numerator // denominator


if __name__ == '__main__':
    print(nCr(5, 3))
    print(i_nCr(5, 3))
