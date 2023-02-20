from termcolor import colored
dist = int(input(colored('Qual a distância da viagem em Km: ', 'green')))
if dist <= 200:
    print('Seu custo para uma viagem menor que 200 Km será de RS {:.2f}'.format(dist * 0.5))
else:
    print('Seu custo para uma viagem maior que 200 km será de R$ {:.2f}'.format(dist * 0.45))