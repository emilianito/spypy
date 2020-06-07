from spypy import count, summary


@count
def fibonacci(x):
    if x == 0 or x == 1:
        return x
    return fibonacci(x-1) + fibonacci(x-2)


def main():
    print(fibonacci(6))
    print(summary())


if __name__ == "__main__":
    main()

