s = float(input('Qual o seu salário? '))
sn = s * 1.15
print('O seu salario com aumento é \u20ac {:.2f}'.format(sn)) 
print(f'O seu salario com aumento é \u20ac {sn:.2f}') #usando f-strings introduzidas no Python 3.6.