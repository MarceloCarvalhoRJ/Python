a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
ar = a * l
qtde = ar / 2
print('A área total da parede é {:.2f} m\xB2 \nPrecisa de {:.2f} l de tinta para pintar toda a parede'.format(ar, qtde))