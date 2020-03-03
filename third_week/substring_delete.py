s = str(input())
size = len(s)
if s.find('h') == -1:
    s = 'error'
elif size < 2:
    s = 'error'
elif size == 2:
    print('')
elif s.find('h') >= 0:
    first = s.find('h')
    sInverted = s[::-1]
    lastInverted = sInverted.find('h')
    last = size - (lastInverted + 1)
    s1 = s[:first]
    s2 = s[last + 1:]
    sSum = s1 + s2
    print(sSum)
