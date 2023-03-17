
lista = list()
lista_maior, lista_menor, lista_peso = [], [], []

while True:
    nome = input('Qual o seu nome: ')
    peso = (float(input('Qual o seu peso: ')))
    lista_peso.append(peso)
    lista.append(nome)
    lista.append(peso)
    while True:
        continua = input('Deseja continuar [S/N]? ')
        if continua in 'SsNn':
            break
        else:
            print('Valor inválido...digite S ou N.')
    if continua in 'Nn':
        maior_peso = max(lista_peso)
        menor_peso = min(lista_peso)
        for pos, valor in enumerate(lista):
            if maior_peso == valor:
                lista_maior.append(lista[pos - 1])
            elif menor_peso == valor:
                lista_menor.append(lista[pos - 1])
        print(f'Ao todo, você cadastrou {len(lista_peso):.0f} pessoas')
        print(f'O maior peso foi de {max(lista_peso)}Kg. Peso de {lista_maior}')
        print(f'O menor peso foi de {min(lista_peso)}Kg. Peso de {lista_menor}')
        break   
    

