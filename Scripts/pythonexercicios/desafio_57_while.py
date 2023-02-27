sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]m
    print('Opção inválida, digite M para Masculino ou F para feminino.')
if sexo == 'M':
    print('O Sexo escohido foi Masculino!')
else:
    print('O sexo escolhido foi Feminino!')
