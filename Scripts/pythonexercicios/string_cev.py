
# fatiamento
nome, idade = 'Marcelo', 50
print(nome, idade, sep="#", end="...\n")
frase = 'Curso em Video'
print(frase[::-1]) #inverte os valores da string
print(frase[-1]) # informar a ultima letra ou valor da string
print(frase[9:13])
print(frase[9:14])
print(frase[0:14:2])
print(frase[:5])
print(frase[6:])
print(frase[6::3])
print(frase[::3])
print('-' * 20)

PI = 3.141516
print(f'PI = {PI:.2f}')
print(f'PI = {PI:10.3f}')

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
print('.'.join(frase))
print(frase.center(20, '#'))
print(f'{frase:#^20}')

texto = '    Aprendendo Python    '
print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())
print('.' * 50)
nome = 'Marcelo'
idade = 50
linguagem = 'Python'
print('Meu nome é {} tenho {} e estou aprendendo {}'.format(nome, idade, linguagem))
print(f'Meu nome é {nome} tenho {idade} e estou aprendendo {linguagem}')
#fazendo com dicionário
dados = {'nome': 'Marcelo', 'idade': '50', 'linguagem': 'Python'}
print('Meu nome é {nome} tenho {idade} e estou aprendendo {linguagem}'.format(**dados))

#strings multiplas linhas ou triplas
print(f'''
Meu nome é {nome} 
tenho {idade} 
e estou aprendendo {linguagem}''')