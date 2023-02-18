# exemplo 1 - divide a string frutas onde houver espaço.
texto = 'Aprendendo Python com CursoemVideo'
frase = texto.split()
print(frase)

# exemplo 2
texto = 'Aprendendo Python com CursoemVideo'
frase = texto.split('com')
print(frase)

# exemplo 3 - divide a string frutas onde houver virgula.
frutas = 'Maça,Banana,Laranja,Manga'
lista = frutas.split(',')
print(lista[0]) # imprimi o primeiro intem da lista 'Maça'
print(lista[2]) # imprimi o terceiro item da lista 'Laranja'
print(frutas[0]) # imprimi o caracter da posicao 0 de frutas 'M'
print(frutas[2]) # imprimi o caracter da posicao 2 de frutas 'ç'