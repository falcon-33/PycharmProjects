import time
firstList = list(map(int, input().split()))
secondList = list(map(int, input().split()))
i = 1
j = 0
while i != firstList[1]:
    secondList.append(int(input()))
    i += 1
secondListLength = len(secondList)
finalCounter = 0
if secondListLength > 1001:
    print('error')
else:
    secondList.sort()
    while j != secondListLength:
        if firstList[0] >= secondList[j]:
            finalCounter = finalCounter + 1
            firstList[0] = firstList[0] - secondList[j]
            j = j + 1
        else:
            break
    print(finalCounter)
