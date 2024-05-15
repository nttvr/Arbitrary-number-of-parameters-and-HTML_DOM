def test(*params):
    print(params)


test(1, 2, 'string', [4, 5])


def func(n):
    if n == 0:
        return 1
    else:
        return n * func(n - 1)


n = int(input())
print(func(n))
