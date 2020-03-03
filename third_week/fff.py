s = str(input())
pos = s.find('f')
size = len(s)
if pos == -1:
    print(-2)
elif pos > -1:
    first = int(pos)
    pos = s.find('f', pos + 1)
    if pos > first:
        print(pos)
    else:
        print(-1)
