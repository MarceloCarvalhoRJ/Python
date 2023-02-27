from termcolor import colored

soma = count = 0
while True:
    num = int(input(colored('Digite um número \033[30m[digite 999 para sair]\033[m: ', 'yellow')))
    if num == 999:
        print(colored(f'\nVoce digitou {count} numeros e a soma é {soma}', 'cyan'))
        break
    soma += num
    count += 1

print(colored('\nObrigado por usar a nossa calculadora!', 'magenta'))