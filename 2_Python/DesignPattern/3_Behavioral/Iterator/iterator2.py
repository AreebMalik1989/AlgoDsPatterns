import time


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


g = fib()


if __name__ == "__main__":

    try:
        for e in g:
            print(e)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Calculation stopped")
