from termcolor import colored
from time import sleep
import json

def linha():
    print('-' * 40)


def cabeçalho(txt):
    linha()
    print(txt.center(40))   
    linha()


def menu():
    nome_arquivo = 'lista_de_cadastro.txt'
    cadastro_usuarios = []
    opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema']

    cabeçalho('MENU PRINCIPAL')
    for p, c in enumerate(opcoes):
        print(colored(p + 1, 'yellow'), colored(' - ', 'white'), colored(c, 'cyan'))
    linha()

    while True:
        try:
            opcao = int(input(colored('Sua opção: ', 'yellow')))
            if  1 <= opcao <= 3:
                break
            else:
                print(colored('Erro! Digite uma opção válida!', 'light_red'))
        except ValueError:
            print(colored('Erro! Digite apenas numeros!', 'light_red'))

    if opcao == 1:
        lista_cadastro(nome_arquivo)
    
    if opcao == 2:
        novo_cadastro(cadastro_usuarios, nome_arquivo)
    
    if opcao == 3:
        cabeçalho('Saindo do sistema...Até logo!')
        sleep(1)
        exit()


def novo_cadastro(cadastro_usuarios, nome_arquivo):
    cabeçalho('NOVO CADASTRO')
    while True:
        nome = input('Nome: ').title()
        if len(nome) == 0:
            print(colored('Acho que você esqueceu de digitar um nome!', 'light_red'))
        elif nome.isnumeric():
            print(colored('Parece que você não digitou letras no nome. Por favor, tente novamente', 'light_red'))
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
            if idade <= 0:
                print(colored('Idade tem que ser maior que zero!', 'light_red'))
            else:
                break
        except ValueError:
            print(colored('Erro! Digite um número inteiro válido!', 'light_red'))

    grava_usuario(nome, idade, nome_arquivo)

    #salvando cada dicionário (usuário) inserido em um arquivo json.
    try:
        with open('cadastro_cursoev.json', 'r') as arquivo:
            cadastro_usuarios = json.load(arquivo)
    except FileNotFoundError:
        cadastro_usuarios = []

    cadastro_usuarios.append({'Nome': nome, 'Idade': idade})
    with open('cadastro_cursoev.json', 'w') as arquivo:
        json.dump(cadastro_usuarios, arquivo)
    #---------------------------------------------------------------
    print(colored('Cadastro efetuado com sucesso!', 'light_yellow'))
    sleep(1)
    menu()


def lista_cadastro(nome_arquivo):
    cabeçalho('PESSOAS CADASTRADAS')
    read_cadastro(nome_arquivo) 
    sleep(1)
    menu()

  
def grava_usuario(nome, idade, nome_arquivo):
    try:
        with open(nome_arquivo, 'a') as cadastro:
            cadastro.write(f'{nome}, {idade}\n')
    except FileNotFoundError:
        print(colored(f'arquivo {nome_arquivo} não foi criado. Criando novo arquivo!', 'light_red'))
        with open(nome_arquivo, 'w') as cadastro:
            print(colored(f'{nome_arquivo} criado com sucesso!', 'yellow'))


def read_cadastro(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as cadastro: 
            for linha in cadastro:
                nome, idade = linha.strip().split(',')
                print(f"{nome:<28} {idade:>3} anos")
    except FileNotFoundError:
        print(colored(f'Lista sem pessoas cadastradas', 'light_red'))