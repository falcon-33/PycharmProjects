n = int(input())
b = n // 2
if n == 1 or n == 2:
    print('YES')
elif n % 2 != 0:
    print('NO')
elif b % 2 == 0:
    print('YES')
else:
    print('NO')
