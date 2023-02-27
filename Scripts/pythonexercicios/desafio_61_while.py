from termcolor import colored
print('=' * 30)
print(colored(f"{'10 TERMOS DE UMA PA':^30}", "cyan")) # centraliza o texto no espaço de 30 caracteres usando a f-string
print('=' * 30)
primeiro_termo = int(input(colored('Digite o primeiro termo: ', 'light_yellow')))
razao = int(input(colored('Digite a razão: ', 'light_yellow')))
pa = primeiro_termo
print()
print(f'\033[1;35m{primeiro_termo}\33[m', end = ' \033[31m→\033[m ')
i = 1
while i < 10:
    pa += razao
    print(f'\033[1;35m{pa}\33[m', end = ' \033[31m→\033[m ')
    i += 1

print(colored('Fim!\n', 'light_cyan'))