from time import sleep
from spypy import tracer, summary


class Calc:
    @tracer
    def sum(self, x, y):
        sleep(0.2)
        return y + y

    @tracer
    def sub(self, x, y):
        sleep(0.2)
        return x - y

    @tracer
    def mul(self, x, y):
        sleep(0.2)
        return x * y

    @tracer
    def inc(self, x):
        sleep(0.2)
        return self.sum(x, 1)

@tracer
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
