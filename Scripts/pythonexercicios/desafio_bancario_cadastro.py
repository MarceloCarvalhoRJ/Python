from letreiro import letreiro, letreiro_2
from funcoes_bancaria import *

limpa_tela()
letreiro('Bem vindo ao Banco MMC', 'magenta', 'light_blue') 
menu = """
<<<  \033[36mMenu\033[0m  >>>

[\033[1;33m1\033[0m] Cadastrar usuário
[\033[33m2\033[0m] Cadastrar Conta Bancária
[\033[1;33m3\033[0m] Listar usuários
[\033[1;33m4\033[0m] Listar Contas
[\033[30m0\033[0m] Sair

\033[36mEscolha uma opção =>\033[0m """

cadastro_usuarios, cadastro_contas = list(), list()

while True:

    while True:
        try:
            opcao = int(input(menu))
            break
        except (ValueError, AttributeError):
            print(colored('Valor inválido!', 'light_red'))
            sleep(.5)

    if opcao == 1:
        cadastro_usuario(cadastro_usuarios)
        

    elif opcao == 2:
        cadastro_conta(cadastro_usuarios, cadastro_contas)

    elif opcao == 3:
        lista_usuarios(cadastro_usuarios)

    elif opcao == 4:
        lista_contas(cadastro_contas)
        
    elif opcao == 0:
        break

    else:
        print(colored("Opção inválida, selecione novamente a opção desejada.", 'light_magenta'))
        sleep(.5)

letreiro_2('👍 Obrigado por usar os nossos servicos!', 'white', 'light_blue') 
