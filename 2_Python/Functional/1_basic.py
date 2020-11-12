wrapper = lambda *args, **kwargs: lambda f: f(*args, **kwargs)
id_ = lambda a: a
add = lambda a: lambda b: b+a
sub = lambda a: lambda b: b-a
mul = lambda a: lambda b: b*a
div = lambda a: lambda b: b//a
mod = lambda a: lambda b: b%a

def fizzbuzz(n: int) -> str: return (
    'fizzbuzz' if n % 15 == 0 else
    'fizz' if n % 3 == 0 else
    'buzz' if n % 5 == 0 else
    str(n)
)
