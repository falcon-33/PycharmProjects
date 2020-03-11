import string
inFile = open('input.txt', 'r', encoding='utf8')
myList = list()
mySet = set()
while True:
    line = inFile.readline()
    if line == "":
        break
    else:
        myList.append(line)
lenght = len(myList)
i = 0
finalList = list()
while i != lenght:
    finalList = finalList + list(map(str, myList[i].split()))
    i += 1
lenghtFinal = len(finalList)
mySet = set(finalList)
lenghtSet = len(mySet)
print(lenghtSet)
