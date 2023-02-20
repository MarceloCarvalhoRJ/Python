from termcolor import colored 
from random import randint
from time import sleep
print(colored('-=-' * 20, 'light_yellow')) # colore a fonte
print(colored('Vou pensar em um número entre 0 e 5. Tente adivinhar...', 'blue'))
print(colored('-=-' * 20, 'light_yellow'))
num = int(input('Em que número eu pensei? '))
print(colored('Processando...', 'magenta'))
sleep(1.5) #para o programa por alguns momentos.
aleatorio = randint(0, 5) #função que escolhe de forma aleatorio um nr. entre 0 e 5.
if (num == aleatorio):
    print(colored(f'O numero que pensei foi {aleatorio}. \nPARABÉNS! Você venceu!!!', 'yellow'))
else:
    print(colored(f'GANHEI! Eu pensei no número \33[36m{aleatorio}\33[31m e você não acertou.', 'red'))
