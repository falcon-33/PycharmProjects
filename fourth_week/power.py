a = float(input())
n = float(input())


def power(a, n):
    if n != 0:
        a = a * (a ** (n - 1))
        return a
    else:
        return 1


print(power(a, n))
