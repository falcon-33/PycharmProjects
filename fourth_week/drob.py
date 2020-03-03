import math


def reduce_fraction(n, m):
    k = math.gcd(n, m)
    return n // k, m // k


n = int(input())
m = int(input())
print(reduce_fraction(n, m))
