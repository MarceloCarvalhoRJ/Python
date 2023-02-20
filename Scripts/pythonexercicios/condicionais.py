n1 = float(input('Digita a primeira nota: '))
n2 = float(input('Digita a segunda nota: '))
media = (n1 + n2)/2
if(media >= 7):
    print(f'Sua média foi {media:.2f}. \nVocê foi aprovado!')
else:
    print(f'Sua média foi {media:.2f}. \nVocê está reprovado.')