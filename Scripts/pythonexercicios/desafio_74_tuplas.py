from random import randint
numeros = ()
print(f'Os valores sorteados foram: ', end = '')
for i in range(0, 5):
    numero = randint(0, 100)
    numeros += (numero,)
    print(f'{numeros[i]}',  end = ' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

#outra forma:
print('.' * 40)
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end = '')
for num in n:
    print(f'{num} ', end = '')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')