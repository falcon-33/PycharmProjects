import itertools
print(*itertools.combinations([1, 2, 3, 4], 3))
print(*itertools.permutations([1, 2, 3, 4], 2))
print(*itertools.combinations_with_replacement([1, 2, 3, 4], 4))
print(*itertools.accumulate([1, 4, 2, 7], max))
