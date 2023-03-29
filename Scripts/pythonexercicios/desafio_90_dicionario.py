aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
print(f'O nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    print('Situação é igual a Aprovado!')
elif 5 <= aluno['media'] < 7:
    print('Situação é igual a Recuperação!')     
else:
    print('Situação é igual a Reprovado.')

