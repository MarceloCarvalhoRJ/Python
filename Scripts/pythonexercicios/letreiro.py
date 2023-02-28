from termcolor import colored
from emoji import emojize, demojize

def letreiro(texto, cor1, cor2):
    print(colored(' ' + '=' * 35 + ' ', cor2))
    print(colored(f"{emojize(':star:')}{colored(texto.center(33), cor1)}{emojize(':star:')}"))
    #print(colored(f'|{texto:^36}|', cor))
    print(colored(' ' + '=' * 35 + ' ', cor2))

def letreiro_2(texto, cor1, cor2):
    print(colored('-' * 37, cor2))
    print(colored((texto + emojize(' :grinning_face_with_big_eyes:')).center(35), cor1))
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