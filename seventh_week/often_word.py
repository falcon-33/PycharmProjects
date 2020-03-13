from operator import itemgetter
fin = open('input.txt')
myDict = {}
for keys in fin.read().split():
    if keys not in myDict:
        myDict.update({keys: 1})
    else:
        item = myDict[keys]
        myDict.update({keys: item + 1})
tempDict = {}
tempDict = sorted(myDict.items(), key=itemgetter(1), reverse=True)
finalList = []
a = tempDict[0]
lengthDict = len(tempDict)
i = 0
a = tempDict[i]
b = a[1]
previousKey = b
while i != lengthDict:
    a = tempDict[i]
    b = a[1]
    if b < previousKey:
        break
    else:
        finalList.append(a[0])
        previousKey = b
    i += 1
finalList = sorted(finalList)
print(finalList[0])


