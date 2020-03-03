myList = list(map(int, input().split()))
grades = [0] * 11
for now in myList:
    grades[now] += 1
for grade in  range(len(grades)):
    print((str(grade) + ' ') * grades[grade], end=' ')
