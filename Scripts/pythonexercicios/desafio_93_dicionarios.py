jogador = {}

jogador['nome'] = input('Nome do jogador: ').strip()
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
#joga o for para a mesma linha do input, fechando toda a expressao com [] cria a lista na variavel gols.
gols = [int(input(f'Quantos gols na partida {c + 1}? ')) for c in range(0, partidas)] 
jogador['gols'] = gols   
jogador['total']= sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for key, value in jogador.items(): #obs.items() é somente para dicionarios e enumerate() para as listas.
    print(f'O campo {key} tem o valor {value}.')
print('-=' * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
#outra forma de usar o for para percorrer os valores da lista gols.
for item in (f'     => Na partida {key + 1}, fez {value} gols. ' for key, value in enumerate(jogador['gols'])):
    print(item)
print(f"Foi um total de {jogador['total']} gols.")