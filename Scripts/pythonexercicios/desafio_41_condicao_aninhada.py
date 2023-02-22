from datetime import date

ano_nasc = int(input('Informe o ano do seu nascimento: '))
idade = date.today().year - ano_nasc
if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é JÚNIOR.') 
elif idade <= 25:
    print(f'Você tem {idade} anos e sua categoria é SENIOR.')
else:
    print(f'Você tem {idade} anos e sua categoria é MASTER.')
