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
