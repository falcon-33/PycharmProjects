n = list(map(int, input().split()))
counter = 0
for i in n:
    if i > 0:
        counter += 1
    else:
        continue
print(counter)
