a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % 2 == 0:
    if c % 2 == 0:
        if b % 2 == 0:
            if d % 2 == 0:
                print('YES')
            else:
                print('NO')
    else:
        print('NO')
elif c % 2 != 0:
    if b % 2 == 0:
        if d % 2 == 0:
            print('YES')
        elif d % 2 != 0:
            print('NO')
    elif b % 2 != 0:
        if d & 2 != 0:
            print('YES')
        else:
            print('NO')
elif a == b:
    if c == d:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
