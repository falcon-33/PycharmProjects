from operator import itemgetter
fin = open('input.txt')
myDict = {}
for keys in fin.read().split():
    if keys not in myDict:
        myDict.update({keys: 1})
    else:
        item = myDict[keys]
        myDict.update({keys: item + 1})
print(myDict)
tempList = []
tempList = sorted(myDict.items(), key=itemgetter(1), reverse=True)
firstTulpe = tempList[0]
previousValue = firstTulpe[1]
previousKey = ''
finalList = []
print(tempList)
for k in tempList:
    if k[1] == previousValue:
        if k[0] > previousKey:
            finalList.append(k[0])
            previousKey = k[0]
            previousValue = k[1]
            print(1, *finalList)
        else:
            listLen = len(finalList)
            finalList.insert(listLen - 1, k[0])
            previousKey = k[0]
            previousValue = k[1]
            print(2, *finalList)
    elif k[1] < previousValue:
        if k[0] > previousKey:
            finalList.append(k[0])
            previousKey = k[0]
            previousValue = k[1]
            print(3, *finalList)
        else:
            listLen = len(finalList)
            finalList.insert(listLen - 1, k[0])
            previousKey = k[0]
            previousValue = k[1]
            print(4, *finalList)
print(*finalList)
