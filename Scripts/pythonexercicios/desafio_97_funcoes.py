import os
#limpa a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

from termcolor import colored
def titulo(text):
    tam = len(text) + 4
    print(colored('~' * tam, 'yellow'))
    print(colored(f'{text.center(tam)}', 'cyan'))
    print(colored('~' * tam, 'yellow'))


texto = input('Texto: ').title()
titulo(texto)