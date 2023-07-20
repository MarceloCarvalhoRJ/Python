def eat_vowel(user_word):
    word_without_vowel = ''
    for letter in user_word:
        if letter.upper() in ('A', 'E', 'I', 'O', 'U'):
            continue
        word_without_vowel += ''.join(letter)
    #Em Python, uma string vazia é considerada "falsa" em uma condição booleana, enquanto uma string com qualquer conteúdo é considerada "verdadeira". Portanto, o if not word_without_vowel verifica se word_without_vowel está vazia e, se estiver, retorna a mensagem "Essa palavra só tem vogal". Caso contrário, retorna a string word_without_vowel.
    return 'Essa palavra só tem vogal' if not word_without_vowel else word_without_vowel  

#word = input('Digite uma palavra: ').upper()
#print(eat_vowel(word))

for i in range(1, 11):
    if i % 2 == 1 :
        print(i, end=', ')
print()
x = 1
while x < 11:
    if x % 2 != 0:
        print(x, end=', ')
    x += 1
print()
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end='')
print()

for digit in "0165031806510":
    if digit == "0":
        print('x', end='')
        continue
    print(digit, end='')
print()

var = 1  
print('1) ', var > 0)
print('2) ', not (var <= 0))
 
 
# Exemplo 2:
print('3) ', var != 0)
print('4) ', not (var == 0))

print()

#Operadores bit a bit

i = 15
j = 22

log = i and j

numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
numbers[0] = 111
print("\nConteúdo da lista anterior:", numbers)  # Imprimindo conteúdos de listas anteriores.
 
numbers[1] = numbers[4]  # Copiando o valor do quinto elemento para o segundo.
print("Novo conteúdo da lista:", numbers)  # Printing Conteúdo atual da lista.
print ("\nList length:", len (numbers)) # Imprimindo o comprimento da lista.

del numbers[1]
print(len(numbers))
print(numbers)
print(numbers[-1])
print(numbers[-2])
