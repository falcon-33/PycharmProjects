def MinDivisor(n):
    div = 2
    while div <= (n ** 1/2):
        if n % div == 0:
            return div
        else:
            div += 1
            return n


n = int(input())
print(MinDivisor(n))
