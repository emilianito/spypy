from time import sleep
from spypy import history, summary


@history
def sum(x, y):
    sleep(0.2)
    return y + sub(1, y)


@history
def sub(x, y):
    sleep(0.2)
    return x - y


@history
def basic():
    sleep(0.1)
    for i in range(3):
        sum(i, i)
        sub(i, i)
        sub(i, i)


def main():
    basic()
    print(summary())


if __name__ == "__main__":
    main()
