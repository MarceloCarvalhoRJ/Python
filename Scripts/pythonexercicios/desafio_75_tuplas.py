
numero = (int(input(f'Digite um número: ')), int(input(f'Digite outro número: ')), int(input(f'Digite mais um número: ')), int(input(f'Digite um último número: ')))     
print(f'Voce digitou os valores: {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 not in numero:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O valor 3 apareceu {numero.index(3) + 1}ª posição')
print('Os valores pares digitados foram:', end = ' ') 
for n in numero:
    if n % 2 == 0: 
        print(f'{n}', end = ' ') 
