lista = []

for i in range(5):
    valor = int(input('Digite um número: '))
    if len(lista) == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista): 
            if valor <= lista[posicao]:
                print(f'Adicionado na posição {posicao} da lista...')
                lista.insert(posicao, valor)
                break
            posicao += 1
print(f'Lista ordenada: {lista}')