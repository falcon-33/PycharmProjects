from collections import Counter
fin = open('input.txt')
words = []
for word in fin.read().split():
    words.extend(word.split())
counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
pairsSort = sorted(pairs)
words = [pair[1] for pair in pairsSort]
print('\n'.join(words))
