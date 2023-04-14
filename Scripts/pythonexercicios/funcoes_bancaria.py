from time import sleep
from termcolor import colored
from datetime import date

def limpa_tela():
    import os
    '''
    #limpa a tela do terminal
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
     LIMITE_SAQUES = 3
     print(colored('Para voltar ao menu principal, digite 0 a qualquer momento.', 'grey'))

     while True:
            try:
                vlr_saque = int(input(colored('Quer sacar quanto? R$ ', 'light_blue')))

                if volta_menu(vlr_saque):
                    break

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
                    numero_saques += 1
                    saldo -= vlr_saque
                    relacao_saques += f"(\033[31m-\033[m){moeda(vlr_saque)}\n"
                    print(colored('Aguarde a contagem das notas \n', 'light_magenta'), end = '')
                    for i in range(1, 7):
                        # a função flush() é adicionada como argumento para a função print(). Isso força o buffer de saída a ser limpo imediatamente após cada impressão, permitindo que os emojis sejam exibidos um de cada vez. 
                        print('💵 ', end = '', flush = True) 
                        sleep(0.3)
                    print(colored(f'\nOperacão realizada com sucesso!', 'light_yellow'))
                    sleep(.7)
                    break

            except ValueError:
                print('Digite somente numero inteiro. Tente novamente.')        
                 
     return numero_saques, vlr_saque, saldo, relacao_saques


def gerar_extrato(relacao_depositos, relacao_saques, saldo):
    today = f"{date.today().day}-{date.today().month}-{date.today().year}"
    print(f"\n+{colored(' EXTRATO ', 'light_green'):.^40}+")
    sleep(.5) 
    print(f"\033[33m{today:^34}\033[0m")
    if not relacao_saques and not relacao_depositos: 
        print('\nNão foram realizadas movimentações.\n')
    else:
        print(f"{colored('Depositos', 'cyan')} \n{relacao_depositos}")
        print(f"{colored('Saques:', 'cyan')} \n{relacao_saques}\n")
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

    while True: #enquanto o usuario não inserir os 11 digitos do CPF o loop continua.
        cpf = input(colored("Informe o CPF (somente números): ", 'light_cyan')).strip()

        if volta_menu(cpf): #funcao para retornar ao menu principal caso o usuário desista do cadastro, basta digitar '0' e apertar enter.
            return    
        
        if is_numeric(cpf, 11): #funcao para verificar se o input eh uma sequencia X digitos (tamanho) e se eh somente de numeros. 
            break
    
    cpf = format_cpf(cpf) #funcao para formatar em padrão CPF brasileiro o número inserido pelo usuario .

    for usuario in cadastro_usuarios: #verifica em cada dicionário dentro da lista se o cpf cadastrado á existe.
        if cpf == usuario['cpf']:
            print(colored('Já existe usuário com esse CPF!', 'light_magenta'))
            sleep(1)
            return
        
    nome = input(colored('Informe o nome completo: ', 'light_cyan')).strip()

    if volta_menu(nome): #funcao para retornar ao menu principal caso o usuário desista do cadastro, basta digitar '0' e apertar enter.
        return 
    
    while True: #enquanto o usuario não inserir os 6 digitos da data de nasc. o loop continua.
        data_nascimento = input(colored('Informe a data de nascimento (DDMMAA). ', 'light_cyan')).strip()

        if volta_menu(data_nascimento):
            return
        
        if is_numeric(data_nascimento, tamanho=6): #funcao para verificar se o input eh uma sequencia X digitos (tamanho) e se eh somente de numeros. 
            break 
    
    endereco = input(colored("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ", 'light_cyan')).strip()
    if volta_menu(endereco):
        return 
    
    cadastro_usuarios.append({'cpf': cpf, 'nome': nome, 'data_nascimento': format_data(data_nascimento), 'endereço': endereco}) #cria um dicionário dentro da lista com as informacões de cada usuário. format_data -> formata o nr. inserido em dd/mm/aa.

    print()
    print(colored("=== Usuário criado com sucesso! ===", 'light_yellow'))
    sleep(1)

    return cadastro_usuarios


def lista_usuarios(cadastro_usuarios):
    print()
    print('\033[33m-\033[0m' * 16, '«««  \033[33mLista de usuários\033[0m  »»»', '\033[33m-\033[0m' * 16)

    if len(cadastro_usuarios) == 0:
        print('\nNao existe usuários cadastrados!\n') 
    else:
        for usuario in cadastro_usuarios:
            for key, value in usuario.items():
                print(f'\033[36m{key}:\033[0m {value}\n')
            if usuario is not cadastro_usuarios[-1]:
                print(colored('-' * 61, 'light_yellow'))
            sleep(.3)
    print('\033[33m-\033[0m' * 19, '«««  \033[33mFim da Lista\033[0m  »»»', '\033[33m-\033[0m' * 18)
    input(colored("Pressione a tecla ENTER para retornar ao menu principal.", 'grey')) # aguarda o usuário pressionar a tecla 'espaço'


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
    if vlr == '0' or vlr == 0:
        print(colored("Operação cancelada pelo usuário.", 'light_yellow'))
        sleep(.5)
        return True   


def is_numeric(num, tamanho = 11):
    if num.isnumeric():
        if len(num) == tamanho:
            return True
        else:
            num = 'CPF' if tamanho == 11 else 'Data de Nascimento'
            print(f"{num} deve ter {tamanho} dígitos. Tente novamente.")
            sleep(.5)
    else:
        print("Somente números devem ser inseridos. Tente novamente.")  
        sleep(.5)

if __name__ == '__main__':
    #print(deposito())
    #print(cadastro_usuario())
    #print(cadastro_conta())
    help(cadastro_usuario)