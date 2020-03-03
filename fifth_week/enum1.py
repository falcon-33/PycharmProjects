lst = list(map(int, input().split(" ")))
previous = -999999999999999999999
finalLst = list()
for i in lst:
    if i > previous:
        previous = i
        finalLst = finalLst + [i]
    else:
        previous = i
print(*finalLst[1:])
