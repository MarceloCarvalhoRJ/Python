from random import randint
from time import sleep
import os

#limpa a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

#O _ é usado para indicar que não usaremos o valor retornado pela função range na criação da lista. Podemos usar qualquer outra variável no lugar do _, mas essa convenção é comum em Python para indicar que não usaremos o valor da variável.Observe que, nesse caso, estamos criando uma lista [] com 5 números inteiros aleatórios entre 1 e 10, usando a função randint da biblioteca random
def sorteio(): 
    lista = [randint(1, 10) for _ in range(5)]
    print(f'Sorteando 5 valores da lista: ', end = '')
    for n in lista:
        print(n, end=' ', flush=True)
        sleep(.4)
    print('PRONTO!')
    return lista

def soma_pares(lista):
    soma_pares = 0
    for n in lista:
        soma_pares += (n if n % 2 == 0 else 0) #faz a soma dos numeros pares da lista.
    sleep(.4)
    print(f'Somando os valores pares de {lista}, temos {soma_pares}')

lista = sorteio()    
soma_pares(lista)
print()