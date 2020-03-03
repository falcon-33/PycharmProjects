n = list(map(int, input().split()))
previous = 1001
for i in n:
    if i < 1:
        continue
    else:
        if previous > i:
            previous = i
        else:
            continue
print(previous)
