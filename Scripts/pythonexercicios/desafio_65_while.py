from time import sleep
from termcolor import colored

print('\033[1;34m+-' + '-'*20 + '-+\033[m')
print('\033[1;34m|      Calculadora     |\033[m')
print('\033[1;34m+-' + '-'*20 + '-+\033[m')

count = soma = media = maior = 0
menor = 10000
while True:
    num = int(input('Digite um numero : '))
    continua = input('\033[30m(deseja continuar [s/n])\033[m: ').strip().lower()

    soma += num
    count += 1
    media = soma / count
    if num > maior:
        maior = num
    if num < menor:
        menor = num 

    if continua == 'n':
        print(colored('_' * 45, 'light_yellow'))
        print(colored(f'Você digitou \033[1;35m{count}\033[m \033[36mnúmeros é a média foi\033[m \033[1;35m{media:.2f}\033[m ', 'cyan'))
        print(colored(f'O maior numero digitado foi \033[1;35m{maior}\033[m \033[36mo menor foi \033[1;35m{menor}\033[m', 'cyan'))
        sleep(3)
        print('\033[31m\nPrograma encerrado pelo usuário!')
        print('\n\033[1;34mObrigado por utilizar a nossa Calculadora!\033[m\n')
        break
    
    