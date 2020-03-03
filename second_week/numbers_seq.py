number = int(input())
i = 0
if number == 0:
    print(number)
elif number % 2 == 0:
    i = 1
    while number != 0:
        number = int(input())
        if number % 2 == 0:
            i = i + 1
        else:
            continue
    print(i - 1)
else:
    i = 0
    while number != 0:
        number = int(input())
        if number % 2 == 0:
            i = i + 1
        else:
            continue
    print(i - 1)
