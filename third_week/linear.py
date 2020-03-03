a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
try:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print(x, y)
except Exception as ex:
    print(str(ex))
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e, 'f =', f)
