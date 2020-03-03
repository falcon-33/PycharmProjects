s = str(input())
letterF = 'f'
pos = 0
size = len(s)
if s.find(letterF, pos) == -1:
    s = 'no F'
elif s.find(letterF, pos) >= 0:
    first = s.find(letterF, pos)
    if size < 2:
        print(first)
    elif s.find(letterF, pos) + 1 > 0:
        s = s[::-1]
        lastInverted = s.find(letterF, pos)
        if lastInverted == 0:
            last = size - 1
            if last == first:
                print(first)
            else:
                print(first, last)
        else:
            last = size - (lastInverted + 1)
            if last == first:
                print(first)
            else:
                print(first, last)
