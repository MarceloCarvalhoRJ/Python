n = int(input('Informe um numero de 0 a 9999: '))
u = n % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = (n // 1000) % 10
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')

