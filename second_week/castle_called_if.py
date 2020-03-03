aBrick = int(input())
bBrick = int(input())
cBrick = int(input())
dWall = int(input())
eWall = int(input())
if dWall < aBrick and dWall < bBrick and dWall < cBrick:
    print('NO')
elif eWall < aBrick and eWall < bBrick and eWall < cBrick:
    print('NO')
elif (aBrick <= dWall or bBrick <= dWall) and cBrick <= eWall:
    print('YES')
elif (bBrick <= dWall or cBrick <= dWall) and aBrick <= eWall:
    print('YES')
elif (aBrick <= dWall or cBrick <= dWall) and bBrick <= eWall:
    print('YES')
elif (aBrick <= eWall or bBrick <= eWall) and cBrick <= dWall:
    print('YES')
elif (bBrick <= eWall or cBrick <= eWall) and aBrick <= dWall:
    print('YES')
elif (aBrick <= eWall or cBrick <= eWall) and bBrick <= dWall:
    print('YES')
else:
    print('NO')
