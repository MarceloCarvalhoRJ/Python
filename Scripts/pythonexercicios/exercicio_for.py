VOGAIS = 'a, e, i, o, u' 
frase = input('Insira uma frase: ')
for letra in frase: # percorre cada letra dentro da string frase
    if letra.lower() in VOGAIS: # transforma cada letra em minuscula
        print(letra, end='') # mostra todas as vogais digitadas na frase
else:
    print() # adiciona quebra de linha