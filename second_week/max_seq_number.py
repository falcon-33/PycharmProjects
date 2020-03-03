firstNumber = int(input())
seqQuantity = int()
nowNumber = int(input())
maxNumber = 0
maxMaxNumber = 0
if firstNumber == 0:
    print(0)
elif nowNumber == 0:
    print(0)
elif nowNumber == firstNumber:
    seqQuantity = 2
    maxNumber = nowNumber
    while nowNumber != 0:
        nowNumber = int(input())
        if nowNumber == 0:
            break
        elif nowNumber == maxNumber:
            seqQuantity = seqQuantity + 1
        elif nowNumber > maxNumber:
            maxNumber = nowNumber
            seqQuantity = 1
        else:
            continue
    print(seqQuantity)
elif nowNumber > firstNumber:
    seqQuantity = 1
    maxNumber = nowNumber
    while nowNumber != 0:
        nowNumber = int(input())
        if nowNumber == 0:
            break
        elif nowNumber == maxNumber:
            seqQuantity = 1
            seqQuantity = seqQuantity + 1
            maxNumber = maxMaxNumber
        elif nowNumber > maxNumber:
            if maxNumber = nowNumber
            seqQuantity = 1
        else:
            continue
    print(seqQuantity)
elif nowNumber < firstNumber:
    seqQuantity = 2
    maxNumber = firstNumber
    while nowNumber != 0:
        nowNumber = int(input())
        if nowNumber == 0:
            break
        elif nowNumber == maxNumber:
            seqQuantity = seqQuantity + 1
        elif nowNumber > maxNumber:
            maxNumber = nowNumber
            seqQuantity = 1
        else:
            continue
    print(seqQuantity)
