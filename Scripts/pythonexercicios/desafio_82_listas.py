valor, par, impar = [], [], [] #atribuição múltiplas

while True:
    valor.append(int(input('Digite um valor: ')))
    while True:
        opcao = input('Deseja continuar [S/N]): ')
        if opcao in 'SsNn':
            break
        else:
            print('Valor inválido. Digite S ou N.')
    if opcao in 'Nn':
        for num in valor:
            if num % 2 == 0:
                par.append(num)
            else:
                impar.append(num)
        print(f'A lista completa é {valor}')
        print(f'A lista de pares é {par}')
        print(f'A lista de ímpares é {impar}')
        break