from functools import wraps
from .meta import _counters


def count(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        name = f.__qualname__
        if name not in _counters:
            _counters[name] = 0

        _counters[name] += 1
        return f(*args, *kwargs)
    return wrapper
