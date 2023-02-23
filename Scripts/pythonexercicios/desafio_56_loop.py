from termcolor import colored

soma_idade = 0
sexo_f = 0
maior_idade = 0
mais_velho = ''

for i in range(1, 5):
    print(colored(f'------ {i}ª pessoa ------', 'cyan'))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    soma_idade += idade 
    if sexo in 'Ff' and idade < 20: # verifica o f maiusculo e minusculo digitado.
        sexo_f += 1
    if sexo in 'Mm' and idade > maior_idade: # verifica o m maiusculo e minusculo digitado.
        maior_idade = idade
        mais_velho = nome

media = soma_idade / 4

print(colored('=-' * 23, 'cyan'))
print(f'O mais velho é o Sr. {mais_velho} com {maior_idade} anos. \nA média de idade é {media:.2f} \nQuantidade de mulheres menor que 20 anos é {sexo_f}')
print(colored('=-' * 23, 'cyan'))