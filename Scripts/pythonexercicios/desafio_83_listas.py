from termcolor import colored

expression = []
expression = input('Digite a expressão: ')
paren_left = expression.count('(')
paren__right = expression.count(')')
if (paren_left != paren__right) or (expression.rfind('(') > expression.rfind(')')):
    print(colored('Sua expressão está errada!', 'light_red'))
else:
    print(colored('Sua epressão é válida!', 'light_cyan'))

'''expressao = input('Digite a expressão: ')
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) == 0 or pilha[-1] != '(':
            print('Expressão inválida')
            break
        pilha.pop()
else:
    if len(pilha) == 0:
        print('Expressão válida')
    else:
        print('Expressão inválida')'''
