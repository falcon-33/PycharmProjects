inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
lengts = len(lines)
i = 0
newList = list()
lastStr = lines[lengts - 1] + '\n'
lines = lines[0:lengts - 1]
lines.append(lastStr)
lines1 = sorted(lines)
lines1.reverse()
lines1.append('')
while i < lengts:
    x = lines1[i].split()
    x = x[0:2] + x[3:]
    x = ' '.join(x)
    newList.append('\n')
    newList.append(x)
    i += 1
newList.append('')
newList.reverse()
print(*newList)
inFile.close()
outFile.close()
