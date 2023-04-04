import os
#limpa a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

seleção = list()
while True:
    jogador = {}
    print('-' * 35)
    nome = input('Nome do jogador: ')
    jogador['nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    #joga o for para a mesma linha do input, fechando toda a expressao com [] cria a lista na variavel gols.
    jogador['gols'] = [int(input(f'Quantos gols na partida {c + 1}? ')) for c in range(0, partidas)]   
    jogador['total']= sum(jogador['gols'])
    seleção.append(jogador)
    while True: 
        opcao = input('Deseja continuar [S/N]? ').upper().strip()
        if opcao in 'NS':
            break
        print('ERRO! Digite S ou N.')
    if opcao in 'N':
        break
print('-=' * 21)
print('cod nome            gols            total')
print('.' * 42)
for key, jogador in enumerate(seleção): #obs.items() para dicionarios e enumerate() para as listas. 
    print(f"{key:>3} {jogador['nome']:<15} {str(jogador['gols']):<15} {str(jogador['total']):<5}")
while True:
    print('-=' * 21)
    opcao = int(input('Mostrar dados de qual jogador? (999 p/sair) '))
    if opcao == 999:
        break
    elif opcao >= len(seleção):
        print(f'ERRO! Não existe jogador com código {opcao}! Tente novamente')
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {seleção[opcao]['nome']}")
        for jogo, gols in enumerate(seleção[opcao]['gols']):
            print(f"   No jogo {jogo + 1} fez {gols} gols.")
print('«« Volte Sempre »»')    



