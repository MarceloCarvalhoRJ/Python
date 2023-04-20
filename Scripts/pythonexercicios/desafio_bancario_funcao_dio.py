from letreiro import letreiro, letreiro_2
from funcoes_bancaria import *

letreiro('Bem vindo ao Banco MMC', 'magenta', 'light_blue') 
menu = """
<<<  \033[36mMenu\033[0m  >>>

[\033[1;33m1\033[0m] Depositar
[\033[33m2\033[0m] Sacar
[\033[33m3\033[0m] Extrato
[\033[30m0\033[0m] Sair

\033[36mEscolha uma opção =>\033[0m """

saldo = 0
relacao_depositos, relacao_saques = '', ''
limite = 500
numero_saques = 0
vlr_saque = 0
    
while True:

    opcao = int(input(menu))

    if opcao == 1:
        saldo, relacao_depositos = deposito(saldo, relacao_depositos)

    elif opcao == 2:
        numero_saques, vlr_saque, saldo, relacao_saques = saque(numero_saques = numero_saques, vlr_saque = vlr_saque, saldo = saldo, relacao_saques = relacao_saques)
        
    elif opcao == 3:
        gerar_extrato(relacao_depositos, relacao_saques, saldo)
        
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

letreiro_2('👍 Obrigado por usar os nossos servicos!', 'white', 'light_blue')