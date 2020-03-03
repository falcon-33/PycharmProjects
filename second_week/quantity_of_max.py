firstNumber = int(input())
i = 0
nowNumber = int()
maxNumber = int()
if firstNumber == 0:
    print(0)
elif firstNumber != 0:
    nowNumber = int(input())
    if nowNumber == 0:
        print(0)
    elif nowNumber > firstNumber:
        i = 0
        maxNumber = nowNumber
        while nowNumber != 0:
            if nowNumber > maxNumber:
                print('b1')
                i = 0
                maxNumber = nowNumber
                nowNumber = int(input())
            elif nowNumber == maxNumber:
                print('c1')
                i = i + 1
                nowNumber = int(input())
            else:
                print('d1')
                nowNumber = int(input())
    elif nowNumber == firstNumber:
        i = 1
        maxNumber = firstNumber
        while nowNumber != 0:
            if nowNumber > maxNumber:
                print('b2')
                i = 0
                maxNumber = nowNumber
                nowNumber = int(input())
            elif nowNumber == maxNumber:
                print('c2')
                i = i + 1
                nowNumber = int(input())
            else:
                print('d2')
                nowNumber = int(input())
    else:
        i = 0
        maxNumber = firstNumber
        while nowNumber != 0:
            if nowNumber > maxNumber:
                print('b3')
                i = 0
                maxNumber = nowNumber
                nowNumber = int(input())
            elif nowNumber == maxNumber:
                print('c3')
                i = i + 1
                nowNumber = int(input())
            else:
                print('d3')
                nowNumber = int(input())
    print(i)



