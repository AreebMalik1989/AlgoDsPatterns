def fun_a(n: int) -> None:
    if n > 0:
        print(n, end=' ')
        fun_b(n-1)


def fun_b(n: int) -> None:
    if n > 1:
        print(n, end=' ')
        fun_a(n//2)


if __name__ == '__main__':
    fun_a(20)
