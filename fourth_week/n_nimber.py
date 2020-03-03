n = int(input())
i = 2


def func1(n, i):
    while n % i == 0:
        if i < n ** 0.5:
            return n
        else:
            i += 1
print(func1(n, i))
