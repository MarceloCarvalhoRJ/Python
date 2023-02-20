a = int(input('insira o 1º numero: '))
b = int(input('insira o 2º numero: '))
c = int(input('insira o 3º numero: '))
maior = max(a, b, c)
menor = min(a, b, c)
"""
if(a >= b and a >= c):
    maior = a
elif(b >= c):
    maior = b
else:
    maior = c
if(a <= b and a <= c):
    menor = a
elif(b <= c):
    menor = b
else:
    menor = c
"""
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')