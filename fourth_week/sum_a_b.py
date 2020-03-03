a = int(input())
b = int(input())


def sum1(a, b, i = 1):
    if i != b:
        if a == 0:
            return b
        elif b == 0:
            return a
        a = a + 1
        i = i + 1
        sum1(a, b, i)
    else:
        return a, b





print(sum1(a, b, i = 1))
