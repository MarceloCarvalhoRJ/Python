n = float(input('Informe a temperatura em \xb0C '))
fah = (n * 9/5) + 32
print('A temperatura {:.1f}\xb0C corresponde a {:.1f}\xb0F'.format(n, fah))
print(f'A temperatura {n:.1f}\xb0C corresponde a {fah:.1f}\xb0F') #usando f-strings