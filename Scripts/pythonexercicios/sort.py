my_list = []

num = int(input('Quantos elementos voce deseja embaralhar?'))

for i in range(num):
    val = float(input('Entre com a lsita de elementos:'))
    my_list.append(val)
    my_list.sort()

print(f'Aqui está a lista ordenada: {my_list}')