from time import sleep
from termcolor import colored

print('\033[1;34m+-' + '-'*20 + '-+\033[m')
print('\033[1;34m|      Calculadora     |\033[m')
print('\033[1;34m+-' + '-'*20 + '-+\033[m')

count, soma = 0, 0

while True:
    num = int(input('Digite um numero \033[30m[digite 999 para sair]\033[m: '))
    if num == 999:
        print(colored('_' * 45, 'light_yellow'))
        print(colored(f'voce digitou \033[1;35m{count}\033[m \033[36mde números. \nA soma entre eles é \033[1;35m{soma}\033[m', 'cyan'))
        sleep(2)
        print('\033[31m\nPrograma encerrado pelo usuário!')
        print('\n\033[1;34mObrigado por utilizar a nossa Calculadora!\033[m\n')
        break
    soma += num
    count += 1  
