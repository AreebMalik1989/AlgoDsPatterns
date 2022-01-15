def r_sum(n: int) -> int:
    if n == 0:
        return 0
    return r_sum(n-1) + n


def i_sum(n: int) -> int:
    s = 0
    for i in range(n+1):
        s += i
    return s


if __name__ == '__main__':
    print(r_sum(5))
    print(i_sum(5))
