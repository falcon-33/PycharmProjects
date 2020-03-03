firstNumber = int(input())
FirstMaxNumber = firstNumber
nowNumber = 1
SecondMaxNumber = 0
while nowNumber != 0:
    nowNumber = int(input())
    if 0 < nowNumber >= FirstMaxNumber:
        SecondMaxNumber = FirstMaxNumber
        FirstMaxNumber = nowNumber
    elif 0 < nowNumber < FirstMaxNumber:
        if nowNumber > SecondMaxNumber:
            SecondMaxNumber = nowNumber
        else:
            continue
print(SecondMaxNumber)
