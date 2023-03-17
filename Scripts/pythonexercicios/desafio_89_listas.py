from time import sleep
from letreiro import letreiro, letreiro_2
from termcolor import colored

letreiro('CADASTRO DE NOTAS', 'light_magenta', 'light_blue')

alunos = []
while True:
    media = 0
    nome = input('Digite o nome do aluno: ')
    nota1 = (float(input('Digite a nota 1: ')))
    nota2 = (float(input('Digite a nota 2: ')))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continua = (input(colored('Deseja continuar [S/N]? ', 'light_yellow')))
    if continua in 'Nn':
        break
print('=-' * 20)
print(f"{'Nº':>3} {'NOME':<17} {'MÉDIA':>5}")
print('-' * 30)
for pos, aluno in enumerate(alunos):
    print(f'{pos:<3} {aluno[0]:<17} {aluno[2]:>5.2f}')   
while True:
    print('-' * 40)
    mostrar = int(input('Mostrar notas de qual aluno (999 p/sair)? '))
    if mostrar == 999:
        print('\033[33mFinalizando', end = '')
        for i in range(0, 3):
            print('.', end = ' ', flush = True)
            sleep(.4)
        print('\n')
        letreiro_2('Volte Sempre! ', 'cyan', 'light_yellow')
        break     
    else:
        print(f'Notas de {alunos[mostrar][0]} são {alunos[mostrar][1]}')
        
    
    


        