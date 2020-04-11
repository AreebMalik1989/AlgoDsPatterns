"""Simplest strategy without using class"""


def add(a, b):
    print(a+b)


def sub(a, b):
    print(a-b)


if __name__ == "__main__":

    solve = add
    solve(2, 1)

    solve = sub
    solve(2, 1)
