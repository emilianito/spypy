from .meta import _counters, _stamps, _history, _tree


def clear(counters=False,
          stamps=False,
          history=False,
          tree=False,
          all=False):

    if all:
        counters = stamps = history = tree = False

    if counters:
        _counters.clear()
    if stamps:
        _stamps.clear()
    if history:
        _history.clear()
    if tree:
        _tree.clear()


def summary(counters=True,
            stamps=True,
            history=True,
            tree=True):

    _summary = {}

    if counters:
        _summary['counters'] = _counters
    if stamps:
        _summary['stamps'] = _stamps
    if history:
        _summary['history'] = _history
    if tree:
        _summary['tree'] = _tree

    return _summary
