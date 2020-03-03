lendth = int(input())
width = int(input())
pieces = int(input())
if lendth < 0 or width < 0 or pieces < 1:
    print('NO')
elif lendth * width < pieces:
    print('NO')
elif 1 == pieces:
    print('NO')
elif pieces % lendth == 0 or pieces % width == 0 or\
        lendth % pieces == 0 or width % pieces == 0:
    print('YES')
else:
    print('NO')
