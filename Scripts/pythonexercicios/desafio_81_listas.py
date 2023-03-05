
valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    while True:
        opcao = input('Deseja continuar [S/N]): ')
        if opcao in 'SsNn':
            break
        else:
            print('Valor inválido. Digite S ou N.')
    if opcao in 'Nn':
        valor.sort(reverse = True)
        print('-=' * 30)
        print(f'Voce digitou {len(valor)} elementos.')
        print(f'Os valores em ordem descrescente são {valor}')
        if 5 in valor:
            print('O valor 5 faz parte da lista')
        else:
            print('O valor 5 NÃO faz parte da lista.')
        break


