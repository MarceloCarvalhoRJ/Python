'''
        ««« Projeto do Curso de Python da Dio.me »»»
        
-> Este programa aborda vários conceitos fundamentais de Python, como: 
- Loop: utilização de while e for para repetição de código
- Condicionais: uso de if, elif e else para executar diferentes trechos de código
- Funções: criação e uso de funções para tornar o código mais modular e reutilizável
- Modularização: utilização de módulos para organizar e separar o código em arquivos diferentes
- Manipulação de strings: utilização de métodos para manipular strings, como format, split, join e slicing
- Listas e dicionários: criação e manipulação de listas e dicionários para armazenar informações
- Utilização de outras bibliotecas e ferramentas: Biblioteca "termcolor" para colorir o output do console e a tabela de cores ANSI. Funções "letreiro" e "letreiro_2" do arquivo "letreiro.py" para criar letreiros coloridos na tela. 
- Tratamento de erros e exceções: utilização de try/except para tratar erros e exceções em tempo de execução
- Aninhamento de funções: utilização de funções dentro de funções para modularizar ainda mais o código
- Docstrings e argumentos opcionais: utilização de docstrings para documentar o código e argumentos opcionais em algumas funções para aumentar a flexibilidade

-> O objetivo deste programa é simular um sistema bancário simples, com as seguintes funcionalidades:
# - Depósito em conta bancária
# - Saque em conta bancária (com limite de saques e limite de valor por saque)
# - Exibição do extrato bancário (histórico de depósitos e saques)
# - Cadastro de usuários e contas bancárias
# - Listagem de usuários e contas bancárias

-> Para alcançar esse objetivo, o programa utiliza as seguintes funções do arquivo funcoes.bancarias.py:
# - deposito: realiza o depósito em uma conta bancária e atualiza o saldo e o histórico de depósitos
# - saque: realiza o saque em uma conta bancária e atualiza o saldo, o limite de saques e o histórico de saques
# - gerar_extrato: exibe na tela o extrato bancário, mostrando o histórico de depósitos e saques
# - cadastro_usuario: cadastra um novo usuário e adiciona à lista de usuários cadastrados
# - cadastro_conta: cadastra uma nova conta bancária para um usuário existente e adiciona à lista de contas cadastradas
# - lista_usuarios: exibe na tela a lista de usuários cadastrados
# - lista_contas: exibe na tela a lista de contas cadastradas
'''


# Importa as funções "letreiro" e "letreiro_2" do arquivo "letreiro.py"
from letreiro import letreiro, letreiro_2

# Importa todas as funções do arquivo "funcoes_bancaria.py"
from funcoes_bancaria import *

# Limpa a tela do console
limpa_tela()

# Cria um letreiro de boas-vindas com as cores "magenta" e "light_blue"
letreiro('Bem vindo ao Banco MMC', 'magenta', 'light_blue') 

# Define um menu com opções numeradas, utilizei a tabela de cores ANSI.
menu = """
<<<  \033[36mMenu\033[0m  >>>

[\033[1;33m1\033[0m] Depositar
[\033[33m2\033[0m] Sacar
[\033[33m3\033[0m] Extrato
[\033[1;33m4\033[0m] Cadastrar usuário
[\033[33m5\033[0m] Cadastrar Conta Bancária
[\033[1;33m6\033[0m] Listar usuários
[\033[1;33m7\033[0m] Listar Contas
[\033[30m0\033[0m] Sair

\033[36mEscolha uma opção =>\033[0m """

# Cria duas listas vazias, "cadastro_usuarios" e "cadastro_contas"
cadastro_usuarios, cadastro_contas = list(), list()

saldo = 0
relacao_depositos, relacao_saques = '', ''
limite = 500
numero_saques = 0
vlr_saque = 0

    # Loop para tratar do menu principal, encerra somente se digitar zero.
while True:
    # o loop somente será encerrado se o usuário digitar uma das opçõees.
    while True:
        try:
            opcao = int(input(menu))
            break
        except (ValueError, AttributeError):
            print(colored('Valor inválido!', 'light_red'))
            sleep(.5)

    # Opção 1 - efetua depósito.
    if opcao == 1:
        saldo, relacao_depositos = deposito(saldo, relacao_depositos)

    # Opção 2 - efetua saque
    elif opcao == 2:
        numero_saques, vlr_saque, saldo, relacao_saques = saque(numero_saques = numero_saques, vlr_saque = vlr_saque, saldo = saldo, relacao_saques = relacao_saques)

    # Opção 3 - mostra na tela o extrato   
    elif opcao == 3:
        gerar_extrato(relacao_depositos, relacao_saques, saldo)

    # Opção 4 - Cadastro de Usuário
    elif opcao == 4:
        # Chama a função de cadastro de usuário e passa a lista de usuários como argumento
        cadastro_usuario(cadastro_usuarios)

    # Opção 5 - Cadastro de Conta Bancária
    elif opcao == 5:
        # Chama a função de cadastro de conta e passa as listas de usuários e contas como argumentos
        cadastro_conta(cadastro_usuarios, cadastro_contas)

    # Opção 6 - Listagem de Usuários
    elif opcao == 6:
        # Chama a função de listagem de usuários e passa a lista de usuários como argumento
        lista_usuarios(cadastro_usuarios)

    # Opção 7 - Listagem de Contas Bancárias
    elif opcao == 7:
        # Chama a função de listagem de contas e passa a lista de contas como argumento
        lista_contas(cadastro_contas)
        
    # Opção 0 - Sair do programa
    elif opcao == 0:
        # Encerra o loop principal e finaliza o programa
        break

    # Opção inválida
    else:
        print(colored("Opção inválida, selecione novamente a opção desejada.", 'light_magenta'))
        sleep(.5)

# Exibe mensagem de agradecimento ao usuário
letreiro_2('👍 Obrigado por usar os nossos serviços!', 'white', 'light_blue') 
