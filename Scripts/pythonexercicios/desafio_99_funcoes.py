'''
A função maior(lista) recebe uma lista de números e imprime na tela o maior valor da lista. Além disso, ela imprime a quantidade total de valores informados e apresenta cada valor da lista durante a análise.

O loop for que gera a lista aleatória lista1 é executado 5 vezes, criando 5 listas diferentes com um número aleatório de elementos (entre 1 e 20) entre 5 e 10. Em seguida, a função maior(lista1) é chamada para cada uma dessas listas, imprimindo na tela o resultado desejado.

A chamada da função lista1.clear() no final do loop garante que a lista seja limpa após cada iteração, permitindo que uma nova lista seja criada sem acumular os elementos das listas anteriores.
'''
import os
#limpa a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

from time import sleep
from random import randint

def maior(lista: list[int]) -> None: #usando type hints: a função recebe uma lista de inteiros e não retorna nenhum valor.
    """
    Imprime o maior valor da lista passada como argumento e a quantidade total de valores informados.

    Args:
        lista: Uma lista de inteiros.

    Returns:
        None.
    """
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in lista:
        print(n, end= ' ', flush=True)
        sleep(.5)
    print(f'foram informados {len(lista)} ao todo')
    sleep(1)
    print(f'o maior valor informado foi {sorted(lista, reverse=True)[0]}') #em vez de usar a função max() para obter o maior valor da lista, podemos usar a função sorted() para ordenar a lista em ordem decrescente e obter o primeiro elemento da lista, que será o maior valor. Isso evita a necessidade de percorrer toda a lista em busca do maior valor e pode ser mais eficiente em listas muito grandes. 

NUM_INTERACOES = 5
for c in range(NUM_INTERACOES):
    s = randint(1, 5)
    #cria uma lista com s (entre 5 e 10) numeros aleatorios entre 1 a 20
    lista1 = [randint(0, 10) for i in range(s)] 
    maior(lista1)
    lista1.clear()
    sleep(.5)
