class Test:

    def __init__(self, limit):
        self._limit = limit

    # Called when iteration is initialized
    def __iter__(self):
        self._x = 10
        return self

    # To move to next element
    def __next__(self):

        # Store current value of x
        x = self._x

        # Stop iteration if limit is reached
        if x > self._limit:
            raise StopIteration

        # Else increment and return old value
        self._x += 1
        return x


if __name__ == "__main__":

    # Prints number from 10 to 50
    for i in Test(50):
        print(i)

    # Prints nothing
    for i in Test(8):
        print(i)
