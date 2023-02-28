from letreiro import letreiro, letreiro_2
from termcolor import colored

letreiro('BANCO MMC', 'magenta', 'light_yellow')

vlr_saque = int(input(colored('Qual valor quer sacar? R$ ', 'light_blue')))

notas = [50, 20, 10, 1]
qtde_notas = [0, 0, 0, 0]

for i in range(len(notas)):
    while vlr_saque >= notas[i]:
        qtde_notas[i] += 1
        vlr_saque -= notas[i]
    if qtde_notas[i] > 0:
        print(f'Total de {qtde_notas[i]} cédulas de R$ {notas[i]}')

letreiro_2('Volte sempre ao Banco MMC. \nTenha um bom dia!', 'cyan', 'yellow')
      
