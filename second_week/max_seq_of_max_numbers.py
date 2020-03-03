prev = -1
current = 0
max_current = 0
i = int(input())
while i != 0:
    if prev == i:
        current += 1
    else:
        prev = i
        max_current = max(max_current, current)
        current = 1
    i = int(input())
max_current = max(max_current, current)
print(max_current)
