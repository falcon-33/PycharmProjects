def gcb(a, b):
    if b != 0:
        if a > b:
            return gcb(b, a % b)
        elif a < b:
            return gcb(a, b % a)
    return a


a = int(input())
b = int(input())
x = gcb(a, b)
a1 = a // x
b1 = b // x
print(a1, b1)
