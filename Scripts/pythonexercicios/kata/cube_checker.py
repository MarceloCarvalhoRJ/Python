
def cube_checker(volume, side):
    return 0 < volume == side**3

volume = int(input('Digite o volume do cubo: '))
side = int(input('Digite tamanho do lado do cubo: '))

if cube_checker(volume, side) is True:
    print('Os valores inseridos correspondem a um Cubo!')
else:
    print('Não é um cubo!')
