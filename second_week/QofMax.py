maximumNumber = 0
quantityMax = 0
i = -1
while i != 0:
    i = int(input())
    if i > maximumNumber:
        maximumNumber, quantityMax = i, 1
    elif i == maximumNumber:
        quantityMax += 1
print(quantityMax)
