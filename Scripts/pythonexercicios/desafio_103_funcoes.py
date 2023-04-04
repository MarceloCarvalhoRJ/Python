from letreiro import letreiro, letreiro_2
from main import limpa_tela

def ficha(nome, gols ):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gols(s) no campeonato.'
    

#programa principal
limpa_tela()
letreiro('Ficha Jogador', 'cyan', 'light_yellow')
player = input('Nome do jogador: ').title()
goals = input('Número de gols: ')
print(ficha(player, goals))
letreiro_2('Obrigado e Volte Sempre!', 'magenta', 'light_blue')
   
    

