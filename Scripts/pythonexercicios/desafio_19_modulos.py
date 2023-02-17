from random import choice
a1 = input(' Aluno 1: ')
a2 = input(' Aluno 2: ')
a3 = input(' Aluno 3: ')
a4 = input(' Aluno 4: ')
alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print(f'O escolhido para apagar o quadro foi {escolhido.title()}!') #retorna com o nome do escolhido com a primeira letra em maiuscula.
