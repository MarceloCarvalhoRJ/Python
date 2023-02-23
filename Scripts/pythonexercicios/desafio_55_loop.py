# usando estrutura de repeticao
'''
maior = 0
menor = 1000
for i in range(0, 5):
    peso = float(input('Digite um peso em Kg: '))
    if peso > maior:
        maior = peso
    if  peso < menor:
        menor = peso  
print(f'O maior peso digitado foi {maior} kg. \nO menor peso ditidado foi {menor} kg.')
'''
# usando as funcoes max e min ()
pesos = []
maior, menor = 0, 0
for i in range(1, 6):
    peso = float(input(f'Digite o {i}º peso em kg: '))
    pesos.append(peso)
    maior = max(pesos)
    menor = min(pesos)
print(f'O maior peso digitado foi {maior} e o menor foi {menor}')

