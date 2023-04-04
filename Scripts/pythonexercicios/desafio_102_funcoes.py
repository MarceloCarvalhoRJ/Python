from letreiro import letreiro, letreiro_2
from main import limpa_tela


def fatorial(number, show=False):
    """
    Função para calcular o fatorial de um número.
    -> Recebe um número inteiro como entrada.
    -> retorna seu fatorial.
    -> Se o parâmetro show for True, exibe também a expressão completa do fatorial.
    """
    fat = 1
    for i in range(number, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print('x', end='')    
            else: 
                print('=', end='')
        fat *= i
    return fat 


limpa_tela()
letreiro('Calculo Fatorial', 'yellow', 'cyan')
ano = int(input('Digite um numero: '))
opcao = input('Deseja exibir a expressão completa [S/N]? ')
show = (True if opcao in 'Ss' else False)
print(fatorial(ano, show))
letreiro_2('Volte Sempre!', 'magenta', 'light_blue')