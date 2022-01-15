x: int = 0


def fun(n: int) -> int:
    global x
    if n > 0:
        x += 1
        return fun(n-1) + x
    return 0


if __name__ == '__main__':
    print(fun(5))
    print(fun(5))
