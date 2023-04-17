from termcolor import colored, cprint
from emoji import emojize, demojize


def cor_fundo(c):   
    cor = (
    '\033[m',         # 0 - sem cores 
    '\033[0;30;41m',  # 1 - Branco em Vermelho
    '\033[0;30;42m',  # 2 - Branco em Verde
    '\033[0;30;43m',  # 3 - Branco em Amarelo
    '\033[0;30;44m',  # 4 - Branco em Azul
    '\033[0;30;45m',  # 5 - Branco em Roxo
    '\033[0;30;46m',  # 6 - Branco em Ciano
    '\033[7;30m',     # 7 - Branco 
    )
    return cor[c]


def letreiro(texto, cor1, cor2):
    print(colored(' ' + '=' * 35 + ' ', cor2))
    print(colored(f"{emojize(':star:')}{colored(texto.center(33), cor1)}{emojize(':star:')}"))
    #print(colored(f'|{texto:^36}|', cor))
    print(colored(' ' + '=' * 35 + ' ', cor2))

def letreiro_2(texto, cor1, cor2):
    print(colored('-' * len(texto), cor2))
    print(colored((texto + emojize(' :grinning_face_with_big_eyes:')).center(35), cor1))
    #print(colored(f'|{texto:^36}|', cor))
    print(colored('-' * len(texto), cor2))

def letreiro_fundo(texto, cor_fundo):
    """
    funcao traz um letreiro com um titulo
    -> a linha superior e inferior acompanham o tamanho do texto
    -> recebe 2 argumentos, sendo o texto e a cor de fundo (usar on_'nome da cor' ex: on_green).
    -> retorna o letreiro personalizado
    """

    if __name__ == '__main__': #serve para nao carregar o que estiver abaixo do if quando chamar a funcao.
        print(colored('~' * (len(texto) + 4), cor_fundo, attrs=['reverse', 'blink']))
        print(colored((texto).center(len(texto) + 4), cor_fundo, attrs=['reverse', 'blink']))
        #print(colored(f'|{texto:^36}|', cor))
        print(colored('~' * (len(texto) + 4), cor_fundo, attrs=['reverse', 'blink']))
   


'''letreiro_fundo('Testando novo titulo ', 'green')
print(colored('Hello, World!', 'white', attrs=['reverse', 'blink']))
cprint('Aprendendo Python', 'black', 'on_green')
print_white_on_cyan = lambda x: cprint(x, 'white', 'on_cyan')'''




'''
def letreiro(texto, cor):
    
    tam_texto = len(texto)
    espacos = int((36 - tam_texto) / 2)
    print(colored('+' + '-' * 35 + '-+', cor))
    print(colored('|' + ' ' * espacos + texto + ' ' * espacos + '|', cor))
    print(colored('+' + '-' * 35 + '-+', cor))

letreiro('Marcelo', 'cyan')

print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")    
texto = 'CALCULDORA DE MATRIZ'
print(f'{texto:^37}')
print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")

matrix = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        num = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        matrix[l].append(num)
print('╔════════════════════════════════════╗')
print(f'║   \033[33m{matrix[0]}\033[m \033[34m{matrix[1]}\033[m \033[35m{matrix[2]}\033[m    ║')
print('╚════════════════════════════════════╝')

print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")    
texto = 'CALCULDORA DE MATRIZ'
print(f'{texto:^37}')
print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")'''