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

Accumulated Time spent for each decorated function

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

##### @history

Save a list for each decorated function and the time of each call 

````python
from time import sleep
from spypy import history, summary


class Calc:
    @history
    def sum(self, x, y):
        sleep(0.2)
        return y + y

    @history
    def sub(self, x, y):
        sleep(0.2)
        return x - y

    @history
    def mul(self, x, y):
        sleep(0.2)
        return x * y

    @history
    def inc(self, x):
        sleep(0.2)
        return self.sum(x, 1)

@history
def basic():
    calc = Calc()
    calc.sum(
        calc.mul(
            calc.sub(10, 8),
            calc.inc(1)),
        calc.inc(2))


def main():
    basic()
    print(summary())


if __name__ == "__main__":
    main()
````

````
{'counters': {}, 'stamps': {}, 'history': {'basic': [2.5090126991271973], 'sum': [0.40225863456726074, 0.40079402923583984, 0.4010045528411865], 'sub': [0.2012476921081543, 0.2008199691772461, 0.20115375518
798828, 0.2000255584716797, 0.20097613334655762, 0.20099520683288574, 0.20000076293945312, 0.20001840591430664, 0.20098590850830078]}, 'tree': []}
```