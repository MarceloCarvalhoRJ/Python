'''lista = ([1, 9], [0, 'Python', 25])
print(lista[0][1])
print(lista[1][1])'''

veiculos = {
    'Brand' : 'Ford', 
    'Model:' : 'Mustang',
    'Year' : 1998,
    }
for x in veiculos:
    print(x, ':', veiculos[x])  # 1 modo

print('.' * 40)

for x in veiculos.values():     # 2 modo
    print(x)

print('.' * 40)

veiculos['Color:'] = 'Yellow'
veiculos['Km:'] = '80.000'
veiculos['Year'] = 2020
for pos, value in veiculos.items():  # 3 modo
    print(pos, ':', value)


