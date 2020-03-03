def rec1():
    n = int(input())
    if n != 0:
        rec1()
        print(n)
    else:
        print(0)


rec1()
