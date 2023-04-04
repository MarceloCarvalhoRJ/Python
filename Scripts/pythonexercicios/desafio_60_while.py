from time import sleep
print('=' * 27)
print('| \033[1;33mCalculadora de Fatorial\033[m |')
print('='* 27)

while True:
    numero = input('\033[36mDigite um numero \033[m(pressione espaço para sair)\033[36m: ')
    if numero == ' ':
        print('\033[31m\nPrograma encerrado pelo usuário!')
        sleep(1)
        print('\n\033[1;34mObrigado por utilizar a Calculadora!\033[m\n')
        break

    i = int(numero)
    fatorial = 1
    print(f'\033[1;34m{numero}! =\033[m ', end = '')
    while i >= 1:
        fatorial *= i 
        if i > 1:
            print(f'\033[1;35m{i}\033[m', end = ' \033[1;31mx\033[m ')
        else:
            print(f'\033[1;35m{i}\033[m', end = ' \033[1;31m=\033[m ')
        i -= 1
    print(f'\033[1;36m{f"{fatorial:,}".replace(",", ".")}\033[m')
   
