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
