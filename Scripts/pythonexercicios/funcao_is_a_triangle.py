
def is_a_triangle(l1, l2, l3):
    return (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2

print(is_a_triangle(9, 4, 2))

sides = list()
for i in range(3):
    side = float(input(f'Digite o lado {i + 1} do triangulo: '))
    sides.append(side)

'''sides = [0.0, 0.0, 0.0]
for i in range(3):
    sides[i] = int(input(f'Digite o lado {i + 1} do triangulo: '))'''

if is_a_triangle(sides[0], sides[1], sides[2]):
    print('É Triangulo!')
else:
    print('Não pode ser um triangulo.')