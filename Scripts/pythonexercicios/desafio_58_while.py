from termcolor import colored 
from random import randint
from time import sleep

print('\033[1;34m+-' + '-'*20 + '-+\033[m')
print('\033[1;34m|      Calculadora     |\033[m')
print('\033[1;34m+-' + '-'*20 + '-+\033[m')

print(colored('-=-' * 20, 'light_yellow')) # colore a fonte
print(colored('Vou pensar em um número entre 0 e 10. Tente adivinhar...', 'blue'))
print(colored('-=-' * 20, 'light_yellow'))

cont_jogadas = 0
aleatorio = 0
num = 0
aleatorio = randint(0, 10) #função que escolhe de forma aleatorio um nr. entre 0 e 10.

while True:
    num = int(input('Qual é o seu palpite? '))
    if num >= 0 and num <= 10:
        cont_jogadas += 1 # conta qtas jogadas foram necessárias para o usuário vencer.
        if num > aleatorio:
            print('Menos...', end = '')
        elif num < aleatorio:
            print('Mais...', end = '')  
        elif  num == aleatorio:
            print(colored(f'Acertou com {cont_jogadas} tentativas. Parabéns!', 'cyan'))
            break
    else:
        print(colored('Por favor, digite um número válido entre 0 e 10.', 'grey'))
    
