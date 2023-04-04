import os
#limpa a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

def titulo(msg):
    print(msg)
    print('-' * len(msg))

def area(alt, larg):
    area = alt * larg
    print(f'A área do seu terreno {alt} x {larg} é de {area}mº.')


titulo('Controle de Terrenos')
largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))
area(largura, altura)
print()