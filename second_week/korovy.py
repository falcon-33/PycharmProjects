n = int(input())
n = abs(n)
if n == 0 or 21 > n > 4 or 31 > n > 24 or 41 > n > 34\
        or 51 > n > 44 or 61 > n > 54 or 71 > n > 64 \
        or 81 > n > 74 or 91 > n > 84 or 101 > n > 95:
    print(n, 'korov', sep=' ')
elif n == 1 or n == 21 or n == 31 or n == 41 or n == 51\
        or n == 61 or n == 71 or n == 81 or n == 91:
    print(n, 'korova', sep=' ')
else:
    print(n, 'korovy', sep=' ')
