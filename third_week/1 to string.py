s = str(input())
while s.find('@') != -1:
    s = s.replace('@', '', 1)
print(s)
