from termcolor import colored
from random import randint
from time import sleep
from letreiro import letreiro, letreiro_2

letreiro('VAMOS JOGAR PAR OU ÍMPAR', 'light_yellow', 'green')

count = soma = 0
while True:
    num = input(colored('Digite um valor: ', 'cyan'))
    if not num.isdigit() or int(num) < 0:
        print(colored('Entrada inválida! Digite um número.', 'light_grey'))
    else:
        while True:
            par_impar = input(colored('Par ou Ímpar? [P/I] ', 'light_cyan')).strip().upper()[0]
            if par_impar not in 'PI':
                print(colored('Opção inválida. Escolha P ou I', 'light_grey'))
            else:
                break
        num_computador = randint(0, 10)
        soma = int(num) + num_computador
        print('-' * 20)
        if soma % 2 == 0:   
            par = colored('PAR','cyan')
        else:
            par = colored('ÍMPAR', 'cyan')
        print(colored(f'Voce jogou {num} e o computador {num_computador}.\nTotal de {soma} deu {par}', 'magenta'))
        sleep(3)
        if (soma % 2 == 0 and par_impar == 'P') or\
            (soma % 2 == 1 and par_impar == 'I'):
            print('-' * 20)
            print(colored('Você VENCEU!', 'green', 'on_green'))
            print(colored('Vamos jogar novamente...', 'green'))
            count += 1
            print('=-' * 10)
            sleep(1)
        else:
            print('-' * 20)
            print(colored('VOCÊ PERDEU!', 'blue'))
            print('=-' * 10)
            print(colored(f'GAME OVER! Você venceu {count} vezes', 'yellow'))
            sleep(1)
            letreiro_2('Obrigado por jogar comigo!', 'magenta', 'blue')
            break
            
