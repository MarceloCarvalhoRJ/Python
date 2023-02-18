nome = input('Qual é o seu nome: ')
print(f'Seu nome em maiusculo é {nome.upper()}')
#tamanho = len(nome) - nome.count(' ') - outra solucao para a contagem de caracteres sem espaços.
tamanho = len(nome.replace(' ', ''))
print(f'O nome possui {tamanho} caracteres sem espaço.')
name = nome.split()
print(f'O primeiro nome tem {len(name[0])} caracteres')