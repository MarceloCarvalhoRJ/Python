from datetime import date
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if  idade < 18: 
    print(f'Faltam {18 - idade} para o seu alistamento militar!')
elif idade == 18:
    print('Você tem que se alistar imediatamente!')
else: 
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
