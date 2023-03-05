
produtos_precos = ("Maçã", 2.50, "Leite", 3.20, "Pão", 4.00, "Queijo", 8.75, "Café", 6.50, "Ovos", 5.00, "Iogurte", 3.75, "Tomate", 1.90, "Arroz", 12.50, "Azeite", 9.80)
print('-' * 40)
print('LISTAGEM DE PREÇOS 1'.center(40))
print('-' * 40)
for i in range(0, len(produtos_precos)):
    if i % 2 == 0:
        print(f'{produtos_precos[i]:.<32}', end = '')
    else:
        print(f'R${produtos_precos[i]:6.2f}')
print('-' * 40)

#outra solucao com for fazendo percorrer a lista em numeros pares ( de 2 em 2)
print('-' * 40)
print('LISTAGEM DE PREÇOS 2'.center(40))
print('-' * 40)
for i in range(0, len(produtos_precos), 2):
    print(f'{produtos_precos[i]:.<32}R${produtos_precos[i + 1]:6.2f}') 
print('-' * 40)

# outra solucao fazendo um for negativo para acessar a lista de tras para frente:
print('-' * 40)
print('LISTAGEM DE PREÇOS 3'.center(40))
print('-' * 40)

for i in range(len(produtos_precos) - 1, -1, -2):
    produto = produtos_precos[i - 1]
    preco = produtos_precos[i]
    print(f'{produto:.<32}R${preco:6.2f}')

print('-' * 40)