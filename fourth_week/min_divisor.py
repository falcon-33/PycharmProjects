import math


def MinDivisor(n):
    div = 2
    while div <= math.sqrt(n):
        if n % div == 0:
            return div
        div += 1
    return n


n1 = int(input())
print(MinDivisor(n1))
