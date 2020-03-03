s = str(input())
if s.find(' ') != -1:
    numberSpace = s.find(' ')
    first = s[:numberSpace]
    second = s[numberSpace + 1:]
    print(second, first)
else:
    print('error')
