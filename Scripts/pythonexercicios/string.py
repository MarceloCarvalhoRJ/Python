# fatiamento
frase = 'Curso em Video'
print(frase[9:13])
print(frase[9:14])
print(frase[0:14:2])
print(frase[:5])
print(frase[6:])
print(frase[6::3])
print(frase[::3])
print('-' * 20)

# analisando a string
print(len(frase))
print(frase.count('o'))
print(frase.count('e', 5, 14))
print(frase.find('Video'))
print(frase.find('video'))
print('Curso' in frase)
print('python' in frase)
print('-' * 20)

# Transformação na string
print(frase.replace('Video', 'Python'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
texto = '    Aprendendo Python    '
print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())
