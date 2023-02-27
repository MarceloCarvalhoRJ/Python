from datetime import date
from termcolor import colored
maioridade = 0
menoridade = 0
ano_atual = date.today().year
print(colored('-' * 35, 'yellow'))
for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento: '))
    idade = ano_atual - ano
    print(f'A {i}ª pessoa tem {idade} anos.')
    print(colored('-' * 35, 'yellow'))
    if idade >= 21:
        maioridade += 1     
    else:
        menoridade += 1
print(f'O total de pessoas maiores de idade é: {maioridade}. \nO total de pessoas menor de idade é: {menoridade}.')
print(colored('-' * 16, 'yellow'), colored('   x   ', 'green'), colored('-' * 16, 'yellow'))
