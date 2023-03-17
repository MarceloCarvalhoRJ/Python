#indices negativos
frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[-1])  # pera
print(frutas[-3])  # laranja

#matriz
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

#fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

#interar listas
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#compreensao de listas
# cria a lista e coloca a estrutura de for em uma única linha.
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

#apagar uma lista
lista = [1, "Python", [40, 30, 20]]

print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista)  # []

#juntando uma lista a outra.
linguagens = ["python", "js", "c"]
linguagens_2 = ["java", "csharp"]
print(linguagens)  # ["python", "js", "c"]

linguagens.extend(linguagens_2)

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

#cria uma copia da lista sem vincular
lista = [1, "Python", [40, 30, 20]]
lista_2 = lista.copy()

lista_2[0] = 9

print(lista)  # [1, "Python", [40, 30, 20]]
print(lista_2)  # [9, "Python", [40, 30, 20]]