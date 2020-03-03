sList = list(map(int, input().split()))
length = len(sList)
i = 0
finalList = list()
if length % 2 == 0:
    while i != length:
        finalList.append(sList[i + 1])
        finalList.append(sList[i])
        i += 2
    print(*finalList)
else:
    while i != (length - 1):
        finalList.append(sList[i + 1])
        finalList.append(sList[i])
        i += 2
    finalList.append(sList[length - 1])
    print(*finalList)
