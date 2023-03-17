#a funcaao set() elimina os elementos repetidos dentro da lista7tupla e converte em conjunto
#declarando conjuntos {}
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

#os conjuntos em Python nao suportam indexação (carros[0]) e nem fatiamento[1:5]
#para acessar os valores é necessário converter o cunjunto para lista.
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

#A maneira de se interar/percorrer um set é usando um for.
carros_2 = {"gol", "celta", "palio"}

for carro in carros_2:
    print(carro)

for indice, carro in enumerate(carros_2):
    print(f"{indice}: {carro}")

#unindo dois conjuntos/set
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado) # {1, 2, 3, 4}

#Faz a interseção entre dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado) # {2, 3}

#tudo que tem no conjunto a mas não tem no conjunto b ou vice-e-versa.
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado) # {1}

resultado = conjunto_b.difference(conjunto_a)
print(resultado) # {4}

#informa todos os elemento que não estão na interseção
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado) # {1, 4}

#retorna True/False se todos os elementos de um conjunto estão contido em outro
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)

#é ao contratio de subset, verifica se todos os elementos do conjunto a contemplam os do conjunto b.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)

#retorna True/False se nao existe elementos iguais entre os conjuntos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)

#adicionando elemento ao conjunto
sorteio = {1, 23}

sorteio.add(25)  
print(sorteio)  # {1, 23, 25}

sorteio.add(42)  
print(sorteio)  # {1, 23, 25, 42}

sorteio.add(25)  
print(sorteio)  # {1, 23, 25, 42}

#apagando o set
sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.clear()

print(sorteio)  # set()

#fazendo uma copia do set, igual ao usado no list
sorteio = {1, 23}
  
sorteio_2 = list(sorteio.copy())    # precisa transformar o set em lista para poder modificar os elementos
sorteio_2[0] = 5
print(sorteio)    # {1, 23}
print(sorteio_2)  # [5, 23]

#descartando valor dentro de um set.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)  # apesar de não existir o nr 45 ele nao retorna erro.

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}

#ao contrátio na lista, o pop() exclui o primeiro elemento

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros.pop())  # 2
print(numeros.pop())  # 3
print(numeros)  # {4, 5, 6, 7, 8, 9}

#igual ao discard(), a difereça é que o remove aprensenta erro se o valor nao existir dentro do set.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#pode-se utilizar o operador IN tb para verificar a existencia de um valor dentro do set retornando True ou Flase.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False

