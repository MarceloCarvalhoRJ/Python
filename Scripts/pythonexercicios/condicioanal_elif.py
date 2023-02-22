from time import sleep
from sys import exit
from termcolor import colored

print(colored('Escolha uma opção:', 'green'))
opcao = int(input(colored('[1] Sacar [2] Extrato ', 'yellow')))
if opcao == 1:
    saque = int(input(colored(f'Informe o valor do saque: R$ ', 'light_cyan')))
    saldo = 500
    if saque > saldo:
        print(colored('Saldo insuficiente', 'red'))
    else: 
        print(colored('Retire as notas...', 'blue'))
        sleep(1.5)

elif opcao == 2:
    print('Imprimindo o extrato...')
    sleep(1.5)
    
else:
    print(colored('Opção inválida', 'red'))
    exit()

print(colored('Obrigado por usar o nossos serviços!', 'cyan'))
