from termcolor import colored
from random import randint
from sys import exit
from time import sleep

print(colored('/\\' * 8 + '/\\' * 8, 'light_yellow'))
print(colored(' JOGO DA PEDRA, PAPEL E TESOURA ', 'black', 'on_light_cyan'))
print(colored('/\\' * 8 + '/\\' * 8, 'light_yellow'))
opcao = int(input(colored('''O que você escolhe: 
[0] PEDRA
[1] PAPEL 
[2] TESOURA
Qual a sua opção? ''', 'cyan')))
lista = ['Pedra', 'Papel', 'Tesoura']
escolha = randint(0, 2)
if opcao > 2:
    print(colored('Opcao inválida! Jogo encerrado.', 'light_red'))
    exit()
print(colored('JO', 'yellow'))
sleep(.5)
print(colored('KEN', 'yellow'))
sleep(.5)
print(colored('PO!!!', 'yellow'))
sleep(.5)
print('-=' * 20)
if lista[opcao] == lista[escolha]:
    print(colored(f'Eu escolhi {lista[escolha]} e você escolheu {lista[opcao]}. \nEmpatou!', 'grey'))
elif   opcao == 1 and escolha == 0 \
    or opcao == 2 and escolha == 1 \
    or opcao == 0 and escolha == 2:
    print(colored(f'Eu escolhi {lista[escolha]} e voce escolheu {lista[opcao]}. \nParabéns! Você venceu!', 'green'))
else:
    print(colored(f'Eu escolhi {lista[escolha]} e você escolheu {lista[opcao]}. \nNão foi dessa vez, eu ganhei!', 'magenta'))
print('-=' * 20)
