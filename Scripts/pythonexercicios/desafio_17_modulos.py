from math import hypot
co = float(input('Insira a medida do cateto oposto: '))
ca = float(input('Insira a medida do cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'O cumprimento da hipotenusa é {hipotenusa:.2f}')
