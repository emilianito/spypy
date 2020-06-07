Use decorators for get information of functions calls: 
- Count function calls. 
- Get the time which a function has consumed
- Get a list of calls of function
- Get the call tree for a execution given.


##### @count

It accumulates number of call

```python
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
```

output:
```
{'counters': {'sub': 30}, 'stamps': {}, 'history': {}, 'tree': []}
```