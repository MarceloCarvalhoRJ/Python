from time import sleep
from termcolor import colored
from datetime import date

def limpa_tela():
    import os
    '''
    limpa a tela do terminal
    '''
    
    os.system('cls' if os.name == 'nt' else 'clear')


def moeda(p, coin='R$'):
    """
    Retorna uma string formatada com o valor monetário e a moeda especificada.

    Args:
        p (float): O valor monetário a ser formatado.
        coin (str, optional): A moeda a ser utilizada na formatação. Valor padrão é 'R$'.

    Returns:
        str: A string formatada com o valor monetário e a moeda especificada.
    """
    return f'{coin} {p:.2f}'.replace('.', ',')


def deposito(saldo, relacao_depositos):
    """Realiza um depósito na conta bancária especificada.

    Args:
        saldo (float): O saldo atual da conta bancária.
        qtde_depositos (str): A string que armazena a quantidade e valores de depósitos feitos na conta.

    Returns:
        Tuple[float, str]: Uma tupla contendo o novo saldo da conta bancária e a string 'qtde_depositos' atualizada.
    """
    # Entra em um loop infinito para receber o valor do depósito até que seja válido
    print(colored('Para voltar ao menu principal, digite 0 a qualquer momento.', 'grey'))
    while True:
        try:
            vlr_deposito = float(input(colored('\nQual o valor do depósito? R$ ', 'light_magenta')))

            if volta_menu(vlr_deposito): #funcao para retornar ao menu principal caso o usuário desista do cadastro, basta digitar '0' e apertar enter.
                break
            
            if vlr_deposito > 0:
                # Adiciona o valor do depósito ao saldo da conta
                saldo += vlr_deposito
                # Atualiza a string 'relacao_depositos' com o valor do novo depósito
                relacao_depositos += f"{moeda(vlr_deposito)}\n"
                print(colored('💰 Depósito realizado com sucesso! 💰', 'light_yellow'))
                sleep(.5) #funcao moeda, formata por padrao o numero em moeda BRL.
                break
            else:
                # Informa ao usuário que o valor é inválido e pede que insira novamente
                print('O valor deve ser maior do que zero. Tente novamente.')
        except ValueError:
            # Informa ao usuário que o valor é inválido e pede que insira novamente
            print('Digite somente numeros. Tente novamente.')
        

    # Retorna uma tupla contendo o novo saldo da conta bancária e a string 'qtde_depositos' atualizada
    return saldo, relacao_depositos


def saque(numero_saques, vlr_saque, saldo, relacao_saques):
    """
    Realiza o saque de um determinado valor a partir do saldo disponível,
    desde que sejam atendidas algumas condições, como quantidade de saques
    diários e valor máximo de saque.

    Args:
        numero_saques (int): o número de saques já realizados naquele dia.
        vlr_saque (float): o valor a ser sacado.
        saldo (float): o saldo disponível para saque.
        relacao_saques (str): uma string com os valores sacados e depositados.

    Returns:
        tuple: uma tupla contendo o número de saques realizados, o valor sacado,
        o saldo restante e a relação de saques atualizada.

    Raises:
        ValueError: caso o valor de saque não seja um número inteiro.

    Examples:
        >> saque(2, 100, 500, "")
        (3, 100, 400, '(-R$100)\n')
    """

    LIMITE_SAQUES = 3  # define a constante LIMITE_SAQUES com o valor 3
    
    print(colored('Para voltar ao menu principal, digite 0 a qualquer momento.', 'grey'))

    while True:
        try:
            # solicita ao usuário o valor do saque e converte para inteiro
            vlr_saque = int(input(colored('Quer sacar quanto? R$ ', 'light_blue')))

            # verifica se o usuário deseja voltar ao menu principal e encerra o loop
            if volta_menu(vlr_saque):
                break

            # verifica se o número de saques é maior ou igual ao limite de saques permitido e encerra o loop
            if numero_saques >= LIMITE_SAQUES:
                print('Quantidade de saques acima do limite diário.')
                sleep(1)
                break

            if vlr_saque <= 0:
                print('Valor tem que ser maior que 0. Tente novamente.')
            
            elif vlr_saque > 500:
                print(colored('Valor de saque acima do limite de R$ 500', 'grey'))
            
            elif saldo < vlr_saque:
                print(f"Saldo insuficiente! Seu saldo atual é {colored(moeda(saldo), 'light_yellow')}")
                sleep(2)
                break
            else:
                # contador para o número de saques realizados
                numero_saques += 1
                # subtrai o valor do saque do saldo atual
                saldo -= vlr_saque
                # adiciona a relação de saques uma string formatada no padrao moeda BRL indicando o valor do saque 
                relacao_saques += f"(\033[31m-\033[m){moeda(vlr_saque)}\n"
               
                print(colored('Aguarde a contagem das notas \n', 'light_magenta'), end = '')
                
                for i in range(1, 7):
                    print('💵 ', end = '', flush = True) 
                    sleep(0.3)
                
                print(colored(f'\nOperacão realizada com sucesso!', 'light_yellow'))
                sleep(.7)
                break

        # trata a exceção ValueError, caso o usuário digite um valor que não seja um número inteiro
        except ValueError:
            print('Digite somente numero inteiro. Tente novamente.')        
                 
    # Retorna o número de saques, o valor sacado, o saldo atualizado e a relação de saques realizados para serem usados em outras funções.            
    return numero_saques, vlr_saque, saldo, relacao_saques


def gerar_extrato(relacao_depositos, relacao_saques, saldo):
    """
    Gera um extrato bancário com as relações de depósitos e saques e o saldo atual.

    Parâmetros:
    -----------
    relacao_depositos : str
        String contendo a relação de depósitos realizados.
    relacao_saques : str
        String contendo a relação de saques realizados.
    saldo : float
        Saldo atual da conta.

    Retorna:
    --------
    None
    """

    # Obtém a data atual.
    today = f"{date.today().day}-{date.today().month}-{date.today().year}"

    print(f"\n+{colored(' EXTRATO ', 'light_green'):.^40}+")
    sleep(.5)

    print(f"\033[33m{today:^34}\033[0m")

    # Verifica se não houve nenhuma movimentação na conta.
    if not relacao_saques and not relacao_depositos: 
        print('\nNão foram realizadas movimentações.\n')
    else:
        # Imprime a relação de depósitos.
        print(f"{colored('Depositos', 'cyan')} \n{relacao_depositos}")

        # Imprime a relação de saques.
        print(f"{colored('Saques:', 'cyan')} \n{relacao_saques}\n")

    # Imprime o saldo atual formatada em moeda BRL pela funcao moeda().
    print(f"{colored('Saldo Atual:', 'yellow')} {moeda(saldo)}")
    sleep(1)

    print(f"+{'.':.^31}+")

    input(colored("Pressione a tecla ENTER para retornar ao menu principal.", 'grey'))


def cadastro_usuario(cadastro_usuarios):
    """
    Cria um novo usuário no sistema a partir das informações fornecidas pelo usuário.

    Args:
        cadastro_usuarios (list): Uma lista de dicionários contendo informações de todos os usuários cadastrados no sistema.

    Returns:
        list: Uma lista atualizada de dicionários contendo informações de todos os usuários cadastrados no sistema, incluindo o novo usuário criado.
    """
    print(colored('Para voltar ao menu principal, digite 0 a qualquer momento.', 'grey'))

    #O loop só é encerrado qdo o usuario inserir os 11 digitos do CPF.
    while True: 
        cpf = input(colored("Informe o CPF (somente números): ", 'light_cyan')).strip()

        #funcao para retornar ao menu principal caso o usuário desista do cadastro, basta digitar '0' e apertar enter.
        if volta_menu(cpf): 
            return    
        #funcao para verificar se o input eh uma sequencia X digitos (tamanho) e se eh somente de numeros. 
        if is_numeric(cpf, 11): 
            break
    #funcao para formatar o numero fornecido pelo usuário no padrão CPF brasileiro.
    cpf = format_cpf(cpf) 
    #verifica em cada dicionário dentro da lista se o cpf cadastrado já existe.
    for usuario in cadastro_usuarios: 
        if cpf == usuario['cpf']:
            print(colored('Já existe usuário com esse CPF!', 'light_magenta'))
            sleep(1)
            return
        
    nome = input(colored('Informe o nome completo: ', 'light_cyan')).strip()
    #funcao para retornar ao menu principal caso o usuário desista do cadastro, basta digitar '0' e apertar enter.
    if volta_menu(nome): 
        return 
    #enquanto o usuario não inserir os 6 digitos da data de nascimento o loop continua.
    while True: 
        data_nascimento = input(colored('Informe a data de nascimento (DDMMAA). ', 'light_cyan')).strip()

        if volta_menu(data_nascimento):
            return
        #funcao para verificar se o input eh uma sequencia X digitos (tamanho) e se eh somente de numeros.
        if is_numeric(data_nascimento, tamanho=6):  
            break 
    
    endereco = input(colored("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ", 'light_cyan')).strip()
    if volta_menu(endereco):
        return 
    #cria um dicionário dentro da lista cadastro_usurios com as informacões de cada usuário. format_data() -> formata data inserida pelo usuário em dd/mm/aa.
    cadastro_usuarios.append({'cpf': cpf, 'nome': nome, 'data_nascimento': format_data(data_nascimento), 'endereço': endereco}) 

    print()
    print(colored("=== Usuário criado com sucesso! ===", 'light_yellow'))
    sleep(1)
    # retorna a lista cadastro_usuarios atualizada para ser usada por outras funções.
    return cadastro_usuarios


def lista_usuarios(cadastro_usuarios):
    """
    Exibe uma lista com os usuários cadastrados, mostrando suas informações pessoais.

    Args:
        cadastro_usuarios (list): lista de dicionários com as informações dos usuários.
    """
    print()
    print('\033[33m-\033[0m' * 16, '«««  \033[33mLista de usuários\033[0m  »»»', '\033[33m-\033[0m' * 16)

    # Verifica se a lista está vazia
    if len(cadastro_usuarios) == 0:
        print('\nNao existe usuários cadastrados!\n') 
    else:
        # Itera sobre a lista de cadastro_usuários
        for usuario in cadastro_usuarios:
            # Itera sobre o dicionário do usuário para imprimir a chave e o valor.
            for key, value in usuario.items():
                print(f'\033[36m{key}:\033[0m {value}\n')
            # Imprime uma linha de separação entre os usuários, exceto no último
            if usuario is not cadastro_usuarios[-1]:
                print(colored('-' * 61, 'light_yellow'))
            # Aguarda um curto período para melhorar a legibilidade
            sleep(.3)
    
    # Imprime uma mensagem de fim de lista
    print('\033[33m-\033[0m' * 19, '«««  \033[33mFim da Lista\033[0m  »»»', '\033[33m-\033[0m' * 18)
    # Aguarda a entrada do usuário para continuar no intuito de melhorar a visualizacao da lista.
    input(colored("Pressione a tecla ENTER para retornar ao menu principal.", 'grey')) 


def cadastro_conta(cadastro_usuarios, cadastro_contas):
    AGENCIA = '0001'
    conta = len(cadastro_contas) + 1

    print(colored('Para voltar ao menu principal, digite 0 a qualquer momento.', 'grey'))
    print(f'\033[33mAgencia:\033[m {AGENCIA} \n\033[33mConta Corrente:\033[m {conta}')

    while True:
        cpf_usuario = input(colored("Informe o CPF (somente números): ", 'light_cyan')).strip()

        if volta_menu(cpf_usuario):
            return
        
        if is_numeric(cpf_usuario, 11):
            break      

    cpf_usuario = format_cpf(cpf_usuario)
    for usuario in cadastro_usuarios:
        if cpf_usuario == usuario['cpf']:
            cadastro_contas.append({'agencia': AGENCIA, 'conta': conta, 'usuario': cpf_usuario})
            
            print()
            print(colored('=== Conta criada com sucesso! ===', 'light_green'))
            sleep(1)
            return
    
    print(colored('CPF não encontrado no cadastro de usuários. Certifique-se que digitou os 11 digitos.', 'light_magenta'))
    sleep(1)
    
    
def lista_contas(cadastro_contas):
    print()
    print('\033[32m-\033[0m' * 6, '«««  \033[32mLista de Contas\033[0m  »»»', '\033[32m-\033[0m' * 6)

    if len(cadastro_contas) == 0:
        print('\nNao existe contas cadastradas!\n') 
    else:
        for conta in cadastro_contas:
            for key, value in conta.items():
                print(f'\033[33m{key}:\033[0m {value}\n')
            if conta is not cadastro_contas[-1]:
                print(colored('-' * 41, 'light_yellow'))
            sleep(.3)

    print('\033[32m-\033[0m' * 8, '«««  \033[32mFim da Lista\033[0m  »»»', '\033[32m-\033[0m' * 7)
    input(colored("Pressione a tecla ENTER para retornar ao menu principal.", 'grey'))


def format_cpf(id):
    """
    Formata um número inteiro de 11 dígitos no formato de CPF do Brasil.
    :param cpf: o número inteiro de 11 dígitos a ser formatado
    :return: a string formatada no formato de CPF
    """
    cpf = str(id)
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

  
def format_data(date):
    return f'{date[:2]}/{date[2:4]}/{date[4:]}'


def volta_menu(vlr):
    """
    Verifica se o valor de entrada é igual a '0' e, se for, retorna uma mensagem de operação cancelada.

    Args:
        vlr (int or str): O valor de entrada a ser verificado.

    Returns:
        bool: True se o valor de entrada for igual a '0', False caso contrário.
    """
    if vlr == '0' or vlr == 0:
        print(colored("Operação cancelada pelo usuário.", 'light_yellow'))
        sleep(.5)
        return True   


def is_numeric(num, tamanho = 11):
    """
    Verifica se a string inserida pelo usuário contém apenas números e possui o tamanho correto.

    Args:
        num (str): A string inserida pelo usuário.
        tamanho (int): O tamanho correto que a string deve ter (padrão = 11 para CPF).

    Returns:
        bool: Retorna True se a string é numérica e tem o tamanho correto, caso contrário retorna False e exibe uma mensagem de erro.
    """
    #Verifica se a string 'num' contém apenas caracteres numéricos
    if num.isnumeric():
        # Verifica se a string 'num' possui o tamanho correto, definido pelo parâmetro 'tamanho'
        if len(num) == tamanho:
            return True
        else:
            # Caso a string não possua o tamanho correto, exibe uma mensagem de erro e aguarda meio segundo
            num = 'CPF' if tamanho == 11 else 'Data de Nascimento'
            print(f"{num} deve ter {tamanho} dígitos. Tente novamente.")
            sleep(.5)
    else:
        # Caso a string não possua apenas caracteres numéricos, exibe uma mensagem de erro e aguarda meio segundo
        print("Somente números devem ser inseridos. Tente novamente.")  
        sleep(.5)

if __name__ == '__main__':
    #print(deposito())
    #print(cadastro_usuario())
    #print(cadastro_conta())
    help(saque)