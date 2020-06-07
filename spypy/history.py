from time import time
from functools import wraps
from .meta import _history


def history(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        name = f.__qualname__
        if name not in _history:
            _history[name] = []

        start = time()
        res = f(*args, *kwargs)
        end = time()
        _history[name].append(end - start)
        return res
    return wrapper
