def r_fact(n: int) -> int:
    if n == 0:
        return 1
    return r_fact(n-1) * n


def i_fact(n: int) -> int:
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


if __name__ == '__main__':
    print(r_fact(5))
    print(i_fact(5))
