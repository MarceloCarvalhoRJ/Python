from time import sleep
from termcolor import colored

print('=' * 26)
print('| \033[1;33mSEQUENCIA DE FIBONACCI\033[m |')
print('='* 26)

while True:
    tot_termo = int(input('\033[36m\nDigite a quantidade de termos \033[30m(digite 0 para sair)\033[36m:\033[m '))
    if tot_termo == 0:
        print('\033[31m\nPrograma encerrado pelo usuário!')
        sleep(1)
        print('\n\033[1;34mObrigado por utilizar a Calculadora de Fibonacci!\033[m\n')
        break
    elif tot_termo < 0:
        print("Quantidade de termos inválida. Digite um valor positivo.")
        continue
    elif tot_termo == 1:
        print('O mínimo de termos são 2, digite novamente.')
        continue
    i = 2
    a = 0
    b = 1
    print(f'\n\033[1;34m{a}\033[m \033[35m→\033[m \033[1;34m{b}\033[m', end = ' \033[35m→\033[m ')
    while i < tot_termo:
        r = a + b
        print(f'\033[1;34m{r}\033[m', end = ' \033[35m→\033[m ')
        a = b
        b = r
        i += 1
    print('\033[1;35mFim!')
    