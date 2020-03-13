import functools

prints = functools.partial(print, end=' ')
prints(1)
prints(2)

print(functools.reduce(lambda x, y: x + y, [1, 2, 5]))