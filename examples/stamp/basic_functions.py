from time import sleep
from random import random
from spypy import stamp, summary


def _sleep():
    sleep(random())


@stamp
def sum(x, y):
    _sleep()
    return y + sub(1, y)


@stamp
def sub(x, y):
    _sleep()
    return x - y


@stamp
def basic():
    for i in range(3):
        sum(i, i)
        _sleep()
        sub(i, i)
        _sleep()
        sub(i, i)


def main():
    basic()
    print(summary())


if __name__ == "__main__":
    main()
