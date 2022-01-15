def TOH(n: int, A, B, C):
    if n > 0:
        TOH(n - 1, A, C, B)                         # Transfer n-1 stack from A to B using C
        print(f"Transfer ring from {A} to {C}")     # Transfer ring directly
        TOH(n - 1, B, A, C)                         # Transfer n-1 stack from B to C using A


if __name__ == '__main__':
    TOH(4, 1, 2, 3)
