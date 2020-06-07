from spypy import count, summary


class Calc:
    @count
    def sum(self, x, y):
        return y + y

    @count
    def sub(self, x, y):
        return x - y

    @count
    def mul(self, x, y):
        return x * y

    @count
    def inc(self, x):
        return self.sum(x, 1)


def basic():
    calc = Calc()
    calc.sum(
        calc.mul(
            calc.sub(10, 8),
            calc.inc(1)),
        calc.inc(2))


@count
def main():
    basic()
    print(summary())


if __name__ == "__main__":
    main()
