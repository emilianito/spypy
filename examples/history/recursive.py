from time import sleep
from spypy import history, summary


@history
def fibonacci(x):
    sleep(0.2)
    if x == 0 or x == 1:
        return x
    return fibonacci(x-1) + fibonacci(x-2)


def main():
    print(fibonacci(6))
    print(summary())


if __name__ == "__main__":
    main()
