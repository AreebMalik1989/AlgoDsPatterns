def fun(n: int) -> int:
    if n > 100:
        return n - 10
    return fun(fun(n+11))


if __name__ == '__main__':
    print(fun(95))
