now = int(input())
numbersCounter = 0
sumCounter = 0
while now != 0:
    numbersCounter = numbersCounter + 1
    sumCounter = sumCounter + now
    now = int(input())
print(sumCounter / numbersCounter)
