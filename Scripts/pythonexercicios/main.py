from datetime import date
def find_age(year):
    """
    funcao para calcular a idade de uma pessoa
    recebe o valor ano
    retorna a usa idade.
    """
    age = date.today().year - year
    return age

def fatorial(number):
    """
    funcao para calcular o fatorial
    recebe um numero como valor
    retorna o seu fatorial.
    """
    #possível implementação recursiva da função fatorial: Essa função usa um if para tratar o caso base, que é quando number é igual a zero. Nesse caso, o resultado do fatorial é 1. Caso contrário, a função chama a si mesma com o argumento number - 1, multiplicando o resultado pela variável number. 
    if number == 0:
        return 1
    else:
        return number * fatorial(number -1)
    '''fat = 1
    for i in range(number, 0, -1):
        fat *= i
    return fat'''

import os
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    '''
    #limpa a tela do terminal
    '''

