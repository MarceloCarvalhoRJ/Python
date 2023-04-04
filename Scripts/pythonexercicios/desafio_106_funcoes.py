from time import sleep

cor = ('\033[m',  # 0 - sem cores
       '\033[0;30;41m',  # 1 - Branco em Vermelho
       '\033[0;30;42m',  # 2 - Branco em Verde
       '\033[0;30;43m',  # 3 - Branco em Amarelo
       '\033[0;30;44m',  # 4 - Branco em Azul
       '\033[0;30;45m',  # 5 - Branco em Roxo
       '\033[0;30;46m',  # 6 - Branco em Ciano
       '\033[7;37m',     # 7 - Branco
       );


def letreiro_fundo(texto, cor_fundo=0):
    """
    funcao traz um letreiro com um titulo
    -> a linha superior e inferior acompanham o tamanho do texto
    -> recebe 2 argumentos, sendo o texto e a cor de fundo (usar on_'nome da cor' ex: on_green).
    -> retorna o letreiro personalizado
    """
    tam = len(texto) + 4
    print(cor[cor_fundo], end='')
    print('~' * tam)
    print(f'  {texto}')  # print(colored(f'|{texto:^36}|', cor))
    print('~' * tam)
    print(cor[0], end='')
    sleep(1)


def ajuda(word):
    letreiro_fundo(f'Acessando o manual do comando \'{word}\'', 6)
    print(cor[7], end='')
    help(word)
    print(cor[0], end='')
    sleep(1)


# programa principal
comando = ''
while True:
    letreiro_fundo('SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou Biblioteca > ').lower()  # recebe o texto do input
    if comando in 'fim':
        break
    else:
        ajuda(comando)
letreiro_fundo('ATÉ LOGO!', 1)     


