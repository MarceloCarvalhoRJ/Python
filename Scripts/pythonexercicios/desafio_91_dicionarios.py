from random import randint
from time import sleep
from operator import itemgetter

jogadores = {f'jogador{j}': randint(1, 6) for j in range(1, 5)}

print('Valores sorteados:')
for jogador, jogada in jogadores.items():
    print(f'   O {jogador} tirou {jogada}')
    sleep(1)
#usando o itemgetter(1) da biblioteca operator para extrair o elemento da posicao 1 (value).
jogadas_ordenadas = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
'''outra forma de ordenar pelo valor do dicionario
jogadas_ordenadas = sorted(jogadores.items(), key=lambda x: x[1], reverse=True) #compreensao de dicionario. chama a funcao lambda para informar ao sort() fazer o ordenamento pelo valor quando faço x: x[1] (2º elemento do dicionário que eh o valor)'''
print(' == RANKING DOS JOGADORES ==')
for posicao, value in enumerate(jogadas_ordenadas[:3]): #extrai a key e value somente até a posicao 3. 
        print(f'   {posicao + 1}º lugar: {value[0]} com {value[1]}')
        sleep(1)

'''
outra maneira de imprimir a chave e o valor
for key in jogadores:
    print(f'   O {key} tirou {jogadores[key]}')
'''

