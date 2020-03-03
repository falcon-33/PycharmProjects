import math
a = float(input())
b = float(input())
c = float(input())
p = float((a + b + c) / 2)
s = float(math.sqrt(p * (p - a) * (p - b) * (p - c)))
print(s)
