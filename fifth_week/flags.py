n = int(input())
second = str('|  / ')
second1 = second[:1]
second3 = second[2:]
for i in range(1, n + 1):
    print('+___ ', end="")
print()
for i in range(1, n + 1):
    secondFinal = second1 + str(i) + second3
    print(secondFinal, end='')
print()
for i in range(1, n + 1):
    print('|__\ ', end="")
print()
for i in range(1, n + 1):
    print('|    ', end="")
