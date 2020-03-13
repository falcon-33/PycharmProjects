nLines = int(input())
myDict = {}
for i in range(nLines):
    myDict.update({map(str, input().split())})
searchWord = str(input())
for keys, items in myDict.items():
    if keys == searchWord:
        print(items)
    elif items == searchWord:
        print(keys)
    else:
        continue
print(myDict)