def fun(n: int) -> None:
    if n > 0:
        print(n, end=' ')
        fun(n-1)
        fun(n-1)


if __name__ == '__main__':
    fun(3)
