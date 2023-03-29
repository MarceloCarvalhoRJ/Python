counts = dict()

line = input('Enter a line of text: ')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts: ', counts)

counts = {'chuck': 1, 'fred': 42, 'jam': 100}
for key in counts:
    print(key, counts[key])
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())
print('#' * 40)

palavra = 'brontosaurus'
d = dict()
for c in palavra:
    d[c] = d.get(c, 0) + 1
print(d)
print('#' * 40)

conta = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(conta.get('jan', 0))
print(conta.get('tim', 'Chave não encontrada'))
