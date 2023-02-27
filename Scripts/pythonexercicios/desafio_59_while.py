from time import sleep
from termcolor import colored
opcao = 0

while True: # loop principal
    espera = 0.5
    if opcao == 5:
        print('\n\033[1;31mSaindo do programa...\033[m')
        sleep(espera)
        break
   
    print('\033[1;34m+-' + '-'*20 + '-+\033[m')
    print('\033[1;34m|      Calculadora     |\033[m')
    print('\033[1;34m+-' + '-'*20 + '-+\033[m')
    a = int(input('Insira o 1º número: '))
    b = int(input('Insira o 2º número: '))
    
    while opcao != 5: # loop do menu
        print('\n\033[1;33mMenu:\033[m')
        print('[\033[1;36m1\033[m] Somar')
        print('[\033[1;36m2\033[m] Multiplicar')
        print('[\033[1;36m3\033[m] Maior')
        print('[\033[1;36m4\033[m] Novos números')
        print('[\033[1;36m5\033[m] Sair do programa')
        opcao = int(input('\n\033[1;33mEscolha a sua opção:\033[m '))
        # Executa a opção escolhida pelo usuário
        if opcao == 1:
            print(f'\n\033[1;32mA soma de {a} com {b} é igual a: {a + b}\033[m')
            espera = 3
        elif opcao == 2:
            print(f'\n\033[1;32mA multiplicação de {a} com {b} é igual a: {a * b}\033[m')
            espera = 3
        elif opcao == 3:
            print(f'\n\033[1;32mO número maior digitado entre {a} e {b} foi: {max(a, b)}\033[m')
            espera = 3
        elif opcao == 4:
            espera = 1
            break # Sai do loop do menu e retorna para o loop principal
        elif opcao > 5:
            print(colored('Opção inválida. Tente novamente.', 'grey'))
            espera = 0.5
        sleep(espera) # Espera um tempo antes de voltar para o menu

print('\n\033[1;34mObrigado por utilizar a Calculadora!\033[m\n')









