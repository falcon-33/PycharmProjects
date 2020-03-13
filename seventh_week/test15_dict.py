gasCost = {}
n = int(input())
costs = map(int, input().split())
gasTypes = (92, 95, 98)
for now in range(3):
    gasCost[gasTypes[now]] = costs[now]
for i in range(n - 1):
    costs = map(int, input().split())
    for now in range(len(gasTypes)):
        gasCost[gasTypes[now]] = min(costs[now], gasCost[gasTypes[now]])
print(gasCost[92], gasCost[95], gasCost[98])
