from termcolor import colored

# classificacao final de 2020 dos 20 times da série A do campeonto brasileiro
classificados = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
times = ''
for t in classificados:
    times += t + ', '
print(f"{colored('-=' * 20, 'yellow')} \n\033[36mLista de times do Brasileirão:\033[0m {times}")
print(f"{colored('-=' * 20, 'yellow')} \n\033[36mOs 5 primeiro são:\033[0m {classificados[0:6]}")
print(f"{colored('-=' * 20, 'yellow')} \n\033[36mOs 4 últimos são:\033[0m {classificados[-4:]}")
print(f"{colored('-=' * 20, 'yellow')} \n\033[36mOs times em ordem alfabética:\033[0m {sorted(classificados)}")
print(f"{colored('-=' * 20, 'yellow')} \n\033[36mO Bragantino está na {classificados.index('Bragantino')}ª posicão.\033[0m")
print()
