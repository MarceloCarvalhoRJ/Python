from letreiro import letreiro, letreiro_2
from main import limpa_tela

def notas(*notas, calcular_situacao=False):
    """
    Função que recebe um conjunto de notas e calcula algumas informações sobre elas.
    
    Args:
        *notas (float): um conjunto de notas, representadas como números de ponto flutuante.
        sit (bool): se True, a função também calcula a situação das notas e inclui a informação no retorno.
        
    Returns:
        Um dicionário com as seguintes informações:
            - total (float): a soma de todas as notas.
            - maior (float): a maior nota do conjunto.
            - menor (float): a menor nota do conjunto.
            - média (float): a média aritmética das notas.
            - situação (str) [opcional]: a situação das notas, calculada apenas se o argumento `sit` for True.
              Pode ser "RUIM" se a média for menor que 5, "RAZOÁVEL" se a média for entre 5 e 7 (exclusivo),
              ou "BOA!" se a média for maior ou igual a 7.
    """
    total_notas = dict()
    average = sum(notas) / len(notas)
    total_notas['total'] = sum(notas)
    total_notas['maior'] = max(notas)
    total_notas['menor'] = min(notas)
    total_notas['média'] = average
    if calcular_situacao:
        calcular_situacao = 'RUIM' if average < 5 else 'RAZOÁVEL' if 5 <= average < 7 else 'BOA!'
        total_notas['situação'] = calcular_situacao
    return total_notas

#programa principal
limpa_tela()
letreiro('Ficha Aluno', 'yellow', 'light_cyan')
print()
#help(notas) - verifica as instruções inseridas na docstrings da funcao notas
resp = notas(5, 8.7, 8, 8, 3, 10, calcular_situacao=True)
print(resp)
print()
letreiro_2('Volte Sempre', 'magenta', 'light_blue')
print()