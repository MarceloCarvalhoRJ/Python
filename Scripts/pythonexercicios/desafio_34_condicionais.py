sal = float(input('Digite o valor do seu salário: R$ '))

if sal > 1200:
    print(f'Seu salario de \033[32mR$ {sal:.2f}\033[0m com 10% de aumento passou para \033[33mR$ {sal * 1.10:.2f}\033[0m')
else:
    print(f'Seu salario de \033[32mR$ {sal:.2f}\033[0m com 15% de aumento passou para \033[33mR$ {sal * 1.15:.2f}\033[0m')
