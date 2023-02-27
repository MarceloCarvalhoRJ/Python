
def letreiro(texto, cor1, cor2):
    from termcolor import colored
    print(colored('+' + '=' * 35 + '+', cor2))
    print(colored(f"{colored('|', cor2)}{colored(texto.center(35), cor1)}{colored('|', cor2)}"))
    #print(colored(f'|{texto:^36}|', cor))
    print(colored('+' + '=' * 35 + '+', cor2))

def letreiro_2(texto, cor1, cor2):
    from termcolor import colored
    print(colored('-' * 37, cor2))
    print(colored(texto.center(35), cor1))
    #print(colored(f'|{texto:^36}|', cor))
    print(colored('-' * 37, cor2))

'''
def letreiro(texto, cor):
    
    tam_texto = len(texto)
    espacos = int((36 - tam_texto) / 2)
    print(colored('+' + '-' * 35 + '-+', cor))
    print(colored('|' + ' ' * espacos + texto + ' ' * espacos + '|', cor))
    print(colored('+' + '-' * 35 + '-+', cor))

letreiro('Marcelo', 'cyan')'''