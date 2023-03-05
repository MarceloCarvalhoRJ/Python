lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')       
    while True:
        opcao = input('Deseja continuar [S/N]: ')
        if opcao in 'SsNn':
            break
        else:
            print('valor inválido, Digite S ou N.')
    if opcao in 'Nn':
        break
print('-=' * 40) 
print(f'Voce digitou os valores {sorted(lista)}')  