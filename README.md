Use decorators for get information of functions calls: 
- Count function calls. 
- Get the time which a function has consumed
- Get a list of calls of function
- Get the call tree for a execution given.


##### @count

Accumulates number of call

```python
from spypy import count, summary


def sum(x, y):
    return y + sub(1, y)


@count
def sub(x, y):
    return x - y


def basic():
    for i in range(10):
        sum(i, i)
        sub(i, i)
        sub(i, i)


def main():
    basic()
    print(summary())


if __name__ == "__main__":
    main()
```

output:
```
{'counters': {'sub': 30}, 'stamps': {}, 'history': {}, 'tree': []}
```

##### @stamp

Accumulated Time spend for a function

```python
from time import sleep
from random import random
from spypy import stamp, summary


def _sleep():
    sleep(random())


class Calc:
    @stamp
    def sum(self, x, y):
        _sleep()
        return y + y

    @stamp
    def sub(self, x, y):
        _sleep()
        return x - y

    @stamp
    def mul(self, x, y):
        _sleep()
        return x * y

    @stamp
    def inc(self, x):
        _sleep()
        return self.sum(x, 1)


def basic():
    calc = Calc()
    _sleep()
    calc.sum(
        calc.mul(
            calc.sub(10, 8),
            calc.inc(1)),
        calc.inc(2))


@stamp
def main():
    basic()
    print(summary())


if __name__ == "__main__":
    main()
```
```
{'counters': {}, 'stamps': {'main': 0.0, 'Calc.sub': 0.44124484062194824, 'Calc.inc': 0.9938485622406006, 'Calc.sum': 0.9490275382995605, 'Calc.mul': 0.7908306121826172}, 'history': {}, 'tree': []}
````