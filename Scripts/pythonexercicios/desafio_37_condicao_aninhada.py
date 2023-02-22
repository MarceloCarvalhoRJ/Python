from termcolor import colored
from sys import exit
from time import sleep

print(colored('-=-' * 10, 'light_yellow'))
print(colored('Conversor de base numérica...', 'magenta'))
print(colored('-=-' * 10, 'light_yellow'))
n = int(input(colored('Digite um número: ', 'light_green')))
opcao = int(input(colored('''Qual será a base de conversão? 
[1] binário 
[2] octal 
[3] hexadecimal
Sua opção: ''', 'yellow')))
print(colored('Processando...', 'light_blue'))
sleep(1.5)

binario = bin(n).lstrip('0b') #converte em binario e lstrip remove os caracteres '0b' a esquerda.
octal = oct(n).lstrip('0o') #converte em aactal e lstrip remove os caracteres '0o' a esquerda.
hexa = hex(n)[2:] # outra forma - converte em hexadecimal e mostra o texto a partir da posiçao 2 até o final.
if opcao == 1:
    print(colored(f'O numero {n} em binario é {binario}', 'cyan'))
elif opcao == 2:
    print(colored(f'O numero {n} em octal é {octal}', 'cyan'))
elif opcao == 3:
    print(colored(f'O numero {n} em hexadecimal é {hexa}', 'cyan'))
else:
    print(colored('Opção inválida! Tente novamente.', 'red'))
    exit() # encerra o programa caso a opcao seja != 1, 2 ou 3. (biblioteca sys)
