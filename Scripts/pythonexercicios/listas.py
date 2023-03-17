lista = [2, 5, 9, 1]
print(f'\nEssa é a lista: \n{lista}')

lista[3] = 8
print(f'Vamos substituir o elemento da posicao 3 por 8: \n{lista}')

lista.append(7)
print(f'Vamos adicionar no final da lista o elemento 7: \n{lista}')

lista.sort()
print(print(f'Vamos ordenar a lista: \n{lista}'))

lista.sort(reverse = True)
print(f'Vamos ordenar de forma reversa: \n{lista}')
print(f'Essa lista em {len(lista)} elementos.')
#ordenando a lista por ordem crescente de qtde de caracteres em cada elemento.
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  
print(linguagens) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  
print(linguagens) # ["python", "csharp", "java", "js", "c"]

#O sorted() tb tem ordem de forma similar ao .sort, a diferença que a sorted eh uma funcao e precisa ser chamada:
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

lista.insert(2, 0)
print(f'Vamos insirir 0 na posicao 2: \n{lista}')

#remove oitem pelo argumento e não pela posição
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

lista.pop()
print(f'Vamos apagar o ultimo elemento da lista: \n{lista}')

 #informa em qual posicao o elemento está.
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

lista.remove(8) #elimina o elemento nao a posicao
print(f'Vamos apagar o número 8 da lista: \n{lista}')
print('.' * 50)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for p, v in enumerate(valores): # retorna a posicao e o valor do elemento na lista.
    print(f'Achei na posição {p} o valor {v}!')
print('Cheguei no final da lista.')
print('.' * 50)

valores = []
for i in range(0, 4):
    valores.append(int(input('Digite um valor: ')))
print(f'Essa é a minha lista: {valores}')
for p, v in enumerate(valores): # retorna a posicao e o valor do elemento na lista.
    print(f'Achei na posição {p} o valor {v}!')
print('Cheguei no final da lista.')
print('.' * 50)
#diferenca de fazer uma ligacao entre duas lista ou somente uma cópia:
a = [2,6,7,4]
b = a #faz uma ligacao entre a lista a e b 
print(f'lista a {a} \nLista b {b}')
b[2] = 0 #o que mudar em b meda em a tb!
print(f'lista a {a} \nLista b {b}')
print('.' * 50)
a = [2,6,7,4]
b = a[:] #com o fatiamento b é somente uma cópia
b[2] = 0 #muda o valor somente na lista b.
print(f'lista a {a} \nLista b {b}')

#invertendo a ordem da lista
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]
