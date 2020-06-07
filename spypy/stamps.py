from time import time
from functools import wraps
from .meta import _stamps


def stamp(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        name = f.__qualname__
        if name not in _stamps:
            _stamps[name] = 0.0

        start = time()
        res = f(*args, *kwargs)
        end = time()
        _stamps[name] += end - start
        return res
    return wrapper
