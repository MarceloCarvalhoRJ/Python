def no_space(x):
    return x.replace(' ', '')

text = input('Digite o seu texto: ')
print(f'O texto sem espaços ficou assim: {no_space(text)}')