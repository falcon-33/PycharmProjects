s = input()
letters = {}
for c in s:
    if c in letters:
        letters[c] += 1
    else:
        letters[c] = 1
for c in sorted(letters):
    print(c, letters[c])
