def r_fib(n: int) -> int:
    if n <= 1:
        return n
    return r_fib(n-2) + r_fib(n-1)


def i_fib(n: int) -> int:
    if n <= 1:
        return n
    t0, t1 = 0, 1
    s = 0
    for i in range(2, n+1):
        s = t0 + t1
        t0 = t1
        t1 = s
    return s


F = [-1] * 10


def m_fib(n: int) -> int:
    """
    Memoization
    """
    if n <= 1:
        F[n] = n
        return n
    if F[n-2] == -1:
        F[n-2] = m_fib(n-2)
    if F[n-1] == -1:
        F[n-1] = m_fib(n-1)
    F[n] = F[n-2] + F[n-1]
    return F[n-2] + F[n-1]


if __name__ == '__main__':
    print(r_fib(9))
    print(i_fib(9))
    print(m_fib(9))
