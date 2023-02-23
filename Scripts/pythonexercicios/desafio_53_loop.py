f = input('Digite uma frase: ')
frase = f.replace(' ', '').lower()
#c = len(frase)
frase_invertida = frase[::-1] # inverte a ordem da string frase
print(f'O inverso de {frase} é {frase_invertida}')
if frase_invertida == frase:
    print(f'A frase é um Palíndromo!')
else:
    print('A frase NÃO é um Palíndromo.')
 # abaixo outra maneira de fazer usando estrutura de repetição:   
'''poli = True
for i in range(0, c):
    if frase[i] != frase[(c - 1) - i]:
        poli = False
        break
if poli:
    print(f'A frase: {f} \nÉ um Palíndromo!')
else:
    print('A frase NÃO é um Palíndromo.')'''
