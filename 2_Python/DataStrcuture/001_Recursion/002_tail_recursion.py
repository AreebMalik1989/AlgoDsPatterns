def fun(n: int):
    if n > 0:
        print(n, end=' ')
        fun(n-1)


if __name__ == '__main__':
    fun(3)
