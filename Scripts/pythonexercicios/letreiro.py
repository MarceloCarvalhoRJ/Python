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

letreiro('Marcelo', 'cyan')

print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")    
texto = 'CALCULDORA DE MATRIZ'
print(f'{texto:^37}')
print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")

matrix = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        num = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        matrix[l].append(num)
print('╔════════════════════════════════════╗')
print(f'║   \033[33m{matrix[0]}\033[m \033[34m{matrix[1]}\033[m \033[35m{matrix[2]}\033[m    ║')
print('╚════════════════════════════════════╝')

print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")    
texto = 'CALCULDORA DE MATRIZ'
print(f'{texto:^37}')
print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")'''