from spypy import count, summary, clear


@count
def sum(x, y):
    return x + y


@count
def sub(x, y):
    return x - y


def test_basic():
    sum(1, 1)
    sub(1, 1)
    expected = {"sum": 1, "sub": 1}
    assert summary()['counters'] == expected
    clear(counters=True)


def test_twice():
    sum(1, 1)
    sum(1, 1)
    expected = {"sum": 2}
    assert summary()['counters'] == expected
    clear(counters=True)


def nested():
    @count
    def sum_nested():
        sum()
    expected = {"sum": 1, "sum_nested": 1}
    assert summary()['counters'] == expected
    clear(counters=True)
