def leiaint(number):
    while True:
        num = input(number)
        if not num.isdigit():
            print('\033[31mErro! Digite um número inteiro\033[m')
        else:
            return num

n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')

'''
#usar int(input()) para solicitar que o usuário insira um número inteiro e, em seguida, usar try e except para tratar erros se o usuário inserir uma entrada que não possa ser convertida em um número inteiro.

while True:
        try:
            num = int(input(number))
        except ValueError:
            print('Erro! Digite um número inteiro')
        else:
            return num'''