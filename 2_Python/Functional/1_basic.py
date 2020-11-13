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

# Perfect encapsulation & immutability
def counter(a: int = 0):
    class _Counter:
        def get_a(self):
            return a
        def with_a(self, a: int):
            return counter(a)
        def increment(self):
            return counter(a+1)
        def decrement(self):
            return counter(a-1)
    return _Counter()
