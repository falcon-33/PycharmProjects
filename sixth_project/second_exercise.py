quantity = int(input())
sList = list(map(int, input().split()))
finalList = sorted(sList)
print(*finalList)
