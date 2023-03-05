numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    entrada = input('Digite um numero entre 0 e 20: ')
    if entrada.isdigit():
        numero = int(entrada)
        if 0 < numero > 20:
            print('Número inválido. Tente novamente.')
        else:
            print(f'Você digitou o número {numeros[numero].capitalize()}.')
            while True:
                opcao = input('deseja continuar [s/n]? ')
                if opcao not in 'SsNn':
                    print('Digite S ou N.')
                else:
                    break
            if opcao in 'Nn':
                break      
    else:
        print('Valor inválido. Tente novamente')