from letreiro import letreiro, letreiro_2
from time import sleep
from datetime import date
from termcolor import colored
from emoji import emojize

letreiro('Bem vindo ao Banco MMC', 'magenta', 'light_blue') 
menu = """
<<<  \033[36mMenu\033[0m  >>>

[\033[1;33m1\033[0m] Depositar
[\033[33m2\033[0m] Sacar
[\033[33m3\033[0m] Extrato
[\033[30m0\033[0m] Sair

\033[36mEscolha uma opção =>\033[0m """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
qtde_depositos = '\n'
qtde_saques = '\n'

while True:

    opcao = int(input(menu))
    
    if opcao == 1:
        while True:
            vlr_deposito = int(input('\nQual o valor do deposito? R$ '))
            if vlr_deposito > 0:
                saldo += vlr_deposito
                qtde_depositos += f"R${vlr_deposito}\n"
                break
            else:   
                print('valor inválido. Tente novamente.')

    elif opcao == 2:
        
        while True:
            vlr_saque = int(input('Quer sacar quanto? R$ '))
            if numero_saques >= LIMITE_SAQUES:
                print('Quantidade de saques acima do limite diário.')
                sleep(1)
                break
            if vlr_saque <= 0:
                print('Valor inválido. Tente novamente.')
            elif vlr_saque > 500:
                print(colored('Valor de saque acima do limite de R$ 500', 'grey'))
            elif saldo < vlr_saque:
                print(colored(f'Saldo insuficiente! Seu saldo atual é R$ {saldo}', 'light_red'))
                sleep(2)
                break
            else:
                numero_saques += 1
                saldo -= vlr_saque
                qtde_saques += f"(-)R${vlr_saque:.2f}\n"
                print(colored('Aguarde a contagem das notas \n', 'light_magenta'), end = '')
                for i in range(1, 7):
                    # a função flush() é adicionada como argumento para a função print(). Isso força o buffer de saída a ser limpo imediatamente após cada impressão, permitindo que os emojis sejam exibidos um de cada vez. 
                    print('💵 ', end = '', flush = True) 
                    sleep(0.5)
                print(colored(f'\nOperacão realizada com sucesso!', 'light_yellow'))
                sleep(1)
                break
    elif opcao == 3:
        today = f"{date.today().day}-{date.today().month}-{date.today().year}"
        print(f"\n+{colored(' EXTRATO ', 'light_green'):.^40}+")
        print(f"\033[33m{today}\033[0m")
        print(f"{colored('Depositos', 'cyan')} {qtde_depositos}")
        print(f"{colored('Saques:', 'cyan')} {qtde_saques}\n")
        print(f"{colored('Saldo Atual:', 'yellow')} R$ {saldo:.2f}")
        print(f"+{'.':.^31}+")
        
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

letreiro_2('Obrigado por usar os nossos servicos!', 'white', 'light_blue')