from letreiro import letreiro, letreiro_2
from termcolor import colored

maior_18 = homens = mulheres = 0
while True:
    letreiro('CADASTRO DE PESSOA', 'magenta', 'blue')
    idade = int(input('Idade: '))
    if idade >= 18:
        maior_18 += 1
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
        if sexo not in 'MF':
            continue
        else:
            break
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    print(colored('-' * 37, 'magenta'))
    while True:
        continua = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if continua not in 'SN':
            continue
        else:
            break
    if continua == 'S':
        continue
    else:
        print(colored('\n========  FIM DO PROGRAMA  ========', 'light_red'))
        print(colored(f'O total de pessoas com mais de 18 anos: {maior_18}', 'yellow'))
        print(colored(f'Ao todo temos {homens} homens cadastrados.', 'light_yellow'))
        print(colored(f'E temos {mulheres} mulheres com menos de 20 anos.', 'yellow'))
        
        letreiro_2('VOLTE SEMPRE!', 'yellow', 'cyan')
        break
