from time import time
from functools import wraps
from .meta import _tree, _stack


def tracer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        function_name = f.__qualname__
        empty = []
        new_call = {"name": function_name, "stamp": 0, "calls": empty}
        try:
            node = _stack[-1]
            calls = node['calls_reference']
        except IndexError:
            calls = _tree

        calls.append(new_call)
        _stack.append({
            "call_reference": new_call,
            "calls_reference": empty})
        start = time()
        ret = f(*args, *kwargs)
        stop = time()
        node = _stack.pop()
        node['call_reference']['stamp'] = stop - start
        return ret

    return wrapper
