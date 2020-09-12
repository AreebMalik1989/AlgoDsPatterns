import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something ...
        result = func(*args, **kwargs)
        # Do something else ...
        return result
    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper


@debug
@my_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello('Areeb')
