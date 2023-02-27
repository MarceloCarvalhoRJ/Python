from letreiro import letreiro, letreiro_2
from termcolor import colored

letreiro_2('BANCO MMC', 'magenta', 'light_yellow')

vlr_saque = int(input(colored('Qual valor quer sacar? R$ ', 'light_blue')))
ced = 50
tot_ced = 0
while True:
    if vlr_saque >= ced:
        vlr_saque -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'O total de {tot_ced} cédulas de R$ {ced}')
            tot_ced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if vlr_saque == 0:
            break
    
letreiro_2('Volte sempre ao Banco MMC. \nTenha um bom dia!', 'cyan', 'yellow')
      
