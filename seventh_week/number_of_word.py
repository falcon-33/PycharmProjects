file = open('input.txt')
startList = file.read().split()
countDict = {}
for elem in startList:
    countDict[elem] = countDict.get(elem, 0) + 1
    print(countDict[elem] - 1, end=' ')
