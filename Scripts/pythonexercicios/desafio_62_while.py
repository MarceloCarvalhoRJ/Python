from termcolor import colored
from time import sleep
print('=' * 30)
print(colored(f"{'10 TERMOS DE UMA PA':^30}", "cyan")) # centraliza o texto no espaço de 30 caracteres usando a f-string
print('=' * 30)

while True:
    primeiro_termo = int(input(colored('Digite o primeiro termo: ', 'light_yellow')))
    razao = int(input(colored('Digite a razão: ', 'light_yellow')))
    qtde_termo = 10
    outro_termo = 1
    pa = primeiro_termo

    while True: # loop se o usuario quizer mais termos.
        print()
        print(f'\033[1;35m{primeiro_termo}\33[m', end = ' \033[31m→\033[m ')
        i = 1
        while i < qtde_termo:
            pa += razao
            print(f'\033[1;35m{pa}\33[m', end = ' \033[31m→\033[m ')
            i += 1
        outro_termo = int(input(colored('\nVoce que mostrar mais quantos termos \033[30m[digite 0 para sair]\033[m? ', 'light_cyan')))
        if outro_termo != 0:
            primeiro_termo = pa + razao
            pa += razao
            qtde_termo = outro_termo
        else:
            print('\033[31m\nPrograma encerrado pelo usuário!')
            sleep(1)
            print('\n\033[1;34mObrigado por utilizar a Calculadora de PA!\033[m\n')
            break
    break   