myList = list(map(int, input().split()))
secondSet = set()
for i in myList:
    if i in secondSet:
        print('YES')
        secondSet.add(i)
    else:
        print('NO')
        secondSet.add(i)
