from termcolor import colored
vel = float(input('Qual a velocidade do carro Km/h: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(colored(f'Voce ultrapassou o limite de 80 km/h! \nVocê foi multado em R$ {multa:.2f}', 'red'))
else:
    print(colored('Sua velocidade está dentro do limite!', 'yellow'))
