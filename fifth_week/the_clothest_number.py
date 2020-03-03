n = list(map(int, input().split()))
x = int(input())
a = []
i = 0
if x > 0:
    previous = -9999999
    while i != len(n):
        razn = n[i] - x
        if abs(razn) > previous:
            previous = abs(razn)
            i += 1
            print(previous)
            print(abs(razn))
        else:
            i += 1
print(previous)