def power(m: int, n: int) -> int:
    if n == 0:
        return 1
    return power(m, n-1) * m


def power_efficient(m: int, n: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        return power_efficient(m*m, n//2)
    return m * power_efficient(m*m, (n-1)//2)


if __name__ == '__main__':
    print(power(9, 3))
    print(power_efficient(9, 3))
