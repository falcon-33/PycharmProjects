import math
a = float(input())
b = float(input())
c = float(input())
D = (b ** 2) - (4 * a * c)
if D < 0:
    print('error')
else:
    DSqrt = math.sqrt(D)
    x1 = (-b + DSqrt) / (2 * a)
    x2 = (-b - DSqrt) / (2 * a)
    if x1 == x2:
        print(x1)
    elif x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
