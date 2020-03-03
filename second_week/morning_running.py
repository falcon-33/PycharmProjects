firstDayDistance = int(input())
fullDistance = int(input())
days = 1
currentDistance = firstDayDistance
while currentDistance < fullDistance:
    days = days + 1
    currentDistance += currentDistance * 0.1
print(days)
