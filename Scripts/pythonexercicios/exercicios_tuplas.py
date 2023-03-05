print('.' * 40)
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(lanche[::-1])
print(sorted(lanche)) # ordena em ordem alfabética

print('.' * 40)

for comida in lanche: # usando diretamenta a tupla sem o range
    print(f'{comida}')

print('.' * 40)

for i in range(0, len(lanche)): #usando um contador
    print(f'Item {i + 1}: {lanche[i]}')

print('.' * 40)

for pos, comida in enumerate(lanche): # mesmo resultado do range quando a funcao enumerate que informa o valor da variável e a posicao.
    print(f'Item {pos + 1}: {comida}')

print('.' * 40)

a = (2, 4, 6, 8, 10)
b = (1, 3, 5, 7, 9)
c = a + b
print(a)
print(b)
print(c)
for i in range(0, len(a)):
    print(f'{b[i]}, {a[i]}, ', end = '')
print(c.count(10)) # conta qtas x o 10 apareceu na tupla.

'''print(lanche[0])
print(lanche[3])
print(lanche[-1])
print(lanche[1:])
print(lanche[:-1])
print(lanche[:2])'''