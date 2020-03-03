a = int(input())
b = int(input())
aMin = 1
bMin = aMin + b - a
if a < 1 or b < 1 or a > b:
    print('NO')
elif b % (b - a + 1) == 0:
    print('YES')
else:
    print('NO')
