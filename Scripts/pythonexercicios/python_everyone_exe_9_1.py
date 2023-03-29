"""
Exercise  9.1: Write a program that reads the words in words.txt and stores
them as keys in a dictionary. Download a copy of the file from
https://www.py4e.com/code3/words.txt. It doesn't matter what the values are.
Then use the 'in' operator as a fast way to check whether a string is in the
dictionary.
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
dicti = dict()
count = 0
name = input('Name of file: ')
file = open(name) #abre o arquivo e lê cada linha do texto. tem que esta no mesmo diretorio, inclusive o terminal.
for line in file: #cria uma string a cada linha do arquivo texto aberto em file.
    words = line.split()  #cria uma stirng para cada palavra contida na string. mas se for duplicada nao cria.
    for word in words:
       dicti[word] = dicti.get(word, 0) + 1 # get() elimina a necessidade do if para fazer a contagem de palavras repetidas (valor 0 é default). A primeira palavra recebe 1 e depois toda vez que tiver a mesma palavra soma mais 1.
#usando in para verificar se a palavra do texto é uma key do dicionário.
print(dicti, '\n', '-=' * 55)
print(f'→ O texto {name} possui {sum(dicti.values())} palavras.')
 #informa a qtde de palavras do texto

max_value = frequent_word = 0
#verifica qual a palavra mais digita no texto.
for key, value in dicti.items():
    if value is 0 or value > max_value:
        max_value = value
        frequent_word = key
print(f'→ A palavra com maior frequencia foi "{frequent_word}", digitada {max_value} vezes.')

key = 'Interestingly,' 
if key in dicti:  #utilizando in para localizar a chave dentro do dict
   print(f'→ A chave {key} consta no dicionário.')
else:
    print(f'A chave {key} não foi encontrada!.')



