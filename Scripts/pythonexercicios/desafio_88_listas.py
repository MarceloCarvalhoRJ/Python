from letreiro import letreiro, letreiro_2
from random import sample, randint
from time import sleep

jogos_gerados = []

def palpite(qtde_jogos):
    lista_num = list(range(1, 61)) #cria uma lista com 60 numeros de 1 a 60
    for c in range(0, qtde_jogos):
        jogo = sample(lista_num, 6) #cria outra lista com 6 numeros aleatórios retirados da lista_num
        jogo.sort() #ordena os numeros em ordem crescente.
        jogos_gerados.append(jogo) #acrescenta a lista jogos dentro da lista jogos_gerados
        for num in jogo: #percorre cada elemento dentro de jogos
            lista_num.remove(num) #apaga o respectivo elemento na lista_num. assim no proximo sorteio na vai ter numeros repetidos.
    return jogos_gerados # retorna a lista contendo todas as lista de jogos conforme qtde escolhida pelo usuário.

letreiro('JOGA NA MEGA SENA', 'yellow', 'cyan')
qtde_jogos = int(input('\033[36mQuantos jogos você quer que eu sorteie?\033[0m '))
print(f'\033[33m{"-="*4}  sorteando {qtde_jogos} jogos  {"-="*4}\033[0m')

for pos, jogo in enumerate(palpite(qtde_jogos)): #chama a funcao e percorre cada jogo dentro da lista e com a respectiva posição.
    print(f'\033[33mJogo {pos + 1}:\033[0m {jogo}')
    sleep(0.7)

letreiro_2('Boa Sorte e Volte Sempre!', 'magenta', 'light_blue')
