firstNumber = int(input())
currentNumber = 1
if firstNumber == 0:
    print('')
else:
    while currentNumber != 0:
        currentNumber = int(input())
        if firstNumber >= currentNumber:
            continue
        else:
            firstNumber = currentNumber
print(firstNumber)
