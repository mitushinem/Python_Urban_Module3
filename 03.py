def test(*args, **kwargs):
    for a in args:
        print(a, end=', ')

    for key, value in kwargs.items():
        print(f'kwargs[{key}]:{value}', end=', ')
    print()


test(1, 2, 3, a=4, b=5)
test({'a': 1, 'b': 2})


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(7))