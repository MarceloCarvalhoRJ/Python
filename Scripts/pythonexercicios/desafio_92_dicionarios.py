from datetime import date

pessoa = dict()

pessoa['nome'] = input('Digite o seu nome: ')
age = int(input('Ano de nasc.: '))
pessoa['idade'] = date.today().year - age
pessoa['ctps'] = int(input('Digite o nª da CTPS (0 não tem): '))
if pessoa['ctps'] is not 0:
    pessoa['contratação'] = int(input('Ano contratado: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['contratação'] + 35 - age

for key, value in pessoa.items():
    print(f'{key} tem o valor {value}')
  

