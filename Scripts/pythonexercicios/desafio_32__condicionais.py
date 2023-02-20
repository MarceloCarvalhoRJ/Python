from calendar import isleap
from datetime import date
ano = date.today().year
ano = int(input(f'Estamos no ano de {ano}, qual o ano voce gostaria de informar: '))
if(isleap(ano)):
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')