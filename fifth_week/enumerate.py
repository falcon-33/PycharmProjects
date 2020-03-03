n = list(map(int, input().split()))
counter = int(0)
for i in enumerate(n):
    x = int(map(int, n))
    x1 = int(*x[:2])
    print(x1)
    if counter > x1:
        counter = i
    else:
        continue
print(counter)
