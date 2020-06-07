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
