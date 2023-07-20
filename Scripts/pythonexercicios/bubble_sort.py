my_list = []
swapped = True
num = int(input('Quantos elementos voce deseja embaralhar?'))

for i in range(num):
    val = float(input('Entre com a lista de elementos:'))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            swapped = True

print(f'Aqui está a lista ordenada: {my_list}')   