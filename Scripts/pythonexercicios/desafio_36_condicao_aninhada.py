from termcolor import colored
vlr_casa = float(input(colored('Qual o valor da casa: R$ ', 'light_green')))
salario = float(input(colored('Digite o valor do seu salário: R$ ', 'light_yellow')))
anos = int(input(colored('Em quantos anos quer financiar: ', 'blue')))
prestacao = vlr_casa / (anos * 12)
if prestacao > (salario * .30):
    print(colored(f'Prestação mensal de R$ {prestacao:.2f} é maior que 30% do salário. \nEmprestimo negado! ', 'red'))
else:
    print(colored(f'Emprestimo aceito! Você vai pagar uma prestacao de \033[36mR$ {prestacao:.2f}\033[0m', 'yellow'))

print(colored(f"Obrigado pela sua {colored('preferencia', 'cyan', 'on_light_cyan')}!", 'light_cyan'))
