from time import sleep

def titulo(texto):
    tamanho = len(texto) + 4
    print('=' *tamanho)
    print('| \033[1;33mCalculadora de Fatorial\033[m |')
    print('='*tamanho)

titulo('')

while True:
    numero = int(input('\033[1;36mDigite um número inteiro para calcular o seu fatorial (digite um número negativo para sair): \033[m'))

    if numero < 0:
        print('\033[1;32mSaindo do programa...\033[m')
        sleep(1)
        break

    i = numero
    fatorial = 1
    print(f'\033[1;34m{numero}! =\033[m ', end = '')
    while i >= 1:
        fatorial *= i 
        if i > 1:
            print(f'\033[1;35m{i}\033[m', end = ' \033[1;31mx\033[m ')
        else:
            print(f'\033[1;35m{i}\033[m', end = ' \033[1;31m=\033[m ')
        i -= 1
    print(f'\033[1;36m{fatorial}\033[m')
