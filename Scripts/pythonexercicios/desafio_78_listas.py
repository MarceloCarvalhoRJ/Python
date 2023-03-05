numeros = []
pos_max = ''
pos_min = ''
for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {i}: ')))
print('<>' * 30)
print(f'Você digitou os valores {numeros}')
for pos, valor in enumerate(numeros):
    if max(numeros) == valor:
        pos_max += (f'{pos}... ')
    elif min(numeros) == valor:
        pos_min += (f'{pos}... ')
print(f'O maior valor digitado foi {max(numeros)} nas posições {pos_max}')
print(f'O menor valor digitado foi {min(numeros)} nas posições {pos_min}')
