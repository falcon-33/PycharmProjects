n = int(input())
checker1 = 1
temp = 0
sum1 = 0
while checker1 != (n + 1):
    if checker1 != (n + 1):
        temp = (1 / (checker1 ** 2))
        checker1 = checker1 + 1
        sum1 = sum1 + temp
    else:
        break
print(sum1)
