number = int(input())
i = 2
while i < 1000:
    if number % i == 0:
        print(i)
        break
    i = i + 1
