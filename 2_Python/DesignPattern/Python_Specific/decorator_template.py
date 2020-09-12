import functools

def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something ...
        result = func(*args, **kwargs)
        # Do something else ...
        return result

    return wrapper

@my_decorator
def add5(x):
    return x + 5
