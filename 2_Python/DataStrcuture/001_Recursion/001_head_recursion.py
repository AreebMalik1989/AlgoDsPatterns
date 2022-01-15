def fun(n: int):
    if n > 0:
        fun(n-1)
        print(n, end=' ')


if __name__ == '__main__':
    fun(3)
