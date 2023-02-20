frase = input('Digite uma frase: ').lower().strip()
print('Essa frase possui {} letras a'.format(frase.count('a')))
print('A primeira letra a está na posicão {}'.format(frase.find('a')))
print('A última letra a está na posicão {}'.format(frase.rfind('a')))
