from time import sleep
from random import random
from spypy import stamp, summary


def _sleep():
    sleep(random())


@stamp
def fibonacci(x):
    _sleep()
    if x == 0 or x == 1:
        return x
    return fibonacci(x-1) + fibonacci(x-2)


def main():
    fibonacci(3)
    print(summary())


if __name__ == "__main__":
    main()

