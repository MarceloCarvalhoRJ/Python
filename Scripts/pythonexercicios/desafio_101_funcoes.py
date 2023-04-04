from datetime import date
from main import find_age # escopo de importação - funcao que calcula a idade de uma pessoa.

def vote(year):
    ano = int(input(year))
    age = find_age(ano)
    message = 'Voto negado!' if age < 16 else 'Voto Opcional' if (16 <= age < 18) or (age >= 65) else 'Voto Obrigatório!' #utilizando uma expressão condicional (ternária) em substituicao as linhas no comentário abaixo.
    return print(f'Com {age} anos o voto: {message}.')

    '''if age < 16:
        print(f'Com {age} anos o voto: Voto Negado.')
    elif (16 <= age < 18) or (age >= 65):
        print(f'Com {age} anos o voto: Voto Opcional.')
    else:
        print(f'Com {age} anos: Voto Obrigatório.')
    return year'''

print('.' * 20)
vote('Em que ano você nasceu? ')