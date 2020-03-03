aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
print(*sorted(set(aList) & set(bList)))
